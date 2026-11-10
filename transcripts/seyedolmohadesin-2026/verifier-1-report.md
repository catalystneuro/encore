**A. Outcomes (34 claims in the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| recordings-animals | reproduced | The subject descriptions give 22 hermaphrodites and 25 males; the subject ids agree (cells 3, 17). The data hold 189 sex-shared neurons against the paper's 196, but the criterion counts animals only. |
| fig5b-responsive-classes | reproduced | 86 classes under exclusion (a) and 85 under (b), against 84 ± 8.4 (cell 19). |
| fig5b-dimorphic-classes | reproduced | Reading (a), dimorphic and responsive: 83 and 82. Reading (b), dimorphic alone: 86 and 85. All are within 80 ± 8 under both exclusion readings (cell 21). |
| fig5b-layer-counts | partially_reproduced | 7 of 8 counts are within tolerance in all four combinations. Motor dimorphic is always 15 against 13 ± 1.3 (cell 23). This rests on the notebook's own layer assignment (problem 1). |
| fig3-each-stimulus-mixed | reproduced | All 8 cues have at least one dimorphic and one monomorphic class under both exclusion readings (cell 25). |
| sensory-dimorphic-and-monomorphic | not_reproduced | 21 of 24 sensory classes under (a) and 20 of 24 under (b), below the 22 required (cell 27). This depends on which classes count as sensory (problem 1). |
| layers-sensory-most-dimorphic | reproduced | Reading (c) gives sensory > inter > motor under both exclusions: 0.272 > 0.198 > 0.171 and 0.265 > 0.200 > 0.144. Reading (a) fails under both; reading (b) holds only under exclusion (b) (cell 29). |
| fig3a-osmotic-onset-examples | reproduced | AWA p = 4e-11, AWB p = 7e-7; ASER p = 0.45 and ASH p = 0.80, both responsive. The same holds under (b) (cell 33). |
| fig2b-bag-high-odor-monomorphic | reproduced | Readings (a), (b) and (c) all hold under both exclusions. BAG is responsive (p ≤ 3e-4) with sex p ≥ 0.38 (cell 35). |
| fig3a-ash-stimulus-dependent | reproduced | High salt p = 8e-13. Sorbitol p = 0.80 and CuSO4 p = 0.13, both responsive. Exclusion (b) agrees (cell 37). |
| fig3a-aser-salt-concentration | not_reproduced | Low salt p = 0.055 / 0.059, so not dimorphic. High salt is not responsive (p = 0.72 and 0.33 against control) (cell 39). |
| fig2e-i2-dimorphic | reproduced | Pheromone, osmotic and high salt all have p ≤ 0.05 at onset under both exclusions. Low salt is not dimorphic (cell 41). |
| pharynx-dimorphic-food-salt-pheromone | reproduced | Dimorphic pharyngeal classes per cue: food 3 (I4, M2, M5), pheromone 8, low and high salt several, under both exclusions (cell 43). |
| fig2-awa-awb-nociceptive | not_reproduced | AWA is not responsive to CuSO4: smallest p = 0.077 under (a), 0.085 under (b) (cell 45). |
| fig2-adf-m2-switch | reproduced | Reading (b), dimorphic in the direction of a switch, holds for both ADF and M2 under both exclusions; all four windows have the switch direction (cell 47). |
| male-specific-unresponsive | reproduced | Significant tests out of 16: CEMD 0, CEMV 2–3, MCM 1 (cell 49). |
| tail-unresponsive | blocked (data_missing) | No tail neuron has a trace (cell 13). The archive's API shows 47 ophys NWB files and nothing else. A part could be testable from the raw volumes if they image the tail (NeuroPAL IDs list PLM, PHA, ALN), but that means re-tracking the volumes: too_large and methods. The archive metadata do not show whether other trace tables exist (problem 6). |
| figs2f-left-right-similar | reproduced | Band-passed: 77 of 79 classes (herm) and 80 of 82 (male). Raw traces: 72 of 79 and 73 of 82 (cell 51). |
| figs3e-pattern-robust | reproduced | Reading (a): 0.78 / 0.83 of representation-1 classes stay dimorphic under all three. Dimorphic pairs drop from 368 (rep 1) to 262 (rep 2) and 254 (rep 3); exclusion (b) gives 355, 256, 255 (cell 53). |
| figs2e-no-order-effect | blocked (methods_underspecified) | Under exclusion (a), the one-way ANOVA finds a dependence (p = 0.034) while both regressions do not (p = 0.063 and 0.335). Under (b) all three find none (cell 55). The readings disagree, so the criterion sends this to blocked. |
| figs3fg-state-dependence-interneurons | blocked (methods_underspecified) | Interneurons are highest in 22 of 24 OPEN combinations. They are not highest with AVAR / range / divide under either exclusion (cell 85). The claims file's READINGS rule requires all combinations to agree. |
| figs2c-aib-state | reproduced | The criterion is met in 24 of 24 combinations, e.g. high-salt onset interaction p = 0.003 (cell 87). |
| figs8-state-insensitive | reproduced | Met in 24 of 24 combinations: 0.80–0.87 of state tests have p > 0.05, and 0.69–0.80 of dimorphic sensory responses are kept (cell 89). |
| fig4c-functional-connectivity-similar | reproduced | R² = 0.806 under reading (b), against 0.8 ± 0.08; reading (a) also gives 0.806 (cell 59). |
| fig4-stimuli-correlate-sensory | reproduced | Sensory has the highest mean \|r\| and rms r in both sexes, under both CORRELATION readings (cell 61). |
| fig4-pharynx-uncorrelated | reproduced | Pharyngeal-to-other pairs are lowest by both measures, in both sexes and under both readings (cell 63). |
| fig4-functional-dimorphism-small | reproduced | 99.98% of the 5,995 pairs are below 0.4 (cell 65). |
| connectome-link | reproduced | 83 of 86 subclasses outside the pharynx and ventral cord (96.5%) are in all four connectomes (cell 69). |
| fig4d-functional-synaptic-uncorrelated | reproduced | Slope p = 0.64 with Cook's counts and 0.91 with sections. The variant with regularization 3 gives p = 0.009 with counts, but it is a variant only (cell 74). |
| fig4f-synaptic-top-not-functional | reproduced | Without functional dimorphism: 35 of 36 (counts) or at least 30 of 36 (sections), and 6 of 6 of the Figure 4F pairs. The descriptive part is weak: the top 36 have mean \|r\| 0.15–0.18 (cell 76). |
| fig4g-functional-top-not-synaptic | blocked (methods_underspecified) | With Cook's counts both exclusion orders meet the criterion. With sections, order (ii) fails under both "not connected" readings (3 of 6 connected pairs not dimorphic). The orders must agree (cell 78). |
| figs20-multihop-no-match | reproduced | Indirect strength is at least the direct one for 100% of pairs; slope p = 0.215 (counts) and 0.963 (sections) (cell 80). |
| connectome-normalization-sem | not_reproduced | None of the four unit-by-set combinations has all four values in tolerance. After normalization the SEM rises with sections (1.32–1.41) and barely changes with counts (0.66) (cell 71). |
| figs1-behavior | blocked (data_missing) | The archive's API confirms the dandiset holds only 47 ophys NWB files and no drop-test data. |

**B. Problems**

1. [affects a conclusion] `chemo.LAYER_CLASSES`: only one layer assignment is run. The claims file allows any assignment with the paper's totals; this one is the author's, e.g. IL1 and URA as motor, RMG and RIV as inter. fig5b-layer-counts misses only on motor dimorphic (15 vs 13). Moving one non-dimorphic class such as RMG, AVD or RIV into motor could give 8 of 8. sensory-dimorphic-and-monomorphic misses by one or two classes, so a different sensory set could also flip it. No sensitivity run is shown. The same assignment also feeds layers-sensory-most-dimorphic, fig4-stimuli-correlate-sensory, the sensory-sensory exclusion in fig4g and figs3fg.
2. [affects a conclusion] Cell 82, `exp_fit`: the Methods fit an exponential to AVA's *baseline*; the notebook fits the whole trace, which includes the reversal bouts. A baseline-only fit is a reading the paper allows and was not run, and figs3fg is already split by reading. In cell 85, the q < 0.05 fractions are at most 2% (often 0 for sensory and motor), so "inter highest" rests on a handful of cells.
3. [affects a conclusion] Cells 67–78: the Cook counts-or-sections choice decides fig4g. It was rightly run both ways, which is what makes fig4g blocked. One pointer the notebook does not draw out: sections give a pre-normalization mean SEM of 1.143 (paper: 1.14), which suggests the paper used sections.
4. [does not affect a conclusion] Cell 71: the 95% quantile of nonzero weights is the author's own choice. I re-ran reading (b) from the journal supplements and got the notebook's numbers exactly. Taking the quantile over the masked synapses including zeros gives after-values of 0.69 (counts) and 1.41 (sections), also outside tolerance. I also confirmed that Witvliet's sheets put the presynaptic cell in columns (ASHL→AVAL = 8, AVAL→ASHL = 0), so `_sheet(..., False)` is correct.
5. [does not affect a conclusion] Cells 5 and 7: 20220403-h3 and -m3 carry an identical 382-row table. Assigning the first block to h3 and the second to m3 is an inference, but a well-supported one: CEM and MCM appear only in the second block, and the order-matching r values are 0.58/0.54 against 0.31/0.32.
6. [does not affect a conclusion, but leaves tail-unresponsive under-checked] `load_recording` reads only `processing/CalciumActivity/ActivityTraces`. No listing of the other NWB groups shows that no tail trace table exists, even though the NeuroPAL segmentation labels tail cells.
7. [does not affect a conclusion] Cells 19 and 21, chance level: the paper states none. The notebook's own estimate is that, with 32 uncorrected tests per class, a class with no effect is called responsive with probability up to 81%. So about 72 of 89 classes could be expected by chance, and the 84/80 counts are weakly diagnostic. After BH correction, 7.6% of sex tests are significant.
8. [does not affect a conclusion] `chemo.ma_past` counts missing values as 0 inside the window, which dilutes the band-pass next to gaps. The docstring says this follows the code; I could not check that. The function reproduces a rolling mean on synthetic input without gaps.
9. [does not affect a conclusion] Cell 47: for fig2-adf-m2 reading (b), the direction is taken from the window with the smaller p, which is the author's choice. Both windows give the same direction for ADF and M2, so the choice does not matter here.
10. [does not affect a conclusion] Cell 69: connectome-link uses only the sections sheets, whose White cell list (300 × 453) differs from the counts sheet (452 × 468).
11. Helpers tested on synthetic inputs, all correct: `responses` (window positions, onset and offset F0: a step from 10 to 20 gives during = 1.0, off = −0.5), `exclude`, `ttest`, `subclass`/`canonical`, and `stimulus_series` (starts 2 frames before onset, 40 frames long).
12. No misreading of the paper was found in the claims file. The Methods passages it cites (exclusion, responsive, dimorphic, motor state, correlation, normalization) match the paper's text.

**C. Not checked, and what would have allowed it**

- **Layer sensitivity:** a rerun of cells 23, 27 and 29 under an alternative layer assignment (for example Cook et al. 2019's cell types) would show how sensitive the layer claims are.
- **Tail traces:** an h5 group listing of one NWB file would show whether any tail trace table exists.
- **Band-pass filter:** I could not compare `band_pass` or `ma_past` with the code's `correct()`, which is not available to me. A side-by-side on a toy trace would settle it.
- **Motor states:** I could not judge the state labels. Printing the AVA traces with the fitted baseline and the state labels for a few animals would allow it, as would the per-layer *counts* (not fractions) of q < 0.05 pairs in cell 85.
- **Cook counts sheet:** I did not check its parse (`_sheet` header offsets on SI 3) against the sheet; I only checked SI 5 indirectly through the SEM match. A printed known connection (e.g. ASHL→AVAL) from each Cook sheet would settle it.
- **Recorded-neuron set (a):** I could not recompute it for connectome-normalization-sem, because it needs the trace labels.
- **Figure 5B per stimulus:** Data S4 is unavailable, so the per-stimulus responsive and dimorphic counts cannot be compared with the figure.
