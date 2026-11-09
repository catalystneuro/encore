**A. Outcomes** (29 claims in the claims file; the notebook tests 28 and treats 1 as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| fig1e-recording-counts | reproduced | Cell 16: sessions, mice and units match exactly in every area, and AMM has 110 units. |
| fig6-session-counts | reproduced | Cell 18: all 24 counts match. |
| fig1d-performance | reproduced | Cell 20, reading (a): touch 73.6%, light 74.8%, paired t-test p = 0.561 (paper 0.56). |
| fig1d-outcome-fractions | reproduced | Cell 21, reading (a): all 8 fractions within tolerance. |
| fig1h-thit-tcr-selective | partially_reproduced | Cell 24: S1 30.5, S2 16.7 and ALM 23.0 are within tolerance; MM 36.4 is just outside (32.9 ± 3.29). 86% of selective neurons have AUC > 0.5. Other seeds give MM 35.0 to 36.4 (cell 25), so the verdict depends on the seed. |
| fig2c-rule-prestim-units | partially_reproduced | S1 is 5.6% (10 neurons) against 4.5 ± 0.56; S2, MM and ALM are within tolerance. MM and ALM are both above S1 and S2. Seeds give S1 3.4 to 5.6. |
| fig2d-stimulus-prestim-units | reproduced | 0, 0, 0 and 0.8%, all within one neuron. |
| fig2e-stimulus-poststim-units | reproduced | 36.2, 35.8, 13.6 and 14.5%, all within tolerance. |
| fig2f-prestim-predicts-touch-response | reproduced | Cell 27: MM r = 0.958 (28 neurons) and ALM r = 0.841 (25 neurons), both p < 1e-4. |
| fig3b-rule-decoding | reproduced | Cell 29: true medians 0.606, 0.617, 0.708 and 0.682 are all within tolerance and above shuffled. The S1 shuffled median is 0.564 against the paper's 0.50; see B7. |
| fig3c-rule-decoding-motor-stronger | reproduced | Cell 31: CIs do not overlap in MM and ALM and do overlap in S1 and S2. The shuffled CIs agree with the paper's within about 0.01. |
| fig3de-stimulus-decoding-controls | reproduced | Cell 31: CIs overlap before the stimulus and do not overlap after it, in all four areas. |
| figs3-svm-rf-decoding | reproduced | Cell 34: all 8 true medians within 10% of the paper, all above shuffled. |
| fig4c-prestim-distance-predicts-divergence | partially_reproduced | Cell 36: the top group is larger (1.171 against 0.966) but p = 0.004, not < 0.001. The code variant gives p = 0.001. |
| fig4e-subspace-overlap | partially_reproduced | Cell 38: the difference is negative with p < 0.05 in all four areas, but only S2 (−0.218) is within tolerance. S1 −0.29, MM −0.47, ALM −0.42; the code variants give the same picture. |
| fig4f-prestim-overlap-predicts-poststim | reproduced | Cell 39: r = 0.688, p = 1.3e-5 (32 sessions); the code rule gives 31 sessions, r = 0.686. |
| figs4ef-coding-dimensions | partially_reproduced | Cell 42: 7 of 8 judgements match. The MM stimulus CD is not aligned: true [0.218, 0.521] overlaps shuffled [0.150, 0.441]. |
| figs4h-choice-right-left | partially_reproduced | All four true means are below 0.5. S2 is 0.422 against the paper's 0.32 (off by 0.102). |
| fig5b-first-hit-switches | not_reproduced | Under the criterion (non-first blocks with a hit) the counts are touch 63 and light 75, against 88 and 91. Both counts fail; the before-or-at-cue+1 condition holds (0.57, 0.65). The all-block counts are exactly 88 and 91, and the paper says "total number of block switches", so the criterion's definition is probably not the paper's (B2). |
| fig5de-motor-states-track-switch | reproduced | Cell 46: all four MM and ALM CIs exclude 0 with the paper's sign, and the values are close to the paper's. |
| figs5-sensory-states-no-tracking | reproduced | All four S1 and S2 CIs include 0. |
| fig6c-pre-inhibition-tactile | partially_reproduced | With the Methods resampling, MM is below 0 but ALM is [−0.707, 0.005]. The code variant gives ALM [−0.682, −0.018], which is the paper's interval. S1/S2, sham and AMM include 0. |
| figs6b-pre-inhibition-hit-rate | reproduced | MM and ALM are below 0 (ALM upper bound −0.007) and S1/S2 includes 0. This is borderline: a second draw of the same procedure gives an ALM upper bound of +0.002 (B1). |
| fig6d-post-inhibition-tactile | reproduced | All three CIs below 0. |
| figs7gh-visual-sensitivity | reproduced | Cell 53: all 8 judgements match. |
| fig6-ppc-inhibition | reproduced | Cell 54: all four CIs below 0 (tactile post upper bound −0.009). |
| fig6fg-detection-task | reproduced | Cell 55: all 6 judgements match; AMM and PPC include 0 in both windows. |
| fig6ij-laser-only-licks | not_reproduced | Cell 56: 11 of 12 CIs include 0. Detection task, short laser, MM is [0.045, 0.483]: licking increases, so it does not argue for an inability to lick. The six long-laser cross-modal CIs match the paper's intervals almost exactly (B5). |
| fig1e-probe-locations | blocked (data_missing) | I checked the archive: all 179 assets are NWB and there is no histology or atlas data. Electrode `location` is "unknown" in every file (cell 5). The electrode group location only names the target area, which restates the claim and does not test it. |

**B. Problems**

1. [affects a conclusion] Cell 49, `change`: Monte Carlo error is not reported at the bootstrap boundaries.
   - For `tactile_hit` the "methods" and "code" CIs come from the same procedure (there is no false-alarm group), yet the ALM upper bound is −0.007 in one and +0.002 in the other. That flips figs6b.
   - fig6c ALM (upper bound 0.005) and PPC (−0.009) are in the same position.
2. [affects a conclusion] Cell 44, fig5b:
   - The paper's 88 and 91 equal the notebook's count of all blocks, including first blocks. The count of blocks with a hit including first blocks is never printed.
   - `rel` is counted in file rows. Pre-stimulus-lick trials were removed from the files, so `rel <= 1` can cover trials several positions after the cue, which biases the "switched by cue+1" fraction upward.
3. [affects a conclusion] `bonferroni_significant`, cells 23 to 25: with 1000 resamples and a = 0.05/(2N) < 0.0005, the interval is the minimum and maximum of the resamples. A single extreme resample decides significance. The seed spread (cell 25) straddles the tolerance for fig1h MM and fig2c S1, so those two partial outcomes depend on the seed.
4. [affects a conclusion] `opto_licks`, fig6ij: the windows differ between tasks.
   - Cross-modal short laser-only trials score licks 0 to 2 s after laser offset, which is after the laser has ended.
   - Detection short trials score −0.8 to 1.2 s from offset, which covers the laser.
   - Without the code I could not confirm either window, and the one failing CI uses the detection window.
5. [does not affect a conclusion] fig6ij: the paper's cross-modal intervals match the long-laser rows (for example MM [−0.312, 0.030] against the paper's [−0.31, 0.03]). The paper's detection intervals match neither the short nor the long rows. The "all twelve" criterion therefore tests more than the paper reports.
6. [does not affect a conclusion] Cell 38: the main rule (≥ 10 units) gives 12 ALM sessions against the paper's 11. The code's rule (> 10) matches the paper's session counts.
7. [does not affect a conclusion] Cells 29 and 34, chance level. The paper draws chance at 0.5 and reports shuffled medians of 0.50 to 0.55 (LDA) and 0.51 to 0.53 (SVM). The notebook's are 0.53 to 0.56 (LDA) and 0.535 to 0.562 (SVM), from a single permutation per session. On synthetic null data the helpers give 0.50 for balanced classes and 0.54 for 60/40, which is consistent with class imbalance under prior-weighted LDA.
8. [does not affect a conclusion] Cells 10 and 34, `cv_accuracy`: normalization and the `usable_features` filter use all trials, including the test fold. These steps do not use labels, so no labels leak.
9. [does not affect a conclusion] Cell 20, reading (b) drops the last 20 rows. Trials have already been removed from the files, so these are not the last 20 trials. Reading (a) passes anyway.
10. [does not affect a conclusion] Cell 41: for figs4h the notebook changed its reading of "needed condition" to the pooled rule after seeing that the first reading left 1 S1 session. S2 fails under either reading.
11. [does not affect a conclusion] Cell 10: the shared clock is not established for YT086 2020-03-20 (MM, 5 units), which is in the main set. Cell 5 checks for NaN electrode coordinates in one file only.
12. [does not affect a conclusion] Cell 46: the 10-fold point estimates of tau for S1 and S2 (for example S2 to-touch 0.58) are as large as those for MM and ALM. The absence claim in figs5 rests on wide CIs from 8 to 10 sessions.

