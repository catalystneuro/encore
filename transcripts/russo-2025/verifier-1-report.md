**Verifier report, round 1: Russo et al. 2025 on DANDI:000458 (0.230317.0039)**

Note first: the brief said the conclusion cells and summary had been removed, but they had not. Cell 0 of both notebooks still has the outcome table, and the "Result:" markdown cells are still there (main notebook cells 15 to 92; opto notebook cells 8, 11 and 14). I reached the outcomes below from the code outputs and the claims file. The claims file has 39 claims. No attempt record was among my materials.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| source-data-link | partially_reproduced | Figure 2B part holds: all five means are within 10% (cell 80: −2.0 to +9.5%). Figure 1C part fails: 10 sessions (20 under reading b) against 26 ± 3, and the medians are 16.5% and 37.2% low. |
| fig1a-tms-late-rest-active | reproduced | Means 1.379 and 0.771 uV, both within tolerance. Two-sided signed-rank p = 0.00049, rest larger in 12/12. PLF medians 0.215 > 0.165. I checked the sheet parsing against the xlsx. |
| fig1b-ieeg-late-rest-active | reproduced | Active is lower in 5/5 subjects. PLF medians 0.515 > 0.44. |
| figs2-tms-controls | reproduced | S2G p = 0.61. Rest median is above passive (1.2 vs 0.65) and cycling (0.8 vs 0.62). The posterior TMS and SSEP parts cannot be tested from public data. |
| figs2a-tms-early-component | reproduced | Medians 2.15 > 1.75, both within tolerance. The tests cannot be run from box-plot summaries. |
| figs3b-ieeg-early-no-modulation | reproduced | All four p ≥ 0.31. With five pairs this test cannot find an effect, as the criterion says. |
| fig5a-human-mouse-similar | blocked (data_missing) | The human grand averages are not public, and the Source Data sheet list has no Figure 5 sheet (I checked). |
| fig1c-eeg-late-rest-larger | reproduced | All four readings give p ≤ 0.002 with rest larger (10/10 at high intensity). |
| fig1d-lfp-late-rest-larger | reproduced | p = 0.0195 (7/9 mice) under a(i). All readings give p < 0.05. |
| fig1e-csd-late-rest-larger | reproduced | p = 0.0195 (7/9 mice). All readings give p < 0.05. |
| figs1b-mouse-plf | reproduced | LFP p = 0.0195 and CSD p = 0.027, rest larger. EEG gives p = 0.0059 (paper 0.055), which does not decide the claim. |
| figs4-intensity-dependence | reproduced | Holds under the all-channels reading: EEG and CSD significant at high and medium but not low; LFP significant at all three. It is fragile: LFP low is p = 0.039, and p = 0.055 with the file's valid channels and trials (cell 23). |
| speed-threshold-robust | partially_reproduced | EEG holds at every threshold. LFP fails at 5 cm/s (p = 0.098) and CSD fails from 0.5 cm/s (p = 0.074 to 0.36) (cell 26). The criterion has no partial clause; I call it partial because the EEG part holds in full. |
| figs5-early-component-mouse | reproduced (borderline) | EEG early p = 0.16 to 0.84. LFP is larger when active (p = 0.0195). CSD reaches p = 0.048 only under reading (b) and gives 0.055 at high intensity alone. |
| figs6-posterior-no-modulation | blocked (data_missing) | Cell 3 lists the awake electrical blocks of all 24 files: targets are MOs and SSp only. The archive metadata describes cortical stimulation only. Nothing in the claim can be tested. |
| triphasic-pattern | partially_reproduced | The pattern is present in every mouse (cell 32). The silence measures 171.5/160.8 ms under reading (a) and 57.9/71.4 ms under reading (b), against 127.8 ± 4.1. See problem 3. |
| fig2b-thalamus-leads | not_reproduced | Measure factor F = 1.41, p = 0.24. No Tukey comparison of SM-TH is significant. At rest SM-TH is 173.4 ms against 172 to 176 ms for the other measures. Only 7 mice have relay units. |
| figs7a-active-shorter-latency | reproduced | Active latency is shorter for all five measures, by 12 to 27 ms (cell 38). |
| figs7b-latency-correlation | reproduced | All four mixed-model slopes are positive, p ≤ 4e-20, from 7 mice. |
| fig3a-thalamic-rate-higher-active | reproduced (fragile) | Only reading (c) passes: per trial, 17.2 vs 13.9 Hz, p = 0.00054. Per unit p = 0.41 and per mouse p = 0.30. See problem 2. |
| figs9-mos-rate-no-modulation | not_reproduced | On the paper's test (per-mouse medians) p = 0.0117, rest larger, so the claimed absence fails. |
| figs10a-fs-trn-no-modulation | reproduced (fragile) | Under reading (c), FS p = 0.35 and TRN p = 0.88. Under readings (a) and (b), FS is lower when active (p = 0.0068 and 0.039). |
| fig3b-bimodal-isi | not_reproduced | Relay dip test p = 0.73. Median ISI is 2.6 ms and only 8 of 296 units are above 17.88 ms. k-means gives HF 278 / LF 18 with a 6.9 ms threshold. |
| figs11d-hf-earlier-less-variable | not_reproduced | HF units are later than LF (8.24 vs 6.69 ms, p = 0.00017), the reverse of the claim. The SD difference is not significant. |
| figs12-intensity-shifts-to-hf | reproduced (weak) | Responsive units go 13 → 216 → 303 and HF fraction 0.600 → 0.972 → 0.973. Per mouse, 3 of 4 mice have a higher HF fraction at high than at low intensity. The low-intensity value rests on 10 units. |
| fig3e-baseline-rate-doubles | reproduced | Pooled per-trial rate 6.82 → 14.60 Hz, both within tolerance. HF and LF both give corrected p < 1e-5, and the per-unit reading agrees. |
| fig3e-lf-synchrony-reduced | not_reproduced | No reading meets the criterion. The LF increase is significant only with the k-means split in 75–250 ms (18 LF units), and its active mean of 57.8 ms is outside 40.7 ± 8.2. With 150–250 ms, or with the paper's 17.88 ms split, LF does not change. The author's "partially" goes beyond the criterion. |
| fig3e-hf-frequency-reduced | reproduced | HF 369 → 268 Hz, both within tolerance, corrected p < 1e-5. LF p = 0.55. The per-unit reading agrees. |
| figs13-thalamic-features-predict-eeg | not_reproduced | 5 of 8 effects match under both readings. The criterion requires 8 for reproduced and 6 or 7 for partial. |
| figs13d-lf-crosscorrelation | not_reproduced | LF pairs are more correlated when active, the reverse of the criterion's direction, and HF pairs also differ (p < 1e-5). |
| discussion-orthodromic-initial-excitation | reproduced | SM-TH latency SD exceeds MOs (p < 1e-5; 7/7 mice). SM-TH vs TRN latency gives p = 0.073 by unit and 0.44 by mouse, with 18 TRN units. |
| fig2fg-opto-thalamic-inhibition-delays-rebound | partially_reproduced | All four unit delays are within tolerance. 5 of 6 signed-rank tests pass; SM-TH 75 vs 125 ms gives p = 0.20 (38 units, 2 mice). The LFP part cannot be tested because the deposit has no LFP. |
| figs8b-opto-cortical-inhibition-minimal | reproduced | All six means are within tolerance (the tolerances are wide). SM-TH shifts are −10.8 and 1.3 ms, against 47.0 and 52.2 ms with thalamic light. |
| fig2h-opto-gaba-suppresses-both | reproduced | All four tests give lower rates during the light, p < 1e-7. This depends on an alignment assumption (problem 5). |
| fig4e, fig4f, fig4hi, figs14a, figs14b (model) | blocked (other) | Not attempted. The notebook says only "not runnable" in cell 0. See problem 1. |

