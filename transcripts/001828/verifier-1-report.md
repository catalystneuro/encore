**A. Outcomes, one per claim (38 in the claims file)**

The attempt record was not among my materials, so these counts come from the claims file and the notebook only.

| Claim | Outcome | Reason |
|---|---|---|
| fig1b-anxa1-downregulated-rnaseq | blocked (data_missing) | The claims file says the claim stays blocked without cMfn2KO data. Cell 21 reads only `GSE282753_counts_mitopark.txt.gz`. The MitoPark half holds: DESeq2 FDR 2.9e-5 and edgeR 7.5e-4, log2FC about −1 (cell 24). |
| fig1c, fig1e, fig1h, fig1j, fig1m, figs1-6ohda-partial-th-loss, fig1p, figs1-vta-no-effect, fig2c, fig2f, fig2i, fig2n (12 claims) | blocked (data_missing) | I checked the archive's asset list. Its 1014 assets are 498 mp4 videos plus NWB files for open field, maze, reaching and evoked release only. There is no histology, imaging or qPCR. |
| figs2-evoked-da-dcp-ccp | reproduced | Reading (a) holds under every z-score, baseline and window reading. dCP peak 1.21 vs cCP 0.61 (session z), p = 0.001 to 0.004, dCP above baseline in 10/10 sessions (cell 26). Reading (b) holds at 3 or 4 of 5 powers. |
| fig3d-anxa1-ramp-to-touch | not_reproduced | The DAT part fails in all 8 readings (Sidak 1v2 ≥ 0.35). The Anxa1 part holds only under contact events, 1 s windows, session z (p = 0.048, Sidak 2v3 = 0.045) (cells 29–30). |
| fig3e-dlight-dcp-ccp-reward | not_reproduced | The dLight-dCP part fails in every reading (ANOVA p ≥ 0.21). The cCP part holds in 5 of 8 readings (cell 34). |
| fig3fg-auc-change-from-baseline | partially_reproduced | The criterion holds under baseline z-scoring: with 2 s windows under both Bonferroni families (×8 p = 0.047 and 0.040), and with 1 s windows under the ×4 family. It fails under session z in every reading (cell 36). The third window here is much stronger than the second (raw p 0.0002), the reverse of the legend. |
| fig3i, fig3kl, fig3o | blocked (data_missing) | No nosepoke assets exist. The 20 "self-stimulation" files hold 4 dLight mice with trains at fixed 4 s intervals (cell 11), not the 25 ChRmine mice of Figure 3I. |
| fig4b-speed-correlation-dcp | not_reproduced | Anxa1: mean r 0.066, 9/10 positive, paired t p = 0.080 / 0.071 and Wilcoxon p = 0.065 against the shuffles. dLight-dCP passes (p = 0.010 / 0.008) (cell 38). The criterion needs both groups. |
| fig4b-speed-correlation-ccp-negative | reproduced | Mean r −0.158, 0/7 recordings positive, t-test p = 0.0005 and Wilcoxon p = 0.0156 (= 2/128, as the claims file predicts) (cell 40). |
| fig4c-vame-motifs | blocked (data_missing) | The dandiset's `VAME_42` labelling has 42 labels (0–41) and is not the paper's 37-motif labelling. Motif 42, named by the paper, does not exist, and motif 28 (stationary, said to rise in MP-middle) has 0% of frames in the Figure 5 mice (cell 42). |
| fig4e, fig4f, fig4h, fig5g, fig5i | blocked (data_missing) | Each depends on fig4c, and the header says only the paper's labels give an outcome. For information, on the dandiset labels: fig4f is within tolerance in 1 of 4 readings, with R = −0.5713 against a bound of −0.572; fig4h's best R is 0.683, outside 0.83 ± 0.083; fig5g holds under standardized scaling; fig5i fails (\|R\| 0.64, and PC2 p = 0.041). |
| fig5h, fig5j-tetx-five-motifs, fig5j-shared-and-stage-motifs, fig5m | blocked (data_missing) | There are no motif categories, and the motif numbers are not the paper's (same evidence as fig4c). |
| fig5c-tetx-locomotion | reproduced | Linear speed −28.5% (p = 0.0036) and angular speed −35.5% (p ≈ 1e-7), n = 18/14 as in the legend (cell 50). Immobility has no value in the data, so under the header it is not judged; that part is untested. |
| fig5e-early-models-locomotion | reproduced | TeTx is closer to the early models than to MP-middle on both available measures: linear 1.0 vs 38.2 points, angular 16.1 vs 25.5 (cell 52). Immobility is unavailable. The acceleration spread (p95 11.3) is also closer to the early models (14.1–14.2) than to MP-middle (7.3). |
| fig6c-maze-locomotion | not_reproduced | No speed reading meets the criterion. The only reading with TeTx slower and a group p < 0.05 (tail base, confidence 0.9: p = 0.035) has day-4 Sidak p = 0.19. n is 17 + 10 against the legend's 18 + 10 (cell 60). |
| fig6d-maze-preference-learning, fig6d-maze-efficiency | blocked (data_missing) | The maze files hold pose only, plus external videos (asset metadata checked): no end-zone entries, rewards or arena geometry. Efficiency cannot be tested at all. Preference could at most be approximated from pose and video, which the criterion does not provide for. |
| fig6j-reaching-accuracy | not_reproduced | The main run (mice recorded before the preprint) holds in 0 of 8 readings. The Arch day-4 Sidak test fails (p 0.04 to 0.34), though controls improve and TeTx is lower on day 4. The all-mice variant holds in 4 of 8, but the claims file excludes mice recorded after the preprint from the main run (cell 63). |

