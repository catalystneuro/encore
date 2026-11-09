**Verifier report, round 1: Perich, Gallego & Miller 2018 on DANDI:000688 (0.250122.1735)**

The claims file has 28 claims. The notebook tests 5 and marks the other 23 blocked (data_missing).

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| methods-neuron-counts | partially_reproduced | Per-session counts fit the widened ranges for 715 of the 2002 ways to pick 9 of the 14 Monkey C candidates. Only C 2016-09-29 falls outside (PMd 114). No choice brings the pooled >5 Hz counts within 10%: M1 535–634 against 918, PMd 844–1224 against 2221 (cell 13). |
| fig3b-pmd-higher-dimensional | reproduced (fragile) | Under rule (b), window (a), FWHM kernel and the notebook's noise-of-the-average scale, PMd > M1 in 21/21 sessions with medians 9 and 13, both within tolerance (cell 15). With the SD kernel the medians are 7 and 10, outside tolerance, which would make it partial. The claims file accepts any one reading. |
| figs4d-dimensionality-robust-to-size | reproduced | The PMd mean exceeds the M1 mean at every size, both rules and both windows (cell 18). Paired sessions show PMd > M1 in every session at sizes 40–70 (cell 19). |
| figs4c-null-potent-index-centered | reproduced | Main reading (absolute values): mean 0.043 (all 21) or 0.041 (19), 0% with \|index\| > 0.9 (cell 21). One secondary combination (all 21, FWHM kernel, squares) fails narrowly: the mean prints as 0.100 and the notebook's check marks it as failing. |
| fig6c-null-leads-potent | partially_reproduced (weak) | Only 2 of 8 readings reach p < 0.05: window (a), SD kernel, at −18.1 ms (p = 0.033) and −51.4 ms (p = 0.035). Neither is within ±3.5 ms of −35 (cell 23). The FWHM-kernel and window (b) readings are not significant. The end-of-Force part cannot be tested (no Force trials). |
| fig2d-cf-behavioral-adaptation | blocked (data_missing) | No Force or Washout trials (cells 5 and 7, archive check). |
| fig7bc-vr-behavior-similar | blocked (data_missing) | No Rotation or Washout trials. |
| figs2-covariance-preserved-example | blocked (data_missing) | Needs Force and Washout blocks. |
| figs3a-covariance-like-baseline-split | blocked (data_missing) | Needs Force and Washout blocks. |
| figs3b-covariance-preserved-vr | blocked (data_missing) | Needs Rotation and Washout blocks. |
| figs5e-glm-cell-counts | blocked (data_missing) | Under M6, models are trained on the second half of Force. |
| figs5e-pot-null-similar-training | blocked (data_missing) | Same. |
| fig3e-local-rpr2-unchanged | blocked (data_missing) | Needs Early and Late Force. |
| fig3g-local-models-generalize | blocked (data_missing) | Same. |
| fig4d-null-m1-fails-early | blocked (data_missing) | Same. |
| fig4c-null-tracks-behavior | blocked (data_missing) | Same. |
| figs6-pc-m1-fails | blocked (data_missing) | Same. |
| figs6de-per-monkey | blocked (data_missing) | Same. |
| figs5f-rpr2-distributions | blocked (data_missing) | Same. |
| figs7a-unnormalized-change | blocked (data_missing) | Same. |
| figs7e-dimensionality-range | blocked (data_missing) | Same. |
| figs7f-factor-analysis | blocked (data_missing) | Same. |
| figs7cd-single-neuron-models | blocked (data_missing) | Force and Washout. |
| fig5-washout-null-m1 | blocked (data_missing) | No Washout trials. |
| fig6e-planning-change-in-null | blocked (data_missing) | Needs Force trials. |
| fig7de-vr-all-generalize | blocked (data_missing) | Needs Rotation trials. |
| fig7f-vr-washout-unchanged | blocked (data_missing) | Needs Washout trials. |
| cf-vr-dissociation | blocked (data_missing) | Every claim it depends on is blocked. |

**Archive check for the blocked claims.** I queried the DANDI API for all 111 assets. Each session is described only as "center-out" or "random target reaching task"; there are no epoch or perturbation fields. The candidate files hold 155–286 reward trials and last 13–23 minutes, which is one Baseline epoch, not a full session of at least 524 rewards. The archive does not contradict data_missing.

Under the claims' criteria, no blocked claim could be partly tested. Two Baseline-only quantities could be computed, though neither decides a claim:
- the Baseline-half against Baseline-half covariance r (the reference distribution of Figure S3);
- a Basic-model significant-cell count fit on Baseline.

### B. Problems

