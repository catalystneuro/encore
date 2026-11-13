A. Outcomes for the 28 claims in the claims file

| Claim | Outcome | Reason |
|---|---|---|
| gaze-anticipates-action | reproduced | Cell 23: before right turns the eye signal differs from before left turns in each monkey, in both windows and for every eye choice (500 ms, both eyes: K −0.77 SD, p = 4e-148; S −1.00 SD, p = 4e-146; 39/40 and 20/20 sessions). The direction depends on an assumed sign of the eye signal (cell 24, problem 1). |
| gaze-anticipates-landmarks | partially_reproduced | Cell 26: the eye signal differs between right and left returns in each monkey, p ≤ 1.5e-10 under every reading. The side relative to the turn is not tested independently, because the sign was chosen on the assumption that the eyes deviate toward the side the view rotates to, and that is what this test measures (problem 1). |
| learning-trials | reproduced | Cell 17: S 12.26 (12.3 ± 2), K 16.53 under reading (a) and 15.82 under (b) (14.8 ± 2.4). The curves are the files' own; their column order was checked against `learningtrial` in 66 of 66 sessions (cell 8). |
| learning-to-90 | reproduced | Cell 18: 0.898 of sessions that reach both criteria, 0.803 of all sessions; both fall within 0.89 ± 0.089. |
| probe-transfer | not_reproduced | Cell 20: monkey K, 12 sessions: 28.3% in the first 5 trials (44 ± 4.4) and 58.3% after the new entries (73 ± 7.3); Wilcoxon p = 0.072. Monkey S has no probe session in hc-12 and none in hc-21 (data_missing for that part). |
| probe-faster-criterion | blocked (methods_underspecified) | The criterion needs learning curves recomputed from the introduction with the unnamed method of reference 60. Monkey S also has no probe sessions (data_missing). |
| cells-recorded | partially_reproduced | Cell 14: 186 cells with more than 100 spikes (189 ± 18.9). The archive holds only the 189 deposited cells, so the 270 recorded cells (128 S, 142 K) cannot be checked. |
| responsive-cells | blocked (metadata_insufficient) | The point-of-gaze space needs a calibrated eye signal. The three-space count of 59/186 (cell 30) is only a lower bound. |
| state-space-most-responsive | not_reproduced | Cell 30: the state-space count is 57, 33, 42 or 24 across the four readings, and 62 at most under the one-sided variant, against 84 ± 8.4. The chi-squared tests could not be run without gaze. |
| multi-space-coding | blocked (metadata_insufficient) | 46 of 59 three-space responsive cells code in two or more spaces (cell 28), but the gaze-only cells could change the fraction. |
| direction-center-vs-periphery | partially_reproduced | Cell 32, permute surrogates, cell set (b): IC higher in the centre at p = 0.045 and sparsity higher at p = 0.0074. Neither reaches p < 0.001. Set (b) here is the three-space responsive set, standing in for the four-space set. |
| direction-tuning-not-maintained | not_reproduced | Cell 34: the closest reading, (b) with permute, tests n = 59 cells (tolerance met), 4 high (band met), but 16 low against 20 ± 2. Every other reading also misses the low count. |
| state-space-ic-higher | partially_reproduced | Cell 47 (full/permute): state minus position, median 0.014, p = 1.1e-4; state minus direction, median 0.021, p = 2.5e-7. These are two of the three comparisons, which the criterion grades as partial. The notebook marks the claim blocked although these two comparisons need no gaze. |
| sparsity-state-vs-direction | reproduced | Cell 37, full/permute: median difference +0.016, p = 0.0022. The other three readings fail. |
| sparsity-state-vs-position | not_reproduced | Cell 38: the overall test is significant under both permute readings, and under the shift readings the individually significant count is 1 to 6, against 15 ± 1.5. |
| sparsity-gaze-vs-state | blocked (metadata_insufficient) | Needs the point-of-gaze space. |
| state-space-selectivity | not_reproduced | Cell 40: even over the three-space set, which is a lower bound, the low count is 7 to 9 under every reading (needs 3 to 5). The high count is ≥15 under full/permute, 13 under toreward/permute, and at most 8 under shift (needs 11 to 13). |
| landmark-identity-distance | not_reproduced | Cell 44: the distance count is at most 31, even over all 186 cells with all laps, against 64 ± 6.4. |
| landmark-identity-center | blocked (metadata_insufficient) | Cell 45: the bounds straddle the target (for example 9 to 16 for view (a) and 11 to 23 for view (b), successful laps), so the count over the paper's responsive set cannot be decided without gaze. |
| path-selectivity | blocked (metadata_insufficient) | Cell selection needs significant point-of-gaze IC, and there is no calibration. |
| gaze-aligned-dynamics | blocked (metadata_insufficient) | Foveation is defined as ±10° and needs gaze in degrees. |
| latency-skew | blocked (metadata_insufficient) | The gaze-aligned latencies and the cell set need gaze. |
| eccentricity-modulation | blocked (metadata_insufficient) | Eccentricity relative to gaze needs calibration. |
| foveation-selectivity | blocked (metadata_insufficient) | Needs foveation. |
| fields-per-cell | blocked (methods_underspecified) | The field definition is in S1 Appendix, as the claims file says. |
| spatial-selectivity-fraction | blocked (metadata_insufficient) | Reading (a) is testable and fails: 46/186 = 0.247 at best (cells 28 and 47). Readings (b) and (c) need the four-space responsive set. |
| gaze-map-landmarks | blocked (metadata_insufficient) | Needs point-of-gaze maps. |
| dimensionality-control | blocked (methods_underspecified) | The method is in S1 Appendix A5, which is not available. |

