**A. Outcomes** (45 claims in the claims file)

| claim id | outcome | reason |
|---|---|---|
| fig1d-fastigial-lesion-contra-choice | blocked (data_missing) | No lesion mice. The archive lists 13 subjects, all ALM-recording mice, and its `variableMeasured` is only Units and ElectrodeGroup. |
| fig1e-fastigial-lesion-slow-initiation | blocked (data_missing) | No lesion mice and no lick times (same archive check). |
| fig1d-dentate-lesion-no-effect | blocked (data_missing) | No lesion mice. |
| fig1g-fastigial-activation-early-sample-no-effect | reproduced | Cell 14: one-sided p = 0.31 (contra) and 0.41 (ipsi), both > 0.05, in 6 mice. These are recording sessions, not the paper's behaviour sessions. |
| fig1g-fastigial-activation-delay-errors | reproduced | Cell 16: performance falls from 0.873 to 0.630, p < 1e-4 (no resample of 10,000 had the opposite sign). |
| fig1h-fastigial-activation-delay-bias | reproduced | Cell 18, reading (a): 2 mice with a significant contra bias and 3 with an ipsi bias. Both directions remain at p < 0.01. Reading (b), the 1.255 s stimulus, is not in the data. |
| fig1h-fastigial-activation-response-contra-bias | blocked (data_missing) | Cell 7: every code starts at sample or delay onset, so there is no response-epoch stimulation. |
| fig1i-fastigial-activation-licking-unaffected | blocked (data_missing) | No lick times, so bout rate and duration cannot be measured. The early-lick part can be tested and shows no change (cell 24: 0.079 vs 0.127, two-sided p = 0.35). |
| fig1g-dentate-activation-little-effect | reproduced | Cell 20, reading (a): drop of 0.038, one-sided p = 0.108, so no significant drop (paper p = 0.06). This rests on only 3 of 8 mice; ipsi trials alone give p = 0.04. |
| fig1j-photoinhibition-silences-fastigial | blocked (data_missing) | No CN recordings. |
| fig1k-inhibition-early-sample-no-effect | blocked (data_missing) | Codes 5 and 6 both start at delay onset and last through the delay (cell 7). There is no 0.5 s sub-epoch stimulation. |
| fig1k-inhibition-late-sample-delay-errors | blocked (data_missing) | Same as above. Only a pooled 1.3 s delay drop exists (cell 22: 0.848 to 0.693, p = 0.0002), which is not the criterion. |
| fig1k-inhibition-delay-bias | partially_reproduced | Reading (b) names CD12, CD13 and CD16; CD16 is absent. CD12 and CD13 are biased the same way under both side assignments (cell 22: files give 2 contra, table gives 2 ipsi). Across all 4 photo-inhibition mice both directions appear under both assignments. Recording sessions, not Ext. Data Fig. 2g sessions. |
| fig1k-inhibition-response-ipsi-bias | blocked (data_missing) | No response-epoch stimulation. |
| fig1l-inhibition-execution-unaffected | blocked (data_missing) | No lick times or video. The early-lick part (lick_early, codes 5 and 6 against 0, 4 mice) could be tested but was not. |
| ed10-vgat-fastigial-perturbation-performance | blocked (data_missing) | No VGAT-ChR2 subjects in the archive metadata (genotypes are L7-cre or unknown). |
| fig2-alm-selective-fraction | reproduced | Cell 26: 800/1082 = 0.739 (correct trials, 1.3 s) and 0.753 (1.5 s), inside 0.738–0.902. The 1.3 s value sits 0.001 above the bound; the all-trials readings (0.734) fall outside. |
| fig2-cn-selective-fraction | blocked (data_missing) | No CN units. |
| fig2-preparatory-more-in-alm | blocked (data_missing) | No CN units. The ALM half would fail anyway: 0.50–0.525 of all neurons and 0.68–0.71 of selective ones, against 0.59 ± 0.059. |
| fig2-peri-movement-equal | blocked (data_missing) | No CN units. The ALM half would also fail: 0.572–0.587 of all neurons, against a lower bound of 0.603. |
| ed4-lick-modulated-few | blocked (data_missing) | No lick times (archive `variableMeasured` and the trials-table columns). |
| fig2cd-selectivity-emerges-gradually | partially_reproduced | ALM meets the criterion only when the response epoch fixes the preference (cell 28). With the sample or delay epoch the maximum falls at −0.45 to −0.05 s, so the result depends on that reading, against the paper's "qualitatively similar". The CN half is not in the data. |
| ed4e-cn-predicts-movement | blocked (data_missing) | CN. |
| ed4f-preparatory-all-nuclei | blocked (data_missing) | CN. |
| ed4g-fastigial-contra-late-delay | blocked (data_missing) | CN. |
| fig3-cn-altered-by-alm-inhibition | blocked (data_missing) | CN. |
| fig3b-cn-net-disinhibition | blocked (data_missing) | CN. |
| fig3c-cn-selectivity-abolished | blocked (data_missing) | CN. |
| ed6-cn-selectivity-both-alm-hemispheres | blocked (data_missing) | CN. |
| fig3d-alm-altered-by-cn-inhibition | not_reproduced | Cell 32: latency 14.7–22.1 ms (bootstrap mean, any bin label or trial set), outside 3.3–10.9 ms. The count, 267 of 676, is outside 197 ± 19.7; only the fraction, 0.395, falls inside its 10% band. |
| fig3e-alm-mean-rate-unchanged | not_reproduced | Cell 34: no reading has both rates in tolerance (all neurons 3.23/3.65; modulated 4.41/5.62, the second outside 3.95–4.83). The paired test differs (p = 0.010). |
| fig3e-alm-increase-decrease | partially_reproduced | Cell 36: counts 158/109 (all trials) and 136/84 (correct) are outside 108 ± 10.8 and 89 ± 8.9. The increase fraction 0.592 is inside 0.495–0.605 on all trials, but the fraction fallback strictly applies only when the data hold fewer neurons, and they hold more (676 vs 454). |
| fig3f-alm-selectivity-abolished-by-cn-inhibition | reproduced | Cell 39: the criterion is met only with the last 500 ms window and 5 preference trials of each type (photo CI −0.27 to 0.52). The other three combinations fail (photo CI excludes 0), and n = 430 against 329 ± 32.9. |
| fig4bc-fastigial-targets-alm-thalamus | blocked (data_missing) | No anatomy data. |
| ed8-snr-sc-converge | blocked (data_missing) | No anatomy data. |
| fig4-fastigial-activation-alm-latency | not_reproduced | Cell 41: latency is in tolerance with the bin-start label (2.1–5.1 ms), but the modulated fraction, 0.25–0.32 (137–178 of 557), is far below 0.509 ± 0.051 and the count 227 ± 22.7, under both windows and both trial sets. |
| fig4e-fastigial-activation-abolishes-alm-selectivity | reproduced | Cell 50: under every reading the difference CI excludes 0, 86–88% of control-selective neurons lose significance, and 5–6 gain it against 105–107 that lose it. The power control, though, loses 65–75% from trial count alone. |
| fig4f-fastigial-effect-persists | reproduced | Cell 46: 13.1% significant in the first qualifying bin (5.9–8.1% on correct trials) against 1% chance and 1.5% before onset, p < 1e-10. Every qualifying bin lies after the go cue (see B5). |
| fig4g-dentate-effect-recovers | not_reproduced | Cell 43: with the paper's method the latency is 0.0–1.4 ms, outside 3.3–13.3 ms. Cell 48: the late fraction (3.4–5.3%) is above chance and above the pre-onset level in every bin. Only "lower than fastigial" and the count (165) are met. |
| fig4i-cd-control-separation | reproduced | Cell 54: the interval is above 0 in 121/130 sample windows and 130/130 delay windows (22 sessions). |
| fig4i-fastigial-collapses-cd | reproduced | Cell 56, reading (b): fastigial separation falls (diff CI −15.1 to −1.6 and −14.1 to −3.2), while the dentate difference CI includes 0 in both windows. Reading (a) fails. |
| cd-captures-selectivity | partially_reproduced | Cell 58: selectivity is within tolerance (62.1%) only with independent trials and squared ratio. Variance is within (24.0%) only for single-trial activity, a dimension the notebook added; it chose trial-type means as its main reading, and those give 34.2%, outside 22.8–31.2. |
| ed10c-alm-inhibition-endpoints-predict | blocked (data_missing) | No VGAT mice and no ALM photo-inhibition codes. |
| ed10d-fastigial-endpoints-no-prediction | not_reproduced | Cell 60: on photo-activation trials the slope is 0.42 (CI 0.13–0.71), p = 0.005, so the projection still predicts licking direction (n = 215; control slope 1.21). |
| ed10ef-alm-drives-licking-after-fastigial | blocked (data_missing) | VGAT behaviour data are not in the archive. |