That gives 4 reproduced, 1 partially_reproduced, 5 not_reproduced and 28 blocked.

**B. Problems**

1. [affects a conclusion] **Motif labels used inconsistently** (cells 41–58). The notebook says the dandiset's motif numbers are not the paper's and blocks fig5j and fig5m for that reason. It still treats fig4c, 4e, 4f, 4h, 5g and 5i as tested on the same `VAME_42` labelling. The header rules this out ("a new VAME fit is not a basis for an outcome"), and the Methods describe 100 states reduced to 37 motifs, not 42.
2. [affects a conclusion] **Start times of kinematics and motifs never checked** (`frame_aligned`, `z_on_frames`). `kin_t0` and `motif_t0` are loaded but never used or printed. The alignment assumes kinematics and motif labels start at t = 0, yet they have 30 frames fewer than the pose (the VAME window). An offset of 0.5 to 1 s would shift every 0–1 s motif-onset AUC (fig4e, 4f, 4h) and, slightly, the fig4b correlations.
3. [affects a conclusion] **Notebook picks its own main reading for fig3fg** (cell 35 markdown). It calls the session z-score "the main reading". The claims file names both z-scorings and does not rank them, and the claim holds only under the baseline one.
4. [does not affect a conclusion] **Conflicting genotype for mouse 687662** (cell 19, `fp_reach_group`). It is anxa1-flp in the open field (Anxa1 group, fig4b) and Dat_cre in the water-drop session (DAT group, fig3d). This is unresolved. The DAT part of fig3d fails by a wide margin either way, and Anxa1 in fig4b would only get weaker without it.
5. [does not affect a conclusion] **Arch day-1 laser label departs from the Methods** (cell 62). All 17 Arch `test1` files say the laser was "activated immediately after the mouse's first reach attempt", whereas the Methods say it was off on day 1. The claims file asks for this departure to be reported; it is printed but not stated as one.
6. [does not affect a conclusion] **Maze speed is unsmoothed** (`maze_speed`, cell 60). Raw mean-of-six-points speeds are 3 to 4 times the tail-base speeds, and the day-4 mean6 values jump. The same pixel scale across days ("one camera") is assumed, not checked. All readings fail, but the not_reproduced rests on noisy measures.
7. [does not affect a conclusion] **Sidak post hoc tests use separate t-tests** (cells 60 and 63) rather than Prism's pooled error term. The notebook states this.
8. [does not affect a conclusion] **`edger_exact` is not edgeR's default pipeline.** It uses GLM common and tagwise dispersions with `exactTest`, not the classic or `estimateDisp` route. fig1b is blocked anyway.
9. [does not affect a conclusion] **Preferred limb uses all sessions** (`accuracy`, `pref="mouse"`). It is taken from every phase of a mouse, including test8 and events without a distance.
10. [does not affect a conclusion] **Recording sets cannot match the legends.** For example, Anxa1 open field has 8 mice and 10 recordings against the legend's 9 and 9; the water-drop groups have 15/8/21/15 recordings against 10/4/13/11. The notebook uses all recordings, as the criterion says, and reports the counts.
11. [does not affect a conclusion] **The 2 s pre-train baseline in figs2** (cell 26) covers 2 to 4 s after the previous train's onset, so the decaying response may raise it.

**C. What I could not check, and the output that would have let me**

- The values of `kin_t0`, `motif_t0` and `z_t0` per file. A printed table of these, plus a check of motif-onset AUCs shifted by ±15 and ±30 frames, would settle problem 2.
- Whether GEO GSE282753 really lacks cMfn2KO counts. A printed list of the GEO supplementary files would show it.
- Whether any NWB file holds nosepoke tables, or end-zone and reward data for the maze. My check covered the asset list and asset metadata only. A printed list of the `intervals/`, `processing/` and `acquisition/` groups per file kind would show it.
- Whether a `correct` event's time is the drop-touch frame. A printed sample of event frames against the video would show it.
- The maze pixel scale per day. A printed pose x/y range for each day would show it.
