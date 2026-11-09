**A. Outcomes** (32 claims in the claims file: 17 tested in the three notebooks, 15 not tested)

| Claim | Outcome | Reason |
|---|---|---|
| fig1cd-new-pheromones-leave-nest, fig1e-categorical-response, fig1f-hexanol-like-native, fig1f-mho-differs, fig1f-vehicle-differs, figs2cf-gcamp-ants-behavior | blocked (data_missing) | These need behaviour videos. The archive query found only 14,685 two-photon `.nwb` files: odours plus paraffin oil, 22 subjects, nothing else. |
| table1-transgenesis, fig2b-s1a-transgene-fluorescence | blocked (data_missing) | There are no injection records or epifluorescence images in the dandiset (same archive query). |
| fig2cd, figs1, figs2ab, fig2e, fig2f, ablation-al-volume-trend, figs3-single-insertion | blocked (data_missing) | These data are at the Brain Image Library or NCBI, not in DANDI:000467. No part of them can be tested from this dandiset. |
| fig3f-general-odorants-unique | not_reproduced | Across ants, only 11 of 28 ant–odorant cases are nearer the same odorant (needs more than half). This part does not depend on the ROI reading. The within-ant part also fails under all four size-filtered readings (b), with 4 to 36 identical odorant pairs. |
| fig3fg-hexanone-broad | not_reproduced | 3-hexanone has the largest area in 6 of 6 ants, but its median area over ethylpyrazine's is 1.91, short of the required 2. The ratio is 1.91 with and without the AL mask. A near miss. |
| figs4a-bilateral-symmetry | not_reproduced | Under every ROI reading at least one ant's two ALs differ by more than one ROI (e.g. bix: 4 vs 7). The correlation part holds. |
| fig4b-vehicle-no-response | not_reproduced | Under all 8 readings the vehicle produces responding ROIs. Under bix it is 1 ant (ant2-m4-d26, 2 ROIs, largest value 0.327). Under the unfiltered readings (a) it is 9 to 11 ants. |
| fig4-no-decreases | not_reproduced | There are 594 odour-specific regions of at least 10 µm at −0.2 or below in 2 or more trials, 540 of them 10–20 µm, in 13 of 13 ants. The most negative is −0.45. See problem 9 on motion. |
| fig4-large-lasting-responses | not_reproduced | No reading meets both parts. b/i: median 0.59, 75% still elevated after the pulse. b/ii: median 1.18, but only 46% elevated. Under the unfiltered readings the medians are 0.37 and 0.42. |
| figs5a-sparse-median-6 | partially_reproduced | Under all four size-filtered readings, at 48% and at each ant's higher concentration, the largest median is 3 to 4 (limit 6.6). Under all four unfiltered readings it is 33 to 48. Those counts come from noise fragments (problem 4). |
| figs5a-concentration-more-glomeruli | not_reproduced | Both parts hold only under bix and biy. The sign test fails under biix and biiy (p 0.48 and 0.13). The "lower set within higher set" part fails under every unfiltered reading (8 to 17 of 52 pairs). |
| figs5b-shared-glomerulus | not_reproduced | No reading meets it. Best is bix: median 1, but exactly one shared ROI in only 6 of 13 ants (needs more than 6.5) and 4 of 8 at 48% (needs more than 4). |
| figs5c-mho-rarely-overlaps | not_reproduced | Met only under bix and biy. Fails under the other six readings (medians 1 to 4.5). |
| fig5ab-focal-glomeruli | not_reproduced | No reading reaches the needed identification counts. Best is aiix: PGb 12, 6G 11, PGa 9 (needs 12 or more, 12 or more, and 10 to 12). Under bix: 7, 4, 0. |
| fig5d-stereotyped-positions | not_reproduced | No reading meets it. PGa's anterior offset is 4 to 8.5 µm under the unfiltered readings (paper: 12.9 ± 1.9), and PGa has n=0 under bix. 6G fails on at least one centre/plane variant under every reading. |
| fig5c-s6-tuning | partially_reproduced | PGb responds to heptanone, heptanol and hexanol and not to 6MHO, and 6G responds to 6MHO, under both models and both plane readings. PGa was never identified (0 trials), so its two named combinations are untested rather than failed (problem 1). |
| fig5c-6g-slow | partially_reproduced | PGb returns near baseline (end/peak 0.18 or less, last-5 mean 0.17 or less), and 6G stays at or above half its peak for 36 to 37 s, under all four readings. PGa is untested. Only 7 ants for PGb and 4 for 6G. |
| figs7a-6g-extended | not_reproduced | 6G was identified in only 3 of the 5 ants with 144 s recordings. Plateau 2.4 to 4.8 s (expected 30 ± 3), return 32 to 71 s (expected 80 ± 8), no trial over 100 s. Weak evidence: n=3. |
| figs7c-temporal-lme | blocked (other) | PGa was not identified under the only reading the single-glomerulus traces (M3) were computed for, so the glomerulus factor has one level. All four fits failed with "list index out of range" and no p-values were produced (cell 39). It would be testable under aiix, where PGa is found in 9 ants. |
| fig6-shared-panic-pathway | not_reproduced (imaging half) | figs5b-shared-glomerulus and figs5c-mho-rarely-overlaps are both not reproduced. The behaviour half is blocked (data_missing, as fig1e). |