I checked the archive myself for the blocked claims. The hc-12 listing holds data.tar.gz, the descriptor (pdf and docx), scripts.tar.gz, and under orig/ two docx files. None of them gives an eye calibration, eye units or a sign convention: the descriptors say only "eye X,Y coordinates". None of the scripts handles gaze. hc-21 has the same structure. So the gaze-based claims are blocked as the notebook says. Two of the notebook's blocks are too broad: state-space-ic-higher could be graded on two of its three comparisons, and spatial-selectivity-fraction reading (a) could be graded. The onset-aligned part of latency-skew might also be computable from the camera data and the maze geometry, but only on a substitute cell set.

B. Problems

1. [affects a conclusion] Cells 22 to 26 assume the sign of the eye signal (negative = rightward), and the files do not record it. The argument from where the eyes rest during optokinetic stimulation is reasonable, but the data cannot rule out the opposite sign, under which both gaze claims fail. For gaze-anticipates-landmarks the test measures the same effect during a view rotation that was used to set the sign, so it cannot come out against the claim.
2. [affects a conclusion] `surrogate_counts`, "shift" reading: each chunk is moved by an independent circular offset, and the moved chunks overlap. In a synthetic check, 41% of frames end up empty and 28% are covered two or more times. On a homogeneous Poisson train with 200 bins, the mean surrogate IC was 0.108 against an actual 0.032, and 100% of surrogates exceeded the actual value. Combined with the bilateral p (problem 3), a cell with no coding at all comes out "significant" (p = 0.002). Claims-file Method W reading (b) is therefore never validly tested, which weakens the "not reproduced under any reading" verdicts. The negative normalized-IC medians under shift in cell 32 show the same bias in the real data.
3. [does not affect a conclusion] `tail_p` and `sig` (cells 28 to 47) count a cell as responsive when its IC is significantly below the surrogates. This follows the claims file's "bilateral", but responsiveness implies high IC. Only the two-sided p is stored, so the cells that are significant on the low side cannot be identified.
4. [affects a conclusion] `turn_types`: for the state-space selectivity index (SSI), the three rotational moves are taken as the 2xy tags of any direction, 72° rotations to the right and 72° rotations to the left. This is the author's own assumption, stated in the module docstring. Other typings the paper allows, such as splitting the 36° move by direction, were not run, and state-space-selectivity rests on this choice.
5. [does not affect a conclusion] Cell 47 and the summary table in cell 0 mark state-space-ic-higher blocked, although the criterion grades two of three comparisons as partial and both pass. Those comparisons are also shown only for full/permute.
6. [does not affect a conclusion] `frame_table`, "toreward" reading: it drops the return paths entirely. Claims reading (b) keeps the returns that follow correct trials. Counts under a faithful (b) would lie between the two printed readings, which already fail.
7. [does not affect a conclusion] `probe_info` (cell 16): a probe session is defined by its first 10 trials, and the introduction falls at trials 10 to 16 in several sessions, against 37 and 60 in the S3C examples. The entries were not checked to be the eastern ones. The first-5-trials mean (28% against 44 ± 4.4) does not depend on the introduction trial.
8. [does not affect a conclusion] `anova_two` uses type II sums of squares. MATLAB's `anovan` defaults to type III, and the data are unbalanced. The gap on the distance count is far too large for this to matter.
9. [does not affect a conclusion] Cells 23 and 26 pool turns across sessions in the rank-sum tests (pseudo-replication). The session-level counts printed alongside support the same direction.
10. [does not affect a conclusion] In cell 6 some files show an abscissa maximum of 1.62 and an orientation range of −180° to 90°, which are unexplained. The notebook does not check per file that the camera-data columns follow the descriptor's 12-column layout. The `star_remapped_cell_r.m` script itself documents an older 11-column layout, and the descriptor warns that file structures vary.

C. What I could not check, and the output that would settle it

- Whether shift-reading significance comes from the low tail: per-cell upper and lower tail p for IC.
- The column layout per file: the number of columns of `time_60`, the range of tag values, and the range of the state-space radius (needed to confirm the −3 to 3 grid).
- State-space-ic-higher and the IC differences under all four readings, not only full/permute.
- The SSI counts under alternative move typings.
- The probe sessions: start-arm sequences relative to the rewarded arm, and percent correct with the introduction trial defined as in S3C.
- learning-to-90: the upper confidence bound at the criterion trial, to see how often t90 = 0 is trivial.
- The eye-signal sign: any event with a known screen side, such as the side of landmark appearance on returns combined with the vertical channel, would test the sign independently.
