**A. Outcomes (61 claims in the claims file: 32 tested in the two notebooks, 29 blocked)**

| Claim | My outcome | Reason |
|---|---|---|
| fig2c-male-blampfc-excitability-up | not_reproduced | Ephys cell 10, group-housed = 2022 cohort (21 neurons/7 mice, the paper's n): the interaction is significant (p=3e-13), but no Sidak test reaches p<0.05 under either spike reading or either error term (smallest p 0.116). The curves cross over: isolated neurons fire more at 60–320 pA and less at 340–500 pA. With all 37 group-housed neurons it would pass. |
| fig2e-female-higher-baseline-excitability | partially_reproduced | Cell 12: the interaction (p≈1e-68) and Sidak tests at 80–180 pA pass under both readings. Females fire more at "most steps" only at 0 mV (16/26), not at −20 mV (12/26). The −20 mV count is biased low by the re-arm rule (problem 1). Males fire significantly more at 440–500 pA. |
| supt1-male-input-resistance-up | not_reproduced | Cell 14: right direction (+20 MΩ) but p=0.052 and 0.053 for the 21 neurons. With all 37 neurons p=0.002. |
| ed2e-nonspecific-bla-excitability | reproduced | Cell 16: interaction p=0.021 and 0.0057; isolated neurons fire more at 17/26 steps. |
| ed2bcd-nonspecific-bla-no-rank | reproduced | Cell 18: rank and rank×current p≥0.20 in b and c. In d, housing p=0.98 and rank×housing p=0.13. |
| ed3c-male-rank-blampfc-excitability | partially_reproduced | Cell 20: interaction p=1e-13 and rank 1 fires least. Tukey puts rank 1 below rank 3 (360–500 pA) but never below rank 2. Only one Tukey reading was run (problem 4). |
| ed3d-female-rank-blampfc-none | reproduced | Cell 22: rank p=0.43/0.83, interaction p≈1. |
| fig2d-female-blampfc-excitability-down | blocked (data_missing, unverified) | 11 of 14 isolated-female files show flat traces, leaving 3 neurons from 1 mouse. Not shown to be missing data rather than a loader problem (problem 2). |
| fig2-threeway-sex-current-housing | blocked (data_missing, unverified) | Needs the isolated females, as above. |
| supt1-female-input-resistance-threshold | blocked (data_missing, unverified) | Needs the isolated females, as above. |
| ed5d-cue-response-modest | not_reproduced | Imaging cell 12: the nonspecific mean peaks at −0.52 (3 s baseline) and −0.41 (5 s). The BLA-mPFC peak (0.11) comes at 2.9 s, so it is not transient. The nonspecific result is probably an artefact (problem 3). |
| fig3f-blampfc-distinct-clusters | reproduced (low confidence) | Cell 15: chi-square p=1.9e-5 and 8e-4 under both spans, which meets the criterion. But the cut gives only 2 clusters (66 nonspecific against 3 BLA-mPFC neurons in the responsive one). The population labels are an assumption, and cohort 9's trace artefact may drive the difference (problem 3). |
| ed5ef-alcohol-water-nonoverlapping | reproduced | Cell 17: overlap over the smaller excited set is 0.17/0.20 (reading a) and 0.12/0.00 (reading b), all below 0.5. BLA-mPFC excited sets are only 5–8 neurons. |
| fig3h-nonspecific-decoding-85 | blocked (other) | Cell 19: under M5's own rule only 1 of 10 and 2 of 9 mice have ≥5 decoding bouts of each liquid; most have 0–2 water bouts. I agree the method cannot run. |
| fig3h-blampfc-decodes-better | blocked (other) | Same as above. |
| ed6b-decoding-above-chance | blocked (other) | Same as above; no chance level could be compared. |
| fig3k-blampfc-response-predicts-bouts | not_reproduced | Cell 22: r²=0.083 (reading a) and 0.015 (reading b), against 0.59±0.059; corrected p≥0.85. n=9, not 11. |
| fig3ijl-no-other-correlations | reproduced | Cell 24: all three correlations have uncorrected p≥0.14. |
| ed6ij-cue-responses-no-correlation | not_reproduced | Cell 26: the BLA-mPFC cue response correlates with alcohol bouts (r²=0.54, p=0.025 at 3 s; p=0.019 at 5 s). |
| ed6k-bout-duration-not-number | reproduced | Cell 28: p=0.68 (n=9). |
| fig5b-isolation-increases-mpfc-alcohol | not_reproduced | Cell 32: bout reading a gives one-sided p=0.49 (nonstimulated) and 0.13 (all trials); over 20 draws the median p is 0.24/0.14. Only reading b passes (p=0.024/0.022). |
| fig5c-isolation-no-water-change | reproduced | Cell 34: all p≥0.50. |
| fig5d-isolation-decreases-mpfc-sucrose | not_reproduced | Cell 36: one-sided p 0.22–0.56; with all trials, reading a puts SI above GH. |
| fig6c-stim-increases-mpfc-alcohol-gh | not_reproduced | Cell 39: one-sided p=0.34/0.30 and 0/20 draws significant; matched stimulated bouts per mouse are 0–8. |
| fig6de-stim-fewer-alcohol-inhibited | not_reproduced | Cell 41: inhibited proportion two-sided p=0.25/0.47 (5 mice). |
| fig6f-stim-decreases-mpfc-alcohol-si | not_reproduced | Cell 43: stimulated is higher than nonstimulated; one-sided p=0.78/0.55. |
| fig6gj-stim-no-water-effect | reproduced | Cell 45: every test on all sessions has p≥0.12. |
| fig6k-stim-decreases-mpfc-sucrose-gh | not_reproduced | Cell 47: one-sided p=0.63/0.11. |
| fig6lm-stim-fewer-sucrose-excited | not_reproduced | Cell 49: excited proportion p=0.89 under reading a; one-sided 0.036 only under reading b; 1/20 draws significant. |
| fig6n-isolation-occludes-sucrose-effect | reproduced | Cell 51: p=0.47/0.12. |
| ed8n-stim-fewer-sucrose-inhibited-si | not_reproduced | Cell 53: the reading-a seed gives p=0.048, but reading b gives 0.18 and only 1/20 draws are significant (median p 0.09). |
| ed8op-stim-no-alcohol-proportions-si | reproduced | Cell 55: all-session p≥0.65. |
| fig1c, fig1-threeway, fig1d, fig1e, ed1c, ed1d, ed1e, ed1g, ed1i, ed1l, ed1n, ed1r, ed5c | blocked (data_missing) | Checked the archive: the 359 assets are icephys, cued-2BC imaging, resident-intruder imaging and mp4 videos. There are no multi-day home-cage licks, ranks, blood alcohol or unimplanted mice. |
| fig4e, fig4cd, fig4hi, fig4g, fig6q | blocked (data_missing) | The optogenetics-with-behaviour cohorts (ChR2/eYFP, NpHR/eYFP) are not in the dandiset. |
| ed4ef, ed4gm, ed4kl | blocked (data_missing) | The ChrimsonR/NpHR intruder cohorts are absent. All 77 videos belong to imaging sessions, and asset metadata lists no pose estimation, although the dandiset description advertises "pose tracking". |
| ed7-mpfc-responses-stable | blocked (data_missing) | No group-housed T1/T2 stability sessions; every imaging session is labelled pre- or post-isolation. |
| ed6cd-rank-stratified-correlation | blocked (metadata_insufficient) | Imaging subject metadata has no rank. |
| ed9e, ed9fg, ed9hi, ed9k-o, ed9q | blocked (data_missing) | The 24 resident-intruder files (6 mice × 4 sessions) hold OnePhotonSeries, PlaneSegmentation and a video each, but no interaction annotations or pose data. Testing needs new pose tracking. |
| ed9c-coregistered-fraction | blocked; possibly testable | PlaneSegmentation footprints are present in all 24 resident-intruder files. If they hold every ROI rather than only the 199 co-registered ones, a CellReg-style registration could test this claim. The notebooks never opened these files. |

**B. Problems**

1. [affects a conclusion] `count_spikes`, `REARM_MV=5`: this hysteresis is the author's own addition to the claims file's "upward crossings of −20 mV". On a synthetic train of 10 spikes with troughs at −22 mV it counts 1 at −20 mV and 10 at 0 mV. That is why female counts at −20 mV fall below the 0 mV counts at high currents (one mouse 12.48 at 0 mV against 8.92 at −20 mV, cell 12). It decides the "most steps" condition of fig2e. It also bears on the female groups of ed3d.
2. [affects a conclusion] `load_cell` and cell 4: only the first acquisition series containing "Clamp" and the first stimulus series are read. The 11 "empty" isolated-female files are 31 or 62 MB, the same sizes as the recorded 2024-cohort files (the 2025 files are 4.3 MB). The notebook never lists the other series in those files, so data_missing for fig2d, fig2-threeway and supt1-female is not established.
3. [affects a conclusion] `event_z`, `SD_FLOOR`: on sparse non-negative traces this rule keeps only baselines that contain a transient, which biases z downward. On synthetic traces with random onsets I get a mean z of −0.45 and 84% NaN; the true value is about 0. Cohort 9 has such traces (cell 10 removes 8.2% of bout-neuron pairs), and its cue peaks are −0.63 to −0.87 against about 0 for cohort 10 (cell 12). This undermines ed5d (nonspecific), the cluster and population contrast of fig3f, and the nonspecific parts of ed5ef, fig3ijl and ed6ij. No alternative handling (session s.d., or no floor) was run.
4. [affects a conclusion] Cell 20, ed3c: Tukey uses per-step error only, while fig2c and fig2e ran both a per-step and a pooled-error post hoc. Rank 1 against rank 2 (for example 2.8 against 5.3 spikes at 200 pA) could reach significance under the pooled reading, which would change partial to reproduced.
5. [affects a conclusion] `mpfc_stim` and `proportion_test` (cells 39–55): "nonstimulated" means trial types 1–3, so forced trials are included. The criteria of fig6c, fig6f and fig6de say "stimulated and nonstimulated **choice** trials", which is type 3 only.
6. [affects a conclusion] Ephys cell 7: taking the 2022 cohort as Fig. 2c's group is a reasonable count-based assumption. But the fig2c and supt1-male outcomes flip with it (all 37 neurons pass both). The notebook shows both, but the dandiset cannot settle which is right.
7. [affects a conclusion] Imaging cell 0: cohorts 9/10 = nonspecific and cohort 16 = BLA-mPFC is an assumption from mouse counts. All CNMF-E ROIs are used, uncurated (1113 and 347 ROIs against 540 and 196 neurons; mPFC 748/439/925/543 against 240/281/284/343). Every imaging outcome rests on both, and the population contrast in fig3f may be a cohort or preprocessing difference.
8. [does not affect a conclusion] Cell 5 claims that a session whose forced-trial licks mismatch has wrong trial types, "and so which choice trials were stimulated". Cell 10's bout table shows a clean swap instead: in the mismatching sessions reward bouts fall only in type 1 and water bouts in type 2, consistent with counterbalanced coding of types 1 and 2. That says nothing against type 4. The "matched subset" variants therefore discard valid sessions; the primary analyses use all sessions.
9. [does not affect a conclusion] `fig3f`, cell 15: the "highest cut with a nonresponsive cluster" gives 2 clusters, which hardly matches the statement's "several functional clusters". The chi-square treats ROIs from 19 mice as independent units. Both follow the criterion as written.
10. [does not affect a conclusion] `load_session` stores `t0`, but `event_z` is always called with `t0=0`. The lag check in cell 6 supports alignment in 40 of 53 sessions, but `t0` is never printed.
11. [does not affect a conclusion] Single licks (not part of a bout) are ignored when deciding M2 isolation (`session_bouts`), so a baseline can contain licks.
12. [does not affect a conclusion] I confirmed on synthetic data that `split_plot_anova` matches a hand-computed balanced split-plot ANOVA exactly (F 3.948 and 6.902), and that `bouts` and `session_bouts` behave as documented.

**C. What I could not check, and which output would have let me**

- The acquisition and stimulus series names, shapes and conversions in the 14 flat icephys files, and whether any of them holds a response (B2).
- Female and male excitability curves with `REARM_MV=0`, or a plain −20 mV crossing count (B1).
- Per-cohort trace minima, the share of zero samples, and NaN rates under `SD_FLOOR`; ed5d and fig3f rerun without the floor or with a session-s.d. z; the cohort makeup of fig3f's cluster 1 (B3).
- ed3c post hoc with pooled error (B4), and fig6c, fig6f and fig6de with type-3 trials only (B5).
- ROI counts per resident-intruder file, and whether PlaneSegmentation holds all ROIs (decides whether ed9c is testable).
- The `t0` values per session.
- The blocked-claim reasons in the attempt record were not available to me, so for the 29 claims outside the notebooks I relied on my own check of the asset list and metadata.
