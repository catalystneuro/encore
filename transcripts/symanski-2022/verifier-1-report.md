**A. Outcomes** (all 47 claims in the claims file)

| claim | my outcome | reason |
|---|---|---|
| fig1b-performance | reproduced | Mean over rats is 75.74% (cell 12) and mean over sessions 76.11%. Both fall inside 77.0 ± 1.3, the first by only 0.04. |
| fig1c-sampling-duration | reproduced | 0.819 ± 0.017 s and s.d. 0.245 s are both within tolerance. Correct vs incorrect signed-rank p = 0.72 (cell 14). |
| fig1d-turn-direction | not_reproduced | Both binomial tests give p < 1e-90 with more same-direction turns. But the counts miss tolerance in both rat sets (cell 16): 5 rats 1390/30, 430/24; 6 rats 1615/47, 490/30 (opposite turns 47 vs 32 ± 3, 30 vs 21 ± 2). The fraction is 95.9–97.1% against 95.4 ± 0.12. The rule includes the counts. |
| fig1s1e-sniff-rate | blocked (data_missing) | No thermocouple in the files. Confirmed in the archive: asset variableMeasured lists only Units, ElectricalSeries, LFP, Position and SpatialSeries, and the electrode table has only CA1, PFC and OB. |
| fig1s1f-air-performance | blocked (data_missing) | Every epoch is "odorplace" (cell 7). The 3,174 rewarded trials equal the paper's odor-cued correct trials, so no air trials are hidden in the files. |
| fig2d-beta-power-increase | reproduced | All three regions, both readings, p ≤ 1.2e-4 (cell 21). |
| fig2d-rr-power-no-increase | not_reproduced | The CA1 decrease is not significant in either reading (p = 0.099 and 0.21). Reading A also shows significant rises in PFC (p = 0.049) and OB (p = 9e-8) (cell 23). |
| fig2e-beta-coherence-increase | reproduced | All three pairs, both readings, p ≤ 2.6e-5 (cell 25). |
| fig2e-rr-coherence-increase | partially_reproduced | CA1-OB and PFC-OB are significant; CA1-PFC is not (p = 0.11 and 0.10). Same in both readings (cell 27). |
| fig2e-beta-coherence-odor-vs-reward | reproduced | All pairs higher during odor, both readings, p ≤ 3.8e-6 (cell 31). |
| fig2e-rr-coherence-odor-vs-reward | blocked (methods_underspecified) | Reading A holds all three parts, though CA1-PFC p = 0.055 is marginal. Reading B holds one part (CA1-PFC p = 0.027, PFC-OB p = 0.074) (cell 33). |
| fig2d-power-odor-vs-reward | partially_reproduced | Reading A holds 4 of 6 (RR in CA1 and PFC significant); reading B holds 5 of 6 (RR PFC p = 0.014) (cell 35). Both readings fall in the partial band. |
| fig2de-correct-incorrect-no-difference | blocked (methods_underspecified) | In reading B the two named tests disagree: signed-rank finds PFC beta power p = 0.023, rank-sum finds nothing (cell 37). Reading A is clean only for this seed: 7 of 20 seeds give a signed-rank p < 0.05 (cell 39). |
| fig2g-air-beta-coherence | blocked (data_missing) | No air sessions in the archive (as for fig1s1f). Only the odor side (3,174 trials) exists. |
| fig2f-swr-odor-vs-reward | reproduced | Fewer SWRs at the odor port in 38/38 sessions (p = 7e-12) under reading (a) and 37/38 (p = 8e-10) under (b) (cell 41). |
| fig2s1f-rr-beta-coupling | reproduced | The pooled MI exceeds all 500 shuffles in every region under both trial readings (cell 43). |
| fig2s2d-phase-offsets | not_reproduced | CA1 leads PFC in beta and in RR, and CA1 leads OB in RR, in both windows. But CA1-OB beta is significant (p = 0.011 and 0.012) where the paper says p > 0.05 (cell 46). The rule has no partial clause. |
| fig2s1e-run-theta-shift | blocked (methods_underspecified) | Reading a: CA1 p = 0.011, PFC p = 1, so partial. Reading b: CA1 p = 0.058, PFC p = 1, so not reproduced (cell 48). PFC fails under both. |
| unit-counts | partially_reproduced | The files hold 915 CA1 and 508 PFC units, a curated subset, so the 1,309/717 totals cannot match. Active counts match (871–876 and 493–494). Later counts miss in every reading (cell 52): CA1 odor-active 138–146 vs 170 ± 17, task-responsive 111–122 vs 138 ± 14; PFC interneurons 64–97 vs 44 ± 4. The Methods' interneuron rule needs spike width, and the files have no waveforms. |
| fig3-choice-selective-fraction | not_reproduced | CA1 is 33–35% (in tolerance). PFC is 35.9–41.1% against 31 ± 3.1 in every reading (cell 54). |
| fig3ij-si-anticorrelated | partially_reproduced | All correlations are negative with p < 0.002. r is within tolerance only for CA1 under SI reading b (−0.589). PFC is −0.536 to −0.550 against −0.68 ± 0.068 (cell 57). Both SI readings fall in the partial band. |
| fig3s1e-nonselective-si | blocked (methods_underspecified) | SI reading a matches the Results (both p ≥ 0.05). SI reading b matches neither reading of the paper: PFC r = −0.44, p = 7e-5 (cell 59). |
| fig3s1c-odor-vs-reward-rate | reproduced | p ≤ 8e-5 in both regions under both readings, odor rate higher (cell 61). |
| fig4c-interneuron-si | not_reproduced | CA1 Spearman is r = −0.19, p = 0.26 (SI a) and r = −0.40 (SI b, out of tolerance). PFC p = 0.025 under SI b. 39 and 23 selective interneurons vs 32 and 10. The 9.5 Hz variant is also n.s. (cell 63). |
| fig4d-ccg-lags | not_reproduced | No pair type is skewed under any window or threshold (all p > 0.2, cell 66). Pair counts (196–368) are far above 87–283; see B3. |
| fig5c-local-locking | partially_reproduced | The significance pattern holds: CA1 pyramidal beta p = 5e-8; PFC beta p = 0.64 and 0.20. Several fractions are out of tolerance: PFC pyramidal RR 19.8% vs 22.7 ± 2.2; PFC interneuron RR 29% vs 43% or 33%; CA1 interneuron RR or beta, depending on the denominator (cell 70). Chance 0.05 matches the paper. |
| fig5d-cross-region-beta | partially_reproduced | The stated rule holds under both chance levels: CA1 interneurons to PFC beta p = 4e-7 at 0.0167 and p = 0.010 at 0.05; others n.s. at 0.0167 (cell 72). The expected counts are out of tolerance: 12 vs 9, CA1 pyramidal 3 vs 11 and 3 vs 10, PFC pyramidal 6 vs 10. |
| fig5gh-phase-preference | partially_reproduced | 7 of 8 hold in both readings. PFC interneuron beta is significant (p = 0.006) where the paper says not (cell 74). |
| fig5-rr-more-than-beta | not_reproduced | RR > beta in proportions holds in both regions, all readings. The PFC Rayleigh-Z rank-sum gives p = 0.091 in all readings (cell 76). |
| fig5s1de-beta-rr-overlap | reproduced | All four p ≥ 0.5 (cell 78). |
| fig5s1fh-selective-and-locked | reproduced | All tests p ≥ 0.45 under both locking definitions (cell 80). |
| fig5e-beta-mvl-correct-incorrect | reproduced | CA1 pyramidal p = 0.039, CA1 interneurons 0.014, PFC pyramidal 0.031 (n = 6), all with lower incorrect MVL (cell 84). CA1 pyramidal is fragile (p 0.033–0.054 across seeds), and see B4. |
| fig5f-rr-mvl-no-difference | reproduced | All four groups p ≥ 0.13 (cell 86). |
| fig5s2-ca1-int-pfc-beta-accuracy | reproduced | p = 1e-4 (n = 33) and p = 1.5e-4 (n = 22) under both set readings (cell 88). See B4. |
| fig6d-discrimination-time | not_reproduced | Ranges reach 1000 ms (CA1) and 100–1000 ms (PFC), outside the widened bounds, in all four readings (cell 91). Only 12 CA1 and 18 PFC sessions, against the paper's 24. |
| fig6c-even-odd-control | not_reproduced | 4–7 of 12 CA1 sessions and 10–13 of 18 PFC sessions cross the bound, far above the 10% partial limit (cell 93). |
| fig6e-glm-choice-prediction | blocked (methods_underspecified) | Reading a: CA1 0.2 s and PFC 0.4 s before exit, both at the tolerance edge, so reproduced. Reading b: CA1 0.12 s, PFC 0.12 s (vs 0.3), so partial (cell 96). |
| fig6e-glm-with-interneurons | not_reproduced | Reading a: CA1 with interneurons is 0.4 s, outside 0.2 ± 0.1. Reading b: CA1 with interneurons is not earlier than pyramidal alone (0.12 vs 0.12) and PFC changes (0.32 vs 0.12) (cells 96, 99). Both readings fail; the notebook's "blocked" disagrees (B1). |
| fig7-spatial-field-counts | reproduced | Results' 26-session set: CA1 365/591 and PFC 163/278, all within tolerance (cell 103). |
| fig7b-odor-active-more-fields | not_reproduced | With P(X ≥ k): Results set CA1 p = 0.15; Methods set PFC p = 0.059. Only the code's P(X > k) on the Methods set gives both below 0.05 (cell 105). |
| fig7s1b-odor-active-higher-rate | reproduced | Both regions, both session sets, p ≤ 5e-10, active cells higher (cell 107). |
| fig7c-field-properties-no-difference | not_reproduced | CA1 width (p = 1.6e-7) and sparsity, and PFC peak (1e-4) and sparsity, all differ (cell 109). |
| fig7s1e-trajectory-selective-odor-active | not_reproduced | CA1 goes the opposite way (17% vs 25%, p = 1). PFC p = 0.107 on the Results set (cell 111). |
| fig7d-trajectory-choice-unrelated | not_reproduced | PFC p = 0.010 and 0.006, so the absence fails (cell 113). |
| fig7e-odor-decoder-first-quintile | not_reproduced | Quintile 1 is at chance in both regions on the Results set (p = 0.53, 0.19). Only PFC on the Methods set gives p = 0.031 (cell 117). |
| fig7f-spatial-decoder-all-quintiles | reproduced | All quintiles, both regions, both readings, p ≤ 9e-5 (cell 120). |
| fig7s1f-ensemble-rate-near-port | reproduced | The CA1 ensemble peaks at bin 0: 4.01 Hz within 20 cm vs 1.15 Hz beyond (cell 122). |

