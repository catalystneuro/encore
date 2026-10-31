**Verification report, round 1: Daume et al. 2024 on DANDI:000673 (0.240118.2135)**

The claims file has 57 claims. The three notebooks test 30 of them; the other 27 were not run, and none of the three notebooks marks fig3h as tested or blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| cohort-counts | reproduced | All counts match exactly: 44 sessions, 36 patients, 1,454 units, 1,922 LFP channels, and every per-area count (nb1 cell 12). |
| fig1d-rt-load | reproduced | Median RT is 1.233 s (load 1) and 1.360 s (load 3), both within tolerance; t43 = 5.33, p = 0.0001 (nb1 cell 14). The mean-RT variant gives no effect (t = −0.48), because RTs up to 74 s pull the means. |
| fig1d-accuracy-load | reproduced | 95.10% against 91.02%; t43 = −5.24, p = 0.0001 (nb1 cell 15). |
| behaviour-overall-accuracy | reproduced | 93.05 ± 7.22%; false negatives 76.08 ± 20.11% of errors; both within tolerance (nb1 cell 17). |
| fig2a-theta-gamma-pac | reproduced | The largest mean z is at 4 Hz phase, 80 Hz amplitude; at 4 and 6 Hz there are local maxima at 50/40 Hz and 80 Hz (lfp cell 7). Only artefact reading (a) is shown. |
| fig2b-pac-channel-proportions | partially_reproduced | Reading (a): hippocampus 144, amygdala 130, vmPFC 41 and dACC 14 are within tolerance and all far above the null (p = 0.005). pre-SMA is 17 against 5, out of tolerance. Reading (b) puts four counts out of tolerance (lfp cell 9). |
| fig2c-hippocampus-load | reproduced | Load 1 is higher under both readings: n = 144, t = −4.16, FDR p = 0.001; reading (b) FDR p = 0.014 (lfp cell 11). |
| fig2c-no-load-effect-other-areas | not_reproduced | Reading (a): amygdala FDR p = 0.0475 and pre-SMA 0.0017, both with load 3 higher. Reading (b): pre-SMA and dACC FDR p = 0.014 (lfp cell 11). |
| edf2b-hippocampus-load-patients | reproduced | Reading (a): hippocampus, 23 patients, p = 0.0095, load 1 higher; no other area p < 0.05. This depends on O1: under (b) the hippocampus gives p = 0.11 (lfp cell 14). |
| edf2c-low-gamma-no-load-effect | not_reproduced | pre-SMA p = 0.003 uncorrected and 0.015 FDR, under both readings (lfp cell 16). |
| tables1-slow-fast-theta | not_reproduced | Under every reading, pre-SMA tests (and under one reading hippocampal slow theta–low gamma) also give p < 0.05, not just the two hippocampal high-gamma tests (lfp cell 18). |
| fig2f-rt-single-trial-pac | not_reproduced | The hippocampal PAC term is not significant under any reading (p 0.19–0.64; the estimate is positive under artefact (a)). The amygdala gives p = 0.046 under O5(b) (lfp cell 20). |
| edf3-hippocampus-pac-controls | partially_reproduced | Under artefact (a), gamma power is higher in load 3 by both estimates (p = 0.035 and 0.006); theta power, phase-phase coupling and the preferred-phase t-test show no difference. Waveform asymmetry, peak frequency and the second phase-phase-coupling ratio were not run (lfp cell 32). See problem 5 on the V test. |
| edf3a-kappa-load | reproduced | t = −4.54, p = 0.0001 (a); p = 0.0024 (b) (lfp cell 24). |
| edf3e-nesting | reproduced (conditional) | Holds only under the notebook's own 'peak' alignment: 105 of 144 nested (in tolerance), load test p = 0.0002. Under the Methods' literal 'amplitude maximum' alignment only 9 of 144 are nested (lfp cell 28). |
| edf3f-raw-mi-load | reproduced | Reading (a): t = −4.03, p = 0.0002. Reading (b): p = 0.066 (lfp cell 26). |
| methods-spectral-slope | not_reproduced | Over 2–150 Hz the slope differs between loads (p = 0.007 and 0.002). Over 30–150 Hz it does not (p = 0.12 and 0.28). The 2–150 Hz values (−1.726/−1.730, s.d. 0.43) match the paper's −1.753 ± 0.39 far better than 30–150 Hz (−1.84, s.d. 0.65), so that range is the likelier reading. The difference itself is tiny (0.004) (lfp cell 30). |
| category-cell-counts | partially_reproduced | All counts are within tolerance (94, 181, 40, 18, 13). pre-SMA sits at the threshold: 18 exceeds the 99th percentile of 17, but p = 0.010 (nb1 cell 19). |
| fig3b-persistent-activity | partially_reproduced | Both baseline tests give p = 0.0001 under both readings. Preferred against non-preferred gives p = 0.072 in Hz (a) and p = 0.0013 in % change (b); the criterion needs both readings (nb1 cell 23). |
| edf4b-persistent-activity-by-area | partially_reproduced | The vmPFC part holds (all p ≥ 0.06). The hippocampal and amygdala preference tests fail in Hz (p = 0.24, 0.18) and hold in % (p = 0.019, 0.039) (nb1 cell 25). |
| fig3c-category-load | partially_reproduced | In Hz: preferred trials p = 0.022 (load 1 higher), non-preferred p = 0.20. In %: preferred p = 0.77 (nb1 cell 27). |
| fig3d-category-correct-incorrect | reproduced | All trials, % change, at least 1 or 2 incorrect trials: p = 0.0035 and 0.010, n = 251 and 229 (paper 246). This is fragile: in Hz p = 0.12–0.40, and every preferred-trial reading fails (nb1 cell 29). |
| category-no-rt-effect | reproduced | All p ≥ 0.05 (lowest 0.098) (nb1 cell 31). |
| pac-neuron-counts | partially_reproduced | The shuffle test holds (p = 0.005), but only 8 of 269 hippocampal and 5 of 422 amygdala neurons qualify (12 and 24 under FDR reading (b)), against the paper's 79 and 163 (pac cell 5). |
| pac-category-overlap | partially_reproduced | The overlap does not exceed chance (p = 0.13 and 0.57), but the counts (4 and 2) are far out of tolerance and rest on n = 8 and 5 (pac cell 8). |
| fig4c-pac-neuron-firing-single-trial-pac | not_reproduced | Hippocampal SC term p = 0.85 and 0.18; amygdala p = 0.050 and 0.041. Only 8 and 5 pairs, so this is not an informative test (pac cell 17). |
| fig4e-hippocampus-pac-neurons-accuracy | partially_reproduced | Correct > incorrect holds (p = 0.02–0.03); maintenance against baseline fails (p = 0.51); n = 8 against 63 (pac cell 12). |
| fig4g-hippocampus-pac-neurons-load | not_reproduced | Both baseline tests fail, and load 3 < load 1 is significant (p = 0.009); n = 8 (pac cell 13). |
| fig4-amygdala-pac-neurons | partially_reproduced | Baseline test p = 0.12 fails; the other three tests are null as claimed; n = 5 (pac cell 15). |
| edf8fgh-frontal-controls | blocked (other) | Panels f and g (SFC) were not run, though the data are present. Panel h: pre-SMA p = 0.039 in Hz with at least 1 incorrect trial. In % with at least 1 incorrect trial, the n are exactly the paper's 201/180/201 and all p > 0.5 (nb1 cell 33). |
| fig3f, fig3g, edf5d, edf5c, edf5fg, fig3h, edf7a, edf7bc, fig5b, fig5cd, fig5e, fig5f, edf8b, edf8c, edf8de, fig6a, edf9ef, fig6c, fig6d, fig6e, edf9g, edf9jk, fig6g, fig6h, fig6i, edf9hil, fig6j (27 claims) | blocked (other: not run) | Nothing in the archive blocks these. The archive lists all 44 files, with LFP in 43 sessions and units in all, and the notebooks load spikes, trials and LFP for every area. See section A2. |

