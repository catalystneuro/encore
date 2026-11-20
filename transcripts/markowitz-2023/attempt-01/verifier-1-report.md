**A. Outcomes** (24 claims in the claims file; the notebook tests 14 and marks 10 blocked)

| Claim | My outcome | Reason |
|---|---|---|
| fig1e-velocity-timescales | partially_reproduced | Cell 12: both measures are significantly negative at all 20 timescales under 10 s. The rate measure is significantly positive at 27 of 100 timescales of 10 s or more (max r 0.185). The amplitude measure is never significantly positive at 10 s or more (max r 0.007), so the claim holds for one measure. |
| fig1h-syllable-dlight-differs | partially_reproduced | Cell 15: H = 258.85, outside 209.29 ± 20.93. P = 1.6e-35 and n = 518 match the paper. |
| fig1l-identity-not-decodable | reproduced | Cell 17: accuracy is 0.0287 from peak amplitude and 0.0335 from waveform, both below the 0.054 criterion. Chance is 1/37 = 0.027 and shuffled labels give 0.0269. The paper gives no numeric chance level, only "compared to 100 shuffles". |
| fig2b-dlight-usage-across-syllables | reproduced | Cell 19: held-out r = 0.160 against a null 95th percentile of 0.034 (0 of 200 shuffles exceed it); 508 pairs. |
| fig2i-dlight-entropy-across-syllables | reproduced | Cell 19: held-out r = 0.270, 0 of 200 shuffles exceed it. |
| fig2e-dlight-predicts-future-usage | partially_reproduced (provisional) | Cell 22: P < 0.05 at n = 10 and at 8 of the 10 values up to 190; P = 0.12 at n = 130 and 0.08 at n = 150. The shuffle null is inflated (problem 1), so this may become reproduced once fixed. |
| ed7-dms-fewer-transients | reproduced | Cell 24: DMS median 56.1/min against DLS 62.1/min, U = 17, P = 0.0064. With DLS as the first group U = 95; the ED7b legend gives U = 97. |
| ed7-dms-no-usage-prediction | not_reproduced | Cell 25: DMS is significant at 8 of 10 values of n ≤ 190, and its mean r (0.013 to 0.032) is larger than DLS's. Problem 1 makes the test conservative, so this outcome is robust. |
| fig3e-optoda-learning | reproduced | Cell 27: U = 198 (paper 197), one-sided P = 0.0013, f = 0.82; 20 Opto-DA and 12 control mice, matching the paper's U/f. |
| fig3f-cumulative-counts | reproduced | Cell 27: U = 182 (paper 184 ± 18.4), P = 0.0083, f = 0.76. |
| fig3e-learner-count | not_reproduced | Cell 29: 7 learners against the paper's 9. All 7 are in the code's list; 3442 (change 47.3) and dls-ai32jr-1 (41.7) fall below the control maximum of 54.5 (vta-nacc-ctrl-6). |
| fig3h-stim-post-correlation | reproduced | Cell 30: r = 0.891 with P = 0.016 on this attempt's 7 learners, and r = 0.888 with P = 0.001 on the code's 9. Both are within tolerance. |
| fig3l-no-kinematic-effect | blocked (metadata_insufficient) | The literal criterion gives 9 of 20 Opto-DA mice significant (not_reproduced), but 9 of 12 no-opsin controls are also significant (cell 32). Problem 2 shows the substitute catch set is not the paper's, so the test cannot be interpreted. |
| fig3m-long-stim-velocity | blocked (metadata_insufficient) | The literal criterion gives 1 of 3 significant (partially_reproduced), but the catch set includes onsets during ongoing 3-s trains (n_catch 1159 against n_stim 606). With catch trials at least 4 s after a stimulation, 0 of 3 are significant while both controls stay significant (cell 33). |
| fig2a-food-reward-transients | blocked (data_missing), partly testable | I confirmed in the asset list that the archive has no food-reward sessions or consumption times. The spontaneous half (2.12 ± 0.80 z, n = 5,247) could be computed from the photometry files. |
| fig1f-syllable-vs-movement-onset | blocked (other: not attempted); testable | dLight, 2D speed and syllables are all present. |
| fig2k-dlight-predicts-sequence-variability | blocked (other: not attempted); testable | Same data as fig2e. |
| fig3i-optoda-entropy | blocked (metadata_insufficient) | Catch trials are not marked. The entropy after stimulation against the pre-stimulation baseline could still be tested. |
| ed10d-optoda-vigour | blocked (other: not attempted); probably testable | There are 94 velocity-session files from 9 mice. I did not check whether the fast/slow condition is labelled in them. |
| fig4b-endo-da-influence-consistent | blocked (other: not attempted); testable | 8 dLight+ChrimsonR mice have both photometry and closed-loop sessions. |
| fig4c-endo-da-predicts-learning | blocked (other: not attempted); testable | Same mice as fig4b. |
| fig4f-catch-dlight-predicts-learning | blocked (metadata_insufficient) | Needs dLight on catch trials; only the substitute catch set (problem 2) is available. |
| fig4h-decoding-model | blocked (other: not attempted) | Data are present. The model is complex, but the paper's code is public. |
| fig5-rl-model | blocked (other: not attempted) | A simulation built on observed transition matrices and dLight; the inputs are available. |

