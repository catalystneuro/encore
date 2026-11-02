# Verifier report, round 1: Fan et al. 2024 (DANDI:000959, version 0.261020.0242)

The claims file holds 36 claims. My outcomes: 23 reproduced, 4 partially reproduced, 2 not reproduced and 7 blocked.

## A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| design-days-per-area | reproduced | Cell 7 gives 15/15/15 days for L Eyes, 12/12/12 for T Eyes and 5/5/5 for T Mouth. Every count matches. |
| design-sessions-per-day | partially_reproduced | Cell 9: monkey L has a mean of 6.02 control runs per day, against an expected 5 ± 0.5. Every other mean, range and the duration hold (L social 10.0, range 9–11; T social 14.0, range 14; T control 5; about 296 s). |
| fig1e-stim-counts-comparable | reproduced | Cell 12: the smallest FDR-corrected p is 0.908 for stimulations and 0.942 for shams, so all exceed 0.90. |
| figs1d-stim-counts-nonsocial | reproduced | Cell 13: no corrected p is below 0.05. Not all exceed 0.10, though: shams between monkeys give corrected p = 0.082 (OFC and dmPFC). |
| figs1e-eyes-more-than-face | reproduced | Cell 16: under both readings and both event sets, the corrected p ranges from 1.1e-7 to 4.4e-5, which is below 10⁻⁴. Eyes are higher in every case. |
| figs1e-eyes-vs-rdm-comparable | not_reproduced | Cell 17: under the deciding reading (a, the day's total), Eyes exceed RDM with corrected p of 0.0004, 0.00003 and 0.0004. Reading (b, the mean per run) gives p of 0.40–0.52 (see B1). |
| fig2a-density-map-ofc | reproduced | Cell 21: the OFC stimulation-minus-sham sum is positive in the Face and in the Eyes, under both normalisations (z-score 7.47 and 3.71; total 0.0093 and 0.0046). |
| fig2c-ofc-social-gaze-distance | reproduced | Cell 23, Methods reading: combined p = 0.00021, L p = 0.0067, T p = 0.016, all with negative medians. |
| fig2c-dmpfc-accg-no-distance-effect | reproduced | Cell 25: dmPFC p = 0.21, ACCg p = 0.39. |
| fig2e-ofc-contralateral | reproduced | Cell 28, Methods reading: contralateral p = 0.00048 (negative), ipsilateral p = 0.058, contralateral vs ipsilateral p = 0.046 with contralateral more negative. Per monkey: L 0.018/0.073, T 0.012/0.30, against the paper's 0.015/0.073 and 0.012/0.204. |
| fig2e-dmpfc-accg-no-hemifield-effect | reproduced | Cell 29: all six p are 0.10 or higher. |
| fig2f-nonsocial-no-distance-effect | reproduced | Cell 31: OFC 0.22, dmPFC 0.64, ACCg 0.50. |
| fig2gh-nonsocial-no-hemifield-effect | reproduced | Cell 32: all nine combined tests give p of 0.16 or higher. |
| methods-ofc-distance-longer-windows | reproduced | Cell 34, Methods reading. 2 s: combined 0.003, L 0.012, T 0.23. 3 s: combined 0.003, L 0.007, T 0.20. |
| methods-ofc-no-change-in-fixation-number | reproduced | Cell 37, reading (a): no per-monkey test is below 0.05 (smallest 0.121). |
| methods-ofc-longer-face-looking | partially_reproduced | Cell 39 (a): all the tests hold (OFC whole Face 0.0025, dmPFC 0.80, ACCg 0.93, OFC Eyes 0.039). Under the median reading the combined (52.8 ms) and monkey L (65.1 ms) differences fall within tolerance, but monkey T's (46.2 ms, against 39.5 ± 3.95) does not. Under the mean reading none of the three falls within tolerance. |
| methods-mouth-stimulation-no-effect | reproduced | Cell 41: 0 of 27 tests give p < 0.05, and the values are close to the paper's (1, 1, 0.19; 1, 0.125, 0.19). With 5 days this test cannot fall below 0.0625, so it is uninformative (B11). |
| methods-eyes-vs-mouth-bootstrap | not_reproduced | Cell 43: the contralateral test over all Eyes days gives p = 0.078 (a) or 0.156 (b), robust across seeds (0.059–0.070). Both hemifields combined gives 0.043 (a), where the paper has 0.799, so the pattern is inverted. Neither reading satisfies the rule. |
| fig3b-ofc-inter-looking-interval | reproduced | Cell 47: OFC p = 0.044 (stimulation shorter), dmPFC 0.77, ACCg 0.34. The result is fragile (B5). |
| ili-nonsocial-no-effect | reproduced | Cell 49: OFC 0.70, dmPFC 0.13, ACCg 0.84. |
| ili-missing-trials-41 | reproduced | Cell 51: 41.3% under reading (a) and 39.9% under (b), both within 41 ± 4.1. |
| figs3b-ili-trial-level | reproduced | Cell 54: OFC p = 0.017 (stimulation shorter), dmPFC 0.39, ACCg 0.62. |
| figs3c-reciprocation-day-level-none | reproduced | Cell 58: OFC 0.11, dmPFC 0.56, ACCg 0.32. Trials with no sequence: 86.4% (a) and 85.1% (b), both within 86 ± 8.6. |
| fig3d-ofc-reciprocation-latency | reproduced | Cell 60: OFC p = 0.023 (stimulation shorter), dmPFC 0.72, ACCg 0.36. |
| partner-monkey-unchanged | partially_reproduced | Cell 62: under reading (a) of the M2 reciprocation latency, dmPFC gives p = 0.044. The criterion needs no p < 0.05 under every reading. The distance and inter-looking-interval tests, and reading (b), all hold. |
| figs4a-causal-strength-no-stim-effect | blocked (too_large) | Cell 66 estimates 680 CPU hours with PyEMD. That is plausible, but the estimate was not done for the subsets these claims actually need (B3). |
| figs4b-causal-strength-no-epoch-effect | blocked (too_large) | Same as above. |
| epoch-days-76-of-81 | reproduced | Cell 64, reading (a): 76 days, and the five excluded are exactly the dates the code names. |
| ofc-slope-unchanged-by-epoch | blocked (too_large) | Same as above. |
| fig4c-dmpfc-slope-late-greater | blocked (too_large) | Same as above. |
| fig4d-dmpfc-slope-permutation | blocked (too_large) | Same as above. |
| dmpfc-slope-positive | blocked (too_large) | Same as above. |
| fig5a-trigger-duration-unchanged | partially_reproduced | Cell 68: OFC holds (p = 0.61 / 0.36), but dmPFC triggering fixations are longer after stimulation under both readings (p = 0.019 / 0.028; paper 0.269). |
| fig5b-pupil-unchanged | reproduced | Cell 70: 0 of 70 bins below 0.05 in each area (smallest p: 0.31, 0.51, 0.11). |
| fig5cd-saccade-counts-unchanged | blocked (other) | The archive holds no saccade events. Its metadata lists variableMeasured as SpatialSeries and EyeTracking only, and the interval tables are fixations. Gaze at 1 kHz is present, so the claim could be tested after an Otero-Millan detection run. The notebook's reason, "not_runnable", is not an allowed reason. |
| fig5e-h-saccade-kinematics-unchanged | blocked (other) | Same as above. |

## B. Problems

1. **[affects a conclusion]** Claims file, figs1e-eyes-vs-rdm-comparable. The deciding reading (a) compares day totals over 10–15 social runs with totals over about 5 control runs. That comparison is bound to differ. The paper's "all p > 0.30" fits only the per-run mean, reading (b), which gives p of 0.40–0.52 here. This looks like a misreading in the claims file. I report it and have not corrected it.
2. **[affects a conclusion]** Cell 0, saccade claims. The block reason "not_runnable" is not an allowed reason. The claims file prescribes a with_inputs run of the Otero-Millan detection, the archive holds raw 1 kHz gaze for both monkeys, and the detection software is public (listed in the paper's key resources). This was not attempted or costed.
3. **[affects a conclusion]** Cell 66, causal-decomposition cost:
   - The estimate times one 100-ensemble, single-threaded PyEMD run, multiplies it by 10, and applies it to all 19,474 social trials.
   - The epoch and slope claims (ofc-slope, fig4c, fig4d, dmpfc-slope-positive) need only the first 90 stimulation trials per day. That is about 6,840 trials over 76 days, or about 2,430 for the OFC days alone.
   - Reading (b), the Yang et al. defaults, was never timed.
   - Running in parallel, or with a faster EMD implementation, was not considered.
   
   "too_large" is plausible but not demonstrated.
4. **[does not affect a conclusion]** Cell 43. The bootstrap runs only the Methods fixation reading. The opening comment says the code's M1-only reading is shown for every distance claim. Under that reading the gap is larger (contralateral: Eyes −30.2 against Mouth −1.6 px), so the variant might differ.
5. **[does not affect a conclusion]** Cell 47, fig3b. OFC p = 0.044 depends on excluding events that start at the trial sample, which applies to 91 trials. Counting them gives p = 0.058. The strict choice follows the criterion ("starts after it"), but the result sits at the threshold.
6. **[does not affect a conclusion]** Cell 68, fig5a. 29% of trials (5,695 of 19,474) have no M1 Eyes event in progress at the trial time, even though every trial was triggered online by an Eyes fixation. The clock check (cell 5) also finds only 70.8% of trials inside an Eyes event, with 65 runs below 0.5. This selection is left uninvestigated, and the failing dmPFC test depends on it.
7. **[does not affect a conclusion]** Cell 21. The x-axis label "contra <- -> ipsi for L" is reversed: for monkey L, left (negative dx) is ipsilateral (`IPSI_SIDE`).
8. **[does not affect a conclusion]** Cell 21. The ROI masks use the first social run of each day, while the distances use each run's own ROIs. Three recalibrated days are affected.
9. **[does not affect a conclusion]** Cell 37. The combined two-monkey whole-Face fixation count at 1.5 s changes with OFC stimulation (p = 0.025, reading a). That test is outside the per-monkey criterion and the paper does not report it.
10. **[does not affect a conclusion]** `signrank`. scipy uses the exact test where MATLAB uses a normal approximation for n > 15. In a synthetic check at n = 27, the near-threshold p-values moved from 0.0436 to 0.0448, 0.0463 to 0.0475, 0.0585 to 0.0593 and 0.0187 to 0.0204. None crosses 0.05.
11. **[does not affect a conclusion]** Claims file, methods-mouth-stimulation-no-effect. With n = 5 the smallest exact two-sided p is 0.0625, so this claim of absence cannot fail.
12. **[does not affect a conclusion]** `window_pairs` offsets times by run_id × 10⁶ s. This is valid only if all times lie in [0, 10⁶) s, and the notebook never prints them. The clock-check contrast (0.708 at the true times against 0.05 when shifted) indicates the pairing is correct.
13. **[does not affect a conclusion]** `reciprocation`. When a mutual event's M1 and M2 starts are equal, the stable sort places M1 first. The tie rule is unspecified. On synthetic inputs, `window_pairs`, `trial_distance`, `first_latency` and `reciprocation` otherwise gave the expected values.

## C. Not checked, and the output that would have allowed it

- **Time magnitudes:** I could not confirm the range of trial and event times that problem 12 depends on. Printing `meta.t_first` and `meta.t_last`, and the min and max of `events.start`, would settle it.
- **Saccade data in the files:** I could not confirm there are no saccade or processing tables. Printing the set of `intervals` and `processing` group names in a file would settle it.
- **Mutual-event tables:** I could not check whether `mutual_face` means the non-eye Face (excluding Mouth) as `m1_neface` does. Comparing counts of `mutual_wholeface` with the sum of `mutual_eye`, `mutual_face` and `mutual_mouth` would show this.
- **Trigger events (fig5a):** I could not tell whether the trials with no Eyes event in progress are spread evenly. A breakdown of those trials by area and trial type would show it.
- **Bootstrap under the code reading:** this was not run, so I could not judge the variant (problem 4).
- **Causal decomposition cost:** I could not judge whether the blocked claims could have been run. Timings for reading (b), and a cost for the stimulation-trial subsets per area, would show it.
- **Extra control runs for monkey L:** I could not tell whether L's 6.02 control runs per day include runs the paper did not analyse. A per-day listing of control-run numbers for the 14 L days with 8 control runs would show it.
