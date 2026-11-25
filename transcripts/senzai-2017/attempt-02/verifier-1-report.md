**A. Outcomes** (31 claims in the claims file: 29 tested in the notebook, 2 blocked)

| Claim | My outcome | Reason |
|---|---|---|
| unit-counts | reproduced | GC 583 and MC 503 against 586 ± 58.6 and 500 ± 50 (cell 9). The counts come straight from the dataset's labels. |
| first-stage-labels | partially_reproduced | GC+MC 0.985 and wI 0.906 (1.2) / 0.926 (1.8) pass. Dentate nI below 0.425 ms is 0.899 under both thresholds, just under 0.90 (cell 11). Two of three groups pass. |
| interneuron-rates | reproduced | Reading (a), dentate units: nI 7.65 Hz and wI 2.05 Hz, both within tolerance, KW P = 1.4e-13 (cell 13). |
| gc-narrower-waveform | reproduced | GC 0.71 ms vs MC 0.74 ms, MWU P = 3.6e-14 (cell 15). Fragile: the latency is cut off at the end of the stored window for 44% of GC and 69% of MC, and the wide-band variant gives P = 0.43 (problem 5). |
| optotag-drd2 | partially_reproduced | MC suppressed 0.642 (baseline i) and 0.670 (baseline ii), far outside 0.271 ± 0.027. GC 0.030 / 0.066. MC is more than 4× GC under both baselines (cell 17). |
| mc-more-active | reproduced | MC > GC in wake (both readings, KW P ≈ 1e-100) and in NREM (KW P = 1e-23) (cell 19). |
| gc-nrem-highest | partially_reproduced | NREM (0.398 Hz) is above wake (0.079) and REM (0.205), adjusted P ≈ 0. Wake and REM also differ (adjusted P ≈ 0) under both wake readings (cell 21). |
| ca3-wake-highest | not_reproduced | The CA3 NREM median (0.473) is above wake (0.450 / 0.445), and NREM vs wake is not significant (adjusted P = 0.77 / 0.69). The ordering itself fails (cell 21). |
| nrem-wake-ratio | reproduced | GC median ratio 4.67 vs MC 1.09, MWU P = 1e-130 (cell 23). The MC half of the statement is not covered by the criterion (problem 10). |
| theta-modulation | reproduced | MRL GC 0.429 > MC 0.347, KW P = 7e-16. Under reading (a), GC phase is later (circular mean 0.54 vs 0.25 rad), KW P = 8e-13 (cell 25). |
| gamma-modulation | reproduced | MRL GC 0.323 > MC 0.217, KW P = 3e-34. Under reading (a), GC phase is earlier (−0.47 vs −0.06 rad), KW P = 2e-23 (cell 25). |
| gamma-rate-correlation | not_reproduced | Reading (a): MC r = −0.119, P = 0.0076. Reading (b): MC r = −0.182 (within tolerance) but P = 1.9e-4. GC r is outside tolerance in both readings (−0.234, −0.413). The MC P misses 1e-4 in both readings, so not even the partial criterion is met (cell 27). |
| ds2-recruitment | reproduced | Peak ratio GC 6.70 > MC 5.04, KW P = 1.9e-6. Peak time GC −3 ms vs MC +1 ms, KW P = 3e-8 (cell 29). |
| monosyn-gc-to-mc | partially_reproduced | The automatic test finds 63 GC→MC and 8 MC→GC pairs. Readings (a) 0.108, (b) 0.081 and (c) 0.014 are all outside 0.055 ± 0.0055. The ratio 63:8 is at least 4:1 (cell 37). |
| burst-facilitation | reproduced | Second spike above first in 56 of 63 pairs, Wilcoxon P = 2.9e-9 (cell 39). |
| state-transmission | not_reproduced | 63 detected pairs: Wilcoxon P = 0.52, and NREM is lower in only 32 (cell 41). On the authors' 32 pairs P = 0.0175, which would be partial (problem 4). |
| zero-lag-synchrony | partially_reproduced | No reading has all three values within tolerance. MC cells 0.429 is out. CA3 cells 0.08099 misses the 0.081 lower bound by 1e-5. GC pairs 0.0013 passes. Under the cells reading, MC and CA3 are both more than 10× the GC pair fraction (cell 43). |
| tmaze-central-active | partially_reproduced | Only MC passes (KW P = 5e-10). GC P = 0.41 and CA3 P = 0.21 (cell 48). |
| tmaze-multiple-fields | partially_reproduced | Reading (a): GC 0.049 and CA3 0.486 are out, MC 0.626 is in. GC is lowest and KS P = 1.6e-37 (cell 50). |
| tmaze-peak-info | reproduced | Peak GC 2.54 < MC 4.89 Hz, KS P = 4.8e-4. Information GC 0.033 < MC 0.424 and CA3 0.240, KS P = 1.6e-41 and 1.7e-28 (cell 52). |
| tmaze-splitters | reproduced | Chi-square P = 0.72 (main reading) and 0.098 (all units), so P ≥ 0.05. This is an absence result with almost no power: 8 splitters in total (problem 7). |
| remap-positive | reproduced | GC P = 0.0025, MC P = 3.3e-10, CA3 P = 1.5e-14 (cell 58). |
| remap-gc-lt-mc | not_reproduced | The GC median (0.161) is below MC (0.281), but KW P = 0.685 and the Bonferroni MWU P = 1. Neither test holds (cell 60). |
| remap-fractions | partially_reproduced | GC 0.458 and MC 0.549 are out of tolerance, CA3 0.546 is in. GC is lowest (cell 62). Place-cell counts are 24/102/141 against the paper's 30/111/144. |
| pv-remap | partially_reproduced | Taken literally at seed offset 0, the criterion is met for every size. At n = 20, though, GC and MC differ by 0.0025 and GC > MC under 2 of 5 seeds (Bonferroni P 0.84 at seed 0). Only sizes 5, 10 and 15 hold robustly (cell 64; problem 3). |
| inheritance-tmaze | reproduced | 5 of 19 GC fields overlap (0.263 ≤ 1/3). On the authors' pairs, 3 of 14 (cell 66). |
| inheritance-openfield | reproduced | n = 18, median r = −0.005, Wilcoxon P = 0.25 (cell 68). |
| mc-deeper | reproduced | DS2 amplitude MC 1144 µV > GC 451 µV, MWU P = 4.6e-44. The variant agrees (cell 31). |
| gc-mc-classification | reproduced (provisional) | Agreement 0.949 and stable across seeds (cell 33). However, the waveform used is 300 Hz high-passed, while the criterion says unfiltered (problem 2). The stored-waveform variant gives 0.927. |
| gc-mc-distance | blocked (methods_underspecified) | The claims file gives no criterion. The archive does hold `shank_electrode_number` and the probe geometry, so part of it could be tested (problem 8). |
| gc-backpropagation | blocked (methods_underspecified) | Same as gc-mc-distance. The multi-channel stored waveforms and the wide-band signal in 17 files could give a site-ordered delay, if the depth order were established. |

