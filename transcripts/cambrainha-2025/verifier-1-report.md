**Verification report, round 1: Cambrainha et al. 2025 on DANDI:000713 (0.240702.1725)**

The claims file has 18 claims. My outcomes: 3 reproduced, 2 partially reproduced, 12 not reproduced, 1 blocked. I disagree with the notebook on four of the five claims it treats as blocked (fig3c-scaling-hit-rate-higher, fig3c-hit-rate-rises-with-threshold, fig4a-active-most-scaling, figs8-halves-and-phase-order).

The main uncertainty is the surrogate chance level. The paper says the lowest surrogate kurtoses are around 6. The notebook gets a minimum of 2.80 and a 5th percentile of 3.16 (cell 17). My synthetic test of the helper gives 3.1–3.5 for independent Poisson units, so the kurtosis step as coded here may not match the paper's.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| sessions-selected | not_reproduced | All V1 units: 97 sessions and 68 mice with > 128 units (98 with ≥ 128). Default quality filters: 1 session (cell 15). The paper has 62 sessions and 44 mice; no reading of the criterion lands within tolerance. I confirmed 153 session files from 81 subjects on the DANDI API. |
| fig3a-kurtosis-broader-than-surrogate | partially_reproduced | The real windows spread more than the surrogates (IQR 1.98 vs 0.64), and some exceed κ_surr_max (real maximum 89.8 vs 34.3). The lowest surrogate kurtoses are 2.80 (minimum) and 3.16 (5th percentile), against 6 ± 0.6. That matches the criterion's partial clause. The "majority above κ_surr_max" condition fails (0.000), cell 17. |
| fig3c-scaling-hit-rate-higher | not_reproduced (notebook: blocked) | Under the adopted CV reading (a), the scaling hit rate is below the no-scaling hit rate at all 236 thresholds from 3 to 15 (e.g. κ=7: 0.615 vs 0.655; κ=12: 0.591 vs 0.642), cell 19. So any κ_surr_max up to 12.5, including the paper's ≈7, fails the test. The grid is empty only because of a few outlier surrogate windows. Only CV reading (b), which drops 83% of windows, passes. |
| fig3c-hit-rate-rises-with-threshold | not_reproduced (notebook: blocked) | Under CV (a) from κ = 3 to 12.5, the Spearman correlation is −0.64 and the hit rate falls from 0.641 to 0.587 (cell 22). From κ = 7 to 12 it is flat at 0.615–0.630, then drops to 0.591 (cell 19). |
| fig3d-relative-gain-24 | not_reproduced | Under CV (a), the largest gain over all thresholds is −1.19%; the gain at κ=12 (−7.9%) is below the gain at κ=8 (−3.0%), cell 24. No reading gives 24 ± 3% together with a rise from 8 to 12. |
| figs1-other-window-lengths | not_reproduced | Neither the 10-s nor the 60-s windows pass under any reading. 60-s gains at κ=12 are −8.1% / −3.6% (CV a); the 10-s onset is 10.55 (cell 26). |
| figs2-strict-units | not_reproduced | Session counts are 68 (good units) and 1 (default filters), against 43 ± 4.3. Under CV (a) on good units, the gain at κ=12 is −15.9% (cell 28). |
| fig4a-active-most-scaling | not_reproduced (notebook: blocked) | The NNI phase has the most high-kurtosis windows, not the fewest: at κ=7 the fractions above are NNI 0.50, active 0.31, passive 0.15. Only 16 of 97 sessions have a higher median kurtosis in active than in NNI (cell 30). Under CV (b), where a grid exists, the order holds at 0% of points. |
| fig4-exponents-active | not_reproduced | At most 2 of 4 means fall within tolerance. μ is 1.43–1.57 (paper 0.73); z is 0.10–0.17 (paper 0.3 ± 0.1), cell 44. |
| fig4-exponents-passive | not_reproduced | 48 of 48 readings fail, with at most 1 mean within tolerance. Passive z is not higher than active (0.152 vs 0.156, p = 0.37), cell 46. |
| fig4-exponents-nni | not_reproduced | 96 of 96 readings fail, with at most 1 mean within tolerance; μ ≈ 1.33 against 0.38 (cell 48). |
| fig4bc-static-exponents-trend | partially_reproduced | Holds the same way under all 144 readings: active α and β differ from trivial (p ≈ 1e-17), and the α and β orderings hold. The z ordering fails (active 0.156 > passive 0.152), cell 50. |
| figs3-exponents-stable-with-threshold | blocked (methods_underspecified) | Here the start of the threshold grid changes the outcome, and no adopted-reading grid from the paper's ≈7 was run. Under CV (b) (8.55–12), α, β and z are stable but μ has fewer than 10 sessions. On the CV (a) variant grid 4–12, NNI z departs by 0.084 against an SD of 0.056 (cell 52). |
| figs4-initial-kurtosis-poor-predictor | reproduced | Spearman 0.18 for the active phase and 0.19 for all phases pooled, both below 0.3 (cell 34). |
| figs5a-firing-rate-order | reproduced | Under CV (a), active < NNI < passive at 141 of 141 points, with ρ ≤ −0.976 in every phase (cell 36). |
| figs5c-hit-rate-firing-rate-nonmonotonic | reproduced | The below-threshold hit rate rises from 0.601 to 0.751, then falls to 0.654, with SEs of 0.037 or less. This holds under every reading and every seed (cell 38). |
| figs7-fatigue-halves | not_reproduced | Under CV (a) the gains are negative in both halves (first half −8.0% / −11.2%, second half −6.8% / −20.3% at κ 8 / 12). Only CV (b) passes, with 4–6 trials above κ=12 (cell 40). |
| figs8-halves-and-phase-order | not_reproduced (notebook: blocked) | The passive > NNI condition fails: median kurtosis is 5.53 for passive and 6.99 for NNI (a) (cell 32). Under CV (b) passive exceeds NNI at 0% of points. |

