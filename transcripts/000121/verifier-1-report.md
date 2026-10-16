**A. Outcomes** (20 claims, from the claims file; the notebook tests 19 and treats 1 as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| session-configurations | partially_reproduced | Cell 17: 8 of 12 sessions match the Methods. All 4 mismatches are R horizontal and vertical exchanged: 01-15/16 lie on the x axis, 01-17/18 on the y axis. The 5 J sessions match. |
| r-trial-counts | partially_reproduced | Cell 19, grouped by Methods dates: ring 3584 and vertical 3842 are within tolerance; horizontal 4156 (paper 3699) and 3-rings 1340 (paper 912) are not, under every reading. Grouped by geometry, 3 of 4 match, so the Methods' date labels look swapped. |
| j-sessions-complete | blocked (data_missing) | I checked the API myself: version 0.220124.2156 (and 0.210815.0703) lists 12 assets, 5 of them J. No per-session counts are in the paper, so only a lower-bound consistency check is possible, not a test. |
| delays-and-times | partially_reproduced | Cell 21. Reaction times (J 332, R 305 ms) and reach times under reading (b) (J 587, R 486 ms) are within tolerance, and R's RT–delay correlation holds (p=1.8e-205). It fails on: J's RT–delay correlation (p=0.21); R delays running to 1000 ms (bound 990, uniform to 1000); no-delay fractions of 19.8% (J) and 0.2% (R). |
| channels-task-correlated | reproduced | Cell 23: J 72 (expected 74±7.4), R 80 (expected 80). |
| pca-variance | not_reproduced | Cell 25: all 6 J values and R PCs 2–6 are within tolerance, but R PC1 is 72.8 against a lower bound of 72.9. The criterion's partial case requires all R values within, so by its letter this is not reproduced. It is a 0.14-point miss, and the result depends on the day-mean choice (the trial-window variant gives 80.5). |
| spatial-plane-variance | not_reproduced | Cell 27: at best 3 of 7 values are within tolerance under any pairing of readings (4 needed for partial). J is 40–54% against 48–68%. Shuffle p is 0.005–0.16 against the paper's <1e-4. |
| plane-timecourse | reproduced | Cell 29: divergence J 70 / R 90 ms, convergence J 270 / R 350 ms, all within ±50 ms. The divergence times are fragile (see B4). |
| onoff-predicts-kinematics | reproduced | Cell 31, reading (a): all four correlations are positive with p ≤ 0.013. R on-axis (r=0.022, p=0.013) is weak and not supported per session or in 3-rings alone (p=0.065); see B2. |
| speed-axis-within-distance | partially_reproduced | Cell 33: R 11/12 under both readings; J 6/12 (J has only its 2 vertical sessions). |
| distance-after-speed | reproduced | Cell 35: cross-validated r = 0.123 (J, p=1e-30) and 0.233 (R, p=7e-158). It also holds within the single-session R 3-rings task (p=5e-23). |
| speed-distance-projection | not_reproduced | Cell 37: ratios 1.01 (J) and 1.68 (R) against 0.5±0.1. The variant with the plane removed (0.73, 1.14) also fails. |
| single-trial-variance | not_reproduced | Cell 39: speed axis J 1.25% (out of tolerance), R 0.86% (in); plane J 15.7% and R 8.0% (both out). No partial condition is met. |
| ellipse-orientation | reproduced | Cell 41: 72% (J) and 75% (R) of conditions below 45°, one-sided Wilcoxon p = 4e-8 and 8e-10. |
| on-greater-than-off | partially_reproduced | Cell 43: 5 of 6 pairs under (a) and (c), 4 of 6 under (b). J ring fails (p = 0.31–0.69). The paper's stated default test is two-sided Welch, i.e. (b) or (c); either way partial. |
| relative-deviation-decreases | reproduced | Cell 45: all four Spearman rho are about −0.38 to −0.40 with tiny p. See B10. |
| svm-ring-and-distance | not_reproduced | Cell 47: J ring 24.7 (expected 32.2), R ring 12.9 (16.0), J distance 16.3 (18.9), R distance 17.1 (21.4); 0 of 4 within tolerance, and the tuned variant (cell 49) is also 0 of 4. Chance levels in the notebook (4.2%, 2.8%, 8.3%) follow from the target counts; the paper states no chance level. |
| svm-3rings-by-ring | partially_reproduced | Cell 51: J 23.4/34.2/42.3% all within tolerance. R 18.4/21.9/22.0% all outside. Accuracy increases from 4 to 12 cm in both monkeys (for R by only 3.6 points, with SEMs of about 2). |
| arc-error-distance-independent | not_reproduced | Cell 53: the arc-error ANOVA differs between rings (J p=2.7e-10, R p=1.5e-22). The 4 cm-range variant, which matches the Fig 4d legend, still fails for R (p=1.3e-3). |
| distance-error-and-plane-projection | reproduced | Cell 55, reading (a): J 2.505/2.801 cm and R 2.503/3.026 cm, all within tolerance; Welch p = 2.7e-7 and 4e-41. R full error is 0.001 cm inside the bound. |

**B. Problems**

1. [affects a conclusion] `_kinematics` / cell 21: the onset search runs over the whole trial before the peak, so 7–11% of trials in R's line sessions have onset before the go cue (5th percentile −16 ms). R's mean reaction time (305 ms) matches only because these are kept. The median (361 ms) and the 100–800 ms trimmed mean (362 ms) are both outside 311±31.
2. [affects a conclusion] Cell 31: deviations are taken from condition means pooled over two sessions (R ring, horizontal, vertical; J vertical and 3-rings). Session-level shifts in hand position and neural offset can then correlate. R's on-axis result does not survive per session (one session has r = −0.044) or within the single 3-rings session. Deviations from session × condition means are needed.
3. [affects a conclusion] `delay_rates` / `load_session`: the day mean is n_spikes / `recorded_s`, and `recorded_s` is the total in-trial hand time, while unit spans run to about 8300 s against 6520 s recorded (R 01-15). Whether spikes exist between trials is never checked. The R per-session median rates vary from 4.6 to 47 Hz, and the choice moves R PC1 from 72.8 to 80.5 (cell 25). This bears on pca-variance, spatial-plane-variance and single-trial-variance.
4. [affects a conclusion] Cell 29, two issues:
   - The divergence threshold sits inside baseline noise. R's D is 0.87 at −90 ms, already below the 0.9 threshold, and J diverges on D = 0.89.
   - The converged state (200 ms before go) overlaps the time-course bins of short-delay trials, roughly 45% of J trials at 270 ms, which biases convergence earlier.
   - Also, "starts at the center" is not borne out: the pre-onset state is at (−2, −30) mm for J and (18, −13) mm for R.
5. [does not affect a conclusion] Cell 33: `distance_rank` pools R horizontal (5.2 + 10.4k mm) and vertical (10k mm) targets from different sessions. Rank 12 (both at 120 mm) is still significant.
6. [does not affect a conclusion] Cell 21: `per.round(3)` runs before the p formatter, so R's per-session p values print as 0.0e+00.
7. [does not affect a conclusion] Cell 35: the per-task r for "ring" is computed on distances that are constant up to rounding (80.0x mm), so it is meaningless.
8. [does not affect a conclusion] Cells 47 and 55: the plane used for plane-projected SVM is fit on all trials, including the test folds, which leaks labels. The comparison uses an unpaired Welch test on paired errors. Both bias against the claim, which still passes.
9. [does not affect a conclusion] Cell 19: reading (b) silently drops failed trials with no go cue (delay NaN), so it is about the same as reading (a). Including them would not produce a match (R vertical by Methods dates would be 5033 against 4040).
10. [does not affect a conclusion] Cell 45: dividing a nearly distance-independent deviation (absolute rho ≈ 0.07) by distance guarantees a negative correlation, so the test barely discriminates.
11. [does not affect a conclusion] Cell 47: J ring uses 1 of 4 sessions (1020 trials), which handicaps J's accuracy. R, with complete data, also fails.
12. [does not affect a conclusion] Cell 27: 1000 shuffles cannot reach p < 1e-4 (minimum p ≈ 1e-3), but the observed p values are far above that anyway.
13. [does not affect a conclusion] Cell 49: the tuned variant picks hyperparameters on the same 3-rings trials it reports. The notebook says so.

Synthetic tests passed for `infer_config` (all four layouts), `fit_plane` / `plane_coords` (recovers x and y with r > 0.99, axes orthogonal), `on_off`, `deviations` and `_kinematics` (peak at the midpoint; onset within 20 ms; peak speed 3.5% low from the smoothing). Isotropic noise through the plane gives equal on- and off-axis deviations, so on > off is not an artefact of the construction.

**C. Not checked, and the output that would settle it**

- Spike presence between trials (B3): spikes inside versus outside trial intervals per unit, and the rate computed over trial time.
- Session confounds in onoff-predicts-kinematics and speed-axis-within-distance: correlations with deviations from date × condition means, and the within-rank correlations split per task and session.
- Robustness of divergence: the pre-onset spread of D (SD over the −200 to 0 ms bins), and d(t) against a converged state taken only from trials whose delay window does not overlap the bin.
- Whether the horizontal/vertical swap is in the paper or the conversion: the raw `.mat` files are unavailable (the Stanford link returns 403). The files are internally consistent: the hand at maximum speed lies along the target direction (cell 11).
- The paper's trial subsets (912 R 3-rings trials, the 2237 held-out trials) cannot be identified from the files.
- I read the figures' plotted ranges only, not the images.