Totals: 9 reproduced, 5 partially reproduced, 5 not reproduced, 26 blocked.

**B. Problems**

1. **[affects a conclusion]** Cells 4 and 5, `prepare`: the dataset holds more putative pyramidal units than the paper. Photo-activation sessions have 1082 in 9 mice against the paper's 912; photo-inhibition sessions have 676 in 4 mice against 454, plus a 20th session against 19. The notebook never explains this (for example by listing all unit-table columns to look for a quality flag). It bears on every count claim (fig3d, fig3e ×2, fig3f n, fig4, fig4e n, fig4g). It is also a plausible cause of the low mean rate in fig3e (3.23 vs 4.15). And it means the "fewer neurons, judge the fraction" fallback was applied when the data in fact hold more neurons.
2. **[affects a conclusion]** `photo_selectivity`, cell 39: fig3f passes in 1 of 4 reading combinations from a single random draw of the preference trials. Moving from 5 to 10 trials per type in the same window turns the photo CI from (−0.27, 0.52) to (0.066, 0.89). No seed-repeat check was run.
3. **[affects a conclusion]** `captured`, cell 58: the only passing row combines the single-trial activity variant with independent trials. The notebook's stated main choice (trial-type means) fails on variance. Both are defensible readings of "task-related activity", so the outcome rests on which one is accepted.
4. **[affects a conclusion]** fig2cd, cell 28: the outcome depends on which epoch fixes the preference, a detail the paper says does not matter. Neurons are also selected (E2) on the same correct control trials that later give the held-out selectivity, so selection inflates the sample-epoch "CI above 0" test.
5. **[does not affect a conclusion]** `late_tests`, cell 46: every qualifying bin starts 1.5–2.2 s after delay onset, which is after the go cue at 1.3 s. Left and right trials are pooled, and photo-activation trials have far more errors (0.63 correct vs 0.87), so movement-direction composition can drive the response-epoch differences. Dentate also stays above chance. The claims file's criterion allows response-epoch bins, so the outcome stands, but "preparatory activity" is not isolated. The two-proportion test also treats 19 overlapping pre-onset bins as independent samples.
6. **[does not affect a conclusion]** `latency` and `onset_latency`: with the paper's method, pre-onset sign-flip bias (dentate pre-onset change 0.59 spikes/s) puts the onset at 0 ms. Only the author's own baseline-subtracted variant falls in tolerance, and it was correctly not used to decide. The photostimulus onset relative to `pole_out_time` (for example the phase of the 40 Hz sinusoid) was never checked, and the fig3d latency depends on it.
7. **[does not affect a conclusion]** Hemispheres, cell 10: for CD12, CD13 and CD14 the files' ogen site makes ALM ipsilateral to the manipulated CN, which contradicts the paper; CD14's recording side also disagrees with Supplemental Table 1. Both mappings were run where it matters (fig1k-inhibition-delay-bias), so this is handled.
8. **[does not affect a conclusion]** Synthetic test of `hierarchical_bootstrap` (40 null datasets, 5 mice × 3 sessions): mean p = 0.32 and none below 0.05, where roughly 10% would be expected from a calibrated test of this form. The test is conservative, which favours the absence claims (fig1g early sample, fig1g dentate). It is the paper's method, so this is noted only. `spike_width_ms`, `binned` and `onset_latency` (recovers a 5 ms onset) behaved correctly on synthetic inputs.
9. **[does not affect a conclusion]** Cell 9: five sessions fail the clock and lock check (for example BAYLORCD13 20171211, with 15 trials) but are kept in every analysis. No sensitivity run without them.
10. **[does not affect a conclusion]** fig1l: the early-lick part could be tested from `lick_early` with codes 5 and 6, but it was not.
11. **[does not affect a conclusion]** Behaviour claims (fig1g, fig1h, fig1k): these use recording sessions, where each code covers about 11% of trials. The paper's behaviour sessions (25% stimulation) are not in the data. This is stated, but the outcomes rest on different sessions from the paper's.

