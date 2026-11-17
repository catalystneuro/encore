# Verifier report, round 1: Saez et al. 2018 (doi:10.1016/j.cub.2018.07.045) on CRCNS ofc-3

The claims file has 28 claims. The notebook tests 22 and marks 6 blocked. My own outcomes: 6 reproduced, 6 partially reproduced, 10 not reproduced and 6 blocked. The mixed-effects result is provisional because some readings were not run.

I checked the helpers on synthetic inputs and they behave correctly:
- **`encoding_scan`**: its p < 0.05 flags match `scipy.stats.linregress` in every window. It detects an injected effect, and its shuffled false-positive rate is 0% on white noise and 5.8% on smoothed noise.
- **`longest_run` and `run_bounds`**: both give the right answers.
- **`glmm_logit`**: the slope matches a fixed-effects logit (4.08 against 4.09, standard error 0.174 against 0.175) and recovers the true value of 4.

## A. Outcomes

| claim | outcome | reason |
|---|---|---|
| methods-electrode-trial-counts | partially_reproduced | 10 patients. 192 electrodes once the 7 copies found in both arrays are removed (191 analysed, cell 18). Timeouts are 99 of 1,938 rounds = 5.11%, outside 9.98 ± 0.998. s10 played 138 rounds, not 200. |
| behavior-risk-neutral | reproduced | Readings (a) and (b) give 54.9% and 55.1%, within 55.9 ± 8.5. A risk-neutral chooser would gamble on 53.0% (cell 20). |
| fig1c-choice-win-probability | reproduced | Slope 4.79 (p = 1.5e-86) with random intercept and 5.75 (p = 6e-70) with random slope (cell 22). |
| figs2a-choice-gamble-ev | reproduced | Slope 0.163 per $ (p = 2e-69) and 0.161 per $ (p = 4e-45) (cell 24). |
| fig1c-patients-like-controls | blocked (data_missing) | The archive's file list has no healthy-participant data. |
| figs2b-rt-conflict | not_reproduced | Patients: pooled trials p = 0.165, paired over patients p = 0.104 (cell 26). The healthy-subject part is blocked (data_missing). |
| regressors-past-current-uncorrelated | not_reproduced | Under every reading the mean R2 is 0.21–0.59% and the maximum 0.64–2.29%, against 2.1 ± 0.21 and 3.7 ± 0.37 (cell 30). The past and current regressors are even less correlated than the paper says, but the numbers fail tolerance. |
| figs6a-regressor-collinearity | reproduced | With the 8 current regressors, the mean R2 is 0.1648 averaged over patients or 0.1551 pooled (within 0.15 ± 0.015). The largest R2 is 0.570 (cell 32). |
| fig3-present-encoding | not_reproduced | All 8 counts are outside tolerance (for example risk 84 against 50). Chosen value has 41 electrodes, below its shuffled 95th percentile of 50, so the "partial" condition fails too. The peak timing and per-window share conditions hold (cell 36). |
| fig3-latency-duration-similar | reproduced | With outcome reveal at time 0 of the buttonpress epoch, delays give p = 0.235 (reading a) and 0.301 (reading b), and durations give p = 0.207 (cell 38). Under reading (b) the choice delay is 512.5 ms, exactly the paper's value. Under the claims file's timing (reveal 550 ms after the epoch's time 0) the delays differ (p < 0.001 and p = 0.006). |
| hfa-more-than-fp | blocked (data_missing) | There is no broadband signal in the archive. The HFA half can be tested: the mean is 33.3%, outside 20.9 ± 2.09 (cell 40), so this claim would fail even with the broadband data. |
| figs4b-power-at-buttonpress | blocked (data_missing) | There is no broadband signal. The HFA half can be tested: the outcome %EV peaks 800 ms after reveal, within 750 ± 75, under the notebook's alignment (cell 36). |
| fig4-past-encoding | partially_reproduced | All 8 counts are outside tolerance. Past risk has the lowest count (40), and the other 7 past regressors are above their shuffled 95th percentile (cell 40). |
| fig5-past-sustained | partially_reproduced | Under epoch reading (a), both past means exceed both current means with all four p < 0.01 (1.5e-3, 8e-7, 8.8e-3, 8.9e-6), but none reaches p < 1e-6. All means are far below the paper's, for example past outcome 670–820 ms against 1,341 ms (cell 42). |
| behavior-past-no-effect | not_reproduced | Under reading (a), past risk (p = 0.015), past chosen value (p = 0.039) and past RPE (p = 0.047) are below 0.05 (cell 56). |
| fig6-past-short-lived | reproduced | Lags t-2 to t-5 are lower than t and t-1 under both readings (p from 3e-10 to 2e-4). The mean proportion at each of t-2 to t-5 (16.6–19.4%) is at or below the shuffled 95th percentile, about 20.6% (cell 44). |
| figs5d-sharp-boundary | reproduced | Pooled over regressors: t-2 against t-1 p = 2.6e-29, t-1 against t p = 0.97. This pattern holds for 7 of 8 regressors. The test direction matches the criterion (cell 46). |
| mixed-effects-robust | not_reproduced (provisional) | No reading run gives all 16 regressors corrected p < 1e-4. The best is 14 of 16, one model per window (past chosen value 6e-3, past risk 3e-3). Several readings were not run (B1). |
| figs6b-stepwise-similar | partially_reproduced | Following the criterion: Spearman rho = 0.77 (p < 0.001) passes reading (a); the largest difference, 48 points, fails reading (b). In substance the two selections are not similar: stepwise selects 0–2.1% of electrodes against 21–50% (cell 58). |
| figs3a-risk-all-trials | not_reproduced | Peak %EV is 2.32 over all trials against 3.12 on gamble trials only (cell 48). This comparison is confounded by trial count (B6). |
| figs3b-no-motor-encoding | reproduced | 31 electrodes encode left/right, below the shuffled mean of 34.7 and the 95th percentile of 49 (cell 50). |
| anatomy-brodmann-counts | blocked (data_missing) | The archive's file list and data description have no electrode locations or area labels. |
| fig7-all-areas-similar | blocked (data_missing) | Needs the electrode area labels, which are not deposited. |
| no-anatomical-gradient | blocked (data_missing) | Needs electrode coordinates, which are not deposited. |
| tables2-patients-coverage | not_reproduced | Every regressor is present in at least 6 patients, but the mean is 8.62, 8.80 or 10.00 across the three readings, against 7.41 ± 0.4. It also does not match the 7.75 counted from Table S2 (cell 52). |
| fig7f-multiplexing | not_reproduced | Stepwise selection gives 0 and 0. The five-window variant gives 166 and 65, against 132 ± 13.2 and 30 ± 3 (cell 60). |
| figs7-present-past-overlap | not_reproduced | Stepwise selection gives 0 electrodes encoding both present and past. In the five-window selection, choice is not overrepresented (99 against 99.9 expected) and outcome gives p = 0.047, not < 0.01. The counts are far from 39 and 43 (cell 62). |
| fig2-example-electrodes | reproduced | 44 of 84 risk electrodes have a significant negative quadratic term, and 64 of 64 regret electrodes a significant slope (cell 54). The regret half holds by construction (B7). |

## B. Problems

1. **[affects a conclusion]** Cells 63–66, mixed-effects-robust. The claim needs only one reading to pass, but not every combination of readings was run:
   - One model per window (time point a) was fit only with all electrodes and one regressor at a time.
   - It used an electrode-only random intercept instead of electrode nested in patient, which is a stated deviation.
   - Per-window models restricted to encoding electrodes (electrodes b), and all 16 regressors together (regressors b), were never fit.
   - Restricting to encoding electrodes lowered p sharply in the time-averaged fits. The two failures (3e-3 and 6e-3) could plausibly pass in an unrun combination, so the outcome is not settled.
2. **[affects a conclusion]** Cells 11–13, baseline. The claims file names two baseline readings; neither was applied. The deposited game epoch is corrected over [-1000, -800] ms, a pre-fixation window that is neither reading. The cell-13 check that both epochs come from one corrected trace uses the SD of the difference between overlapping samples, which ignores constant offsets. So it does not show that the buttonpress epoch was corrected per trial at all; its first window has trial-to-trial SD of about 4–5. The 1-kHz data would let both readings be run. They could move the encoding counts behind fig3, fig4, fig5, tables2 and fig7f.
3. **[does not affect a conclusion]** Cells 14–16 and 38, alignment of the buttonpress epoch. Reading its time 0 as outcome reveal decides fig3-latency-duration-similar; under the claims file's +550 ms timing it fails. I find the reading well supported:
   - the epoch's time 0 falls 470–600 ms after the csv button press;
   - the gamble outcome becomes encodable from about 250 ms;
   - the Figure 3C legend says "time locked to gamble outcome (t = 0)";
   - reading (b) gives the paper's 512.5 ms choice delay.

   Against it, the csv's `reveal.time` is about 40 ms after the press. The notebook does report both timings.
4. **[does not affect a conclusion]** Cell 58, stepwise selection. The implementation follows STAR Methods and passes its synthetic check. Taking the larger of the two epochs' sums is a stated assumption. Its near-empty result (16 of 191 electrodes) is what makes fig7f and figs7 fail under the stepwise reading. Spearman's rho is computed on proportions that are mostly 0, so reading (a) of figs6b passes only formally.
5. **[does not affect a conclusion]** Cell 26, figs2b. The pooled t test is dominated by s10, whose reaction times reach 80 s with no timeouts, against the paper's 2-s limit. Without s10 the pooled p is 2.2e-6, but excluding s10 is not a reading the claims file allows, so the outcome stands. The flag is about sensitivity. Defining RT as `buttonpress.time` minus `choice.time` is an inference from the data.
6. **[does not affect a conclusion]** Cell 48, figs3a. The criterion compares raw peak %EV, and gamble-only trials are about 55% of the trials, so their R2 is inflated under the null (shuffled peak 2.30 against 1.25). After subtracting chance, all trials would come out higher (1.07 against 0.82). The outcome follows the criterion, but the comparison itself is confounded.
7. **[does not affect a conclusion]** Cell 54, fig2. The regret test is circular: electrodes selected for regret encoding necessarily have a significant slope at their peak window. For risk, 40 electrodes show a significant upright U against 44 inverted.
8. **[does not affect a conclusion]** Cell 30. R2 is computed on the 1,753 HFA trials, not the 1,839 non-timeout trials the criterion names. The values are 5–10 times below the expected ones, so this cannot change the outcome.
9. **[does not affect a conclusion]** Cell 11. s03 electrode 42 is dropped, giving 191 electrodes against the paper's 192. It holds no data of its own, and the effect on counts is negligible.
10. **[does not affect a conclusion]** The claims file may misread the paper on chance. STAR Methods says the shuffled distribution "was taken as the null for that particular regressor-electrode combination", which describes a per-electrode null. The claims file uses only the share of electrodes classified as encoding under shuffles. The notebook's "own-null variant" follows the paper's sentence; its counts still miss tolerance on 7 of 8 current and 7 of 8 past regressors.

    The selection's false-positive rate under shuffles is 18.2% of electrodes (cell 36), close to the paper's mean of 20.9%. Table S2 may therefore not be the plain five-window count, which would explain the count mismatches.
11. **[does not affect a conclusion]** `align_trials`. Matching HFA trials to rounds is greedy. It is verified only through zero mismatches on the current and t-1 values; the t-2 to t-5, left/right and gamble-outcome regressors depend on it unchecked. A misalignment is unlikely.

## C. What I could not check

- **Variables in the .mat files.** The notebook never prints the variable names in `sXX_ofc_hg_events.mat`. Through range requests I read only the zip directory: `data.zip` holds 10 HFA .mat files and 11 csv files, and `ofc_behav_data.zip` holds 10 regressor files. That supports the blocked claims, but a listing of `d.keys()` in `load_hfa` would confirm there are no channel labels or coordinates.
- **Buttonpress-epoch baseline.** I could not tell whether the buttonpress epoch is baseline-corrected per trial. Printing the mean difference (not only the SD) at the best shift in cell 13 would settle it.
- **Unrun mixed-effects readings.** The per-window models on encoding electrodes only, and with all 16 regressors together, would settle mixed-effects-robust.
- **Whether HFA trials are timeout-free.** The 185 rounds without an HFA trial include all 99 timeouts, but nothing shows the HFA trials themselves exclude any. A per-trial `round` column in the HFA-trial table would confirm the alignment directly.
- **Figure images.** Outputs are text only (cell 36's figure is an image I did not inspect), so the per-window bar profiles were judged from the printed peaks.