### A2. Blocked claims checked against the archive
The API for 0.240118.2135 lists 44 assets. Their metadata list ElectricalSeries, ElectrodeGroup and Units, and the notebooks read LFP from 43 files and spikes from all 44.

- **Testable now with no PAC-neuron selection:** fig3h (category neurons × PAC channels; every input is already computed), fig3f, fig3g, edf5c, edf5d, edf5fg, edf7a (the category-neuron part, chance 20%), fig5cd (the category-neuron part), fig6g, and edf8fgh panels f and g.
- **Testable but on the failed selection:** the claims on PAC neurons (edf7bc, fig5b, fig5e, fig5f, edf8b, edf8c, fig6a, edf9ef, fig6c, fig6d, fig6e, edf9g, edf9jk, fig6h, fig6i, edf9hil, fig6j) could run only on the notebook's 8 and 5 PAC neurons.
- **edf8de** also needs waveforms. The helper's docstring implies the files hold them, but I could not confirm that from the API metadata.

### B. Problems
1. **[affects a conclusion]** `process_session_pac_neurons` / `pac_neuron_tests` (pac cell 5): the selection gives 8 and 5 PAC neurons against 79 and 163. Every claim built on PAC neurons is therefore run at n = 8 and 5 and cannot test the paper.
   - I found no code bug. The likelihood-ratio p-values match statsmodels exactly on synthetic counts, and the null error rate is right (about 0.01).
   - The gap therefore lies in a method detail the notebook never probed: per-trial observations or random effects in fitglme, or which FDR family.
   - Uncorrected, 1.8% of combinations pass against 0.1% in shuffles.
   - The notebook includes more neurons than the paper (269/422 against 212/358), which enlarges the FDR family under reading (a).
