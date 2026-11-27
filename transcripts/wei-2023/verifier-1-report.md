**Verifier report, round 1: Wei et al. 2023 on DANDI:000021 (0.251116.2246)**

The claims file has 49 claims. I checked the archive directly through the API. It holds 32 sessions: 13 of the paper's 25 wild-type sessions, 5 Pvalb and 6 Sst opto-tagging sessions (genotypes read from the asset metadata), and 6 Vip sessions. This matches notebook cell 5. Every claim judged on the dataset is therefore judged on that subset, as a deviation.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| source-data-units-link | partially_reproduced | 13 of 25 sessions are held. All 566 Source Data ids of those sessions are found among VISp "good" units, with per-session counts equal to sheet Fig 1d (cell 8). |
| fig1d-unit-count | not_reproduced | Mean units per mouse is 57.0 under reading (a) and 123.4 under (b), against 48±4.8 (cell 10). The paper's own count for these 13 sessions is 43.5. |
| fig2-one-channel-two-clusters | reproduced | Elbow and f(K) both pick K=2 under both readings and all seeds. FS has the lower TPW and the lower REP (0.251 vs 0.302 ms) (cell 12). |
| fig2-fs-rs-counts | not_reproduced | FS fraction is 20.8% under (a) and 17.9% under (b), against 23.3±2.33 (floor 20.97), a narrow miss. Labels agree 98.4% with the Source Data on shared units (cell 14). |
| figs3b-fs-faster | not_reproduced | FS is faster under every reading with p<1e-11, but no reading puts both medians in tolerance. The best are (a)a2 with FS 5.04 / RS 1.40 and Source Data labels a1 with FS 4.55 / RS 2.50 (cell 16). |
| fig2-rs-more-asymmetric | reproduced | Symmetry index median RS 1.645 vs FS 0.845, Mann-Whitney p=3.6e-26 (cell 18). |
| fig2d-three-subclusters-each | not_reproduced | f(K) picks K=2 (a) or 9 (b) for FS; the elbow picks 2 (a) or 3 (b). Only RS gives K=3 (cell 20). |
| figs4-rs1-faster-above | reproduced | 1/V above median RS1 1.54 vs RS2 3.41, Holm p=5e-66 (cell 24). |
| figs4-rs-spread | reproduced | Kruskal-Wallis p=6.4e-7 (a), 2.9e-15 (b), 4.1e-5 (Source Data labels). RS3 has the smallest median in each (cell 26). |
| figs4-fs-spread-absent | reproduced | p=0.978 (a) and 0.267 (Source Data labels), but p=0.013 under (b). It rests on FS clusters forced to K=3 (cell 28). |
| figs5-depth-distribution | partially_reproduced | Kruskal-Wallis p<0.05 with the clusters found here (0.011 under (a), 4e-6 under (b)). With the paper's labels p=0.36 on the CSD depth and 0.34 on the code's own depth, and the CSD depth is unreliable (problem 3) (cell 30). |
| fig3a-isi-fs-rs | partially_reproduced | No median lies inside the CI tolerance. Within 10% only on Source Data labels (FS 20.50, RS 54.67 ms). With own clusters FS is 22.67 ms, 15% off. Mann-Whitney p≈0 (cell 38). |
| fig3a-rs1-excitability | reproduced | Under reading (a) or (b) with period (b), rate, CV and LV all meet the omnibus and both Holm RS1 tests in the right direction (cell 40). With the Source Data labels, RS1 vs RS3 fails for all three measures. |
| fig3a-rs23-visual-responses | partially_reproduced | Under (a), f1/f0 and lifetime sparseness hold; modulation index fails (Kruskal-Wallis p=0.052). Under (b) and Source Data labels, fewer metrics hold (cell 42). |
| fig3a-fs-visual-absent | reproduced | All omnibus p≥0.17 under every label set (cell 44). FS clusters are forced to K=3. |
| fig3c-fs-more-phase-locked | partially_reproduced | FS>RS is significant in 3–4 bands, but never in theta (Holm p≥0.085). RS percentages are outside tolerance, e.g. alpha 78.6 vs 63.9±6.4 (cell 46). |
| fig3c-rs-prefers-theta | reproduced | The criterion holds in every combination of readings. FS range is about 10–12 points against an RS range of 19–25 (cell 48). |
| figs7-spontaneous-less-locked | partially_reproduced | Spontaneous locking is lower in every band under (a) and (b), but the theta shares are FS 88.7% and RS 75.5%, against 19.5% and 4.7% (cell 50). |
| fig3c-fs-stronger-earlier | not_reproduced | Kappa is significant in at most 2 bands (Source Data labels: low and high gamma). There is no significant phase lead in beta or low gamma under any reading (cell 52). |
| fig3d-rs2-gamma-locking | not_reproduced | No gamma omnibus test with RS2>RS1 reaches significance. Only the phase range (167–215°) holds (cell 54). |
| fig3e-fs-cluster-locking | partially_reproduced | Only reading (b), on forced FS clusters, gives FS3>FS2 in high gamma (Holm p=0.014). There, phase differs in alpha and beta but not low gamma (cell 56). |
| figs6c-fs-stronger-across-depth | partially_reproduced | Using the percentage phase-locked as the coupling measure, FS>RS holds in all 15 cells (reading (a) and Source Data labels, CSD depth), but only 3 or 0 of the Holm tests reach p<0.05. Kappa holds in at most 12 of 15 cells (cell 58). |
| figs6d-rs3-supragranular-beta | not_reproduced | RS3/RS1 kappa ratio is 0.96–1.36 against 2±0.2. All Mann-Whitney p>0.05 (cell 60). |
| figs6c-granular-phase | not_reproduced | No granular FS-earlier result in either region reading the criterion names. Only the code-depth variant under (b) gives high gamma p=0.037. Infragranular differences are significant, against the claim (cell 62). |
| fig4g-experiment-classifier-fs-rs | reproduced | 99.91% under (a) (98.69% with Source Data labels) (cell 34). Inflated by leakage (problem 6). |
| fig5d-experiment-classifier-rs | partially_reproduced | 98.29% under (a), 93.27% with Source Data labels: above 95% but below 99% (cell 36). |
| fig6a-fs1-symmetric | reproduced | Under (a): Kruskal-Wallis p=7.8e-15, Holm FS1–FS2 7e-10 and FS1–FS3 5e-12, FS1 lowest (cell 32). FS clusters are forced to K=3. |
| fig7-opto-unit-counts | not_reproduced | Per mouse, Pvalb is 2.6 (a) or 4.2–4.4 (b) against 2.7–3.4; Sst is 1.17–1.33 (a) or 2.0–2.33 (b) against 1.35–1.65 (cell 64). |
| fig7d-pvalb-fs-sst-diffuse | reproduced | Pvalb is 13 of 13 FS; Sst is 3 FS and 5 RS, under both placement readings (cell 66). |
| fig7e-pvalb-sst-one-channel | partially_reproduced | TPW and REP have p<0.01 in every tagged-set reading. Rate is not significant under any period (cells 68, 76). |
| fig7g-pvalb-more-symmetric | partially_reproduced | Pvalb is lower in every tagged set, but the t-test gives p<0.05 only for isolation (a) with the 10 ms baseline (0.043). The main set gives p=0.079 (cells 70, 76). |
| fig7h-pvalb-higher-cv | partially_reproduced | Main set: Pvalb higher, p=0.053 (period a) and 0.86 (period b). Other tagged sets give p=0.002–0.012, but no direction is printed (cells 72, 76). |
| fig7h-pvalb-theta-sst-later | partially_reproduced | Theta kappa is higher for Pvalb (p<0.001). Only the low-gamma phase lag (54.5°, p<0.001) meets 36–55°; beta (22°, p=0.21) and high gamma (60.7°) fail (cell 74). |
| fig4d-ap-sp-models-tpw-rep | reproduced | TPW t-test p=2.5e-4, REP Mann-Whitney p=4.9e-4, AP lower (cell 78). |
| fig4e-in-vitro-ap-sp | partially_reproduced | Adaptation gives Mann-Whitney p=1.26e-3, just above 0.001. The other three are below 0.001 (cell 92). |
| fig4f-model-classifier | reproduced | 83.15% accuracy; 91.6% of FS labelled AP and 77.5% of RS labelled SP (cell 80). |
| fig4g-models-map-to-fs-rs | reproduced | 17 of 18 AP models labelled FS, 11 of 15 SP models labelled RS, the same under all seeds (cell 82). |
| fig4h-cre-lines-map | partially_reproduced | Scnn1a is 2 FS / 2 RS, not a majority. Pooled, excitatory and inhibitory both hold (cell 84). |
| fig5a-sp-models-three-clusters | reproduced | Elbow and f(K) both pick K=3, with counts 5/7/3 equal to the paper's labels (cell 86). |
| fig5c-sp-rs-two-way-mapping | partially_reproduced | Model-based accuracy is 93.3% (92.9–93.8 across seeds), below 94%. All six majority mappings match (cell 88). |
| fig5e-ca-lva | reproduced | Cohen's d is 2.07 and 2.12, SP2 lower; Source Data values (cell 98). |
| fig5g-bifurcation-velocity-sp | reproduced | slope 2.71, r=0.80, p=1e-7 (cell 102). |
| fig5j-sp1-rate-tau | reproduced | d=0.89 for rate (SP1 higher) and 1.13 for tau (cell 94). |
| fig6b-pvalb-sst-models-symmetry | reproduced | Pvalb 2.69 vs Sst 7.74, p=9.98e-4 (cell 90). |
| fig6cf-kv31 | partially_reproduced | 3 of the 5 Source Data conductances give p<0.05, and dendritic Kv3.1 has the largest \|d\| (1.29). "Every conductance" cannot be tested because only 5 are published (cell 100). |
| fig6d-sst-asymmetric-morphology | reproduced | Pvalb p=0.455; Sst p=0.030 with \|above\| > \|below\| (cell 105). |
| fig6e-bifurcation-velocity-inhibitory | reproduced | slope 2.68, r=0.80, p=5.1e-9 (cell 103). |
| fig6g-pvalb-sst-in-vitro | reproduced | Rate p=0.0011, rheobase 0.0008, resting potential 0.0081 (cell 96). The paper gives 0.0067 for rate (problem 15). |
| figs8-rotation-symmetry | blocked (data_missing) | It needs simulations of rotated models. The GitHub tree at f1a4268 holds only examples/395830185, and the dandiset holds no simulations. No part can be tested. |