**B. Problems**

1. **[affects a conclusion]** optotag-drd2, claims file and cell 17. The criterion's mean-rate "≥20% below baseline" rule labels 68 of 106 MC as suppressed, and 93 units across the four types. The paper says the units were "suppressed significantly", and the Figure 1H legend says "37 units showed decreased firing (> 20 %)", which equals 29 MC + 8 wI. So the paper used a stricter rule than the claims file encodes. "decreased by ≥ 20% … in +2 to +15ms bins" can also be read per bin, and that reading was not run. Also, untagged MC have a median response/baseline ratio of 0.794, already under 0.8, which suggests the 20 ms pre-pulse baseline is inflated at 5 Hz. The dataset's `drd2_tagged` column gives exactly 29 MC and 8 wI.
2. **[affects a conclusion]** gc-mc-classification, `wideband_sites` and cell 33. The waveform is the mean of a 300 Hz Butterworth high-passed signal, but the criterion specifies the unfiltered wide-band waveform. The run the criterion prescribes was never done. Agreement without the waveform PCs is 0.899, so the waveform term decides the 90% cut. The 0.927 stored-waveform variant (also filtered, only 0.4 ms of the second derivative) supports the outcome but does not replace the run. The wide-band variant of gc-narrower-waveform (cell 15) uses the same filtered signal.
3. **[affects a conclusion]** pv-remap, cell 64. The KW and MWU P-values are computed on 1000 resampled draws, so they scale with the number of draws. Drawing 20 cells from 24 GC place cells gives near-identical draws. P < 1e-5 therefore says nothing about the cells, and the n = 20 GC–MC difference flips sign with the seed.
4. **[does not affect a conclusion]** state-transmission, cell 41. Following the criterion, the test uses the 63 auto-detected pairs. 31 of them are not in the authors' manually checked table, and the authors' 32 pairs give P = 0.0175. The outcome depends on that pair selection; the paper's n = 31 matches the authors' set.
5. **[affects a conclusion]** gc-narrower-waveform and first-stage-labels, `waveform_features`. The paper measures trough-to-peak on the "unfiltered waveform", but the criterion uses the stored waveforms, which are likely filtered; this was never checked. In 668 units the peak falls at the end of the 1.6 ms window. The GC < MC result rests on lower-bound latencies, and the only wide-band check gives P = 0.43. The nI fraction of 0.899 sits right at the 0.90 cut, so the waveform source could move first-stage-labels too.
6. **[does not affect a conclusion]** gamma-rate-correlation, `phase_modulation`. MRL is biased upward at low spike counts (median 58 spikes for GC vs 447 for MC, with a 1 h cap). A negative rate–MRL correlation is expected from sampling alone, and no count-matched control was run. This bias favours the claim, and it still failed.
7. **[does not affect a conclusion]** tmaze-splitters, `_splitter_test` and cell 54.
   - The chi-square is run with expected counts below 1 (8 splitters in total; GC 0 of 17), and there is no exact test.
   - In `_splitter_test`, `min(best, p)` keeps NaN whenever the first field's p is NaN. The statsmodels rank-0 warnings in cell 2 show that degenerate fits did occur, so splitters may be undercounted.