2. **[affects a conclusion]** fig3h appears nowhere. It is not in any notebook's table and not covered by the "SFC, noise correlation and decoding" blocked line, yet every input it needs is already computed. The other 27 untested claims are blocked by choice, not by the data.
3. **[affects a conclusion]** O6/O7 (nb1 cell 33): % change with at least 1 incorrect trial reproduces the paper's frontal n exactly (201, 180, 201). That is evidence for O6 reading (b), which the notebook does not use. Under (b), fig3b and edf4b reproduce in full and fig3c fails.
4. **[affects a conclusion]** `nesting` (lfp cell 28): the 'peak' alignment is the author's own reading. The Methods say to align on maximal gamma amplitude, which gives 9 of 144 nested. The assumption is stated and plausible (aligning on the envelope maximum averages out gamma cycles), but edf3e rests entirely on it.
5. **[affects a conclusion]** edf3 (lfp cell 32):
   - A V test of the load differences against 0 tests concentration around 0, so a significant V test (p ≈ 0 here) supports "no phase shift". The claims file's reading (a), with its rule "no test gives p < 0.05", misreads the test; this is a claims-file problem, reported and not corrected.
   - Phase-phase coupling was run only at the 1:21 ratio; the second reading (the ratio of each phase and amplitude centre pair) is missing.
   - Bycycle waveform asymmetry and PAC peak frequency were not run.
6. **[affects a conclusion]** O1 has no tie-break. edf2b and edf3f hold under (a) and fail under (b), and the fig2b counts move. Reading (a) removes 11.4% of trials and (b) 25.9%, against the paper's 14.6% with visual inspection, which favours (a).
7. **[affects a conclusion]** fig2f: the RTs used are untrimmed (up to 16.8 s in the trials used; 74 s overall). The paper states no trimming, but the behaviour cells show outliers can reverse a mean-based effect, and this was not tested.
8. **[does not affect a conclusion]** lfp cell 7: only reading (a) of the comodulogram is shown; the claims file asks for both.
9. **[does not affect a conclusion]** lfp cells 11 and 16: in pre-SMA only 3 of 17 channels have load 1 higher, yet the load 3 mean is 6.9 against 1.8. A few outlier channels probably drive the effect; this was not inspected.
10. **[does not affect a conclusion]** nb1 cell 19: for pre-SMA, "above the 99th percentile" and "p < 0.01" disagree at the boundary (18 against 17.0; p = 0.010).
11. **[does not affect a conclusion]** tables1: the notebook counts 20 tests against the claims file's 19, because pre-SMA has fast-theta channels here.
12. **[does not affect a conclusion]** Checked on synthetic data and found correct: `perm_ttest_*` (t matches scipy), `fdr_bh` (matches statsmodels), `eegfiltnew_kernel` (passbands at unity gain), `mi_from_bins` (0 for a uniform distribution), and `circ_kappa_weighted` (recovers von Mises κ of 0.05, 0.5 and 2).

### C. What I could not check
- **Paper code:** the SBCAT-release code is not available here, so I could not confirm the PAC-neuron GLM data layout (per trial or aggregated), the bin edges, or the median-RT rule.
- **Waveforms for edf8de:** whether the files hold unit waveforms. Adding a printed list of each file's units-table columns would settle it.
- **Released LFP:** whether it already excludes artefact trials or channels. A per-channel histogram of removed trials against the paper's 20.4 ± 13.9 would help.
- **Outputs that would have let me go further:**
  - the reading (b) comodulogram;
  - the PAC-neuron selection under a per-trial Poisson GLME with a trial random effect, plus uncorrected per-area counts;
  - per-channel pre-SMA z values by load;
  - fig2f with RT trimmed (for example, RT < 10 s);
  - the edf3e nesting count under alternative local-maximum windows.
