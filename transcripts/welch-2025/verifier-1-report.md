**Verifier report, round 1: Welch et al. 2025 on DANDI:001863 (0.260806.2109)**

The claims file has 36 claims; I had no attempt record. Outcomes below follow each claim's criterion, using the code's 80 frames/s clock that the claims file fixes. No claim in the paper states a chance level.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig1b-accuracy-lower-doi | reproduced | Cell 19: n = 22, median DOI−saline −3.24 points, V = 57, p = 0.0229 (paper 0.024). The 40-trial filter drops no session (cell 3). |
| fig1c-accuracy-time-bins | reproduced | Cell 21 (rolling accuracy): saline is higher at p = 0.0076, 0.0037 and 0.0070 in the 10–25 min bins and p = 0.039 at 35–40 min; 30–35 min is not significant (p = 0.052). |
| fig1d-fewer-trials | reproduced | Cell 23: odor trials p = 0.0112 (paper 0.011), all trials p = 0.0177; DOI lower under both readings. |
| fig1d-fewer-trials-females-only | reproduced | Cell 25: females p = 0.0105 or 0.0150, males p = 0.386 or 0.444 (paper 0.011 and 0.39). |
| fig1e-repoke-no-difference | reproduced | Cell 27: n = 17, p = 0.378 (no difference, as claimed), median difference −0.097 repokes per ITI. |
| iti-false-report-no-difference | reproduced | Cell 29: p = 1.0 under both readings; 6 false reports in 3,227 ITIs. The Results' reward-port variant cannot be run. |
| fig2a-correct-port-duration-doi-odor | blocked: data_missing | There are no reward-port entry or exit events (cell 31). The trial stop time is quadrant entry, not a port poke. Archive check under item 4 of this report. |
| fig2a-supp-no-sex-effect | blocked: data_missing | As fig2a. |
| fig2b-median-port-duration-correct | blocked: data_missing | As fig2a. |
| fig2b-supp-odor-trials-longer | blocked: data_missing | As fig2a. |
| fig2b-supp-omission-no-difference | blocked: data_missing | As fig2a. |
| fig2c-incorrect-port-duration | blocked: data_missing | As fig2a. |
| fig2c-supp-no-sex-difference | blocked: data_missing | As fig2a. |
| fig2d-median-incorrect-no-difference | blocked: data_missing | As fig2a. |
| fig2d-supp-omission-longer | blocked: data_missing | As fig2a. |
| fig3a-odor-trial-duration-longer | reproduced | Cell 34: DOI longer by a median 0.26 s, p = 5e-6. |
| fig3a-omission-duration-no-difference | reproduced | Cell 36: p = 0.32 (no difference, as claimed), median difference +0.55 s. |
| fig3b-iti-duration-no-difference | reproduced | Cell 38: p = 0.098 (no difference, as claimed; paper 0.19), median difference +1.4 s. |
| fig3c-speed-within-trial-lower | not_reproduced | Cell 42, code clock: the signed-rank test gives p = 0.063 (DOI lower in 16 of 22 mice), above the 0.05 cut; the criterion has no partial outcome. The rank-sum variant gives p = 0.51 and the fitted clock p = 0.82. |
| fig3d-speed-iti-lower | not_reproduced | Cell 44, code clock: signed-rank p = 0.079; rank-sum p = 0.57; fitted clock p = 0.063. |
| fig3supp-odor-trial-speed-no-difference | reproduced | Cell 46: signed-rank p = 0.187 (no difference, as claimed); fitted clock p = 0.68. |
| fig3supp-doi-iti-slower-than-odor | reproduced | Cell 48: the ITI is slower by a median 0.83 cm/s, p = 0.0002; the fitted clock agrees. |
| fig3supp-doi-omission-no-difference | partially_reproduced | Cell 50, code clock: odor vs omission p = 0.31 (no difference, as claimed), but ITI vs omission p = 0.0059 (a difference). Under the fitted clock both are significant, which would make it not_reproduced. |
| fig3supp-saline-iti-slower | reproduced | Cell 52, code clock: ITI vs odor p = 0.025, ITI vs omission p = 0.016, ITI slower in both. |
| fig3supp-saline-odor-omission-no-difference | reproduced | Cell 54: p = 0.68 (no difference, as claimed), median difference −0.18 cm/s. |
| fig4abc-sniff-frequency-higher | reproduced | Cell 58: 14 DOI and 13 saline sessions, as expected. DOI mean is higher; Z = 25.2, 28.4 and 19.5 under the three readings (paper 24.9); permutation p < 1e-4. |
| fig4supp-ks-every-mouse | partially_reproduced | Cell 60: 13 matched mice. p < 0.001 in 13 of 13 under reading (b), but in 11 of 13 under reading (a) and the code reading (mice 2209 and 2211 have p = 0.003 and 0.006). The criterion has no rule for choosing between readings. |
| fig4d-sniff-frequency-by-period | reproduced | Cell 62: DOI higher in odor trials, omission trials and ITI under every reading; Z = 4.31, 3.88 and 24.2 under reading (a), resampled p < 1e-4. |
| fig4e-median-sniff-no-difference | reproduced | Cell 64: p = 0.110, 0.147 and 0.110 (no difference, as claimed; paper 0.11); median difference +0.53 Hz. |
| fig5ab-occupancy-similar | reproduced | Cell 68: no measure differs at p < 0.05 (entropy p = 0.063, 5 cm corners p = 0.25, 10 cm corners p = 0.70). The two grand-mean maps correlate at r = 0.92. |
| htr-event-link | reproduced | Cell 70: the series is in 22 of 22 DOI sessions; all 10 mice that have it in both sessions have more events on DOI. |
| fig5supp-htr-within-trial-x-not-y | reproduced | Cell 73, code clock and code timestamps: x r = +0.056, p = 0.005; y p = 0.26. The other two timestamp readings agree; the fitted clock does not (x p = 0.96). |
| fig5e-htr-combined-x | reproduced | Cell 75: 22 mice, x r = +0.149, p < 1e-4, under every reading and both clocks. |
| fig5supp-htr-iti-x | reproduced | Cell 77: x r = +0.15, p < 1e-4; y p = 0.55. |
| fig5f-htr-rate-trial-vs-iti | reproduced | Cell 79, code clock: p = 0.50 (no difference, as claimed), median difference +0.18 HTR/min. The fitted-clock variant reverses this (problem 1). |
| fig5supp-htr-no-sex-difference | reproduced | Cell 81: p = 0.307 (paper 0.31); female median 3.61, male median 3.99 HTR/min. |

