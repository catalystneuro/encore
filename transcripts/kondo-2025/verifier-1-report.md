**A. Outcomes** (22 claims in the claims file; the notebook tests 20 and treats 2 as blocked)

| Claim | My outcome | Reason |
|---|---|---|
| cohort-sex-age | reproduced | Cell 10: 25 subjects, 11 M and 14 F. Ages at the last session run from 16.3 to 31.6 weeks, inside the widened band of 15.3 to 34.1 weeks. |
| task-sessions-collected | reproduced | Cell 12: 364 distinct task sessions and 16 mice with all 15. File names and session descriptions agree. |
| imaging-frame-counts | reproduced | Cell 14: task sessions 363/364 at 54000 frames, resting-state 98/98 at 18000, sensory 29/33 at 27000. The exceptions are listed (four sensory sessions at 36000, one task session at 45413 that ran 25.2 min). |
| training-breaks | reproduced | Cell 16: under every reading, breaks per mouse are 2.80 to 3.28, days per break 2.30 to 2.51, and the span 24.21 to 25.71 days. All are within the stated s.d. |
| fig3c-response-rate-increase | reproduced | Cell 18, reading (a): median 0.556 in session 1 and 0.856 in session 15. Reading (b) gives 0.559 and 0.859. All are within tolerance and rising. |
| fig3c-success-rate-constant | blocked (methods_underspecified) | Cell 20: reading (a) fails, with session 15 at +27% (labels) or +31% (rewards) over session 1. Reading (b) holds (Spearman p = 0.36 / 0.41). The criterion says the claim is blocked when the readings differ. |
| fig3d-tpull-clusters | reproduced | Cell 22: with the 15 values as the feature, all three imputations give A = 7 and B = 18, with the same members. The differences feature gives 3 or 4. |
| fig3e-cluster-a-high-tpull | reproduced | Cell 24: A's early success median beats B's in sessions 1–5 (0.649 vs 0.539) and in session 5 (0.749 vs 0.558). A's late T_pull_final is higher (0.28 vs 0.08 s). None of the differences is significant (MWU p 0.06–0.24), and part (2) follows from how A is labelled. |
| fig3e-cluster-b-similar-rates | blocked (methods_underspecified) | Cell 26: the T_pull part holds. For the success rate the readings of "similar" differ: Mann-Whitney p ≥ 0.05 everywhere, but the 10% reading fails for labels (12.8%, 16.1%) and for rewards in session 15 (17.1%). |
| methods-no-signal-degradation | reproduced (caveat, problem 4) | Cell 28: reading (a) median rho −0.21, Wilcoxon p = 0.178. Reading (b) rho 0.02, p = 0.84. Neither shows a significant decline. |
| fig4ab-landmark-validation | blocked (data_missing) | I confirmed in the archive that the version holds only 495 .nwb and 1343 .mp4 files. Cell 6: `analysis` holds only `atlas_to_data_transform`. No part is testable from DANDI. |
| fig4d-visual-map | reproduced | Cell 33: right VISp is the top ROI of the mouse-averaged map under all four readings (0.94–0.96). Right VISpm is close behind (0.92–0.93), and right VISp is top in only 8–11 mice. |
| fig4d-tactile-map | reproduced | Cell 34, code:3: left SSp-bfd is top (0.87) and exceeds right SSp-bfd (0.55) in all 25 mice. |
| fig4d-auditory-map | reproduced (weak) | Cell 35, code:2 (n = 19): the 80th-percentile region contains VISa_l and nine ROIs. This criterion is passed by chance about 60% of the time (problem 3). |
| figs2b-no-aberrant-transients | reproduced | Cell 37: none of the 1200 combinations has a centre with prominence > 0.1 and width < 0.5 s. |
| fig5abc-dlc-error | blocked (data_missing) | Same archive check as fig4ab: only DeepLabCut estimates and likelihoods are present, no manual annotations. |
| fig5f-lever-tip-correlation | reproduced | Cells 40–41: mean R is 0.978–0.985 under every reading (main reading 0.981 ± 0.021), within 0.98 ± 0.02. |
| fig5f-forepaw-correlation | partially_reproduced | Cell 42: R is within tolerance under every reading (right 0.48 ± 0.22, left 0.05 ± 0.18; right > left in 25/25 mice). But the expected session count, with tolerance 0, is 354 and the notebook analyses 356; there are 357 body-keypoint sessions where the paper has 355. |
| fig6b-movement-order | blocked (methods_underspecified) | Cell 46: no reading holds; the jaw "moves" before 0 in about 100% of sessions. The onset test itself is unreliable (problem 1), so this claim was not actually tested. |
| fig6b-motor-somatosensory-after-reward | reproduced | Cell 48: under every grand-mean reading MOs (0.001–0.014) is below MOp, SSp-ul and SSp-n, which are all above 0. Per-session fractions are 0.38–0.60. |
| fig6b-sensory-areas-track-pupil | blocked (methods_underspecified) | Cell 50: only OB tracks the pupil (r 0.96 vs 0.62). RSPagl, AUDs and VISp correlate more with the lever under every reading. |
| fig6b-variability-decrease | reproduced | Cell 52: the post-onset across-trial s.d. is lower in 43–44 of 44 ROIs (Wilcoxon p ≈ 1e-13; median ratio 0.71–0.79). |

