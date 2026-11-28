**Verifier report: Grosmark & Buzsáki 2016 (doi:10.1126/science.aad1935), round 1**

The claims file has 36 claims. The notebook tests 35 and treats one as blocked (figs11). I wrote no conclusion of my own into the files. I checked the helper functions on synthetic inputs and all of them behaved correctly: `_wcorr` gives ±1 on diagonal posteriors; the per-cell shuffle likelihood update in `_cell_shuffle_r` equals a full recompute; `_null_r` agrees with a direct computation; `tukey_kramer_values` matches `scipy.stats.tukey_hsd`; `ccg_bias` has the right sign; `first_T`, `last_T` and `concat_isis` are correct; and `place_field_test` calls 2 of 100 uniform-firing cells place cells.

Where the D reading changes the outcome (strongly contributing cells, rigid and plastic cells), "main reading" below means Y-a, D-a, P-a.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| sessions-and-tracks | reproduced | Cell 13: 4 rats, 8 sessions, PRE, MAZE, POST in order, 5 linear and 3 circular. Linearised lengths are 1.6, 2.0 and about 2.84 m. |
| place-cell-count | not_reproduced | Cell 15: 573 place cells against 491 ± 49. 63.0% under reading (a) against 54 ± 5.4. Only the pyramidal count (562) matches. |
| fig1c-above-chance | reproduced | Cell 19: rZ is above zero in all 3 epochs under 24 of 24 readings; the largest p is 1.6e-12. |
| fig1c-post-gt-pre | reproduced | Cell 21: Tukey-Kramer POST > PRE under 24 of 24 readings. Per animal, POST − PRE is significant only for Achilles and Cicero. Buddy (p 0.26) and Gatsby (p 0.17) are not; the descriptor calls them rats A and B. Figure S6 shows 3 of 4 animals, all except B, so Buddy disagrees. |
| fig1c-maze-gt-pre | reproduced | Cell 21: 24 of 24 readings; MAZE is the highest epoch in every animal. |
| figs5b-abs-r-above-null | reproduced | Cell 24: observed above null in every epoch under 24 of 24 readings. Both bootstrap readings hold under 24 of 24. |
| figs5e-duration-unchanged | not_reproduced | Cell 26: the rank-sum test is significant under 8 of 12 readings, including the main one (p 5e-4). Medians are within tolerance (176–184 ms). POST is slightly shorter, the reverse of the paper. |
| figs5f-more-participation-post | reproduced | Cell 28: POST > PRE under 24 of 24 readings. |
| figs9b-pcc-post-higher | partially_reproduced | Cell 32: both tests hold under all six Y/D readings. All three medians are outside tolerance (PRE about 0.02, POST about 0.13, dPCC 0.08–0.13). |
| fig2b-strong-contributors | partially_reproduced | Cell 34, D-b with P-a: totals 217, PRE 98 and POST 172 are within tolerance; "both" is 53 (needs 71 ± 7). D-a gives 246, outside tolerance. P-b gives 13–24 cells. |
| fig2-pre-post-overlap | reproduced | 71.7% under D-a with P-a. Chance (all place cells significant in POST) is 37%, against 190/491 = 38.7% implied by the paper. D-b gives 51–55%. |
| rigid-plastic-counts | partially_reproduced | 104/104 (D-b) and 107/107 (Y-b, D-b) are within tolerance; D-a gives 119–120, outside it. The readings disagree. |
| figs19c-pcc-change-per-cell | not_reproduced | Cell 36: 3.8–4.5% of cells PRE > POST (needs 2.2) and 11.9–16.2% POST > PRE (needs 21.4 ± 2.1). |
| fig2d-shuffle-high-dpcc | not_reproduced | Cell 39: shuffling the top 5% already eliminates replay under both readings (mean −0.004; CI from −0.026 to 0.019), which is earlier than the required 9–22%. Shuffling the lowest 75% keeps replay. |
| figs12-high-dpcc-exclusion | reproduced (main reading only) | Cell 40: POST − PRE turns negative at 10% excluded. Excluding the lowest 50% and 75% leaves the CI lower bound at 0.159. |
| fig2e-remove-plastic | reproduced (main reading only) | Cell 41: removing plastic cells gives a CI of −0.055 to −0.009; removing rigid cells gives 0.074 to 0.12. Groups are from D-a. |
| figs2-track-distribution | reproduced | Cell 57: Kolmogorov-Smirnov p 0.48, rank-sum p 0.099. Both groups are enriched at the track ends (0.62 and 0.71 against 0.4). |
| fig3a-plastic-specificity | partially_reproduced | Cell 58: plastic is higher on all five specificity measures and has fewer fields. Coherence (p 0.21) and number of fields (p 0.064) are not significant. |
| fig3b-plastic-improve | not_reproduced | Cell 60: plastic correlations are not above zero under readings a, b or c. Rigid cells increase under a and c. |
| figs13-outfield-rate-falls | not_reproduced | Cell 60: the plastic out-of-field fall is not significant (p 0.065). Rigid cells do fall (p 0.0055). |
| fig4a-rigid-faster | not_reproduced | Cell 45: the PRE difference is not significant (p 0.066), and session-wide reading (c) gives p 0.11. |
| figs14-plastic-ripple-gain | not_reproduced | Cell 47: PRE gain p 0.17. POST, session-wide (a, b) and change tests hold; the rigid change median (0.26) is outside tolerance. |
| figs14-plastic-ripple-bursting | not_reproduced | Cell 47: POST p 0.26 (a) and 0.23 (b). The change goes the wrong way. |
| figs16ab-plastic-synchrony-increase | not_reproduced | Cell 50: the plastic ripple-triggered increase is not significant under either reading (p 0.31 and 0.079). The coactivity part holds (p 0.040 and 0.0094). |
| figs11-cluster-quality-similar | blocked (stated reason too_large; I think it is testable, see B6) | Not run. |
| rate-split-medians | reproduced | Cell 52: all six readings are within tolerance. |
| figs16c-low-rate-coding | partially_reproduced | Cell 55: all four tests hold. The information medians (0.81 and 0.46), the high-rate log-mean (1.425) and both gain-change medians are outside tolerance. |
| fig4c-pre-fast-coactivation | reproduced | Cell 66: Spearman rho 0.87 and 0.81 (p ≤ 1e-19). The fastest window does not change (p 0.57 and 0.17). Only the session-rate reading sess_c was used. |
| fig4c-slow-coactivation-increase | not_reproduced | Cell 66: under ranking (b) rho −0.17 (p 0.13). In Figure S16C terms, low > high gives p 0.21. |
| fig4c-slow-replay | not_reproduced | Cell 66: under ranking (a) the partial correlation does not fall with rank (rho −0.055, p 0.62). |
| fig4d-slow-sequences | reproduced (main reading only) | Cell 70: low-rate group +0.063 (p 5e-4, CI above zero); high-rate group −0.008 (p 0.79). |
| fig4e-gain-sequences | partially_reproduced | Cell 70: high-gain group +0.071 (p 1e-7). The low-gain group also rises (+0.035, CI 0.012 to 0.061), but less. |
| figs16de-more-ripples-post | partially_reproduced | Cell 62: POST intervals are shorter for both event types (p ≤ 1e-50). The ripple-event medians (2.42 and 1.94 s against 3.0 and 2.47) and the LFP medians under both L readings are outside tolerance. |
| figs17-coactivity-preservation | partially_reproduced | Cell 64: the order PRE-RUN < RUN-POST < PRE-POST and all the tests hold. All five values are outside tolerance (0.094, 0.267, 0.393, 0.173, 0.126). |
| figs17d-rigid-plastic-coactivity | not_reproduced | Cell 65: rigid > plastic for PRE-RUN gives p 0.051. The other two group differences hold. |
| figs18-temporal-bias | not_reproduced | Cell 68: the rigid RUN-POST r is significant (0.131, p 0.0013) where the paper says it is not. The plastic RUN-POST r (0.193) is outside tolerance. |

