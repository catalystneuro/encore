**A. Outcomes** (32 claims in the claims file: 20 tested, 12 blocked)

| Claim | Outcome | Reason |
|---|---|---|
| fig2-kord-suppresses-mpfc | blocked (data_missing) | The archive holds only `data.zip`, docs, `filelist.txt` and `checksums.md5` (S3 listing). The files are 172 dopamine-neuron files with four variables (cells 3, 63). There are no mPFC units. |
| figs1e-kord-abolishes-late-activity | blocked (data_missing) | Same reason: no mPFC units. |
| figs6ce-kord-task1-animal | blocked (data_missing) | Same reason: no mPFC units. |
| fig3g-anticipatory-licking | blocked (data_missing) | No lick variable in any file (cell 3). The data description lists none. |
| figs3-task1-licks-more-sooner | blocked (data_missing) | No licks. |
| figs3-salb-spares-licking | blocked (data_missing) | No licks. |
| figs4-cell-types-unchanged | blocked (data_missing) | Only the 172 identified dopamine neurons are present (cell 3), not the 761 VTA neurons. |
| figs5b-task2-salb-below-free-water | blocked (data_missing) | There are no free-water events. `reward_onsets` exist only on odor A to C rewarded trials (cell 63: 0 elsewhere), and no trial type 12 exists. |
| figs5c-odorbc-normalized | blocked (data_missing) | Same reason: no free-water events. |
| anova-slopes-task-drug | blocked (data_missing) | Normalization by the free-water response is impossible (see B5). |
| anova-time-task-drug-interaction | blocked (data_missing) | The free-water response is a required term (see B5). |
| figs6-salb-without-kord | blocked (data_missing) | Files by group are 42/42/41/47 = 172, matching the four KORD groups exactly. The 26 no-KORD neurons are absent. |
| fig4a-task1-saline-post-decrease | reproduced | Cell 14: F(8,328) = 12.61, p = 8.4e-16, slope −2.21, 42 neurons. Paper: F = 12.6, p = 9.1e-16. |
| fig4b-task2-saline-post-increase | reproduced | Cell 16: F(8,320) = 3.70, p = 3.8e-4 (same as the paper), slope +1.30, 41 neurons. |
| fig4b-odorc-below-latest-odora | reproduced | Cell 18: C 12.30 vs A at 2.8 s 15.06 spikes/s, F(1,40) = 22.66, p = 2.5e-5. The single-trial reading also gives p = 1.6e-7. |
| fig4ab-saline-pre-decrease | reproduced | Cell 20: both tasks p ≤ 1e-7 with negative slopes, under both windows and both 40-min readings. 0–400 ms gives p = 3.6e-11 and 5.3e-18, matching the paper's 3.5e-11 and 5.3e-18. |
| fig4c-task1-salb-post-decrease | reproduced | Cell 22: F = 11.34, p = 3.3e-14 (paper 11, 3.3e-14), slope −2.33. The count-once variant with 39 neurons holds too (cell 23). |
| fig4d-task2-salb-flat | reproduced | Cell 25: F(8,368) = 0.70, p = 0.69 (paper 0.69, 0.70), slope −0.27, 47 neurons. |
| fig4cd-salb-pre-decrease | reproduced | Cell 27: all p ≤ 1.4e-9 with negative slopes, both windows. Task 1 0–400 ms gives p = 2.4e-19, the same as the paper. |
| fig5f-task2-slope-signs | reproduced | Cell 33: 29 positive and 12 negative (saline), 24 negative of 47 (SalB) under the trial baseline. All readings are within tolerance. |
| fig5e-task1-significant-slopes-unchanged | reproduced | Cell 35, trial baseline: 16/0 and 16/2, Fisher p = 0.487. Fisher p ≥ 0.05 under every reading. Counts fall outside tolerance under the mean and none baselines (SalB 18 negative). |
| fig5f-task2-significant-slopes-shift | reproduced | Cell 37, trial baseline: 1/9 against 8/7, p = 0.0405 (paper 0.041), negative share 0.10 rising to 0.53. This depends on the reading: mean and none baselines give p = 0.239 (see B3). |
| fig4e-task2-slope-distribution-shift | reproduced | Cell 39: z = 2.15, p = 0.032. The SalB median is lower (−0.06 against 1.42). Holds under all readings (p ≤ 0.037). |
| fig5e-task1-slope-distribution-unchanged | reproduced | Cell 41: z = 0.14, p = 0.886 (paper z = 0.14, p = 0.89). p ≥ 0.63 under all readings. |
| fig5f-task2-slope-variance-up | reproduced | Cell 43: variances 10.23 and 20.29, ratio 0.50, p = 0.029. All within tolerance. Per mouse cannot be shown (no subject IDs); the criterion asks only for a description. |
| fig5e-task1-slope-variance-unchanged | reproduced | Cell 46: ratio 0.59, variances 8.81 and 14.89, p = 0.097. p ≥ 0.053 under all readings, so the result sits near the threshold under the mean and none baselines. |
| fig6ab-odorc-above-odorb | reproduced | Cell 48: saline C−B 0.913 (within 0.95 ± 0.095), F(1,40) = 5.31, p = 0.027. SalB C−B 0.997 (within 1.0 ± 0.1). Rank-sum p = 0.81. |
| fig6cd-omission-dips-intact | reproduced | Cell 50: all four omission rates are below baseline, p ≤ 0.0013. SalB used df (1,46) against the paper's (1,40); the counts are reported. |
| figs5d-omission-unchanged-by-salb | reproduced | Cell 52: no epoch significant under either test or either Bonferroni family. Smallest uncorrected p = 0.023. |
| fig7cd-model-intact | reproduced | Cell 57: every part holds (post-reward slopes −0.114 and +0.149, 100% of task 2 slopes positive, pre-reward slopes negative, omission dips −0.18 and −0.13), in 5 of 5 extra seeds. |
| fig7fgh-model-belief-impaired | reproduced | Cell 59: task 2 slope falls from +0.149 to +0.037, negative fraction rises from 0 to 0.32, task 1 slope −0.154, omission responses stay. Holds in 5 of 5 seeds. |
| fig7ijk-model-timing-impaired | reproduced | Cell 61: passes the claims-file criterion under both readings, in 5 of 5 seeds. A residual omission dip remains (see B1). |