### B. Problems

1. **[affects a conclusion]** Cell 0 blocks the five model claims as "not runnable", with no reason or attempt shown anywhere in the notebook. The criteria ask for a rerun. The model's `stim` branch exists (`git ls-remote` shows `refs/heads/stim` 76ea885) and the figshare analysis article 25773501 resolves. The blocking is unsupported.

2. **[affects a conclusion]** fig3a and figs10a (`rate_readings`, cells 44 and 50) pass only on reading (c), which pools per-trial means across sessions in a rank-sum test.
   - Sessions contribute unequal numbers of trials and different fractions of active trials.
   - Some sessions have very few units. In 551399 the per-trial value is a single relay unit (35 Hz active).
   - So the effect may come from which sessions contribute active trials, not from state. No test within or stratified by session is shown.
   - The criterion allows reading (c), so I keep "reproduced", but the result is not robust. The per-mouse medians go in mixed directions (cell 44).
   - figs10a "adopts" reading (c) because it is the one that passed in fig3a. Under the other two readings FS is modulated.

3. **[affects a conclusion]** In `psth_shape` (cell 32), reading (b) of the triphasic silence is degenerate. With 1 ms bins and baseline rates of 3 to 8 Hz, baseline mean minus 2 SD is at or below zero in many populations, so the rate can never fall below it. That is why 6 of 16 rows give 0 to 5 ms; those are artifacts, not measurements. Relay rows give 93 to 119 ms in several mice. A version on a smoothed PSTH could land near 127.8 ms and change the outcome to reproduced.