**C. What I could not check**

- **Why the unit counts exceed the paper's:** a printout of every column of the NWB units table (and any quality or isolation field), plus per-session unit counts set against Supplemental Table 1, would settle B1.
- **What `photo_stim_id` 5 and 6 mean:** the files carry no stimulus description or laser traces. The mapping to two powers rather than two durations is inferred from cell 7, where code 5's response decays earlier. A per-code time course of the population rate change across 1.3–2.9 s would make the inference firmer.
- **When the photostimulus actually starts:** the fine time course used for the fig3d and fig4 latencies, printed per code over −10 to +40 ms, would show it.
- **Whether fig3f survives re-sampling:** repeating it over, say, 20 seeds for each reading and reporting the fraction passing would show that.
- **Whether the paper's variance is single-trial or condition-averaged:** I could not confirm this from the text, which says only "RMS of the baseline subtracted activity over the sample and delay epochs". The code behind Li et al. 2016 was not available.
- **Whether early-lick trials carry their stimulation code:** a crosstab of `photo_stim_id` by `lick_early` would show whether the fig1i/fig1l early-lick comparisons are valid.
- **Lick data inside the files:** I did not open any NWB file beyond the archive metadata, which lists only Units and ElectrodeGroup. A listing of each file's acquisition and processing groups would confirm that no lick channel exists.
