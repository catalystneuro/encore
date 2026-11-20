## A. Outcomes (29 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| link-units-across-tasks | reproduced | All 101 DANDI VR units and all 67 Mendeley units match distinct table rows. Gaps are ≤0.32 spikes/trial, the next-best row is ≥3.8 away, and ML positions agree (cued nb cell 8). |
| cued-delay-neurons | partially_reproduced | Valid.OdorNew flags 78 rows, matching 78 (the criterion's variant). The Mendeley file holds only 67 units, and 43 are selected at the claim seed (45 at one other seed), outside 50 ± 5. Six of the 11 flagged units missing from the file have ML <900 µm, so part of the shortfall is missing data. |
| session-trial-counts | reproduced | VR: 66 sessions (reading a, at the tolerance edge) or 62 (reading b), mean 58.8 / 59.2 trials. Cued delay: 39 sessions, mean 81.4 (cell 35). All within tolerance. |
| fig2b-anticipatory-licking | reproduced | Reading (a) onsets are 0.3, 0.5, 2.3, 7.9 s, increasing with delay for both neuron sets. Reading (b) fails (cell 14). |
| fig2c-mean-cue-response-decreases | reproduced | The mean falls monotonically under both windows at every seed, e.g. 11.68 > 8.63 > 3.70 > 2.86 spikes/s (cell 16). |
| fig2f-exponential-better-than-hyperbolic | reproduced | Mean ΔR² is +0.0197 with p = 2.2e-5, on n = 43 rather than 50 (cell 18). |
| fig2g-discount-factor-distribution | reproduced | 0.532 ± 0.227, within 0.56 ± 0.056 and 0.21 ± 0.021 (cell 20). |
| ed3f-discount-factor-reliable | not_reproduced | Gain 0.735 and γ 0.815 (selected set), or 0.555 and 0.76 (all units), are below the tolerances (≥0.756, ≥0.837). Only the baseline (0.877) passes (cell 22). |
| fig2k-reward-timing-decoded | reproduced | Data beat shuffle at all four delays under every reading and seed, with p ≤ 1.3e-11 at the claim seed (cell 25). |
| fig2k-better-than-single-discount | partially_reproduced | p < 0.05 at 1.5 s and 9.375 s, but at 3.75 s the single-discount decoder wins (p = 1, medians 1.89 vs 2.48 s) under every reading and seed. The criterion has no partial clause; two of the three delays hold (cell 26). |
| ed6e-exponential-decoding-better-than-hyperbolic | reproduced | p < 0.05 at 1.5, 3.75 and 9.375 s under the Methods baseline at every seed (cell 27). |
| ed5-behavioral-neural-discount-uncorrelated | reproduced | No mouse, window or neuron set reaches p < 0.05. The smallest is p = 0.064 (r = −0.47, m3044, M3 set) (cell 29). |
| ed5g-single-animal-decoding | partially_reproduced | m3054 beats shuffle at all four delays. m3044 fails at 9.375 s (p = 0.33 with all components, 0.074 with 12) (cell 31). |
| ed6g-decoding-matches-simulation | not_reproduced | At the claim seed only 2 of 4 delays agree with the paper (0.6 and 3.75 s). At 1.5 s p = 1.5e-10 where the paper finds no difference, and at 9.375 s p = 1. Results flip across seeds (cell 33). |
| fig3b-vr-ramp-population | partially_reproduced | Within tolerance: n = 91, p = 0.018, 51 positive, 34 negative. Outside: mean slope 0.0836 (needs ≥0.0873) and 6 non-significant (needs 5 ± 0.5) (vr_pop cell 12). |
| fig3-common-value-fit | reproduced | γ = 0.446 ± 0.237, within tolerance. The value function is convex under both readings (68% positive second differences; 100% at or below the chord) (cell 14). |
| ed8b-slope-correlates-with-discount | not_reproduced | r = 0.709 at the claim seed, below 0.729. Two of five seeds fall inside (0.755, 0.740) (cell 18). |
| ed7c-discount-not-related-to-ml-position | reproduced | r = −0.029, p = 0.79 (cell 20). |
| ed7de-gain-baseline-not-related-to-ml-position | reproduced | Baseline r = 0.027 (p = 0.80); gain r = −0.176 (p = 0.095) (cell 20). |
| ed8cd-vr-licking-not-related-to-discount | reproduced | All six correlations have p ≥ 0.31 under both window definitions (cell 22). |
| ed9g-models-agree | blocked (too_large) | No fit was run, only a timing estimate (6.7 h on 4 processes). The data are on the archive; see problem 8. |
| ed8ej-single-animal-vr-fits | partially_reproduced | Counts 31 and 23 are within tolerance, and all six r have p < 1e-5. m3044 gain r = 0.699 misses the 0.702 bound at the claim seed; it is inside at 3 of 5 seeds (single-mouse cell 5). |
| fig4a-discount-correlated-across-tasks | reproduced | n = 40, r = 0.462, one-tailed p = 0.0014 (cell 37). |
| fig4b-bootstrap-correlation | reproduced | Reading (a): 0.365 ± 0.103; reading (b): 0.345 ± 0.106. Both within tolerance with p ≈ 0 (cell 39). |
| ed10-cross-task-decoding | reproduced (fragile) | At the claim seed, reading (a) with the Methods baseline gives p = 0.014 at 9.375 s. The same decoder with a different shuffle draw gives p = 0.16, and 9.375 s passes in only 5 of 10 Methods-baseline runs (cell 41). 1.5 and 3.75 s are robust. |
| fig1f-multi-timescale-advantage | blocked (other) | A simulation; DANDI holds no simulation output. It could only be tested by running the GitHub code. |
| mixing-model-accuracy | blocked (methods_underspecified) | The sharing parameter is lost from the text and the code is not in the repository. |
| ed2e-branching-myopic-bias | blocked (other) | A simulation; nothing on DANDI. The GitHub code could be run. |
| ed2-myopic-bias-maze-lunar | blocked (other or too_large) | A simulation; nothing on DANDI. The Lunar Lander DQN part is heavy. |

## B. Problems

1. **[affects a conclusion]** `vr_single_mouse` cell 5, `cv_fit`. For ed8ej, the per-mouse fit's raw gain `a` is correlated with the population's `a/γ^0.1`. The notebook attributes this to the code, but the claims file says nothing about it, and the like-for-like comparison (`a` against `a`) was not run. The m3044 gain misses tolerance by 0.003, so this choice can decide the outcome.
2. **[affects a conclusion]** `decode` / `run_decoding`, cued cells 25, 31 and 41. M4 readings (a) and (b) give identical data decodings: the data medians match to 3 significant figures, and in my synthetic test singular values beyond about the 8th are below 0.003, so the 12-component cut changes nothing. Differences between the two readings therefore come only from the single shuffle permutation drawn per decoding. Treating them as two readings doubles the chances to pass. This matters for ed10 at 9.375 s and ed5g m3044 at 9.375 s.
3. **[affects a conclusion]** Cued cell 8 and `odor_units`. The Mendeley file holds 67 of the 78 Valid.OdorNew units, and 6 missing units would pass the ML cut. Every cued-delay statistic runs on n = 43 instead of about 50, and the session count (39) would rise if those units' sessions were added. This is missing data, not a code error, but it bears on cued-delay-neurons, session-trial-counts and ed3f.
4. **[affects a conclusion]** Cued cell 33, ed6g. There is one Poisson simulation per seed, and the p-values flip between seeds (at 3.75 s: 0.021, 1, 7e-7, 1, 0.54). The verdict is dominated by simulation noise, so neither a match nor a mismatch is informative.
5. **[does not affect a conclusion]** `split_halves`. The halves are disjoint, while the docstring says the code shares one trial between them. The notebook labels this "standard", but it is a deviation from the code. The effect is negligible at 25 to 125 trials.
6. **[does not affect a conclusion]** `cv_fit` / `CV_MAXITER` (vr_pop cells 10 and 16). The optimiser is a substitute (L-BFGS-B with variable projection, 10,000 iterations), and only 13 of 200 fits meet the tolerance. The 10k and 30k runs agree on the 20-fit subset (γ 0.445 / 0.445; slope ρ 0.720 / 0.725). At 3000 iterations the γ mean is 0.479, outside tolerance, but L-BFGS-B iterations do not correspond to fmincon's. My synthetic test reaches below the true-parameter SSE with rank recovery 0.95 to 0.99, and the analytic gradient checks out (relative error 6e-6).
7. **[does not affect a conclusion]** `vr_trial_rates`. The window is aligned on scene motion (3.05 to 7.35 s), but reward comes a median 7.31 s after scene motion onset. The last bin therefore contains about 40 ms after reward. It is excluded from the SSE (`R[:, :-1]`) but enters the z-score s.d. in `norm_psth`.
8. **[does not affect a conclusion]** vr_pop cell 24, ed9g. "too_large" is extrapolated from 20 SLSQP iterations with numerical gradients over 316 parameters. A reduced run (for example 10 bootstraps), or analytic gradients, would have tested the claim at least partially. The data are present.
9. **[does not affect a conclusion]** `rsquare` (cued cell 12). A constant held-out half gives a held-out R² of −inf, which then makes the unit's mean −inf. It only excludes that unit.
10. **[does not affect a conclusion]** `decode` returns NaN when all predictions are clipped, which produces p = NaN (cued cell 31, seed 3000). Not at the claim seed.
11. **[does not affect a conclusion]** Cued cell 8: one linked pair was recorded on different days (66 of 67 on the same day). The same-day variant in cell 37 agrees (r = 0.438).
12. **[does not affect a conclusion]** fig2b onset reading (b) gives 0.1 s for every delay because the pre-cue s.d. is close to zero (cell 14). Reading (a) carries the outcome.

All other helpers I tested on synthetic inputs behave correctly: the bounded least-squares step `_ab_given` matches brute force, `wasserstein_to_point` matches scipy, and `fit_exp` recovers its parameters. Training and test halves are kept separate in the decoders. The Tikhonov filter s²/(s²+α²) with α = 2 is consistent with Extended Data Fig. 4b's "black line at 2" on the singular values.

## C. Not checked

- **The paper's MATLAB code.** It is not available to me, so I could not verify:
  - that the per-mouse scripts store `a` while the population script stores `a/γ^0.1`;
  - the single-discount decoder (M5) details behind the reversed 3.75 s result;
  - fmincon's convergence.

  Outputs that would have helped: ed8ej with like-for-like gains, and M5 with the other half's baseline.
- **Shuffle robustness.** Several shuffle permutations per decoding, or the p-value distribution over permutations, for ed10 and ed5g at 9.375 s.
- **The six missing eligible cued-delay units.** Bounds on the selected count with them (at most 49) would settle cued-delay-neurons.
- **Several simulation draws for ed6g.** For example 10 draws, with the fraction that agree with the paper.
- **The blocked simulation claims.** The author's reasons were in the removed summary, so I classified these myself. DANDI:000251 (draft, modified 2023-06-20T00:56:22Z, 513 files, no published version) has no simulation or cued-delay files.
- **Opto-tagging on DANDI.** I did not open NWB files, so I could not check for an opto-tag column on the units. The notebook's Valid.VR cross-check (all 101 matched rows flagged) covers this indirectly.
- **ed9g.** A reduced-bootstrap run of the common reward expectation model would have allowed a partial test.