1. **[affects a conclusion] Session set inflates the fig6c t-test (cells 22–23).** The test pools all 21 candidate sessions, but the paper used 16 (9 Monkey C, 7 Monkey M). I re-ran it on the printed per-session lags (cell 24, window a, SD kernel) for every choice of 9 of the 14 C sessions plus the 7 M sessions. Only 38% of choices give p < 0.05 at resolution (a), and 24% at resolution (b). On the 19-session set it is 31% and 23%. "Significantly negative" therefore depends on including 5 extra Monkey C sessions.
2. **[affects a conclusion] Boundary lags in fig6c resolution (b) (cells 23–24, `cca_lag`).** Two sessions peak at −350 and −340 ms, the edge of the search range (C 2016-10-06 and C 2016-10-11). That means their correlation curves have no interior peak. These two values drive the −51.4 ms mean. The notebook neither flags nor excludes edge maxima.
3. **[affects a conclusion] Kernel width changes outcomes (cells 15, 23; `KERNEL_SD_S`).** O4 in the claims file says the kernel reading is "not expected to change an outcome". Here it decides whether fig3b's medians are within tolerance (FWHM yes, SD no) and whether fig6c is significant at all (FWHM never is). This is a wrong expectation in the claims file, not a misreading of the paper. Both claims pass only because their criteria accept "one reading".
4. **[affects a conclusion] fig3b depends on an assumption chosen after seeing results (`dimensionality`).** The 1/(2K) noise scale was adopted after the raw and /√2 scales gave 0 dimensions. The docstring says so. The scaling itself is sound: the variance of a trial difference is 2σ², while the noise in a K-trial average is σ²/K. On synthetic rank-5 data, rule (b) with this scale recovered 5. Rule (a) with the same scale gave 27, because data and noise eigenvalues are compared by rank order; this explains rule (a)'s 26–78 on real data.
5. **[does not affect a conclusion] Wrong justification for the figs4d readings (cell 17).** The markdown says the figs4d readings are "the readings of fig3b whose medians match the paper (… standard-deviation kernel …)". The readings that match use the FWHM kernel; the SD-kernel medians (7 and 10) do not. figs4d was not run with the FWHM kernel. PMd > M1 at full size with FWHM (21/21, window a) suggests the sign would hold.
6. **[does not affect a conclusion] Reduced subsampling in figs4d (cell 18).** It uses 25 subsamples instead of the claims file's 100, and 100 noise repetitions instead of 1000. With 100 repetitions, the "99th percentile" is close to the maximum. The PMd − M1 differences (1.3–3.5 dimensions, s.e.m. 0.2–0.5) make a sign change unlikely.
7. **[does not affect a conclusion] Window (b) averages are poorly aligned (`dimensionality`).** Trials are aligned on trial start and cut to the shortest trial. Because centre-hold times vary, target-locked activity smears, which probably explains the lower window (b) dimensions. Window (b) decides no outcome.
8. **[does not affect a conclusion] Seven session descriptions carry an unread warning (cell 3, `read_metadata`).** The notebook reads `experiment_description` but not `session_description`. The archive metadata for the 7 sessions from C 2016-09-09 to 2016-09-23 reads "Warning: This session with Monkey…", cut off. These are the same sessions where the cursor ends about 4.2 cm from the centre (cell 7). The tested claims use no positions, but the warning was never read.
9. **[does not affect a conclusion] Unsupported prose statement (cell 8).** For C 2016-09-23 and 2016-10-11, the markdown says "signed errors show no constant offset that decays", but no output shows signed errors.
10. **[does not affect a conclusion] Misleading pooled verdict (cell 12).** The table marks the pooled M1 count "within" using all 21 sessions, a superset of the paper's 16. Cell 13 gives the correct check.
11. **[does not affect a conclusion] Monkey M bias in the null/potent index (cell 21).** Monkey M sessions have positive per-session means of 0.08–0.14, three above 0.1. The pooled mean meets the criterion, but there is a consistent positive bias.

**Checks that passed:**
- All numbers trace to the loaded files.
- Lag sign: on synthetic data where null leads potent by 50 ms, `cca_lag` returns −0.05 s, matching the Figure 6B legend.
- `subspaces` recovers W exactly; W·null ≈ 1e−15, and potent and null axes are orthogonal.
- The FWHM conversion to SD (÷2.3548) is correct.
- The 5 Hz rate is computed over both reward-only and all trials, as the criterion allows.
- None of the tested analyses has a train/test split, so leakage does not apply.
- Target decoding is at chance (0.125) before target onset and in the shuffle, which confirms spikes share the trial table's clock.

### C. Could not check

- **fig3b medians on 16-session subsets.** Per-session dimensions are printed only for the SD kernel (cell 16). Printing the FWHM-kernel rule (b), window (a) values per session would show whether the in-tolerance medians (9 and 13) survive the choice of 9 Monkey C sessions.
- **Unrounded figs4c result.** I could not see the exact mean for the failing reading (all 21, FWHM, squares).
- **Lag curves.** The canonical-correlation curves for resolution (b) and window (b) are not plotted (only window a, resolution a). A plot would show whether those peaks are real or edge maxima.
- **The full warning text.** Reading `session_description` for the 7 warned sessions would settle what the warning says. I did not stream the files.
- **Units against the paper's sort.** Nothing in the files says whether the units are the paper's spike sort (done over all three epochs) or a re-sort of Baseline only. This bears on methods-neuron-counts.
- **Target acquisition time.** The window (a) end is taken as stop time minus the 0.5 s hold. No output tests that stop time is the end of the hold, for example by comparing it with when hand speed returns to near zero.
