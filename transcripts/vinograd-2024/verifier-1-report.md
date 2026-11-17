**Verifier report, round 1: Vinograd et al. 2024 on DANDI:001037 v0.260609.1402**

The claims file has 54 claims. The notebooks test 27 and block 27, of which two (methods-cvr2 and fig4ce) were run and then blocked. My outcomes: 8 reproduced, 10 partially reproduced, 10 not reproduced, 26 blocked. The dandiset has 7 two-photon (2P) mice where the paper has 9 or 8, and 4 to 7 mice in the stimulation sessions.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| ed1n-engaging-x1-slower | not_reproduced | x1 is slower than x2 in 3/5 mice. Mann-Whitney p = 0.093 (seed 0), 0.75 (the sample code's best-of-four seeds) and 0.14 (states chosen by cross-validation). The other two mice have a complex slow state, so x1 and x2 tie (rslds cell 10, CV cell 9). |
| ed1p-observing-x1-slower | not_reproduced | x1 slower in 3/5 mice; p = 0.21, 0.40 and 0.21 across the same three readings. |
| ed1m-x1-observe-attack-vs-sniff | blocked (data_missing) | `watch_sniff` is annotated in M30L only (rslds cell 3). One mouse cannot be tested. |
| ed3c-x1-activity-observe-vs-engage | reproduced | p = 1.0 (seed 0) and 0.84 (code seeds); mean difference +0.05 z (cell 15). |
| ed3e-achw-full-session | not_reproduced | Whole session: 40.8 vs 27.0 s, Mann-Whitney p = 0.016. Entry to last removal: 9.9 vs 14.9 s. No reading lands within 25±0.8 / 20±1.7 s (cell 17). |
| ed3f-achw-after-removal | partially_reproduced | The difference is not significant (p = 0.095 and 0.125), but 12.7 and 8.7 s are both outside the 14±1 and 11±1.6 s tolerances. |
| ed3g-decode-observed-attack | reproduced | p = 0.0079 under all three splits with seed 0, and under 2 of 3 splits with the code seeds (cell 20). |
| ed3h-decode-engaged-from-observed | partially_reproduced | p = 0.0079 with seed 0 under both weight readings. With the code seeds p = 0.15 under both, because one mouse is below chance (cell 22). The result depends on the fit. |
| ed4c-x1-neuron-overlap | not_reproduced | Mean overlap 4% against 70±7%; chance is 7% (cell 25). |
| ed4d-weight-dot-product | not_reproduced | p = 0.22 (raw and absolute, seed 0) and 0.55 / 0.69 (code seeds); x1·x1 is larger in only 3/5 mice (cell 27). |
| ed4g-x2-more-spontaneous | not_reproduced | No reading gives x2 > x1 (p = 0.40 to 1.0, cell 30). This is on about 1 min of pre-annotation activity, not the criterion's 5 min baseline (problem 5). |
| ed4hi-amplitude-tau-similar | partially_reproduced | No difference under any reading (all p ≥ 0.125). Amplitudes are 1.5 to 2.3 z against 0.58 / 0.71 expected, and decay constants run into the fit bounds (cell 32). |
| fig1e-2p-x1-slower | not_reproduced | x1 slower in 5/7 mice; p = 0.37, 0.096 and 0.31 (CV). Seven mice could reach p = 0.0006 (cell 35). |
| fig1f-line-attractor-score | partially_reproduced | The mean score is positive (0.83 / 1.32), but it is above 0 in only 5/7 mice. |
| x1-time-constant-range | partially_reproduced | The 2P median is 114 s, inside the range; 5/7 fits lie in 45 to 220 s (cell 37). |
| methods-subspace-angle | reproduced | 88.55° against 87.23 to 88.97°, n = 7 (cell 10). |
| methods-cvr2 | not_reproduced (the notebook says blocked) | The criterion's contiguous-block reading ran. Neural R2 is −81% / −75% against the block mean, 12.5% / 19.8% against the session mean, and hugely negative for the latent R2, against 84.7 / 67.2% (CV cell 7). The random-frame reading was not run (problem 4). |
| fig1m-achw-x1-longer | reproduced | x1 is longer in 7/7 mice. Signed-rank p = 0.0156; unpaired p = 0.165. The claims file accepts both readings (cell 12). |
| fig2d-x1-integration | reproduced | Wa/Wb with Ca: 3 of 4 Dunn comparisons significant; ISI1 to ISI3 rises 1.82 → 3.22 (cell 14). |
| fig2gh-x1-moves-along-attractor | partially_reproduced | The rises hold, but no reading gives ≥3/4 significant comparisons for both metrics. Best reading (mean baseline, comparison a): 2/4 at stimulation end, 3/4 at ISI end (cell 17). |
| ed7f-activated-x1-natural-levels | not_reproduced | p = 0.097 with M70 included. M70's target list is shown invalid in cell 7, and without M70 the printed values give p = 0.0043 with activation higher in 6/6 mice (problem 1). |
| ed8a-x1-integration-8s | reproduced | 3/4 comparisons significant, rise 1.86 → 3.23, n = 6 (cell 21). |
| ed8ef-x1-scales-with-power | blocked (data_missing) | There are no 1 mW sessions (session list, cell 3). |
| ed8c-model-integrates | partially_reproduced | The criterion is met nominally: rises in 7/7 mice under reading (b). But there is no no-pulse control, M70's "rise" is relaxation from −5.4, the fit to data has median R2 −1.32, and reading (a) falls (cell 40; problem 2). |
| ed8gi-x1-stim-no-x2 | not_reproduced | 1/4 comparisons significant (p = 0.036, Wa and Wb with Ca; cell 23). Dropping M70 removes it (problem 10). |
| fig2k-x2-no-integration | reproduced | 0/4 significant under all readings (cell 25). |
| ed8b-x2-no-integration-8s | partially_reproduced | No rise across ISIs, and 0/4 significant under Wa but 1/4 under Wb. Activity stays at 1.5 to 1.9 z against a 0.1 baseline in all 4 mice; n = 4 (cell 27). |
| ed8jl-x2-stim-little-x1 | reproduced | 0/4 significant, and smaller than under x1 activation in every ISI (cell 29). |
| fig2no-x2-off-manifold | partially_reproduced | Relaxation holds (0/4 significant at ISI end; ISI-end distance 1.86 < 2.28 at stimulation end). The off-manifold movement reaches only 2/4 at stimulation end, against the ≥3 required (cell 31). |
| ed9d-attractor-finite | partially_reproduced | (a) Whole trace p = 0.038, but after the third pulse p = 0.26. (b) The pattern holds for the mean but in only 2/7 mice (cell 33). |
| ed9i, ed9mn | blocked (data_missing) | The sessions are absent (cell 3). |
| ed5e, ed5hj, ed6g | blocked (data_missing) | No video, motion SVDs or calibration recordings. The archive's asset metadata lists only ProcessingModule and BehavioralEpochs, and the files are 2.4 to 9.7 MB. |
| ed6k, ed7bc, ed10c | blocked (data_missing) | No ImageSegmentation in the archive metadata. For ed10c, a partial test without the 50 µm exclusion was possible and was not run. |
| ed10g-follower-decoding | blocked (other: testable, not run) | Its criterion needs no 50 µm exclusion. Non-targeted neurons are those not in `ActivatedNeurons`, which the files have (problem 3). |
| ed10hi, ed10lm, ed10p, ed10r, fig3d, fig3e, fig3i, fig3j, fig4a, fig5g, ed12, fig5f, ed12eh | blocked (data_missing) | There are no unitary stimulation sessions (cell 3). |
| fig4ce-excitatory-network | blocked (methods_underspecified) | With the Methods' weights, λmax stays at about 0.50 over 0 to 20% density, so the model is never unstable. Fig. 4c shows unstable regions, so the Methods omit some scaling (network cell 5). |
| fig4hj-inhibition-slow-dense | blocked (other: testable, not run) | The criterion uses the paper's printed 36% and no recorded data, so the dependency on fig4a does not block it (problem 3). |

**B. Problems**

1. [affects a conclusion] ed7f (stored notebook, cell 19) includes M70, although cell 7 shows M70's listed x1 targets do not respond (−0.01 z) and rank 33rd to 55th by weight. Cell 8 keeps M70 "as the projections do not use the target list", but ed7f does use it. A 0- versus 1-based offset in `load_2p` for M70 was never tested.
2. [affects a conclusion] ed8c (rslds cell 40, `simulate`):
   - There is no simulation with the kick set to zero, so the ISI-end rise is not shown to come from the pulses. It could be drift toward the model's fixed point; M70 starts at −5.41 and drifts upward.
   - The criterion's reading (b) is close to circular: adding equal kicks along a slow mode always accumulates. This is a weakness of the claims file.
3. [affects a conclusion] fig4hj and ed10g are blocked on reasons their criteria do not contain: a dependency for fig4hj, and the 50 µm exclusion for ed10g.
4. [affects a conclusion] methods-cvr2 is labelled blocked, but a reading the criterion names ran and missed by more than 50 points. Separately, the held-out latents are inferred from the held-out activity itself (`_cv_job`), so the score is a reconstruction, not a prediction.
5. [affects a conclusion] ed4g and ed4hi (cell 30) use the time before the first annotation, about 1 min, as the baseline. The criterion's window is the 5 min solitary baseline, which the files do not hold; the ED Fig. 4e legend suggests separate baseline recordings. The notebook states the substitution but not as an assumption that qualifies the outcome. The expected amplitude of 0.58 z is below the 1.5 SD detection threshold, so the paper measures amplitude some other way.
6. [affects a conclusion] The `linattr` header lists a seed as a "standard" choice that cannot change a result. Here the seed decides the outcome: ed3h p = 0.0079 vs 0.15, ed3g's train-on-one-trial split, fig1e p = 0.37 vs 0.096. Both seed readings are shown, but nothing is concluded from the instability.
7. [affects a conclusion] That miniscope cell indices match across the two sessions is assumed (rslds cell 4) and cannot be checked: the archive holds no segmentation. ed4c, ed4d and ed3h's own-weights reading depend on it. If cells are not matched, the ed4c and ed4d outcomes are uninterpretable, not negative.
8. [affects a conclusion] For ed8gi, M70 is the only mouse with a pre-stimulation x2 mean far from 0 (−1.26). Cell 3 shows a stored baseline window of frames 300 to 400, which falls inside ISI1 and pulse 2 of 20 s ISI sessions, but does not say which sessions use it. Recomputed from the printed per-mouse values without M70, the Dunn p-values are 1.0, 0.67, 0.080 and 0.061, so nothing is significant.
9. [does not affect a conclusion] In cross-validation (CV cells 5 and 9), the held-out neural R2 is identical across K = 2, 3, 4 to three decimals, so the number of states is chosen by noise. The resulting tests are not significant either way.
10. [does not affect a conclusion] For ed9d (cell 33), the capped model nests the uncapped one (the cap's upper bound of 4 equals the number of pulses), so "finite lower in 7 of 7" is guaranteed by construction.
11. [does not affect a conclusion] x2 sign: M70 and M18R x2 projections turn strongly negative under x2 activation, and the sign of the targeted neurons' weights is not checked. With those two flipped, fig2k still has no significant comparison (minimum p = 0.063), but the means show sustained elevation, 1.0 to 1.4 against 0.19.
12. [does not affect a conclusion] Small details:
    - fig2gh (`distances`) takes the last pulse's post-stimulation frame at onset + 211, against onset + 209 for the others and onset + 210 in the criterion.
    - `autocorr` uses ddof 1 only in c0, so r0 = 0.998.
    - Synthetic tests: `dunn` matches a hand computation, and `periods`, `time_constants`, `merge_bouts` and `transients` behave as documented.
13. [does not affect a conclusion] `rslds_fits.ipynb` still contains the author's "Result" cells (11, 18, 21, 23, 26, 28, 31, 33, 36, 38, 41). They were not removed as intended. My outcomes come from the outputs, not from those cells.

I found no place where the claims file misreads the paper. Its ed8c reading (b) and ed9d reading (a) are weak tests by design.

**C. What I could not check, and the output that would have settled it**

- **Projection baseline windows:** which (session, dimension) uses frames 300 to 400 and which smoothing window. A per-row print of ProjectionMetadata would settle this.
- **x2 sign:** the signs of the stored weights of each session's targeted neurons.
- **M70 index offset:** the evoked response of M70's targets with indices shifted by ±1.
- **Cell positions:** whether any table holds them. A list of every group under `analysis/` with its column names would settle this; the notebook reads only the factor columns.
- **ed8c control:** the same simulation with the kick set to zero.
- **Projection smoothing:** whether the sample code's moving average is centred or trailing. The notebook uses a centred window (`mode="same"`), and I could not read the code.
- **Miniscope cell matching:** no masks are stored, so this cannot be checked from the data.
- **The fits themselves:** stability across more seeds, and whether the in-sample fits are deterministic, could not be checked without re-running.
