## A. Outcomes (38 claims in the claims file: 19 reproduced, 8 partially reproduced, 6 not reproduced, 5 blocked)

| Claim | Outcome | Reason |
|---|---|---|
| fig1d-ri60-vs-rr20-shocks | not_reproduced | Cell 21: schedule p = 0.071 and interaction p = 0.59. The RI60 late-vs-early test gives Bonferroni p = 0.063, which misses the 0.01 bar, so even the partial condition fails. Only 5 RR20 mice have both probes (paper n = 9). |
| fig1e-omission-ri60-longer | partially_reproduced | Cell 23: RI60 34.0 min vs RR20 17.7 min, so the direction holds, but Student's t gives p = 0.070 (Welch p = 0.0005). n = 19 and 4; the paper has 20 and 7. |
| fig1f-omission-shock-no-correlation | reproduced | Cell 25: r = 0.335, p = 0.175, n = 18 (paper r = 0.42, ns). |
| fig2a-phenotype-rule | partially_reproduced | Cell 27: stored labels are 9/9/18, and the rule matches 31 of 32 mice. The one miss is 048.392, with exactly 13 shocks early, against the Methods' "more than 13". The counts match by construction because they are the authors' stored labels. |
| fig2b-only-dpr-increase | reproduced | Cell 29: interaction p = 3e-7. Only DPR changes (Bonferroni p = 0.0004); PR and PS both have p = 1. |
| fig2c-nosepoke-rate | reproduced | Cell 31: ANOVA p = 4e-6; Tukey DPR vs PS p = 0.0002 and PR vs PS p < 0.0001. |
| fig2d-omission-pr-vs-ps | reproduced | Cell 33: PR 51.65 and PS 28.06 min, both within tolerance; Tukey PR vs PS p = 0.037. PS n = 10 (paper 11). |
| fig2k-ps-wait-longer | partially_reproduced | Cell 35: PS has the longest wait, but its mean of 53.9 s is just outside 38 ± 15. Tukey PS vs DPR p = 0.051 (PS vs PR p = 0.045). |
| fig2l-extra-nosepokes | partially_reproduced | Cell 37: all three means are within tolerance and PS < PR, but Tukey p = 0.117. |
| fig2m-inter-reward-interval | reproduced | Cell 39: means 81.8, 72.0 and 69.6 s, all within tolerance, PS longest; both KS tests p < 1e-29. |
| fig2n-rewards-per-session | reproduced | Cell 41: all means within tolerance; ANOVA p = 0.021; Tukey PS vs DPR p = 0.048, which is borderline (see B6). |
| fig2o-escalation-timing | partially_reproduced | Cell 43: part (i) fails because RI30 PR vs DPR gives p = 0.114 (PR vs PS p = 0.006). Part (ii) holds: the DPR median RI60 slope 0.81 is above PR's 0.49. |
| figs1i-ri60-more-rewards | reproduced | Cell 45: 41.9 vs 15.4 rewards per session, p = 1.4e-11. Only 6 RR20 mice. |
| figs2b-males-more-shocks | reproduced | Cell 47: sex effect F1,30 = 9.81, p = 0.0039, males higher. This is not p < 0.0001, and sex is confounded with phenotype (17 of 18 PS mice are female). |
| fig3e-ri30-dms-peaks | blocked (data_missing) | Confirmed against the archive: only 63 fiber photometry assets are large enough to hold photometry (53 RI60, 9 RR20, 1 "Probe Test"; 0.2 MB vs 365 to 591 MB for the rest). There are none for RI30 or the shock probes. The "slower across RI60 in DPR" half could be tested from the early and late RI60 scores, but it was not. |
| fig3f-dms-score-phenotype | not_reproduced | Cell 50: phenotype LR p = 0.10; per-stage ANOVAs p = 0.12 (early) and 0.27 (late). The means are ordered PR > DPR > PS in both stages. The design has 2 stages where the paper had 3 (no RI30 recordings), and without the dropout step p = 0.39. |
| fig3g-dms-score-shock-correlation | partially_reproduced | Cell 52: by the criterion, only reading (c) qualifies: r = 0.375, p = 0.045, n = 29, with no reading within 0.53 ± 0.053. Pooled (a) gives r = 0.17, p = 0.24. Weak support (see B2). |
| fig3h-dms-score-omission-no-correlation | reproduced | Cell 54: r = 0.014, p = 0.96, but n = 12 only. |
| fig4f-dls-score-no-phenotype | reproduced | Cell 56: phenotype p = 0.48. |
| fig4g-dls-score-shock-no-correlation | not_reproduced | Cell 58: pooled r = 0.326, p = 0.024. Without the dropout step r = 0.11, p = 0.45 (see B1). |
| fig4h-dls-score-omission-no-correlation | reproduced | Cell 60: r = 0.31, p = 0.32, n = 12. |
| fig5f-dms-chr2-escalation | not_reproduced | Cell 65: no interaction is significant (p = 0.49 to 0.98), and the ChR2 slope is not the largest in either stage. The per-mouse-slope variant does show FR1 ChR2 > both controls (p = 0.015 and 0.021) but not RI30 (see B3). |
| fig5g-dms-chr2-more-shocks-early | not_reproduced | Cell 67: interaction p = 0.16; Tukey ChR2 vs EYFP on the first probe p = 0.51. n = 32 (paper about 38). |
| fig5h-dms-chr2-mostly-pr | reproduced | Cell 69: 12 of 13 ChR2 mice are PR, vs 6/12 Scrambled and 5/7 EYFP. Fisher p = 0.0497, which is borderline. |
| figs5f-chr2-pr-by-sex | partially_reproduced | Cell 71: males 100% (within tolerance); females 83.3%, 5 of 6, outside 71 ± 7.1. One female ChR2 mouse (126.286) has no probes. |
| fig5i-dms-stim-no-omission-effect | reproduced | Cell 73: ANOVA p = 0.17. |
| fig6-nphr-learning-dropout | blocked (data_missing) | Per arm, the dandiset has NpHR 13, Scrambled 13 and EYFP 16 mice (cell 62). Fig 6F has 16, 15 and 16. The shortfall equals the paper's dropouts (4 NpHR, 2 Scrambled) minus one NpHR mouse that is deposited and flagged (270.476, no RI60). So most dropped mice were never deposited. The "Did Not Learn" flag also marks an EYFP mouse that reached RI60 (244.465), so it is not the paper's dropout criterion. No file says which mouse is in group 1 or group 2 (cell 75). Applied literally, the criterion gives not_reproduced because an EYFP mouse is flagged. |
| fig6g-nphr-fewer-shocks-late | partially_reproduced | Cell 77: NpHR < EYFP on the second probe, but Tukey p = 0.069 for mice with both probes (0.043 when all mice with a second probe are included). |
| fig6h-nphr-more-ps | reproduced | Cell 79: PS fraction NpHR 0.89 vs EYFP 0.33; PR fraction Scrambled 0.60 vs EYFP 0.40. Fisher p = 0.013 and 0.43. |
| fig6i-nphr-no-omission-effect | reproduced | Cell 81: p = 0.21. |
| fig7f-dls-escalation-similar | not_reproduced | Cell 83: the FR1 EYFP vs Scrambled interaction has p = 0.013, and the omnibus FR1 F-test p = 0.034. The paper gives no test for this claim. |
| fig7g-dls-stim-no-shock-effect | reproduced | Cell 85: group p = 0.055 and interaction p = 0.068, both borderline. |
| fig7h-dls-similar-phenotypes | reproduced | Cell 87: chi-square p = 0.12, but the smallest expected count is 1.5, so the test has low power. |
| fig7i-dls-no-omission-effect | reproduced | Cell 89: p = 0.53. |
| figs3ab-dat-protein-not-reduced | reproduced | Cell 91, Zenodo table: DMS p = 0.41, DLS p = 0.20. Only 3 WT vs 4 het mice, all female. |
| figs1a-shock-aversive | blocked (data_missing) | The archive's 4139 assets are all NWB, and no metadata mentions fear or freezing. Every subject belongs to fiber photometry, optogenetics or western blot. |
| figs3cd-open-field | blocked (data_missing) | Same archive check; there are no open field assets. |
| fig3c-gcamp-in-dopamine-neurons | blocked (data_missing) | Same archive check; there is no histology or cell counts. The 16 western blot assets hold blot images only. |