Totals: 16 reproduced, 7 partially_reproduced, 15 not_reproduced, 9 blocked (3 data_missing, 6 methods_underspecified). Where the criterion has no partial clause and its conditions are not all met, I scored not_reproduced (fig1d, fig2s2d, fig3-choice-selective-fraction, fig5-rr-more-than-beta).

**B. Problems**

1. **[affects a conclusion]** Cell 0 summary table / cells 98–99. fig6e-glm-with-interneurons is labelled "blocked: methods underspecified", but neither alignment reading meets the criterion, so the criterion's rule gives not_reproduced. The control's 10 resamples (instead of 100) do not change this, because the CA1-with-interneurons part fails on its own.
2. **[affects a conclusion]** Cell 49/50, `int7`. The main interneuron rule is "rate > 7 Hz" with no width. That is neither the Methods' rule (7 Hz and width < 0.3 ms) nor the code's rate-only rule (9.5 Hz, F7/ParsePyrIN.m, which the claims file names as the variant). It gives 97 PFC interneurons against 44. Every interneuron analysis runs at 7 Hz only: fig4d, fig5c/d/gh/e/s2, fig6e with interneurons, and fig7e. 9.5 Hz is shown only for counts and one fig4c line. The missing width should be recorded as a data_missing part, not filled with a choice the author made.
3. **[does not affect a conclusion]** Cell 65, `ccg_peak`. A pointwise threshold is applied to the largest z of 80 bins. On null data I get P(max z > 1.645) = 0.98, P(> 1.96) = 0.87 and P(> 3) = 0.10, so "significant" pairs are close to all pairs (196 of 203). The outcome is null under z > 3 too, but the reported lags are mostly noise.
4. **[does not affect a conclusion as the criterion defines it]** Cells 82–88, `mvl_pair`. Cells are chosen by a Rayleigh test on their correct-trial spikes, and the correct-trial MVL is then bootstrapped from those same spikes and compared with independent incorrect-trial spikes. Selection alone then pushes incorrect below correct (regression to the mean). Beta-locked cells sit near threshold (median Rayleigh Z 0.95 vs 13.5 for RR), so the RR null in fig5f does not rule this out. A split-half control is missing.
5. **[affects a conclusion, unchecked]** Cell 7 / `Session.__init__`. Unit regions rest on reading `units.electrodes` as the electrode-table label number. The OB argument rules out the row-index reading only. In all 38 files the group name and the label disagree (e.g. Tetrode5 labelled tetrode6), and the group-number reading was never tested. Every unit-based claim depends on this, including the local-LFP choice for phase locking.
6. **[does not affect a conclusion]** Cell 91. The CA1-vs-PFC signed-rank uses 5 paired sessions, where the smallest possible two-sided p is 0.0625. The "similar times" part therefore cannot fail.
7. **[does not affect a conclusion]** Cell 11. The notebook says the readings with and without short-sampling trials "coincide". In fact the files already exclude those trials, so the code's reading that keeps them cannot be run. The pass margin is 0.04 points.
8. **[does not affect a conclusion]** Cell 48 / `lfp_measures` theta block. The 6–12 Hz peak sits on the lowest grid bin (6.59 Hz) for PFC on every day in both windows, so the estimator is pinned at the band edge. The tapers [3 5] used here have no cited source.
9. **[does not affect a conclusion]** `B_values`. Tapers [3 5] on a 500 ms window smooth over ±6 Hz, so reading B's "7–8 Hz" (a single 8 Hz bin) spans about 2–14 Hz and takes in theta. This bears on the reading disagreements in fig2e-rr-coherence-odor-vs-reward and fig2d-power-odor-vs-reward. It is inherent to Path B but not stated.
10. **[does not affect a conclusion]** `A_values`. The 1 s windows centred in the pre-odor window reach up to 0.5 s into sampling, and the reward-window spectra reach 0.5 s past well exit. This is Path A's design, but it shrinks the contrasts.
11. **[does not affect a conclusion]** Cells 57–63. The SI correlations run only at the 7 Hz, active_B selection, although the criterion asks for each reading of unit-counts.
12. **[does not affect a conclusion]** Cell 90, even-odd control. Even/odd groups within one odor have about half the trials of the shuffle groups, and reading c refits the PCA on that subset. Both push the control distance up against the shared null. This follows the criterion and the paper's code, but it may explain part of the crossings.