Tally: 24 reproduced, 2 partially_reproduced, 2 not_reproduced, 9 blocked (data_missing).

### B. Problems

1. [affects a conclusion, in how the result should be read; the outcomes above follow the criterion] **The tracking and HTR times probably do not share the trial table's clock under the 80 frames/s timing.**
   - **Evidence (cells 8–9):** under the code's clock the nose moves a median 0.3 px (first cohort) and −3.4 px (later cohort) over a trial. Under a fitted clock it moves hundreds of px, and shifting the trials by 30 s removes that again. Fitted rates are about 73.7 frames/s in the first cohort and 80.5 in the later one; a ~2 s trial cannot survive offsets of a few seconds.
   - **What depends on it:** every split of frames or HTRs into trial and ITI (fig3c/3d and the speed supplement, fig5supp within-trial and ITI, fig5f).
   - **The variant changes outcomes:** fig5f flips to trial rate below ITI rate, p < 1e-4; fig5supp within-trial x goes to p = 0.96; fig3supp-doi-omission would be not_reproduced.
   - **Caveats on the fit:** it maximises the very statistic used to judge it, so it is somewhat circular. Its quality flag also passes an implausible 71.0 frames/s fit for 2204 DOI (191,703 frames would span 2,700 s, longer than the session). The fit is evidence, not proof.
   - The clock comes from the claims file (from the code), not from the notebook's author, so the criterion's outcomes stand.
2. [does not affect a conclusion] **`r_signrank`** drops zero differences and then uses the exact test. R falls back to the normal approximation when zeros are present. On synthetic data with one zero this gives p = 0.275 against R's approximate 0.268. None of the tested pairs appears to have a zero difference (checked on the trial counts, accuracies and sniff medians).
3. [does not affect a conclusion] **fig4supp-ks-every-mouse.** In reading (a), 5 of 13 mice (2202, 2204, 2208, 2209, 2211) have a lower DOI median than saline, yet the one-sided KS test is significant. The code's test does not establish the "higher-shifted distribution" the statement describes. The criterion follows the code, so this is reported, not corrected.
4. [does not affect a conclusion] **Figure 2 blocked status rests on one file.** Cell 31 lists the HDF5 groups of only `sub-2200_ses-2200-14.nwb`. For all 44 files, `load_session` reads only known paths. The archive API gives no content-level metadata (`variableMeasured` is only "ProcessingModule"), the asset sizes are uniform within each cohort, and the dandiset description names no port events. A DLC-proximity proxy would not be the Methods' beam-break measure, so no part of Figure 2 is faithfully testable; blocked (data_missing) is right.
5. [does not affect a conclusion] **fig5ab, `occupancy_measures`.** The arena box comes from the pooled 0.5–99.5 percentile positions, 27.5 × 15.6 cm at 0.0237 cm/px. Two 10 cm squares overlap across the 15.6 cm height, so the "10 cm corners" cover about 85% of frames and say little about corner use. This is a weakness of the claims file's reading; the outcome holds on the other measures.
6. [does not affect a conclusion] **Fitted-clock speed variant (cell 40).** Speeds are still scaled by 80 frames/s while frames are labelled with the fitted rate. In the first cohort the DOI and saline fitted rates of a mouse differ by up to 4% (2185: 74.58 against 71.67), a small bias in the paired variant.
7. [does not affect a conclusion] **Nose likelihood.** 40–91% of nose frames are below 0.95 and interpolated (cell 8), so speed is mostly computed on interpolated track. The interpolated fraction is not biased by condition: DOI minus saline is positive in 11 of 22 mice (my count from cell 8).

### C. What I could not check

- **Group listing of every NWB file.** That would confirm that no reward-port or extra event series exists in any file for Figure 2 and the Results' false-report variant. Only one file's groups were printed.
- **R parity of the statistics** (signed-rank, rank-sum, `coin::oneway_test`, `ks.test`) and of `clean_nose` against the authors' `CleanTracking`. No R or reference outputs were available. A run of the authors' R code on one session would settle it.
- **Which clock the HTR series uses.** Nose speed or head-keypoint acceleration around HTR times, under the code clock and the fitted clock, would show which one the series is on. HTRs are fast head movements, so the right clock should show a speed peak at the event.
- **The sniff files' descriptions** of the rows dropped for a missing exhalation. The notebook asserts this but never prints `sniff_description`.
- **Whether the fitted clock is plausible against the video length.** Printing the session span each fit implies (frames ÷ fitted rate) would expose fits like 2204 DOI.
