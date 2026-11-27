**A. Outcomes** (46 claims in the claims file; the notebook tests 22 and blocks 24)

| claim | my outcome | reason |
|---|---|---|
| fig1d-fastigial-lesion-contra-choice | blocked (data_missing) | No lesion sessions. DANDI holds 54 ALM NWB files with only Units/ElectrodeGroup; CRCNS holds only the two ALM-recording archives. |
| fig1e-fastigial-lesion-slow-initiation | blocked (data_missing) | Same: no lesion data. |
| fig1d-dentate-lesion-no-effect | blocked (data_missing) | Same: no lesion data. |
| fig1g-fastigial-activation-early-sample-no-effect | reproduced | Cell 14: one-sided p_drop is 0.364 for contra and 0.635 for ipsi, both above 0.05. Tested on the recording sessions of the same 6 mice. |
| fig1g-fastigial-activation-delay-errors | reproduced | Cell 16: pooled performance falls from 0.870 to 0.630, p < 0.0001. |
| fig1h-fastigial-activation-delay-bias | reproduced | Cell 20, reading (a): 2 mice are contra-biased (ANM314760, BAYLORNL15, p ≈ 0) and 2 ipsi-biased (ANM314746 p = 0.003, ANM314757 p = 0.029). Reading (b) is not in the data. |
| fig1h-fastigial-activation-response-contra-bias | blocked (data_missing) | There are no response-epoch codes (codes 0 to 6, cell 3). |
| fig1i-fastigial-activation-licking-unaffected | blocked (data_missing), but part was testable | Bout measures need lick times and response-epoch stimulation. The early-lick part could have been tested from the per-trial LickEarly flag (problem 8). |
| fig1g-dentate-activation-little-effect | partially_reproduced | Cell 22: no drop at p < 0.05 (p = 0.107, change −0.039). This is an absence claim tested in 3 of 8 mice, with reading (a) only, using a test that is conservative (problem 7). |
| fig1j-photoinhibition-silences-fastigial | blocked (data_missing) | No CN recordings in either archive. |
| fig1k-inhibition-early-sample-no-effect | blocked (data_missing) | There is no sample-epoch inhibition code. |
| fig1k-inhibition-late-sample-delay-errors | blocked (data_missing), but part was testable | Late-sample inhibition is absent. The early-delay drop is in cell 24 (code 5, −0.142, p = 0.014). |
| fig1k-inhibition-delay-bias | reproduced | Cell 24, reading (b), code 6: 2 contra-biased and 1 ipsi-biased mouse under the paper's side rule; 1 and 2 under the files' CN side. Uses 4 recording mice, not the behavior cohort. |
| fig1k-inhibition-response-ipsi-bias | blocked (data_missing) | No response-epoch code. |
| fig1l-inhibition-execution-unaffected | blocked (data_missing), but part was testable | The early-lick rate under codes 5 and 6 (4 of 7 mice) was available from the LickEarly flag. |
| ed10-vgat-fastigial-perturbation-performance | blocked (data_missing) | No VGAT-ChR2 sessions. |
| fig2-alm-selective-fraction | reproduced | Cell 26: 0.740 to 0.797 under all four readings, all within 0.82 ± 0.082. Counts are not judged because the data hold 34 of 39 sessions. |
| fig2-cn-selective-fraction | blocked (data_missing) | No CN units. |
| fig2-preparatory-more-in-alm | partially_reproduced | Only the ALM half can be tested. With all neurons as denominator, 0.538 to 0.563 lies within 0.59 ± 0.059. With selective neurons as denominator, 0.71 to 0.73 lies outside. |
| fig2-peri-movement-equal | partially_reproduced | Only the ALM half can be tested. Correct trials give 0.642 or 0.636, within 0.67 ± 0.067; all trials give 0.56 to 0.57, outside. |
| ed4-lick-modulated-few | blocked (data_missing) | No CN units, and lick times were not shown to exist (section C). |
| fig2cd-selectivity-emerges-gradually | partially_reproduced | Only ALM can be tested. Under reading (a), the sample-epoch interval lies above 0, the delay mean (1.80) exceeds the sample mean (0.65), and the maximum falls at +0.23 s, in the response epoch. Under reading (b) the maximum falls at −0.06 s. |
| ed4e-cn-predicts-movement | blocked (data_missing) | No CN units. |
| ed4f-preparatory-all-nuclei | blocked (data_missing) | No CN units. |
| ed4g-fastigial-contra-late-delay | blocked (data_missing) | No CN units. |
| fig3-cn-altered-by-alm-inhibition | blocked (data_missing) | No CN units. |
| fig3b-cn-net-disinhibition | blocked (data_missing) | No CN units. |
| fig3c-cn-selectivity-abolished | blocked (data_missing) | No CN units. |
| ed6-cn-selectivity-both-alm-hemispheres | blocked (data_missing) | No CN units. |
| fig3d-alm-altered-by-cn-inhibition | not_reproduced | Cell 45: latency is 15 to 42 ms under every reading and label, against 7.1 ± 3.8. The count is 228 (all trials) or 106 (correct only), against 197 ± 19.7. The data hold more neurons than the paper (486 tested, 682 pyramidal), so the fraction fallback does not apply. |
| fig3e-alm-mean-rate-unchanged | reproduced | Cell 47, all tested neurons and all trials: 4.03 and 4.21 spikes/s, both within tolerance. Paired p = 0.51, unpaired p = 0.66. |
| fig3e-alm-increase-decrease | not_reproduced | Cell 49: 122/106 (all trials) and 65/41 (correct only), against 108 ± 10.8 and 89 ± 8.9. The increase fraction of 0.535 (all trials) would pass, but the criterion allows the fraction only when the data hold fewer neurons, and here they hold more. |
| fig3f-alm-selectivity-abolished-by-cn-inhibition | not_reproduced | Cell 53: photo-inhibition selectivity is 0.39 [0.19, 0.60] (whole delay) and 0.27 [0.02, 0.53] (last 500 ms). Both intervals exclude 0, also with 5 screening trials. Selectivity is reduced by 73 to 82%, not abolished. |
| fig4bc-fastigial-targets-alm-thalamus | blocked (data_missing) | No anatomy data. |
| ed8-snr-sc-converge | blocked (data_missing) | No anatomy data. |
| fig4-fastigial-activation-alm-latency | partially_reproduced | Cell 39: latency is 3.64 ms only with all trials, the stimulation window, and bins labelled by their start; centre labelling gives 8.6 ms, outside. The count is 177 to 190, against 227 ± 22.7, although all 6 mice are present. |
| fig4e-fastigial-activation-abolishes-alm-selectivity | reproduced | Cell 55: n = 328, matching the paper. The difference interval excludes 0; 89 to 90% of control-selective neurons lose significance and 6 to 9 gain it. The per-neuron part is unverified (problem 3). |
| fig4f-fastigial-effect-persists | reproduced | Cell 43: 13.4% of neurons are significant at ≥1 s after offset, against 1% (p = 3e-47) and against 0.9% before onset (p = 2e-13). See problem 4. |
| fig4g-dentate-effect-recovers | partially_reproduced | Cell 41: latency (centre label 8.3 ms) and count (172) are within tolerance. The recovery part fails: 4.8% after offset is above 1% (p = 2e-10) and above the pre-onset level (p = 0.0013), although it is lower than fastigial (p = 1e-6). |
| fig4i-cd-control-separation | reproduced | Cell 59: the interval excludes 0 from −2.06 s in the sample epoch and in all 131 delay windows. This uses 20 sessions; the paper used 28. |
| fig4i-fastigial-collapses-cd | partially_reproduced | Cell 61: the fastigial collapse holds under reading (b) (difference [5.84, 20.91]) but not under (a) (stimulation interval [0.26, 14.46]). The dentate difference excludes 0 in both windows ([0.15, 4.18] and [0.75, 4.65]), so the "dentate unaffected" condition fails. |
| cd-captures-selectivity | partially_reproduced | Cell 63: under reading (b) on held-out trials, selectivity is 66.3%, within 64.1 ± 3.4. Variance is 35.9 to 38.7% under (b) and 56 to 59% under (a), against 27.0 ± 4.2. It matches only under the notebook's own single-trial variant (problem 2). |
| ed10b-fastigial-activation-errors-during-recording | reproduced | Cell 18: change −0.240, p < 0.0001 (below 0.001), 6 mice. |
| ed10c-alm-inhibition-endpoints-predict | blocked (data_missing) | No ALM photo-inhibition code in either archive. |
| ed10d-fastigial-endpoints-no-prediction | not_reproduced | Cell 65: the slope on stimulation trials is still significant (0.54 [0.19, 0.90] per s.d., p = 0.0028, 181 trials). P(lick right) by quartile is 0.43, 0.49, 0.47, 0.73. Problem 1 may bear on this. |
| ed10ef-alm-drives-licking-after-fastigial | blocked (data_missing) | No VGAT-ChR2 sessions. |