**B. Problems**

1. **[affects a conclusion]** `bdbc.onset_time` (used in cell 46) is the claims file's ±2/3 s.d. rule as written. It has no requirement that a crossing be sustained, and the baseline s.d. comes from 15 samples of a smooth average. I tested it on synthetic traces:
   - Traces with no movement at all got an onset before 0 in 86–100% of runs, most often exactly −0.5 s.
   - A trace rising at +0.3 s got an onset of −0.27 s.

   The grand onsets in cell 46 are all −0.5 s for every keypoint, which shows the same artefact. So no "before 0" or "after 0" result in cell 46 is informative. The outcome stays blocked, but because the claim was never validly tested, not because no reading held. The flaw is partly in the claims file's own rule; the notebook never checked the rule.
2. **[does not affect a conclusion]** Cells 31–35: the TTL channel names are wrong for the six mice #51, #52, #53, #54, #60 and #61. In those sessions `stim_whisker` carries the 10-pulse visual train and `stim_auditory` carries code 3 (tactile). The `ch:stim_whisker` and `ch:stim_auditory` readings therefore mix modalities; for example, the `ch:stim_auditory` map has n = 25 where 19 is expected. Only the `code:` readings are clean, and they are the ones that reproduce.
3. **[does not affect a conclusion; claims-file weakness, reported not corrected]** fig4d-auditory-map: with 44 ROIs, the 80th-percentile region always holds about 9 ROIs, so "more than one ROI" is always true. A random 9-ROI set includes one of the 4 parietal ROIs with probability 1 − C(40,9)/C(44,9) ≈ 0.61. The claims file gives no chance level, and the reproduced outcome carries little evidence. The clock check in cell 7 is also weak for code 2 (the true onset is best in only 15 of 27 sessions).
4. **[affects a conclusion]** methods-no-signal-degradation, `task_session` / `N_BLUE_FRAMES = 8`: F_B0 is the median of 8 frames, not the median over time the criterion asks for. The deviation is stated, but its noise was never measured. The result is borderline (median rho −0.21, 16/25 mice negative, p = 0.18), and subsampling noise pulls rho toward 0. If a full median made reading (a) significant, the outcome would become blocked. The notebook also does not show whether the NWB files hold a raw ROI fluorescence series, which the criterion prefers.
5. **[does not affect a conclusion]** Cell 6: `excitation_lambda` is swapped in every file (blue says 405, UV says 470). The notebook trusts the dataset names and descriptions. That is reasonable but not verified from the data, for example by comparing the intensities of the two stacks. Reading (a) of problem 4 depends on it.
6. **[does not affect a conclusion]** `bdbc.list_assets` labels every non-.nwb file as "mp4", so the notebook's statement that the dandiset holds nothing else was not supported by its own output. My API query confirms it holds only .nwb and .mp4 files. Neither blocked claim checks the "IsVariantFormOf" Matsuzaki-lab repository (mmlab-repo.m.u-tokyo.ac.jp) or the Google Drive linked in the dandiset metadata.
7. **[does not affect a conclusion]** Cell 16: there is one 16-day gap, and the pooled s.d. of days per break is 1.69 against the paper's 0.7. The mouse is not named and the outlier is not discussed. The paper probably excluded or handled it differently; the means still pass.
8. **[does not affect a conclusion]** Cell 6: the trial tables hold T_pull values of 0.0 s where the Methods give a 1 ms start. Also, raw tone TTLs exceed the trial count by up to 145 in some sessions. The trial table is used as the denominator, consistently with the down-sampled tone series.
9. **[does not affect a conclusion]** `task_session` assumes the lever is sampled at 5 kHz (`n = CUE_WINDOW_S*5000`) without printing the sampling rate. Readings (a) and (b) of the response rate agree, so this is harmless here.

**C. What I could not check**

- **fig6b-movement-order:** whether the claim holds under a sound onset detector. Two outputs would let me judge it: per-keypoint grand traces with their baseline s.d., and onsets under a sustained-crossing rule (for example, ≥ 100 ms above threshold).
- **Signal degradation, reading (a):** whether 8 frames approximate the full median. Needed: for a few sessions, the 8-frame F_B0 next to the full-session median, and a listing of the groups under `processing/ophys`.
- **Forepaw session count:** which 2–3 sessions explain 356/357 against the paper's 354/355. A list of the body-keypoint task sessions with their notes would show this.
- **Training breaks:** whose gap is 16 days, and whether a task session falls inside it. Needed: the BR rows with days > 4.
- **Pixel-map readings for fig4d:** not run in the notebook, and I could not run them under my constraints. They are not needed, since the ROI readings decide all three claims.
- **Blocked claims:** I could not check the lab repository and the Google Drive for the manual annotations.