### B. Problems

1. **[affects a conclusion]** `assemble` / `select_wt`, cells 10 and 14: neither isolation reading reproduces the paper's unit set.
   - Reading (a) gives 741 units in the held sessions against 566 in the Source Data: 248 units the paper did not use come in, and 73 of the paper's units are lost.
   - The code's unit tables show the paper kept 618 of the 900 (a)-isolated units.
   - The added units fire very little: in cell 16 the RS median is 0.81 Hz against 2.50 Hz on the Source Data units, which pulls down the rate claims and the FS fraction.
   - The claims file quote ties isolation to "during spontaneous activity", but neither of the claims file's readings includes an activity criterion. This is a gap in the claims file, reported here and not corrected.
2. **[affects a conclusion]** `unit_features`, cell 8: on matched units, features equal the Source Data for only 85% of TPW/REP values and 68–72% of 1/V values. The mismatch is not diagnosed (by session or cause), and it feeds every clustering claim.
3. **[affects a conclusion]** `process_session` CSD block, cell 30: the CSD layer-4 centre disagrees with the code's depth.
   - Per-session median offsets run from −340 to +420 µm, and only 29% of units fall within 100 µm.
   - depth_csd ranges down to −1000 µm (cell 5), which is implausible for V1.
   - This affects figs5, figs6c, figs6d and figs6c-granular-phase.