Reading codes: a = no ROI size filter, b = glomerulus-sized ROIs; i = ROI mean, ii = ROI maximum; x = trial-mean counting, y = per-trial counting.

**B. Problems**

1. **[affects a conclusion]** `alarm_pheromones.ipynb` cell 30 (`MAIN = "bix"`): single-glomerulus traces were computed only for the 7 ants with PGb identified under bix. That reading found 6G in 4 ants and PGa in 0. Reading aiix identifies PGb, 6G and PGa in 12, 11 and 9 ants but was never used for traces. This is the reason PGa is missing from fig5c-s6-tuning, fig5c-6g-slow and figs7c-temporal-lme, and why figs7a-6g-extended has only 3 of 5 ants.
2. **[affects a conclusion]** Cell 39: the `try/except` swallows the figs7c-temporal-lme model failure and prints an empty table. The notebook never says the claim is untestable.
3. **[affects a conclusion]** `al_imaging` docstring and `trial_m3`/`band_stacks`: the traces are not motion-corrected, justified by "shifts … under 1 µm". The notebook's own output contradicts this. Cell 7 shows a median per-trial shift of 10 px (2.9 µm), a maximum of 42 px (12 µm), and 77 of 182 trials over 10 px. The disc ROI is 15 µm across. The claims file (M3) assumes stabilization.
4. **[affects a conclusion]** `draw_rois` under reading a: it intersects pixels across trials on 4×4-binned maps with no minimum size, which breaks maps into fragments.
   - The claims file's reading (a) asks for regions that recur across trials, not pixel-wise intersection.
   - On synthetic pure-noise maps (SD 0.15) the helper returns 387 ROIs under a and 0 under b.
   - On the real data, reading a gives up to 469 ROIs in one ant (about the whole ~500-glomerulus AL) and 137 "vehicle ROIs".
   - This alone decides the reading-a failures of figs5a-sparse-median-6, figs5a-concentration-more-glomeruli, figs5c-mho-rarely-overlaps and fig4-large-lasting-responses.
   - Claims-file issue, reported rather than corrected: reading (a) with no size floor allows ROIs that cannot be "glomerular regions" as the Methods describe them.
5. **[affects a conclusion]** fig4b-vehicle-no-response (cell 12): the paper excluded trials with large motion artifacts, and the notebook built an exclusion variant. That variant was applied to figs5a, figs5b and figs5c but not to the vehicle trials. Under bix the claim fails on a single vehicle trial (ant2-m4-d26), which has 123 to 137 ROIs under the unfiltered readings. That pattern suggests a non-specific trial, but its fraction of AL above threshold is not printed.
6. **[affects a conclusion]** `trial_m3`: the claims file's second ROI reading for the traces, "the region of at least 0.2" around the centre, was not run. Only the 15 µm disc was used.
7. **[does not affect a conclusion]** `DISC2`: the helper's Minimum filter uses a 13-pixel disc. ImageJ's radius-2 Minimum kernel is 21 pixels, so noise suppression is slightly weaker.
8. **[does not affect a conclusion]** Cells 31 and 39: volume times use `arange * VOLUME_S` without the per-plane `starting_time` offset that the helper docstring describes. The offset is under 1.2 s and about the same for PGb and PGa.
9. **[does not affect a conclusion under the reader's rule]** fig4-no-decreases (cell 22): the notebook does not check whether the negative regions sit in the same place for every odour or on AL edges. Both would point to motion, which the paper names as the source of small decreases. The vehicle check rests on one trial.
10. **[does not affect a conclusion]** fig5d-stereotyped-positions: "PGa anterior in every ant" and "6G lateral in every ant" hold by construction of the identification step, as the notebook itself notes.
11. **[does not affect a conclusion]** The alarm notebook's header says 14 claims are blocked; the claims file has 15 untested claims.

The synthetic checks found no problems in these parts of the helper:
- `_shift` aligns correctly.
- Clipping and the Minimum filter commute.
- `offsets_um` matches the files' "up is lateral, right is anterior".
- `onset_and_max` and `_split_wide` behave as specified.
- Byte-offset reads match h5py (cell 4).

**C. What I could not check, and the output that would have let me**

- **Single-glomerulus traces under other readings:** traces for aiix or aiy would test PGa in fig5c-s6-tuning, fig5c-6g-slow and figs7c-temporal-lme, and use 5 of 5 ants for figs7a-6g-extended.
- **Whether unfiltered ROIs are noise:** a per-ant image of the ROI masks over the max-projection map, for both drawings.
- **Stabilization quality and its effect on traces:** shift against volume for a few trials, and a PGb trace with and without motion correction.
- **Image orientation (array rows taken as image rows):** a mean-F0 image for one ant with the identified PGb, 6G and PGa marked, to compare with Figure 5B and its gap.
- **Vehicle artifact:** the AL fraction of at least 0.2 for each vehicle trial, and fig4b-vehicle-no-response rerun with the flagged-trial exclusion.
- **Negative regions in fig4-no-decreases:** their overlap across odours and their distance to the AL border.
