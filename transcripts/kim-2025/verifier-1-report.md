A. Outcomes for all 28 claims in the claims file

| Claim | My outcome | Reason |
|---|---|---|
| illusion-data-link | reproduced | sub-630506 has an ICwcfg1 block with 12 stimuli at 400 repeats. Codes 3, 4, 10 and 11 (Ic1, Lc1, Tre1, Tre2 by the code's map) are among them, and the session has 75 V1 units (nb1 cells 3 and 8). All 11 of the code's subjects are present; sub-619293 is an extra session. |
| illusion-fig1c-isomap-geometry | reproduced | All three tests hold (slope-0 component of 1, as-is 3, mean overlap 0.00 < 0.22 < 0.32). They also hold in all 8 combinations of N-space or 2D Isomap, Methods or code threshold, and all VISp or quality units (nb1 cell 10). Other sessions are a variant: 9 of 12 pass (cell 13). |
| illusion-fig3a-orthogonal-variance-example | reproduced | Geodesic distance Lc1–Ic1 is 60.0 against 17.6 for Lc1–Tre2. Orthogonal variance is 0.0270 against 0.0161. The same order holds with quality units (cell 15). The 132-pair Spearman variant is weak (ρ 0.15, p 0.086). |
| illusion-geometry-similar-across-datasets | reproduced | Across 12 sessions, dimensionality falls 0.243 → 0.081 → 0.033 and overlap rises 0.142 → 0.398 → 0.603. Both change at every step, with p 0.0005 at slopes 0 and 2 (the exact minimum for n 12). Both unit readings agree (cell 17). |
| data-v1-units | reproduced (depends on the unit reading) | 30 sessions; the excluded ones are the 1st and 7th by session id, which I confirmed on the archive and which matches the code's 0 and 6. With the Methods' three criteria the mean (71.1) and total (2133) are out of tolerance. With AllenSDK's default "good" label added (66.9 ± 25.5, total 2008) every value is in tolerance (nb2 cell 7). |
| fig1b-across-neuron-slope-near-1 | reproduced (depends on the unit reading) | With "good" units: mean 1.0489, SD 0.0665, n 3570, all within tolerance. With the Methods criteria the mean is 1.0552, outside ±0.001 (nb2 cell 10). |
| fig1b-across-stimulus-slope | reproduced | Mean 1.134 and SD 0.206 are in tolerance; mean and median are above the across-neuron values; Mann-Whitney p 5e-105 (cell 12). |
| figs1-gain-variance | blocked (other) | Not run in either notebook, and no reason is given there. The spike data are in 000021, so it is testable (see 4 below). |
| figs2-behavioral-state | reproduced | Moving median 0.999 against stationary 1.067, p 1.5e-303. The largest pupil tertile has the lowest median (1.039), Kruskal-Wallis p 2e-46, and every median is in 0.9–1.1 (cell 15). |
| figs3-higher-visual-areas | reproduced | All five area medians are in 0.9–1.1. Session counts are within tolerance (cell 17). |
| figs4ab-noise-correlation-under-manipulation | reproduced | The largest change in noise correlation is 7e-15. The PC1 fraction changes for 100% of stimuli at slopes 0 and 2 (cell 21). |
| fig1d-dimensionality-falls-with-slope | reproduced | Decreases at every step, 0.282 → 0.123 → 0.061, p 1.9e-9 (cell 23). |
| figs5a-movie-slope-near-1 | partially_reproduced | Median 1.131 passes the second window (0.85–1.15) and fails the first. But 24 sessions were used against an expected 23 with tolerance 0: no truncated movie was detected (cell 55). |
| figs5c-space-occupancy-peak | reproduced (by the criterion, see problem 3) | Peak at slope 0.8; slopes 0 and 2 are lower with p 1.7e-6 (cell 25). |
| fig2a-overlap-rises-with-slope | reproduced | Rises at every step, 0.062 → 0.276 → 0.425, p 1.9e-9. The code variant agrees (cell 27). |
| fig2b-decoding-falls-with-slope | blocked (other: compute time, not data size) | Only a timing was run (cell 57). The data are present, and a partial test was feasible (4 below). |
| fig2c-continuity-from-slope-1 | reproduced | The mean largest component first reaches 119 at slope 1.1 (1.2 with the code's threshold). At slope 0 it is 107.2, p 5.7e-5 (cell 29). |
| fig2d-tangent-angle-rises-below-1 | blocked (other) | Not run in either notebook, and no reason is given there. The data are present. |
| fig3bc-geodesic-orthogonal-correlation | reproduced | ρ is positive in 30 of 30 sessions, mean 0.323; one-sided Wilcoxon p 9e-10 (cell 32). |
| fig3d-correlation-peaks-near-1 | reproduced | Peak at 1.2; ends lower than as-is, p 2.6e-7 and 0.011 (cell 34). |
| fig3e-local-alignment-peaks-near-1 | reproduced | Peak at 1.0; ends lower, p 1e-6 and 0.005 (cell 36). |
| fig3f-global-alignment-peaks-near-1 | reproduced | Peak at 1.1; ends lower, p 8e-8 and 5e-4 (cell 38). |
| fig4a-overlap-consistency-within-mice | reproduced | Peak at 0.9 (0.650; 1.0 is equal to 3 decimals); ends lower, p 1.9e-9 (cell 41). |
| fig4c-rsm-similarity-within-mice | reproduced | Peak at 1.1, and at 1.1 under all 4 extra seeds; ends lower than as-is. As-is (0.471) is above every manipulated slope (cells 43 and 53). |
| fig4d-overlap-consistency-across-mice | reproduced | Peak at 1.2 over 435 pairs; p 6e-70 and 6e-31 (cell 45). |
| fig4e-rsm-similarity-across-mice | reproduced | Peak at 1.1 under all seeds; ends lower (cells 47 and 53). |
| figs6-higher-areas-consistency | reproduced (by the criterion's reading a only) | In all four panels the value at slope 1 is within one SEM of the maximum. The peak window (reading b) holds only across mice: within mice the peaks are at 0.3 for LM and 0.4 for PM, on flat curves (cell 49). See problem 4. |
| figs4c-shuffling-alters-dependence | blocked (other) | Not run. Two of its three analyses (the RSM ones, 4C and 4E) are cheap and were testable. |

Chance levels: 1/12 and 1/119 are stated correctly in the clock checks. As-is SVC accuracy in one session is 0.376 against a chance of 0.0084 (nb2 cell 57).

B. Problems

1. [affects a conclusion] Unit selection differs between claims (nb2 cells 7, 10, 12, 19). data-v1-units and fig1b-across-neuron are passed on the AllenSDK reading (Methods criteria plus the "good" label). Every other 000021 and 000022 claim uses the Methods criteria alone (2133 units, not 2008). The "good" reading is reasonable, since the Methods thresholds are AllenSDK's defaults, but it should apply to every claim. Under the reading actually used downstream, data-v1-units (mean, total) and fig1b-across-neuron (mean) fail.
2. [affects a conclusion] figs5a, cell 55 / `movie_session`: 24 sessions against the paper's 23. Truncation is checked only by frame order. Bin durations of 0.368–0.500 s in sub-769319621 and of about 0.384–0.417 s in six other sessions point to timing irregularities that were never examined as the paper's "truncation".
3. [does not affect a conclusion, but makes the criterion weak] figs5c, `occupied_voxels`. As-is occupancy equals the trial count (5950) in 28 of 30 sessions, so the measure is at ceiling, and the "peak" at 0.8 sits on a plateau from 0.6 to 1.0. The fall at slope 2 (mean 341) comes from points leaving the as-is box. Also, the grid is anchored at the minimum of the points inside the box, not at the box edge; I could not compare this with compute_percent_filled.
4. [does not affect a conclusion; a weakness in the claims file, reported and not corrected] figs6, reading (a). Within-session SEMs (0.024 and 0.035) are about ten times the spread of the LM and PM curves between slopes 0 and 1.1. Slope 0 passes reading (a) as well as slope 1 does, so the reading cannot tell them apart.
5. [does not affect a conclusion] fig2b and figs4c are blocked for compute time. "too_large" is the wrong category, and a partial test was skipped: as-is and slopes 0, 1 and 2 over 30 sessions is about 1.5–2 CPU hours. Cell 58's quoted timings (11 s, 110 s) differ from the printed 14 s and 131 s.
6. [does not affect a conclusion] The trio test in `trio_tests` (nb1 cell 10) computes the strongly connected component on the 3-node subgraph. Whether the trio is joined through the other 9 stimuli at slope 0 was not reported. "Among" in the criterion supports the subgraph reading.
7. [does not affect a conclusion] The 000248 trial slots are rebuilt by the author's alternation rule (`illusion_trials`), which is an assumption. It is well supported: no image frame falls outside a slot in any of the 12 sessions, the 5300 slots equal 12×400 + 10×50, and the clock check passes (LDA accuracy 0.576 against 0.089 for the preceding window, no response to Blank trials).
8. [does not affect a conclusion] `shuffle_within_stimulus` permutes all neurons together, which would not destroy noise correlations. It is unused; `decode_session` shuffles each neuron separately, which is correct.
9. [does not affect a conclusion] figs4ab example: `keep[7]` is session 8 of the 32. The code's "index 7" probably refers to the 30-session list (index 7 there is also session 8), so this is fine.
10. [does not affect a conclusion] HVA session counts over all 32 sessions (24, 28, 24, 20, 26) match the paper's counts exactly, given its one excluded RL session. This suggests the paper used all 32 sessions with area-specific exclusion. The medians pass either way.
11. Process note: unlike the 000248 notebook, the Allen notebook still contains the author's "Result" conclusion cells, so I saw them. My outcomes come from the code outputs.

Helper checks on synthetic data:
- `manipulate` hits the target slopes exactly and keeps means, mean log variance and noise correlations (differences of order 1e-16).
- `overlap_matrices_fast` equals `overlap_matrix`.
- `centroid_geodesics` equals sklearn `Isomap.dist_matrix_`.
- `orthogonal_variances` equals `orthogonal_variance`.
- `rsm` equals a brute-force loop over r1 < r2.
- `largest_scc` and `effective_dimensionality` behave as expected.

C. What I could not check

- figs1, fig2d and figs4c: the notebooks give no block reason. All the data they need (spike times, natural scenes tables) are in 000021, as cell 3 shows, so they could be tested. Gain variance takes about 250k small Nelder-Mead fits, which is feasible. A short cell stating each block reason would have settled this.
- fig2b: output from `decode_session` at as-is and slopes 0, 1 and 2 for all 30 sessions would have allowed at least a partial outcome.
- figs5a: listing each session's per-repeat duration and the largest frame interval would have identified the third excluded session.
- Problem 1: rerunning the cell 19 measures and fig1b-across-stimulus with "good" units would show whether any outcome moves.
- figs5c: whether the paper's compute_percent_filled drops out-of-box points and where it anchors the grid; the code was not available to me.
- I could not verify the AllenSDK `filter_by_validity` line reference in nb2 cell 8.