### B. Problems

1. **[affects a conclusion]** Cells 34, 43 and 49 (`K0`). Every rigid/plastic comparison uses only the D-a classification, which gives 120/120 cells, outside the rigid-plastic-counts tolerance. The D-b classification gives 104/104, matching the paper, but it is never carried into the group comparisons. This touches fig2e, figs2, fig3a, fig3b, figs13, fig4a, both figs14 claims, figs16ab, figs17d and figs18. Several of these rest on p values near 0.05 (fig4a PRE 0.066, figs17d 0.051).
2. **[affects a conclusion]** Cells 38–41 and 70. The reruns behind fig2d, figs12, fig2e, fig4d and fig4e use only Y-a, L-a, S-a, D-a. Their criteria require the outcome to hold under readings Y and D, so the "reproduced" outcomes for figs12, fig2e and fig4d stand on one reading.
3. **[affects a conclusion]** `rescore`. For fig2d each top cell is rotated once, giving a single shuffled template per percentage. The Methods say "place field templates (n = 1,000 each)", so this assumption contradicts the paper. The 5% result is therefore one random draw, and the bootstrap interval leaves out the variance between shuffles.
4. **[affects a conclusion]** `N_NULL` = 200, `N_PCC` = 100 and `N_RERUN` = 30, against 1,000 each in the paper. The deviation is stated, but its effect is never checked. Per-cell significance (fig2b, figs19c) and the rerun intervals depend on these counts.
5. **[affects a conclusion]** `place_field_test`. The notebook finds 573 place cells against 491, which is 17% more, and never looks into why. This count is the unit set of every later claim. The alternative reading of the 5 cm kernel (width rather than SD) was not run. The claims file says this choice "should not change outcomes", and that assertion goes untested.
6. **[affects a conclusion]** figs11, blocked as too_large. According to the data descriptor, the PCA features (`.fet`) and cluster assignments (`.clu`) sit in `X.tar.gz`, which I listed on S3 at 0.8–2.3 GB per session (11.7 GB in total). The 4.8–14.7 GB files are the `_spk` waveform tarballs. `X.tar.gz` can be streamed the same way the notebook streamed the sessInfo tarball, so the claim could be tested.
7. **[affects a conclusion]** Cell 66. Of the three session-rate readings the fig4c criterion takes over from fig4a, only `sess_c` is run. The Figure 4B legend ("overall session (SESS) firing rates") supports `sess_c`. However, fig4c-slow-coactivation-increase fails only on ranking (b) (p 0.13), and the untried rate readings could change that.
8. **[does not affect a conclusion]** Cell 21. The per-animal results are not mapped to the paper's labels. The descriptor gives A = Buddy, B = Gatsby, C = Achilles, D = Cicero.
9. **[does not affect a conclusion]** Cell 40. Excluding from the lowest dPCC is tested only at 50% and 75%, not at the 5% steps the criterion describes.
10. **[does not affect a conclusion]** `offline_sets`. S-b uses the NWB file's buzcode NREM, with no quiet waking, instead of a recomputed scoring with stated thresholds. S-a counts Drowsy as quiet waking; the descriptor makes this reasonable.
11. **[does not affect a conclusion]** `run_mask`. Reward areas are excluded only because OneDLocation already covers just the stem (2.84 m = π × 1 m − 0.30 m). The notebook never states this. The circular "cw" direction also has no velocity-sign filter.
12. **[does not affect a conclusion]** Cell 38 has a dead loop (`EVSEL`).

### C. What I could not check

- **Contents of `X.tar.gz`:** a listing of its member names would confirm the `.fet` and `.clu` files are there.
- **Place-cell count sensitivity:** counts under the kernel-as-width reading, and with the 1 Hz peak rule dropped.
- **D-b group comparisons:** cells 45–68 rerun with the D-b classification.
- **Shuffle-count sensitivity:**
  - one session run with 1,000 null templates and 1,000 per-cell shuffles, compared with the reduced counts;
  - fig2d averaged over many shuffled templates per percentage.
- **Running intervals:** the range of `pos_t` against `MazeEpoch`. The RUN intervals in cells 49 and 68 are not intersected with the maze epoch, which matters only if position is tracked outside MAZE.
- **LFP channel:** no ripple-triggered LFP or power spectrum on the chosen channel, which would confirm it is in the pyramidal layer.
- **Rank-based Tukey-Kramer:** not compared against MATLAB's `multcompare`, though its p values are far from the threshold.