**C. What I could not check**

- **Electrode mapping (B5):** a per-file table of each unit's electrodes value against the electrode-table label, group name and location, under the label, group and row readings, with region counts for each.
- **Waveforms:** a printout of the units-table columns and of the processing modules in one file, to confirm there is no waveform or spike-width field.
- **Thermocouple:** an inventory of acquisition, processing and stimulus objects in one file would settle it. I checked asset metadata only, and did not stream file contents.
- **Hidden air epochs:** per-epoch performance, to rule out air epochs labelled "odorplace". The 3,174 rewarded-trial match makes this unlikely.
- **Phase-locking bias (B4):** fig5e and fig5s2 with locking decided on one half of the correct trials and MVL measured on the other half.
- **Interneuron threshold (B2):** fig5c/d/gh/e, fig4c/d and fig6e rerun at the 9.5 Hz rate-only rule.
- **fig4d:** the distribution of peak z and lag per pair type, and counts under a max-over-bins (global) jitter band.
- **LFP reading A:** the number of tetrodes and tetrode pairs per region per session; without it I cannot judge how much the averaging dilutes the contrasts.
- **"Ref OFF" channels:** the electrode `referenced` description, to confirm "Ref OFF" means ground-referenced.

I checked the helper functions on synthetic inputs (`rayleigh` false-positive rate 0.052, `tort_mi` against the analytic value, `si`, `count_in`, `flood_width`, `skaggs_sparsity`, phase zero at the peak, `task_responsive`, `cv_accuracy` at chance 0.50 and with signal 0.84, coherence of a signal with itself = 1). All behaved correctly.
