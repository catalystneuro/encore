**A. Outcomes** (41 claims in the claims file. The notebook tests 19 and treats 22 as blocked. Claims are judged on the BH-FDR responsiveness test, which the file's opening comment and criteria name as the main reading.)

| claim | outcome | reason |
|---|---|---|
| figs1f-angle-awake-vs-anesthetized | blocked (data_missing) | The archive holds 36 C57 mice and only silicon-probe sessions. No session is anesthetized and there is no tracked whisker data, only raw video (cell 62; API asset list). |
| figs1j-curvature-awake-vs-anesthetized | blocked (data_missing) | Same as above. |
| figs1d-bending-larger-closer | blocked (data_missing) | Needs anesthetized kinematics; there are none. |
| figs2-tungsten-responsiveness | blocked (data_missing) | No tungsten recordings: there are 191 assets (67 processed, 67 raw, 57 mp4) and every session is a silicon-probe session. |
| figs2-tungsten-tuning | blocked (data_missing) | Same as above. |
| si-unit-yield | reproduced | 1,160 units (within 1141 ± 114) from 36 mice, exact (cell 12). SNR is not applied. The paper's Fig. S1B gives 1,301 of 1,358 units passing SNR and false alarms, so SNR can remove at most about 22 more units, and the count stays within tolerance. |
| fig2-wall-responsive-counts | reproduced | BH-FDR gives 782, 541, 337 and 96, all within tolerance (cell 14). The uncorrected variant fails badly (1,061 responsive). |
| fig2-distance-tuned-counts | not_reproduced | Tuned 600, activated 478 and suppressed 214 are within tolerance, but "both" is 92 against 29 ± 2.9 (cell 16), and the criterion has no partial clause. The value 92 matches the 94 implied by the paper's own Fig. 2F counts (213 − 119). |
| fig2f-tuning-categories | reproduced | Proximity 271, map 120, ambiguous 87, suppressed-only 122 and untuned 182 are all within tolerance under reading (a). The ratio is 2.26 (cell 18). |
| figs4a-baseline-activated-lower | reproduced | 5.40 against 6.97 sp/s, both within tolerance; K-S p = 2.9e-7 (cell 20). |
| figs4a-baseline-suppressed-similar | reproduced | K-S p = 0.643, at or above 0.05; difference +0.29 sp/s (cell 22). |
| figs4b-activated-increase-suppressed-decrease | partially_reproduced | Both one-tailed tests hold (p ≤ 1e-8). The activated-population baseline is 5.36 under reading (a) and 5.40 under (b), against 6.36 ± 0.704, so it is out of tolerance under both readings (cell 24). |
| figs4c-untuned-no-change | reproduced | p = 0.484; wall rate 6.36 against 6.32 ± 0.953 (cell 26). |
| fig2de-preferred-distances-span | reproduced | 7 mm is the most frequent preferred distance in both populations (57% and 37%), and all 8 farther bins are occupied (cell 28). |
| figs4ef-crossvalidated-stability | not_reproduced | Reading (a) holds (same preferred distance in 0.724 of activated against 0.507 of suppressed units), as does trough-keeping (0.897 at 7 mm against 0.293 farther). Reading (b) fails: the activated Spearman correlation is 0.815 against 0.831 for suppressed (cell 30). The criterion requires both readings. |
| figs4j-ventral-location | reproduced | Both readings hold (median depths 350/275/250 µm against 525 µm unresponsive; the 0–400 µm half has higher fractions) (cell 34). This rests on the unverified orientation of rel_y (B5). |
| figs4l-temporal-windows-map | partially_reproduced | Sustained 133 and onset 90 are within tolerance under reading (a). Offset is 68 under (a) and 42 under (b), against 34 ± 3.4. The order sustained > onset > offset holds (cell 32). |
| fig3a-decoding-above-controls | reproduced | All 8 group-against-control pairs are higher with p = 1.83e-4 under both cross-validations (cell 38). |
| fig3-overall-decoding-accuracy | reproduced | 10-fold, 3–11 s: 70.4, 60.9, 48.4, 33.7, 16.4 and 11.0%, all within tolerance and in the paper's order (cell 40). Shuffled 11.0% matches the paper's chance level of 11.1% (100/9). |
| fig3c-decoding-by-distance | partially_reproduced | Part (a) fails only at 9 mm (proximity 79.4 < map 81.5). Part (b) holds at 7/7 distances with q < 0.05. Proximity at 15 mm is 32.0, against 36.29 ± 3.63 (cell 42). |
| fig3c-decoding-error | reproduced | Submillimetre and only-map conditions hold; all four values are within tolerance under both cross-validations (cell 44). |
| figs5c-single-neuron-decoders | reproduced | Directions and q < 0.05 hold at 7, 11, 13, 15 and 17 mm. Every group is below its population value, and all four values are within tolerance (cell 46). |
| figs5de-svm-robust | not_reproduced | All qualitative conditions hold (map highest; proximity and combined above map at 7 mm; map highest at 13–23 mm in 6/6). The combined group is 61.9 against 54.43 ± 5.44 under both cross-validations (cell 48), and the criterion has no partial clause. |
| fig4-cut-baseline-unchanged | blocked (metadata_insufficient) | Nothing identifies the paper's 195 "stable-waveform" units from 18 of the 25 cutting mice. On all 384 units the baseline falls 6.41 → 4.74 sp/s (p = 1e-14; cell 54), which would contradict the claim. Part of it is testable (B10). |
| fig4b-cut-wall-firing-reduced | blocked (metadata_insufficient) | Same population problem. On 175 units the decrease holds (10.32 → 6.43 sp/s, both values within tolerance), but n is 175 against 86 (cell 56). |
| fig4b-cut-per-unit-changes | blocked (metadata_insufficient) | Same population problem; the counts (139/113/17) cannot be compared on twice the population. |
| fig4c-map-units-after-cut | blocked (metadata_insufficient) | Post-cut passes carry no wall distance; the zaber line is two-level (cell 62). Unchecked: other columns of wall_pass_epochs (C2). |
| fig4jk-proximity-units-after-cut | blocked (metadata_insufficient) | Same as above. |
| figs5fg-cut-decoding | blocked (metadata_insufficient) | Same as above. |
| figs6-opto-local-inhibition-gain | blocked (data_missing) | No vGat-Cre/GtACR mice: all 36 subjects are C57 (API metadata and cell 62). |
| figs6i-telc-kinematics-unchanged | blocked (data_missing) | No SpVi-TeLC mice. |
| telc-unit-yield | blocked (data_missing) | Same. |
| fig5d-telc-preferred-closer | blocked (data_missing) | Same. |
| fig5e-telc-category-shift | blocked (data_missing) | Same. |
| fig5e-telc-untuned-ambiguous-unchanged | blocked (data_missing) | Same. |
| figs6j-telc-untuned-higher-firing | blocked (data_missing) | Same. |
| figs6k-telc-tuned-baseline-similar | blocked (data_missing) | Same. |
| figs6k-telc-tuned-wall-higher | blocked (data_missing) | Same. |
| figs6l-telc-increase-at-close-distances | blocked (data_missing) | Same. |
| fig6ghi-tuning-shape-telc | blocked (data_missing) | The judged part is experimental and needs TeLC units. The model part is "reported, not judged" and was not reported. |
| fig6-model-telc-loses-map | reproduced | 1,225 neurons. Tuned 593 → 631, both within tolerance. Map share of tuned neurons 32.7 → 16.6%, proximity share rises (cell 60). See B7 on which output was captured. |

**B. Problems**

1. [affects a conclusion] Claims file: its `checks` log says the uncorrected responsiveness test was made the main reading, but the opening comment and every criterion still say BH-FDR is main. The notebook follows the current text. Under the uncorrected reading, fig2-wall-responsive-counts, fig2f, fig2-distance-tuned-counts and others fail (cells 14, 16, 18). The deposit's own labels match the BH-FDR classification unit for unit (cell 7), which supports BH-FDR. The file should settle this explicitly.
2. [affects a conclusion] Claims file, fig2-distance-tuned-counts: the expected values 656 and 29 contradict the paper's Fig. 2F. That figure's counts imply 591 tuned units and 94 "both" (266 + 118 + 88 = 472; 472 + 119 = 591; 213 − 119 = 94). The criterion has no reading for these values, so the claim fails on a number the paper contradicts itself on. The notebook finds 600 and 92.
3. [does not affect a conclusion] Cell 7/12, `isi_fa`: SNR is called "not computable" even though cell 34 builds mean waveforms from the raw voltage. SNR could have been approximated the same way. The Methods' duplicate-unit exclusion (r > 0.1 in 1-ms bins) is also neither applied nor mentioned. The count stays within tolerance in any case (see A).
4. [does not affect a conclusion] Cells 3–4, `unit_table`: in the two 1-mm-step sessions (38 units), both distances of a bin are pooled, while the deposit uses one distance per bin. This is the notebook's own choice, justified by the Methods' binning sentence, and was not run under the deposit's reading.
5. [affects a conclusion, if wrong] `unit_peak_depths`: depth is taken as the electrodes table's `rel_y`, assuming 0 is at the tip. That assumption is stated in the docstring but no output checks it. A reversed axis would invert figs4j.
6. [does not affect a conclusion] Cells 50–51: in 20230711 and 20230608 (the second is noted "very unstable"), 20 and 50 deposit trials fall after the cut gap. They are kept in the classification population, so they may be single-whisker passes.
7. [does not affect a conclusion] Cell 60, `run_model`: the model run printed four count lines. The paper's 590 and 636 tuned counts equal lines 2 and 4 exactly (362 + 228; 476 + 160), but the capture took lines 1 and 3 (593, 631). The notebook does not say which line is the Methods' nine-bin classification. Both pairs pass, and in both the map share falls.
8. [does not affect a conclusion] Cell 48: the SVM is run on every third time bin. This is stated as a deviation, and the same thinning leaves MCC unchanged (70.44 against 70.26).
9. [does not affect a conclusion] Cell 30, figs4ef: the Spearman reading compares medians whose ranges over the 100 splits overlap (activated 0.768–0.855, suppressed 0.771–0.890). The failure of reading (b) is therefore fragile, but the criterion is applied as written.
10. [affects a conclusion] Cells 49–58, cutting claims: blocking is defensible, but parts were testable and not tried. The session notes flag 6 of the 25 mice as "not stable" or "very unstable" (Ephys101, 106, 127, 36, 78, 87). Dropping them leaves about 19 mice, close to the paper's 18. A pre/post waveform-stability proxy could also be computed from the raw voltage, as cell 34 already does for depth. The large baseline drop on all units may come from drift that the paper's selection removes.
11. [does not affect a conclusion] Helper checks on synthetic inputs passed:
    - `bh` matches the hand-computed BH correction.
    - The K-S tail mapping in cell 24 is correct (wall > baseline gives a small p for "less").
    - `signrank` gives the expected one-sided tails.
    - `dist_bin` edges are correct.
    - `classify` labels synthetic proximity and map units correctly.
    - On null data, `summarize_cm` and `decode` (both cross-validations) are at chance (11.4–11.8%), as is `single_neuron_decoder` (11.0 ± 0.3%).
    
    In the decoder, z-scoring uses training data only, and no pass falls in both train and test.

**C. Could not check**

1. The orientation of `rel_y` (B5). An output printing the electrodes table's `rel_y` against site index, with its description or the channel map, would settle it.
2. Whether a post-cut wall distance exists anywhere. Outputs that would settle it: the column names and descriptions of `intervals/wall_pass_epochs` and of `DigitalInputEvents` in a raw cutting file, and whether the pre-cut distance sequence repeats as a fixed order (cell 62 lists only the group names). The brainstem.org lab notebook named in the dandiset was not consulted.
3. Which model output corresponds to the Methods' nine-bin classification (B7). Labelling the four printed analysis lines would settle it.
4. The cutting claims on a stability-filtered population. Outputs that would settle it: cells 54–58 rerun without the sessions noted unstable, or with a waveform-stability proxy.
5. Which baseline gives the paper's 6.36 sp/s for figs4b. Neither reading reproduces it, and no other candidate was tried.
6. The SNR-filtered unit count. An SNR column from raw-voltage waveforms would settle it.