4. **[affects a conclusion]** Cell 22: FS is forced to K=3. The notebook states this as a deviation. It means every FS1–FS3 outcome is conditional on clusters the paper's procedure does not produce here (figs4-fs-spread-absent, fig3a-fs-visual-absent, fig6a, fig3e, figs5).
5. **[does not affect a conclusion]** `name_by_overlap` can return names outside `names`; I confirmed this on synthetic input, where an FS cluster was named "RS1". The reading (b) counts printed in cell 20 are therefore wrong (RS clusters sum to 1374, but there are 1317 RS units). The labels used downstream (cell 22) are correct.
6. **[does not affect a conclusion]** `upsample_index` runs before the train/test split in `classifier`, so duplicated rows land in both train and test. On pure noise, the random forest scored 91% where balanced chance is 50%. This follows the paper's code, as the claims file directs, but the accuracies in fig4f, fig4g, fig5c and fig5d do not show real separability. Labels also come from K-means on the same features.
7. **[affects a conclusion]** Cells 46 and 50: spontaneous phase-locking is 4 to 16 times the paper's (FS theta 88.7% vs 19.5%). The nearest LFP channel (LFP reading (a)) may carry the unit's own spike waveform. This was not investigated, and it bears on the figs7 and fig3c percentages.
8. **[affects a conclusion]** Cell 64: the tagged units include 6 whose peak is off centre, and the wild-type exclusions are not applied to them. The Sst mean symmetry index is 2.47 here against 1.45 in the Source Data. fig7g sits at p≈0.04–0.08, so this could change its outcome.
9. **[affects a conclusion]** Cell 76 prints no direction for CV in the alternative tagged sets, and it omits cv_dg_b. Period (b) is the one that matches the Source Data CV (Spearman 0.848 vs 0.502, cell 40). This bears on fig7h-pvalb-higher-cv.
10. **[does not affect a conclusion]** Cells 34 and 36: the classifiers are not run on reading (b). fig5c and fig5d use 20 resamplings instead of 100 and fig7d uses 20×20; this is stated, and the seeds are stable.
11. **[does not affect a conclusion]** `process_session`: spikes are mapped to the next LFP sample with `searchsorted`. That shifts phases systematically by up to 0.8 ms (about 26° at 90 Hz), equally for every group.
12. **[does not affect a conclusion]** `isi_stats` on `isis_within` output: LV pairs straddle trial boundaries.
13. **[does not affect a conclusion]** Isolation reading (b) is "every VISp unit the NWB units table lists", but the notebook keeps only quality=="good" units. This is probably equivalent; it was not checked.
14. **[does not affect a conclusion]** Cell 92: AP width has n=13/14 of 18/15 cells, and NaN values are dropped silently.
15. **[does not affect a conclusion]** Cell 96: the paper's maximum-rate p is 0.0067, but here it is 0.0011 on the same Source Data column. "Maximum spike rate" may be a different feature from 1000/avg_isi. Both values are below 0.01.

### C. Not checked, and the output that would settle it

- **Paper's own features:** clustering the 1204 units of sheet Fig2d (TPW, REP, 1/V) would test fig2d's K=3 independently of the feature mismatch.
- **Feature mismatch:** a per-session and per-feature table of the Source Data mismatches in problem 2.
- **CSD vs code depth:** per-probe CSD centre against the code's depth offset, plus CSD plots.
- **CCF layer reading:** I did not open the NWB electrodes table, so I could not check whether its CCF x/y/z coordinates plus the CCF annotation would allow the CCF-layer region reading. The notebook says no layer is available.
- **Spike contamination:** spontaneous and drifting-grating phase-locking with an LFP channel at least 100 µm from the peak.
- **Tagged-set checks:** fig7g and fig7h after excluding off-centre units, with CV direction and cv_dg_b printed for every tagged set.
- **Chance baseline:** the paper states no chance level. A label-permutation baseline for each classifier would expose the leakage in problem 6.
- **Model parameters:** whether the 33 models' parameters (for fig6cf and figs8) are published outside the two repositories.