4. **[affects a conclusion]** In the opto notebook, `delays()` (cells 7 and 10) pairs units across protocol folders by `cluster_id` and assumes the IDs come from one spike sort. This is never checked, for example by matching duration or peak channel. The per-unit delays, their SDs and all the signed-rank tests for fig2fg and figs8b depend on it.

5. **[does not affect a conclusion]** fig2h assumes `opto_5` spike latencies are timed from light onset (opto.py docstring). The sharp drop in 0 to 50 ms (38/38 relay units lower) is consistent with that, but no PSTH is shown. Separately, "all units, SM-TH, TH light" gives 7.37 → 7.15 Hz with 201/207 units lower, which implies a few units with large increases. These were not examined.

6. **[does not affect a conclusion]** figs8b uses the five MOs-light mice, while the Figure S8B legend says two. No variant restricted to two mice was run. The tolerances are wide enough that the outcome is unlikely to change.

7. **[does not affect a conclusion]** In `units_table`, TRN units are units under 0.35 ms inside the SM-TH nuclei. The 30 units located in RT (cell 7) are excluded. The paper classes TRN by spike width among thalamic units, and a reading that includes RT units was not run. This bears on the TRN parts of figs10a, fig3b and the discussion claim (18 TRN units).

8. **[does not affect a conclusion]** `mask_artifact_reversed` replaces −3.2 to +2.4 ms, not −3 to +3 ms; I confirmed this on synthetic input. That span is outside every analysis window.

9. **[does not affect a conclusion]** `gfp_peak_latency` uses all 30 EEG channels and all MOs LFP channels, including channels the file flags invalid, under both readings.

10. **[does not affect a conclusion]** Several "reproduced" outcomes rest on borderline p-values:
    - figs5 CSD: p = 0.048, only under reading (b), which counts the high and medium values of the same mouse as independent. Medians are 1.85 vs 1.87.
    - figs4 LFP low intensity: p = 0.039, and 0.055 with the file's valid channels and trials.

11. **[does not affect a conclusion]** The fig3b k-means split gives LF groups of 18 units (or 8 with the 17.88 ms threshold), unlike the paper's 700. Every downstream HF/LF claim (figs11d, fig3e-\*, figs13, figs13d) is therefore tested on groups that do not match the paper's. The notebook says this only indirectly.

12. **[does not affect a conclusion]** `responsive()` falls back to a one-spike SD when the baseline is silent. On synthetic Poisson units at 0.2 to 0.5 Hz this gives about 1.5% false positives, which is acceptable.

### C. What I could not check, and the output that would have settled it

- **Whether fig3a reading (c) is driven by which sessions contribute active trials:** rest and active trial counts and mean rates per session, plus a rank-sum within each session or a session-stratified test (van Elteren).
- **Triphasic reading (b):** baseline mean and SD per population at 1 ms, and reading (b) recomputed on a 5 to 10 ms smoothed PSTH.
- **Opto unit matching:** a table showing, for each `cluster_id`, that duration, area and peak channel agree across the ES, ES+opto and opto folders.
- **fig2h alignment:** a PSTH of `opto_5` from −200 to +200 ms per region, and the units whose rate rises during the light.
- **figs12 low intensity:** the number of units behind each mouse's HF fraction.
- **TRN:** the figs10a, fig3b and discussion results with RT-located narrow units included.
- **figs8b:** the results by mouse, to show which two mice would match the paper.
- **Model claims:** any record of an attempt to build or run the `stim` branch.