No claim in this paper states a chance level for a selection, so there was none to compare.

**B. Problems**

1. [does not affect a conclusion] The claims file criterion for fig7ijk is weaker than the paper's word "abolished". It only requires that the omission minimum is not below the intact run's minimum. Under the timing impairment the mean omission RPE is still −0.073 (B) and −0.032 to −0.043 (C) in cell 54. That is about 40% of the intact dip, and for B about 4 standard errors below zero given the noise of 0.25 per point averaged over 50 simulations. So the dip is reduced, not gone. The verdict follows the criterion; whether "abolished" holds is left open.
2. [does not affect a conclusion] Cells 50 and 48 use 47 SalB neurons (df 46), where the paper prints df 40. This is consistent with the paper's own inconsistency, and the counts are reported as the criterion asks.
3. [does not affect a conclusion] fig5f-task2-significant-slopes-shift reproduces only under the trial-by-trial baseline (cell 37). That reading is the Methods' wording and the notebook's stated default, and it is the only one that recovers the paper's exact counts and p (1/9, 8/7 at our 8 vs 9; p = 0.0405 against 0.041). Under the mean and none baselines it fails (p = 0.239). The criterion for this claim does not say "under a reading", so this choice should be stated with the conclusion.
4. [does not affect a conclusion] Three task 1 SalB file pairs share 65 to 99.7% of their spikes (cell 5), so they are probably the same neuron deposited twice. The notebook keeps all six files to match the paper's n and runs a count-once variant. Every task 1 conclusion holds in that variant (cells 23, 27, 29, 35, 41, 46).
5. [does not affect a conclusion] `anova-time-task-drug-interaction` and `anova-slopes-task-drug` were blocked outright. Some of each could be run as a stated deviation: the tr × task and tr × drug × task terms without the free-water covariate, and the task and task × drug terms on unnormalized slopes. That would not satisfy the criterion, so blocked stands, but the notebook should say that part could be tested.
6. [does not affect a conclusion] `vta.load` skips zip members that are not `.mat`, and the notebook never prints the zip's member list. A lick or free-water file inside `data.zip` would go unnoticed (see C).
7. [does not affect a conclusion] In `vta.neuron_table`, the 40-min reading takes the session's first spike as recording onset. That is a stand-in, but both readings give the same conclusions (cells 10, 29 to 52).

Helper checks on synthetic inputs all came out as expected:
- `_count`: half-open window, NaN start gives NaN.
- `auroc`: 1.0 and 0.5 on separable and identical inputs.
- `isi_anova`: recovers a slope of −2.00 with df (8, 32) for 5 neurons.
- `slopes`: recovers about −2 under every baseline reading, and the mean and none readings agree.

The model port matches the linked MATLAB at d667730 in every part I compared:
- the observation matrix and impairment in `SimulateOdorC.m`
- `TDlearning.m`
- training carries `w(end,:)`, the weights before the last update
- 10 trials per simulation for odors B and C, one of them an omission
- awgn in `Organize_for_Plotting.m`

**C. What I could not check**

- Whether `data.zip` holds members other than the 172 neuron `.mat` files (licks, free water, mPFC units). Printing `zipfile.ZipFile(...).namelist()` in cell 1 would have settled it. The data description and `filelist.txt` suggest it holds none.
- `belief_td.blur_matrix`, `blur_vector`, the tonic and phasic indexing in `simulate`, and the A-odor simulation scripts, line by line against the MATLAB. A cell comparing one fixed-seed trace (b, rpe) with a MATLAB or Octave run of the same observation series would have verified the port directly.
- That the 21 trials with no trial type are the paper's exclusions. A per-group count of these trials, with each one's effect on that group's ANOVA, would have shown whether leaving them out matters. Given how small they are, I expect it does not.
- How independent the neurons are. There are no subject IDs, so the claim's "seen in individual mice" for the variance result cannot be tested. Cell 44 gives per-session variances only.
