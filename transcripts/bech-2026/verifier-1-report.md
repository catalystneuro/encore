**A. Outcomes** (40 claims in the claims file)

| claim | outcome | reason |
|---|---|---|
| session-list-link | partially_reproduced | 98.0% of listed sessions found (cell 5). Every list used in a test matches in sessions and mice, but the pool list has 1451 sessions against the 1449 the claims file gives; 30 of them are not in the dandiset and 3 more have no readable table. |
| expert-sessions | not_reproduced | The Methods' rule, run on all behavioural sessions as the criterion requires, gives 318 sessions in 49 mice (expected 201 ± 20.1 and 41 ± 4.1). Blocks per session, 24.7, is within 23 ± 2.3. 12 sessions of the code's list fail the rule (cell 7). |
| fig1c-auditory-hit-both-contexts | partially_reproduced | With the code's list: W+ 95.7, W- 93.7 (in tolerance). With the rule's sessions: W- 88.4, outside 94 ± 5 (cell 10). The claims file has no rule for when the two selections disagree. |
| fig1c-whisker-context-modulation | reproduced | 84.3/31.4 and 83.9/31.7, all within the SDs (cell 12). |
| fig1d-independent-of-noise-identity | reproduced | In both noise groups under both selections, W+ is higher, p ≤ 1e-17 (cell 14). |
| fig1c-catch-higher-wplus | reproduced | 13.3/4.4 with t -8.52 and p 1.6e-10 under the code's list, the paper's p (cell 16). |
| fig1e-context-off-no-discrimination | reproduced | Off-day transition tests give p 0.275 and 0.545, so no discrimination (cell 28). |
| fig1g-first-trial-switch | reproduced | All four values within the SDs; t 20.9 and -14.2 (cell 18). |
| fig1f-gradual-further-adaptation | reproduced | +2 is closer to the new context than +1, and +4 at least as close as +2, in both directions and both selections (cell 20). |
| fig1h-temporal-integration | reproduced | Fitted curves run in the stated directions. Both anticipation readings give p ≥ 0.05 under every variant (cell 22). |
| fig1i-pupil-larger-wplus | reproduced | Pupil 0.534 vs 0.513 mm², Bonferroni p 0.017. Whisker angle and jaw give corrected p 0.56 and 1.0 (cell 64). |
| fig1i-posture-before-lick | reproduced | Jaw 0.282 vs 0.247 (corrected p 0.0038). Whisker angle 87.0 vs 88.4 computed, 97.3 vs 98.6 stored (corrected p 0.012 and 0.010) (cell 66). |
| fig1j-jaw-speed-context | partially_reproduced | The jaw-speed parts hold (2.96/2.50 and 2.83/2.58; corrected p 0.0015 and 0.0099). The claimed absence fails: whisker speed differs by context, corrected p 0.018 (0.012 with the stored angle) (cell 68). The criterion has no partial clause; strictly this is not_reproduced. |
| fig1k-model-accuracy | blocked (other) | Not run "within the time limit". The data exist: all 60 model sessions have trial tables (cell 5) and the face-video data load. |
| fig1k-context-strongest-feature | blocked (other) | As above. |
| fig1l-shap-whisker-trial-in-block | blocked (other) | As above. |
| supp1c-wplus-blocks-longer | partially_reproduced | With the code's list: 195.5 vs 185.4 s, t 5.39, p 3.4e-6, all as required. With the rule's sessions, W- is 189.4 s, outside 185 ± 4 (cell 24). |
| supp1d-faster-response-wplus | partially_reproduced | Directions and corrected tests hold; under the code's list t -8.71, p 1.8e-10 and t -3.95, p 6.2e-4, essentially the paper's. All four means are about 100 ms above the paper's, outside ± 9 (cell 26). |
| fig2c-catch-little-effect | blocked (methods_underspecified) | Null (ii) with d' ≥ 0.5 gives 11 sites (more than 3); every other reading gives 3 or fewer (cell 32). |
| fig2d-auditory-a1-frontal | blocked (methods_underspecified) | Null (ii) with d' 0.5 or 0.8: reproduced. Null (i), and d' ≥ 2: not (cell 34). |
| fig2e-whisker-sensory-premotor-reduction | blocked (methods_underspecified) | Same split of readings as fig2d (cell 36). |
| fig2e-rsc-tjs1-increase-wminus | blocked (methods_underspecified) | Readings give reproduced, partially and not (cell 38). |
| fig2-no-effect-control-mice | blocked (methods_underspecified) | 61, 20 and 0 of 246 groups pass d' 0.5, 0.8 and 2 (cell 42). |
| supp2-muscimol-ws1-rsc | reproduced | wS1: -0.405 (W-, p 3.2e-4) and -0.653 (W+, p < 1e-5). RSC W-: +0.206, p 0.060 (cell 46). In W- the wS1 p does not reach the paper's < 1e-5. |
| fig2f-latency-frontal-not-rsc | blocked (methods_underspecified) | Reproduced at d' 0.5 and 0.8; partially at d' 2 (cell 44). |
| fig2cd-rsc-no-effect-catch-auditory | blocked (methods_underspecified) | Null (ii) at d' 0.5 and 0.8 finds an RSC catch effect (W+ d' 0.84); the other readings find none (cell 40). |
| fig3c-jaw-onset | not_reproduced (low confidence) | On the Methods' trial set (correct whisker trials), onset is 135 ± 14 ms and only 2 of 5 mice reach d' ≥ 1. The code's set gives 86.3, inside 108 ± 24 (cell 70). Implementation problems (B2) could change this. |
| fig3e-auditory-similar-across-contexts | partially_reproduced | The contexts are similar (max \|d'\| 0.75); A1 comes first, but RSC is not before wM1/2. Same under every reading (cell 50). |
| fig3f-whisker-divergence-after-50ms | reproduced | wS1 and wS2 \|d'\| ≤ 1.08 from 20 to 50 ms; RSC and wM1 above 2 by 120 ms; all baselines (cell 52). |
| fig3h-rsc-first-context-discrimination | partially_reproduced | In the ROI ranking RSC is first (50 or 60 ms; wM1 next at 80 ms) under all readings (cell 54). The pixel version was not run. |
| fig3-gcamp-consistent-controls-flat | partially_reproduced | The GCaMP6f part holds. tdTomato and GFP mice show W+ vs W- d' of 2.8 to 4.7 in RSC/wM, so the controls part fails (cell 56). |
| supp3c-rsc-projects-to-wm | blocked (data_missing) | Confirmed on the API: only behavior, image and ophys NWB files, no light-sheet or tracing data. |
| fig4b-wminus-higher-correlation-correct | blocked (too_large) | The ophys files are 62 GB median, 138 GB max (API). Part testable, see C. |
| fig4b-no-context-modulation-incorrect | blocked (too_large) | As above. |
| fig4b-connected-network | blocked (too_large) | As above. |
| fig4c-inhibition-propagates-forward | reproduced | All three parts hold at both baselines (cell 58). |
| fig4d-trajectories-follow-lick | not_reproduced | In W-, RSC at (-1.5, 0.5) is closer to no-lick, and wS1, wS2, wM1/2 and ALM are all closer to lick (cell 74). |
| fig4e-rsc-tjs1-smaller-angle | partially_reproduced | Holds in W+. In W-, RSC is 37.5° against ALM 30.3° and wM2 30.4° (cell 76). |
| fig4fg-angle-predicts-lick-change | reproduced | Methods angle: r -0.41 (p 0.0088) in W- and -0.33 (p 0.043) in W+ (cell 78). |
| supp4d-photoactivation-control | reproduced | The stimulated ROI rises; 0 or 1 of 8 other ROIs fall below control, both sites, both baselines (cell 60). |

Chance levels: the paper states none for the claims that were run. Fig 1K's balanced-accuracy chance (0.5) was never reached because the model was not run.

**B. Problems**

1. **Opto null (i) cannot detect a context-shared effect** [affects a conclusion] (claims file; `opto_map` null='blocks'). Shuffling block labels and recomputing ΔP against control trials leaves the laser effect inside the null. I checked this on synthetic data: a laser effect of about -0.21 averaged over contexts gave a null mean of -0.208, so d' ≈ 0. The notebook shows the same thing: null means range from -0.35 to 0.18 (cell 30). The code follows the Methods sentence faithfully. But under this reading no effect shared by both contexts can ever pass, so the "every reading agrees" rule can never be met for fig2d or fig2e. That is the paper's own Figure 2D finding (similar effect in both contexts). This is a claims-file reading that does not fit the paper's figures; it drives the blocked outcomes in fig2c, d, e and cd.
2. **fig3c implementation departs from the Methods** [affects a conclusion] (cell 70):
   - Any trial with a single frame under 60% likelihood is dropped. Low likelihood tends to coincide with jaw movement, so this biases the onset.
   - Trials are pooled within each mouse, with no averaging within session and then over sessions as the Methods state.
   - The 70% session rule is not applied.
   - One of the 6 jRGECO1a mice is missing.
   - The readings disagree and the result sits near the tolerance edge.
3. **fig3h pixel part was not attempted** [affects a conclusion]. Only short trial windows are needed (about 40 frames for each W+ hit and W- miss). With windowed reads that is tens of GB, not whole 60 GB files. The claim that the stack is "unchunked" is stated, never shown.
4. **fig1k, fig1k-context and fig1l were not run** [affects a conclusion] for time only; the data are present.
5. **Muscimol injection day is taken by date rank** [affects a conclusion] (`pharma`, cell 46). This is never checked against the files. Only 2 of 14 wS1-muscimol sessions and 4 of 12 RSC-Ringer sessions are typed `pharma_session` (cell 5).
6. **Computed whisker angle is about 10° off the stored one** [does not affect a conclusion] (`_dlc_one`). The notebook's angle per the Methods is about 87°; the stored `whisker_angle` gives 97.3 and 98.6, the paper's exact numbers, as do its p-values. Likewise the fixed ×200 jaw-speed variant reproduces the paper's t and p, so the paper used ×200. Both versions pass.
7. **supp1d has an unexplained ~100 ms offset** [does not affect a conclusion]. The t and p match the paper while every mean is about 100 ms high, which points to a different definition of lick time. It was not investigated.
8. **The fig3e "peak" order reading is uninformative** [does not affect a conclusion] (cell 50). Every ROI peaks at 120 ms, the edge of the window.
9. **Some widefield trials may be misaligned** [does not affect a conclusion] (`_grid_one`). Trials where the first frame after the stimulus comes up to 81 s late (gaps in imaging) are kept as if aligned. How many there are is not reported.
10. **Three files lose their trial tables** [does not affect a conclusion] (`_trials_one`). Their tables are discarded because `BehavioralEpochs` is missing. They are in the pool list only.
11. **Expert rule run on every session type** [does not affect a conclusion] (cell 7). The rule includes opto, pharma and widefield sessions. 60 sessions with the `context_` prefix are excluded without identification. Either way the count stays far above 201.
12. **Site count differs** [does not affect a conclusion]. The opto maps use 41 sites; the claims file says 39.
13. **Context Off days are labelled pink/brown, not white noise** [does not affect a conclusion] (cell 28). This was not checked. The behaviour (W+ minus W- of 5.6 Off against 49.4 On) fits Off days.
14. **No rule for disagreeing selections** [affects a conclusion] (claims file). Where the expert rule and the code's list disagree (fig1c-auditory, supp1c), the claims file says nothing. I scored these partially_reproduced.

**C. What I could not check, and the output that would settle it**

- **Muscimol days:** print the `session_type` and date rank of each listed muscimol and Ringer session (B5).
- **Widefield alignment:** print the number of trials per session whose lag exceeds one frame (B9).
- **fig3c:** print trials kept per mouse after the NaN filter, and the onset computed with session-then-mouse averaging. Also show why the sixth mouse is absent (B2).
- **Pixel stack size:** print the shape, chunking and dtype of `processing/ophys/dff0` for one session (B3).
- **Excluded sessions:** print the session types and lists of the 60 `context_` sessions (B11).
- **fig4d and fig4e:** print the PC3 loadings and the sign convention used, to check them against the code.
- **fig4b:** part of it could be tested from the grid ROI traces: seed-to-seed zero-lag correlations in the 2 s before each trial, with a block-shuffle null. It was not run.
- **fig1k:** the balanced accuracy and its 0.5 chance level.