The helpers I tested on synthetic inputs behaved correctly: `bootstrap_auc` matches sklearn AUC on an explicit resample; `bonferroni_significant`, `consecutive`, `gauss_smooth` (σ = 1 bin), `binned_rates` (left-closed bins), `hierarchical_bootstrap` against a known effect, `coding_dimension_dots` (stimulus-only input gives a dot product of 1), and the null behaviour of `cv_accuracy` all gave the expected results.

**C. Not checked**

- The paper's analysis code was not available to me, so I could not confirm:
  - the units the soft-normalization offset of 5 applies to (the notebook applies it to rates in Hz, with smoothed rates up to 318 Hz), which affects the fig4c and fig4e magnitudes;
  - the laser-only lick windows (B4);
  - the GetFirstHitInfo definition behind fig5b.
- Whether the files already lack each session's last 20 trials. Printing the original trial numbers, or the gap pattern at the end of each session, would settle this.
- Outputs that would have settled specific outcomes if added to the notebook:
  - fig5b: the number of blocks with a hit including first blocks, and first-hit positions in original trial numbers;
  - opto (cells 49 to 56): the ALM and PPC CI bounds over several seeds, or the Monte Carlo SE of each bound;
  - figs4h: the S2 bootstrap mean over several seeds;
  - fig1h and fig2c: percentages averaged over the 5 seeds;
  - electrode x, y, z checked in all 49 files, not one.
- I did not view the notebook's figure images.