No chance levels apply: the paper states none for any selection.

## B. Problems

1. [affects a conclusion] `seiler.dropout_mask` / `zscored_dff(mask_dropouts=True)`: the dropout step is the author's own choice. It is in neither the Methods nor the authors' code, and it decides fig4g (p = 0.024 with the mask, 0.45 without). It also weakens fig3f without the mask (p = 0.10 becomes 0.39). Cell 15 gives a reason for it (|z| above 1000 in 6 sessions), but how much the outcomes depend on it is not stated anywhere.
2. [affects a conclusion] Cell 52 tests three readings for fig3g with no correction. The partial outcome rests on reading (c) alone at p = 0.045, while the pooled reading, which is the closest to the paper's "shocks received in shock probes", gives r = 0.17.
3. [affects a conclusion] `escalation` (cell 64) fits one OLS over pooled sessions with no mouse term. Mice contribute 1 to 13 FR1 sessions, so the late session indices come only from slow learners. The per-mouse slope variant reverses the FR1 result for fig5f. The criterion fixed this design in advance, but the design is weak.
4. [affects a conclusion] For fig6-nphr-learning-dropout, cell 75 uses the "Did Not Learn" flag but never compares the per-arm mouse counts with Fig 6F's 16/16/15. That comparison shows the dropped mice are mostly missing from the dandiset, which makes this claim blocked, not testable.
5. [affects a conclusion] Cells 3 and 13: only 6 RR20 mice are in the dandiset (Fig 1D has 9, the Methods 7), 5 with both probes and 4 with an omission probe. fig1d, fig1e and figs1i are underpowered against the paper's design. fig1e also hinges on Student vs Welch: the variances differ about 250-fold.
6. [affects a conclusion] Cells 19 and 41: there are 21 training sessions with 0 rewards and some with a nosepoke rate of 0. The notebook never inspects them (empty or truncated file vs real session). They enter the per-mouse means for fig2c, fig2n and figs1i, and fig2n's key Tukey p is 0.048.
7. [affects a conclusion] Cell 15: the number of mice with late photometry differs from Fig 3E (PS 11 vs 13, PR 4 vs 5, DPR 7 vs 6). The paper's session set and artifact exclusions cannot be recovered, and fig3f also lacks the RI30 stage, so its comparison with F2,33 is not like-for-like.
8. [does not affect a conclusion] In cell 35, the fig2k PS mean is driven by one mouse at 171 s. The median-of-sessions variant (32.2 s) would fall within tolerance. The criterion specifies the mean.
9. [does not affect a conclusion] fig2a's 9/9/18 counts come straight from the stored labels, so they are circular. Only the rule check (31 of 32) is informative.
10. [does not affect a conclusion] Cell 15: some recordings end up to 2257 s before the behavioral session does, and events outside the recording are dropped silently. The number of events kept per session is never shown.
11. [does not affect a conclusion] Cells 54 and 60: the absence claims fig3h and fig4h rest on n = 12 and have little power to detect r = 0.1 or −0.21.
12. [does not affect a conclusion] fig3e: the RI60 part of the claim (DPR peaks growing from early to late) could be tested from the existing `sc` table, but it was not.