**B. Problems**

1. **[affects a conclusion]** Cells 7 and 8: the 2015 laser traces are anomalous, and the sessions stay in every code-2 and code-4 analysis without a sensitivity run.
   - ANM314746_20151020: codes 1 and 2 last 1.300 s, though the descriptor says 500 ms.
   - ANM314756_20151020: 0.78 to 0.83 s.
   - ANM314757_20151021: the trace does not match the trials (onset −572 and −1873 ms, peak 0.17 mW), and DANDI keeps only 34 of its 302 trials.
   - BAYLORNL14_20170603: onset IQR of about 1300 ms, with only 39 to 54% of trials at the named epoch.

   ANM314746_20151020 is one of the 8 fastigial coding-direction sessions and the one that barely collapses (36.4 to 31.7). By my arithmetic, dropping it moves the fastigial stimulation separation from 6.09 to about 2.4. That could flip fig4i reading (a), and it may carry the residual slope in ed10d.
2. **[affects a conclusion]** Cell 63: the only combination that puts both numbers within tolerance pairs held-out trials with variance computed from single trials. That variant is the notebook's own addition and is not in the claims file. It also fits poorly with "task-related activity". Under the claims file's readings the variance fraction fails.
3. **[affects a conclusion, unverified]** Cell 55: "lose significance" compares about 200 control trials against about 30 photo-activation trials per neuron, so neurons would lose significance from low power alone. There is no matched-count control (subsampling control trials, or the same count on dentate sessions).
4. **[does not affect a conclusion under the criterion]** Cell 43: every bin ≥1 s after offset lies in the response epoch, with trial types pooled. Photo-activation shifts choices, so the mix of lick directions differs between control and photo-activation trials, and rate differences can come from movement. Splitting by licked direction would separate this. The same applies to the dentate residual in fig4g.
5. **[does not affect a conclusion]** `latency()`: a bin labelled by its start includes spikes up to 10 ms later, and bins are clipped at a start of 0. On a synthetic test with an effect starting at 5 ms, it returned 0 ms. fig4's latency passes only under this most lenient label. Running all three labels was correct, since the paper leaves this open.
6. **[affects a conclusion]** Cells 3 and 4: the unit counts do not reconcile with the paper. The data hold 1084 pyramidal units against the paper's 912 (photo-activation mice) and 682 against 454 (inhibition mice). So the count criteria for fig3d, fig3e-increase-decrease, fig4 and fig4g are judged on a different population. The lab's compiled lists in `analyses_scripts.zip` were not used to reconcile (`analysis_compile_all_ALM_data.mat`, 194 MB; `analysis_compiled_all_ALM_DCNstim_FR.mat`; `analysis_compiled_all_ALM_DCNsilencing_selectivity.mat`).
7. **[does not affect a conclusion]** `hier_boot`: on a synthetic null (6 mice × 3 sessions, 200 simulations) it gave 0 false positives at one-sided 0.05. The method is the paper's scheme, but being conservative it favours the absence claims (fig1g early sample, dentate with 3 mice).
8. **[affects a conclusion]** Blocked claims that are partly testable: both deposits carry a per-trial LickEarly flag (`lick_early`, read in `_dandi_one` and `_reduce_session`). That allows the early-lick rate for control against delay photo-activation (fig1i, 6 mice) and against codes 5 and 6 (fig1l, 4 mice). They were blocked outright.
9. **[does not affect a conclusion]** Cell 9: the clock check leaves out the inhibition sessions. Their 15 to 42 ms latency (fig3d) is the result most exposed to a spike/event misalignment, and spikes were not checked against trial events in those sessions.
10. **[does not affect a conclusion]** `selectivity_tests` runs the t-test on rate (count ÷ per-trial epoch length); the paper says spike counts.
11. **[does not affect a conclusion]** `Session.pyramidal` takes the files' `cellType` label. The waveforms are loaded but never checked against the > 0.45 ms rule, and 52 units differ in cell type between DANDI and CRCNS.

**C. What I could not check, and which output would have settled it**

- Whether lick or tongue channels exist. The descriptor says `timeSeriesArrayHash` holds tongue-movement recordings; printing `idStr` per session would show whether ed4 (ALM part) and the fig1i/fig1l bout measures are testable.
- Whether the residual stimulation separation and the ed10d slope survive excluding the anomalous sessions. Needed: cells 61 and 65 rerun without ANM314746_20151020, ANM314757_20151021, ANM314756_20151020 and BAYLORNL14_20170603.
- Whether neurons lose significance in fig4e beyond what lower power explains. Needed: the lose/gain counts with control trials subsampled to the photo-activation count, and the same for dentate.
- Whether the persistence in fig4f/g is a movement effect. Needed: fig4f/g fractions computed within licked direction.
- The selectivity-onset clock check (cell 9) on the inhibition sessions.
- A reconciliation of unit counts against the lab's compiled `.mat` lists.
- The notebook's own discussion of the 2015 laser traces, which is in the removed summary.