### B. Problems

1. **[affects a conclusion]** `surr_max`, cells 10–11: blocking on κ_surr_max.
   - The blocking rests on the single largest of 11,639 surrogate values. Only 5 surrogate windows exceed 15 (cell 17), and the maximum swings between 24 and 35 across seeds.
   - Windows with as few as 2 active units are included, where N_cutoff is forced to 1 (cell 7: 14 windows have fewer than 64 units).
   - The notebook never identifies which windows set the maximum.
   - For fig3c (both claims), fig4a and figs8, the outcome is the same for any grid start up to 12.5, so they should be not_reproduced rather than blocked.
2. **[affects a conclusion]** `momentum_kurtosis`: the surrogate chance level (2.8–3.6) does not match the paper's (≈6).
   - On independent Poisson data, the helper gives κ of 3.1–3.5 with covariance input and 3.7–6.7 with z-scored (correlation-matrix) input. That second reading was never run.
   - The notebook does not apply this mismatch consistently: it blocks five claims for it, but treats fig3d, figs1, figs2 and figs7, which use the same kurtosis, as tested.
3. **[affects a conclusion; claims file]** O5, used in cell 10: trial density.
   - The paper (Appendix 5) has "three to five trials" per 30-s window. The go hit/miss reading gives 0–4, median 2.
   - About 682 trials per session over 120 windows would give about 5.7 per window. This suggests the paper counted more trials, for example aborted trials as failures. O5 offers no such reading.
   - Every hit-rate claim depends on this.
4. **[affects a conclusion; claims file]** O9 and `fit_exponents`: the μ fit.
   - Both claims-file readings fit ranks 1 to K, which includes the noise floor of the spectrum. Only 1.7% (reading a) or 4.3% (reading b) of windows reach r² ≥ 0.85 (cell 42).
   - So μ rests on 44, 18 and 7 sessions (active, passive, NNI).
   - If μ fell within tolerance, fig4-exponents-active would become partially reproduced, since α (reading b) and β are already within.
5. **[affects a conclusion]** Selection, cells 7 and 15: every downstream claim runs on 97 sessions and 68 mice, not the paper's 62 and 44. This follows the claims file's main reading, but no reading recovers the paper's set.
6. **[does not affect a conclusion]** `stable_eval`, cell 52: it evaluates every 10th grid point, not every point as the criterion says.
7. **[does not affect a conclusion]** `boot_curves`: it uses 10⁴ Poisson-bootstrap resamples instead of 10⁵ resamples with replacement. This is stated; the SEs only set margins.
8. **[does not affect a conclusion]** Cell 24: reading (b) of the fig3d maximum picks points with 2–21 trials (e.g. 54.9% at κ = 39.5 from 2 trials; ∞ under CV b). None is within tolerance either way.
9. **[does not affect a conclusion]** Cell 50: test (a) compares active and surrogate session values as unpaired, although they come from the same windows. The p-values are tiny either way.

Checks that passed:
- Every number derives from the loaded data.
- On synthetic data the helpers behave correctly: Gaussian κ ≈ 3; the ISI shuffle keeps spike counts and keeps spikes inside the window; the trial swap keeps hit totals; `hit_curves` matches a brute-force count; independent Poisson gives α 1.07, β 0.95, z 0.006.
- The O3 poolings are identical, as cell 13 shows and the algebra requires.
- Rejecting CV reading (b) is reasonable: the paper calls excluded windows rare artefacts, and (b) drops 83% of windows. Reading (c) drops 1.8% and gives the same outcomes as (a).
- There is no train/test structure, so no leakage.
- The archive holds every variable the blocked claims need (spike times, stimulus blocks, trials), and the notebook read them. The blocks are about method, not data.

### C. What I could not check, and which output would settle it

- **Which surrogate windows set κ_surr_max:** a print of their N, firing rate and session, and κ_surr_max after dropping windows with N < 64 or N < 128. This decides whether the grid is really empty.
- **The blocked claims at the paper's level:** fig3c, fig4a, figs8 and figs3 run under CV (a) with the grid starting at the paper's ≈7 and at the 99th and 99.9th percentiles of the surrogate kurtosis. This would settle figs3 in particular.
- **The surrogate chance level:** momentum-space kurtosis with z-scored input, to see whether the paper's ≈6 is recovered.
- **Trial density:** hit rates with aborted and catch trials counted, plus trials per window under each reading, to compare with "three to five".
- **μ fit range:** μ fitted over the upper ranks only (for example ranks up to K/2), with its r² pass rate.
- **Figures:** I did not render the PDF, so I could not compare the real-window kurtosis distribution or the curves with Figures 3A, 3C, 4A and S8.