Things I checked and found correct:
- `mixed_anova` (cell 19) gives exactly the same F and p as pingouin `mixed_anova` on synthetic unbalanced data.
- `classify`, `drop_bursts`, `reward_measures`, `peak_score`/`psth` timing, `zscored_dff` (the first second is NaN and the transient lands in the right place), `session_length` and `omission_time_min` all behave as documented on synthetic inputs.
- The LR degrees of freedom in `phenotype_model` (4 and 3) are correct.
- I found no leakage or train/test issue; none applies here.

## C. What I could not check

- Anything inside the files: I downloaded nothing. That covers the zero-reward sessions, the dropout masking on raw traces, the meaning of the "Did Not Learn" flag, and the clock mismatch in 332.393. Outputs that would help: a table of zero-reward and zero-rate sessions with subject, stage, phenotype, file size and event counts; and fig2n and fig2c recomputed without them.
- Whether fig3g reading (c) survives without the dropout step. Needed output: the readings (b) and (c) with `DMS_score_nomask`, plus the per-session dropout fractions of the sessions that enter fig3g and fig4g.
- The Zenodo table layout. Cell 91 reads rows i+1 to i+8 and columns 7 and 8 without printing them. Needed output: the parsed blocks with their header row.
- Per-mouse wait distributions for fig2k. Needed output: the per-mouse means and number of waits, so the 171 s mouse can be inspected.
- The Figure S1 to S7 legends, which are not in the PMC text. figs1i, figs2b and figs5f were judged on main-text statements only.

I saved the paper text under `paper/` (main text and figure legends only, no figures).
