**A. Outcomes (57 claims in the claims file; the attempt record wasn't among my materials)**

| Claim | Outcome | Reason |
|---|---|---|
| cell-counts | reproduced | 1,189 CA1 cells from 9 rats, 219 control cells from 3 rats, 620 cells at most in one session (nb01 c20). |
| fig1c-object-tuned-fraction | not_reproduced | Under width reading b the CA1 fraction is 0.187 (inside tolerance), but the control "chance" is 0.041 (9/219) or 0.073, both outside 0.0503±0.005. Paper chance 5.03% against 4.1–16.9% here. Width reading a: 0.278 and 0.119–0.169. Binomial p<0.05 in all four (nb01 c22). |
| fig1d-field-distances | not_reproduced | 0 of 12 readings pass. The largest distance is 104–125 cm against a limit of 88.8 cm, and some minima are 3.3 cm. The mean is inside tolerance in 8 of 12 (c25). |
| fig1e-object-cells-and-object-vector-cells | not_reproduced | 0 of 12 readings pass; at most 2 of the 3 values are inside tolerance in any reading (c28). |
| fig1f-orientation-coverage | reproduced | Pearson r is −0.25 to −0.73 with p<1e-4 in 11 of 12 readings (c33). |
| fig1g-no-experience-effect | blocked (data_missing) | Confirmed on the archive: the data descriptor lists only timestamp, x, y, object position and spike times. There are no cell IDs across days and no exposure day. |
| fig1h-cross-day-stability | blocked (data_missing) | Same as fig1g. The 283 unmatched tetrode population units cannot be tied to days. |
| figs2e-within-trial-stability | reproduced | r=0.409 (width a) and 0.424 (width b), both inside 0.405–0.495, p<1e-10 (c35). |
| figs2c-no-proximodistal-effect | blocked (data_missing), partly testable | The notebook missed that this can be tested in part (B2). Using its own per-rat counts (c23), width reading b gives r=0.37, p=0.37 (8 implants) or r=0.42, p=0.23 (10). That matches the paper's r=0.42, p=0.22. Width reading a gives p=0.052 and 0.035. |
| figs3a-ca3-object-tuned | not_reproduced | Fractions are 0.326 and 0.191 against 0.23±0.023, on 341 cells rather than 313 (c37). |
| fig2d-spatial-change-no-o | reproduced | Median 0.454 against 0.795, z=−12.14, p=6e-34 (c39). |
| fig2d-rate-overlap-no-o-unchanged | partially_reproduced | Speed-filtered rates give p=0.013; whole-trial rates give p=0.24. Both readings are allowed and they disagree (c39). |
| fig2-fraction-changed-no-o | reproduced | 0.664 and 0.667 against 0.675±0.0675 (nb02 c6). |
| fig2d-o-om-change | reproduced | Spatial p=4e-44 and rate p≤4e-4, both with lower O–OM medians; changed fraction 0.654 and 0.685 (nb02 c8). |
| fig2d-om-no-prime-change | reproduced | Spatial p=4e-37, lower for OM–NO'. Rate p=0.999 and 0.75. The "retained fields" part is not tested (c39). |
| fig2d-no-no-prime-change | reproduced | z=−11.34, p=9e-30 (c39). |
| figs3f-ca3-changes | partially_reproduced | Spatial tests 4 of 4 significant. Rate overlap: 0 of 4 significant with whole-trial rates, 1 of 4 with speed-filtered rates (OM–NO' p=0.008). Run on 341 cells, not 313 (c42). |
| figs4-object-traces | not_reproduced | Trace fraction 0.061–0.098 against 0.183±0.018. The NO–NO' changed count (908–916) is inside tolerance (nb02 c10). |
| figs2d-traces-no-interference | reproduced | Width reading b: p=0.47–1.0 in all 16 readings. Width a fails (p<1e-12), but only because its starting fraction (0.278) already misses 0.199. It rests on half the paper's trace cells (B9). |
| ovs-method-extra-cells | reproduced (fragile) | 27 of 96 readings fall in 40±4, all under the author's own "x-b" exclusion; none under "x-a". Counts range from 9 to 53 (c31). |
| fig3b-decode-presence | reproduced | 16 of 16 sessions under both speed readings; accuracy 0.62–0.76, shuffle means 0.494–0.51 (nb03 c6). |
| fig3c-bin-size | reproduced | Medians rise at each step up to 1 s; gain 1→10 s is 0.03 against 0.11 for 0.1→1 s (c8). |
| fig3d-number-of-cells | reproduced | r=0.58 and 0.60, p<1e-97; mean accuracy 0.53 at k=1 and 0.74–0.75 at k=500 (nb05 c4). |
| fig4b-distance-decline | reproduced | H=47.3 and 48.9; medians fall monotonically; bins 1v2, 2v3 and 4v5 all p≤0.0034. Bin 1 minus bin 5 is 0.18 (paper 0.19). Exactly 16 sessions, so the session readings coincide (c10). |
| fig4c-each-session-decreasing | reproduced | 16 of 16 sessions on both measures (c12). |
| fig4e-angle-flat | not_reproduced | Speed reading a with sectors from 0° gives H=10.26, p=0.036; the other three readings give p=0.065–0.21 (c14). |
| fig4h-population-vector-correlation | reproduced | Holds with 20 cm rings under all four filter/blanking readings. Not with equal-area bins (3v4 not significant) (c16). |
| figs5a-decode-no-from-no-prime | reproduced | 16 of 16 sessions, but the tetrode sessions have only 3–15 cells each (c18). |
| figs5b-fixed-distance-bins | reproduced | H=50.7 and 52.9; highest bin 1, lowest bin 5 (c20). |
| figs5c-half-trial-control | reproduced | p=0.98 (c22). |
| figs5d-control-sessions | blocked (data_missing) | Confirmed: the control file holds each cell once, so only 1 of 14 sessions reaches 25 cells. A variant over all 14 sessions gives p=0.14–0.22 (c24). |
| figs5e-shuffled-labels | reproduced | Speed reading a: means 0.499–0.502, smallest t-test p=0.063. Speed reading b: bin 1 t-test p=0.009 (c26; see B5). |
| figs5f-random-partition | reproduced | H=29.7 and 31.4; bin 1 highest, bin 5 lowest (c28). |
| figs5ghi-fields-and-rates | not_reproduced | Only part (i) holds. Rates peak in bin 2 in both trials, and NO and O differ in bins 3 and 4 (p=0.004, 0.013) (c30). |
| figs6-behaviour-decoders-flat | not_reproduced | Occupancy decoder H=22.8, p=1.4e-4. Speed decoder p=0.062. Head direction is not in the archive (descriptor) (c32). |
| figs6hij-behaviour-matched | partially_reproduced | Speed- and occupancy-matched decoders hold in all 8 readings (p<1e-5, bin 1 highest). Head direction is blocked (data_missing, confirmed) (c34). |
| figs6k-uniform-prior | reproduced | H=47.3 and 47.2; bin 1 highest (c36). |
| figs6l-sampling-thresholds | reproduced | All four thresholds pass in all 8 readings (c38). |
| tables1-without-bin-1 | reproduced | p=3.7e-6 with bin 2 highest. H is 27.96 and 28.23, just outside 25.06±2.51 (c40). |
| fig5b-words-more-informative | reproduced | Words higher in every bin; per-bin p≤1.4e-6, pooled p=1e-27 (nb06 c6). |
| fig5bc-words-information-falls-with-distance | reproduced | H=11.6 and 13.1, p=0.021 and 0.011; bin 1 highest (c8). |
| fig5b-counts-uninformative | not_reproduced | The Kruskal-Wallis part holds (p=0.19, 0.29), but the t-tests against zero give p<0.05 in bins 2–5 (c10). |
| fig5e-kl-divergence | reproduced | H=15.5 and 18.0; bin 1 vs bin 5 p≤0.002; shuffled data p=0.41 and 0.98 (c12). |
| fig5-entropy | not_reproduced | Word entropy is 1.9–5.9 bits against 1.65±0.165 in every reading (c14). |
| figs7cd-number-of-words | reproduced | All tests p≥0.78 (c16). |
| figs7e-downsampled-words | blocked (other) | The output does not test the claim: the word selection leaks the trial label (B1). A rerun is needed. |
| fig6ab-single-cell-distance-tuning | partially_reproduced | Mean 0.016, inside-bounds fraction 0.977–0.985 and positive fraction 0.125–0.129 are inside tolerance. The negative fraction 0.047–0.056 is outside 0.038±0.0038 (nb04 c5). |
| figs5l-without-positively-tuned | reproduced | H=25.4 and 23.9; bin 1 highest (c7). |
| figs5m-without-object-tuned | reproduced | Width b with all unlinked cells removed: p=0.032 and 0.035. Keeping unlinked cells: p<1e-7 (nb03 c44). |
| fig6c-subsets-decline | partially_reproduced | Sizes ≥20 decline in every reading. The full criterion passes in only 1 of 12 combinations (speed b, size list b, signed-rank). Sizes 5 and 10 fail elsewhere, and in every combination under the Methods' speed filter (nb05 c6). |
| fig6d-reorganization-grows-with-cells | reproduced | Passes under speed reading b for all three size lists. Under speed a the extremes fall at 400 cells (0.071 against 0.070) (c6). |
| figs8-smaller-datasets | reproduced | All four Kruskal-Wallis tests p<1e-15, with the trends in the right direction (c8). |
| fig6ef-least-tuned-cells | not_reproduced | At 20% kept, the bin 1 minus bin 5 difference is −0.35 and the slope +0.08: the opposite sign to the paper (nb04 c9). |
| fig7-single-cell-properties | not_reproduced | Spatial information r is −0.002 to −0.038 against −0.13, in every reading (c13). |
| fig7-slope-variant | not_reproduced | Spatial information r ≈ 0 against 0.10; spatial correlation r is +0.07–0.09 against −0.08 (c13). |
| figs5jk-walls-no-pivot | not_reproduced | 6 of 6 tests p≤0.001: decoding error is 8–10 cm larger near the walls, PV correlation 0.077 lower (nb03 c42). |
| figs8eh-least-tuned-smaller-datasets | reproduced (borderline) | The slope first reaches zero at 0.4 kept for both datasets. That is just inside 0.6±0.2 (exactly at the edge) and inside 0.5±0.2 (nb04 c11). |

My tally: 33 reproduced, 5 partially reproduced, 14 not reproduced, 5 blocked.

**B. Problems**

1. **[affects a conclusion]** nb06 c4, `session_measures` (downsampling for figs7e). The top-c words are chosen separately in each trial and then pooled. A word that is in one trial's top set but not the other's is kept only for that trial's samples, so it becomes perfectly informative about the label. On synthetic data, swapping the ranks of two words raised the mutual information from about 0.001 to 0.08 bits. The notebook's 0.30 bits (higher than the 0.08–0.16 for all words) and its 80 of 80 pairs are therefore not evidence. This follows the paper's "In a given trial" wording; the claims file says "per session and distance bin". That mismatch is a claims-file ambiguity, reported here, not corrected.
2. **[affects a conclusion]** figs2c is marked blocked (nb01 c0). The Supplementary Figure 2C legend gives the cell counts in proximodistal order (39, 129, 43, 13, 242, 151, 26, 135, 378, 33). These identify every rat one-to-one from the deposited counts. Only the split of rat 27207 between its two probes is missing. The claims file also says the claim "needs the implant sites" without noting this.
3. **[affects a conclusion]** nb01 c37 and c42. The CA3 analyses use all 341 cells from 4 rats against the paper's 313. Using only the 120 tetrode cells, 2 of the 4 spatial tests become non-significant. The choice is not justified.
4. **[affects a conclusion]** nb01 c30–31, ovs-method-extra-cells. The exclusion readings (x-a/x-b), the spatial-information λ, the field rule and the distance reading are all the author's own, giving 96 combinations. The pass rests entirely on x-b. Neither exclusion reading matches the paper's 28.8% excluded (x-a 59–70%, x-b 19–21%).
5. **[does not affect a conclusion]** `shuffled_accuracy` (fig3b, figs5e). Labels are permuted against fixed decisions, so accuracy is about 0.5 by construction. The deviations the t-tests pick up come from unequal NO/O sample counts. This is consistent with the paper's description, but the test says little.
6. **[affects a conclusion]** fig6c, fig6d, figs5e and fig2d-rate-overlap each pass or fail depending on a reading the criterion allows, and fig6c/6d use only 20 random subsets. The notebook's "per reading" tables don't flag this.
7. **[affects a conclusion]** `fields`: fields are taken as connected regions above 3 × MAD, not the Methods' iterative contour from the peak. This can split or merge fields, and the fig1d/1e counts and ranges (no-field counts of 2–72) are sensitive to it.
8. **[does not affect a conclusion]** nb01 c11–12: 11 CA1 units fail the inclusion rules as computed here and are kept. The count still passes.
9. **[affects a conclusion]** figs2d depends on figs4, whose trace set (72–117 cells) is about half the paper's 218. The absence result is weaker evidence than it looks.
10. **[does not affect a conclusion]** fig6ef/figs8eh: cells are sorted by a tuning measured on the same data they are then decoded on. That is circular, but it is the paper's procedure. In figs8eh the tetrode result is averaged over 14 per-session curves rather than pooled.
11. **[does not affect a conclusion]** `spatial_information`, λ reading si-a: λ is not the map's occupancy-weighted mean, so the values can be negative (minimum −0.34 bits/spike). Both λ readings fail fig7 anyway.
12. **[does not affect a conclusion]** CA3 session 3 has the O and OM object positions reversed relative to the protocol (nb01 c10). It is flagged but not handled; figs3a fails regardless.
13. **[does not affect a conclusion]** In the Neuropixels population files, y is a copy of x. The notebook correctly swaps in tracking from the CA1 file (`decoding_sessions`), and the variant run on the raw files shows that the swap matters.

**C. What I could not check, and what output would have let me**

- **figs6 occupancy decoder** (`behaviour_decoder`, the author's implementation): I couldn't tell whether its 0.56–0.71 accuracy reflects behaviour or the decoder itself. A NO-half-versus-NO-half control and per-session accuracies would settle it.
- **figs7e:** a rerun with the top-c words chosen once over both trials per session and distance bin.
- **figs2c:** whether any unit ordering in the 27207 file separates the two probes (242 and 378 cells). Per-unit depth or channel isn't deposited, so this probably can't be fixed.
- **figs3a/figs3f:** which 313 of the 341 CA3 cells the paper used. Per-session CA3 counts and inclusion flags would help.
- **fig1d:** how many cells have their nearest field beyond 88.8 cm. A histogram tail count would show whether the range fails on a few outliers.
- **fig6c:** whether sizes 5 and 10 are reliably significant. 100 subsets per size instead of 20.
- **Raw tracking fields:** the notebook never printed the fields of the tracking struct. The data descriptor I read lists only timestamp, x and y, so the head-direction block is confirmed from metadata rather than from the files.
- **Not re-run:** I did not download the data or re-run any notebook cell. My checks are code reading, synthetic tests of `equal_sample_edges`/`assign`, `_template_corr` and the downsampling step, and arithmetic on printed outputs.