8. **[does not affect a conclusion]** Blocked claims, cells 69–70. I checked the archive metadata: neither the dandiset nor the asset metadata has site coordinates. The files do hold `shank_electrode_number`, the probe description (8 sites, 20 µm vertical steps), and a per-file DS2 profile (`res["ds2_profile"]`). That profile could have confirmed the lab's convention of listing channels by depth, and 34 of the 63 GC→MC pairs are on one shank. "metadata_insufficient" overstates the case; the real block is that the claims file has no criterion.
9. **[does not affect a conclusion]** zero-lag-synchrony, claims file vs cell 43. The criterion says shanks are unknown, but the `shank` column exists and is used for all files. Same-shank pairs show 0 synchronous pairs out of 5,288 (a spike-sorting overlap effect), so they inflate the pair denominators. With different shanks only (MC 0.133, CA3 0.029, GC 0.002 of pairs), the outcome stays partial.
10. **[does not affect a conclusion]** nrem-wake-ratio, claims file. The criterion tests only the GC half. MC NREM vs wake gives Wilcoxon P = 2e-4 (both readings at P ≤ 2e-4), which runs against "equivalent rates", but the criterion only reports it.
11. **[does not affect a conclusion]** Cell 5. It only shows that same-day "b" files are not duplicate files. It does not test whether the same neurons appear in both files of a day, which would be pseudo-replication across units.
12. **[does not affect a conclusion]** Theta and gamma phase, cell 25. Phases are compared with a linear KW test, not a circular test. Reading (b) splits the cluster at 0 and is not meaningful; reading (a) is the valid one.

Synthetic tests of the helpers all behaved correctly:
- `burst_index` gives 0.95 on a Poisson train.
- The CCG test detects a 5% transmission at 3 ms, gives no false positive under the null, and has the correct lag sign.
- `waveform_features` returns 0.50 ms on a known 0.5 ms waveform.
- `fields_1d` and `burst_spikes` are correct.
- A simulation with no facilitation biases the first/second transmission estimate toward first > second, so the burst-facilitation result is conservative.

**C. What I could not check, and the output that would have let me**

- **optotag-drd2:** per-unit 1 ms PETH bins over +2 to +15 ms and the pre-pulse baseline, to apply the per-bin and significance readings.
- **gc-mc-classification:** the k-means agreement with unfiltered wide-band waveforms.
- **gc-narrower-waveform and first-stage-labels:** the NWB description or filter attribute of `units/waveforms`, and wide-band trough-to-peak latencies for interneurons.
- **Blocked claims:** the per-file DS2 amplitude printed against `shank_electrode_number` for each shank, to establish the depth order.
- **tmaze-splitters:** the number of units whose splitter p is NaN, and a Fisher exact test.
- **T-maze linearisation:** a plot or table of `central_arm_position` and `side_arm_angle` over a few runs, including their values outside the arms.
- **gamma-rate-correlation:** MRL from spike counts subsampled to equal n.
- **Theta and gamma reference channel:** that `hilus_reference` lies in the hilus, from its DS2 amplitude.
- **state-transmission:** a per-pair table showing which of the 63 pairs are in the authors' table, with their wake and NREM values.
