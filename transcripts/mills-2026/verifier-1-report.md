**A. Outcomes for the 11 tested claims**

The claims file has 48 claims. The notebook tests 11 and treats 37 as blocked. Counts below are from the claims file and the notebook cells.

| Claim | Outcome | Reason |
|---|---|---|
| fig2-recorded-neurons | not_reproduced | Cell 12: units below 50 Hz are 1515 paired ASt, 0 TS, 885 CeA and 633 unpaired ASt, against the paper's 193, 212, 145 and 71. Mouse counts are 15, 0, 6 and 4 against 15, 7, 8 and 4. The Neuropixels units have no region label, so the paper's ASt subset can't be counted. |
| figs9-sustained-only-cs-shock | partially_reproduced | Cell 14: the phasic ANOVA is not significant (p 0.24 and 0.23). All four sustained ANOVAs give p < 0.001, and Tukey puts CS-shock above both CS-reward groups, under both bin sizes and both timepoint readings. But the run covers 10 of the paper's 15 mice: the slow group has 112 neurons (expected 96 ± 10) and df is 333, not 479. |
| fig2q-trajectories-diverge | reproduced | Cell 16: mean distance over 0 to 18 s is 7.36, against a baseline maximum of 2.87 in the complete PC space (7.16 against 1.94 with 41 PCs). This uses 112 neurons from 10 of 15 mice. |
| figs8-single-trial-divergence | partially_reproduced | Cell 18: with the iterations pooled (reading c), shock-reward similarity is lower at p ≈ 1e-50 for all five seeds. The per-animal readings (a, b) give p 0.0625 to 0.125, and with 5 animals they cannot reach p < 0.01. The unpaired part can't be tested. |
| fig3h-cs-decoded-paired-only | not_reproduced | Cell 20: the paired part misses the claim's p < 0.01. Two-sided Mann-Whitney p is 0.015 to 0.065 across five seeds; one-sided p is below 0.01 in only 1 of 5 seeds. Accuracy is above chance in 4 of 6 mice, from 6 of the code's 9 paired mice. The unpaired part can't be tested. Chance is 0.476 to 0.528, which agrees with the shuffle chance the paper describes (0.5 for two classes). |
| figs13-imaging-mice-discriminate | reproduced | Cell 22: both paired groups show more defensive behavior to CS-shock (Drd1a t(9) = 3.61, p 0.006; Drd2 t(8) = 2.37, p 0.046) and neither unpaired group does, under both freezing rules. Mouse counts are 10, 9, 8 and 6, matching the paper. The Drd2 result is near the threshold and rests on an assumed pixel scale. |
| fig5j-drd2-cs-shock-responses | partially_reproduced | Cell 25: paired is higher in both windows (t 6.23 and 5.03, p < 1e-6). But the neuron counts are 1189 and 625, far outside 296 ± 30 and 257 ± 26, because every CNMF-E ROI is used. Mouse-level tests give p 0.17 and 0.16. |
| fig5h-drd1-no-difference | not_reproduced | Cell 26: all four tests are significant with paired higher (p 0.0016 to 3.5e-5), and 3 of 4 with the deconvolved trace. The paper's t-values for CS-shock are negative. Scaled to the paper's n, the long-window effect (d ≈ 0.22) would still give p ≈ 0.01. The ROI set is uncurated (847 and 608 against 320 and 237). |
| fig5k-drd2-cs-reward-no-difference | not_reproduced | Cell 27: the short-window test on raw fluorescence gives p = 0.034, and the criterion needs neither test to be significant. The effect is small (d ≈ 0.1, same direction as the paper's t = 1.85) and would not be significant at the paper's n. The deconvolved variant has neither test significant. |
| fig5m-drd2-rich-clusters-cs-shock | not_reproduced | Cell 29: none of the 8 readings gives a positive Spearman correlation at p < 0.05 (lowest p is 0.197). Average linkage gives one giant cluster (1864 to 1968 of 2036 ROIs). |
| figs15-no-context-encoding | not_reproduced | Cell 31: the Drd2 peak rate differs between contexts (p 0.042), and Drd2 freezing is not higher in context A (p 0.63). The Drd1a results do match: no activity difference and more freezing in A (p 0.011). |

Blocked claims, checked against the archive. The asset list has 706 assets: 83 NWB files, 541 avi and 82 mp4. API metadata for all 13 Neuropixels files lists only ElectricalSeries, Units and ElectrodeGroup. Streaming the structure of one of them (sub-Ast-NPX-10) shows empty `stimulus/presentation`, no intervals and no processing. So these are correctly blocked:

- All figs7 claims, figs10b, figs10-high-defensive, fig3h-behavior and fig3j to fig3m: no unpaired ephys mouse has trial events.
- fig2e: TS units are absent.
- figs14 and figs14q: no NWB file is an unpredicted-US session.
- The RNAscope and optogenetic claims: no such files exist.

Parts of some blocked claims could be tested:

- **figs5:** the port-entry half (paired only) is tested in cell 33 and passes (t(11) = 8.31, p 4.6e-6).
- **figs10-no-reward-relationship:** the paired repeated-measures ANOVA over latency quartiles needs only trial-table port entries and spikes, which share a clock (cell 5). It was not run.
- **fig2o-region-differs-cs-reward:** the one-sample t-test of ASt phasic CS-reward z against 0 could be run on 112 units. Cell 14 already shows a mean of 7.09.
- **fig2o-ast-greater and fig2p:** an ASt against CeA comparison is possible, but there are only 22 CeA units from 2 mice.
- **figs10lm and fig3fg:** possibly testable in 2 ASt mice (3016, 3024), where the port and shock checks agree on a pose offset (cell 7).
- **fig1b, fig1j and figs2:** the data is at GEO, which the claims file says. The notebook's reason, "pipeline in R", is not a data reason.

**B. Problems**

1. [affects a conclusion] Cell 0 table and cell 32 group figs10-no-reward-relationship with the claims blocked for lack of unpaired data. Its paired latency-quartile test is runnable and was not run.
2. [affects a conclusion] fig2o-region-differs-cs-reward, fig2o-ast-greater and fig2p are marked fully blocked. The ASt one-sample test, and an ASt against CeA comparison on Open Ephys data, were possible (see A).
3. [affects a conclusion] Cells 24 to 29 (fig5h, fig5j, fig5k, fig5m) run neuron-level tests on all CNMF-E ROIs, 2.4 to 4 times the paper's counts. The fig5h and fig5k significances are mainly due to the larger n, and mouse-level tests are not significant. Also, the long-window mean z is negative in every group (−0.24 to −0.82). That suggests fluorescence decays within each clip, which could differ between cohorts, and it was not examined.
4. [affects a conclusion] Cell 31 (figs15): the 30 × 40 cm scale assumption gives 7.5 to 32.8 px/cm in the context chambers. Freezing hardly changes with a fixed 14 px/cm or with the max or sum rule. That points to many frames with near-zero displacement (possibly duplicated pose frames), which was not checked. The same question applies to cell 22 (figs13).
5. [does not affect a conclusion] Cell 4 defines `latency` as the first port entry at or after onset. Cell 5 shows the tone ending more than 8 s before that entry in at least 5% of trials, meaning the mouse was already in the port. The Methods say collection ends the tone, so the tone duration (`reward_off − reward_on`) is the collection latency. The figs9 slow group is therefore contaminated, which adds to the 112 against 96 mismatch. The direction of the result is unlikely to change, since the slow group already matches all CS-reward trials.
6. [does not affect a conclusion] In cell 18 (figs8), readings (a) and (b) cannot reach p < 0.01 with 5 animals, which the notebook doesn't say. Reading (c) treats 100 resamples of the same trials as independent, so its p is inflated.
7. [does not affect a conclusion] Cells 3 and 10 say the Neuropixels units have no region or channel column. In NPX-10 they have `probe_depth`, a `label` column (good or mua), and `acquisition/NeuropixelsHistologyImages`. That could support region assignment, but with no events nothing becomes testable.
8. [does not affect a conclusion] Cells 0 and 15 call the fig2q run the "code's variant". In the complete PC space (112 components from 1200 samples) the distance equals the neuron-space distance whatever the PCA is fitted on, so the printed value is also the Methods' main reading.
9. [does not affect a conclusion] Cell 7 finds a pose offset that the two methods agree on within 0.6 s for 3012, 3016 and 3024, but doesn't use it. Pose and ephys spans also differ by up to 183 s in the 2019 sessions, so a constant offset can't fix those.
10. [does not affect a conclusion] Cells 9 and 24: the Drd1a unpaired group includes G4B2-C8-6860 (1 imaged CS-shock trial, 4 CS-reward, truncated session) and G2B1-C4-6886 (1 ROI).

The helper functions behave as documented on synthetic inputs (`binned`, `cue_z`, `window_mean`, `ca_cue_z`, `behaviour_frames`, `pixels_per_cm`). One exception: `pixels_per_cm` underestimates the scale by about 18% if body points stay 3 cm from the walls.

**C. What I could not check, and which output would have settled it**

- Whether the Open Ephys pose can be mapped to the trial clock: a per-session fit of offset plus drift between pose and port entries would show it.
- Whether frames are duplicated in the pose data: the per-frame displacement distribution (share of exactly-zero displacements), and freezing and darting reported separately, for figs13 and figs15.
- How many CS-reward events are imaged to 3 s but not 10 s. `cs_imaged` needs 10 s, which may drop such trials from the short window; only 15 of an expected ~22 reward trials are kept.
- figs9 rerun with tone duration as the latency.
- Mouse-level results for fig5k, and for the Drd1a CS-reward windows in fig5h.
- The GEO data for fig1b, fig1j and figs2, which is outside this round's access.