**B. Problems**

1. [affects a conclusion] Cell 22, `future_usage`: the shuffle permutes `pk` including its NaN peaks (81,696 instances have no peak, cell 10). After shuffling, a NaN lands on a used instance and the whole (session, syllable, segment) group's r becomes NaN in the null but not in the observed value. I ran the function unchanged on synthetic data with 10% NaN peaks: 66% of groups drop out of the null, and the null's 95th percentile rises from 0.0077 to 0.0178. The test is therefore conservative. This may explain the two non-significant points (n = 130 and 150) in fig2e. It does not change ed7-dms-no-usage-prediction, which is already significant. Fix: shuffle only finite peaks.
2. [affects a conclusion] Cells 32 and 33, `trials`: the paper's Methods state that stimulation was given on 75% of target detections, so true catch trials are about 25% of detections. The substitute catch set is 31 to 47% of target onsets per mouse (for example, mouse 1528 has 1,270 stimulations and 1,067 catch trials). Most no-opsin controls show stimulation above catch (9 of 12 for 250 ms; 2 of 2 for 3 s), which points to a biased selection. In the pulsed analysis, onsets during an ongoing 3-s train are counted as catch trials.
3. [affects a conclusion] Cells 0 and 31: the notebook calls fig3l and fig3m "blocked once run" without stating that the pre-set criterion defines exactly this substitute catch set. The blocking should rest on evidence from problem 2 (the catch fraction and the control results), and the literal-criterion outcomes should be reported alongside it.
4. [does not affect a conclusion] Cell 30, `r_shuffle`: `(r < |null|).mean()` is a two-sided test but is labelled one-sided. It is conservative, and P stays below 0.05.
5. [does not affect a conclusion] Cell 12: `keep = cnt == mode` also drops bins with more frames than the mode, while the criterion drops only those with fewer. At timescales of non-integer frames, such as 0.25 s (7.5 frames), this can discard about half the bins.
6. [does not affect a conclusion] The photometry selection in cells 5 and 10 never excludes habituation sessions. Asset metadata shows "Habituation session 1" files for dms-dlight-1, -4 and -6. The closed-loop analysis does exclude them (cell 27).
7. [does not affect a conclusion] Cell 17 uses `min_samples_leaf=5` and a single label shuffle. The paper used 1,000 trees and 100 shuffles.
8. [does not affect a conclusion] Cell 19 prints shuffle P = 0.000 from 200 shuffles; it should be reported as P < 0.005.
9. [does not affect a conclusion] Paper consistency checks pass: 14 DLS and 8 DMS mice, 518 = 14 × 37 pairs, U/f for fig3e implies 20 × 12 mice, and 3 Opto-DA plus 2 control mice had 3-s sessions. Helper functions `onsets`, `syllable_table` (0 to 0.3 s window = 10 frames), `outgoing_entropy`, `binned_onset_counts`, `monday_baseline` and `session_passes_filters` behaved correctly on synthetic inputs.

**C. Not checked, and what would settle it**

- Whether the NaN peaks fall inside groups or cover whole segments in the real data. Adding the number of groups contributing to each shuffle null, or rerunning fig2e and the DMS test with NaN-free shuffles, would settle fig2e.
- Whether online labels stay aligned with pulses after sorting the 547 rotated closed-loop clocks. The pulse-onset check (0.938 against 0.041) pools rotated and unrotated sessions; splitting it by `rotated` would settle this.
- Why 3442 and dls-ai32jr-1 are not learners here. Per-target stimulation and baseline counts and the chosen baseline day for these two mice and for vta-nacc-ctrl-6 would show it.
- The paper's "n = 378 experiments" for baseline photometry, against 194 DLS no-stimulation sessions passing quality here. A session count before and after each filter, per mouse, would reconcile them.
- The cause of the H difference in fig1h (258.85 against 209.29). Showing H with and without the quality filter and per session set would help.
- For fig3l and fig3m, the fraction of target onsets that were stimulated per session, compared with the paper's 75%, and the same analysis restricted to onsets at least 2 s from any pulse.
