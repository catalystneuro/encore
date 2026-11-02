**Verification report, round 1: Le Merre, Heining et al. 2026 on DANDI:001260 (0.250911.0744)**

The claims file has 40 claims. My outcomes: 12 reproduced, 3 partially reproduced, 10 not reproduced, 15 blocked (9 methods_underspecified, 6 data_missing).

### A. Outcomes

| claim id | my outcome | reason |
|---|---|---|
| dataset-ki-counts | reproduced (partial under the notebook's main reading) | With 000473 the recordings are 99 and the PFC share is 53.6% (cell 14). Under the main rule (12 *active* epochs of ≥6 spikes) there are 20,354 units and 10,900 PFC units, both outside tolerance. The Unit quality control passage, which is this claim's own source, says "≥4 ISIs in at least 12 separate 3-s epochs" and does not say active. Under that reading (the notebook's "variant") all four values hold: 25,929 or 24,898 units, 52.3–52.4% PFC, 13,559 or 13,040 PFC units. |
| fig1h-waveform-classes | partially_reproduced | Cell 16: the fractions hold under both denominators (78.1/18.2%; 81.1/18.9%) and the histogram is bimodal (modes 0.26 and 0.64 ms, valley 0.36 ms). All three counts miss: ww 15,894 (expected 19,186 ± 1,919), nw 3,698 (from 3,780), unclassified 762 (from 776). |
| fig1i-nw-higher-metrics | reproduced | Cell 18: nw is higher than ww for log10FR, B and M, with p from 1e-156 to 1e-76. The variant gives the same. |
| extfig1d-sleep-like-differ | reproduced | Cell 20: the epoch-type effect has p < 1e-6 for all three metrics in ww units. With the Methods detector, sleep-like epochs have lower FR, higher B and lower M. The FR direction flips under the code's detector. |
| extfig1-epoch-counts | not_reproduced | Cell 22, per probe recording: sleep-like time 20.2%, 180.5 active epochs and 125.5 sleep-like epochs, against 6%, 227 and 19. The code's detector also fails (8.7%, 203, 83.5), and so does the per-session reading. The detector itself is suspect (problem 1). |
| extfig1f-burstiness-memory-uncorrelated | not_reproduced | Cell 24: B ~ M slope −0.19, p = 1.8e-66, marginal R² 0.024. A claim of absence fails at p < 0.05. |
| fig2a-som-memory-burstiness | partially_reproduced | Cell 28: the B–log10FR gradient angle is 110°, so part 1 holds. Part 2 fails under both readings: 3 of the top 10% memory nodes and 23 of the top 25% lie in the top quartile of node B. |
| fig2b-pfc-regular-territory | reproduced | Cell 30: PFC share 50.5% (54 ± 5.4). PFC median B is lower (p = 2e-32) and its fraction with M < 0 is lower (0.541 vs 0.682, p = 4e-53). |
| fig2e-category-stability | reproduced | Cell 32: stability 0.573 as a mean over transitions and 0.594 pooled; chance 0.184 under both. The paper's chance level of 18% matches. |
| fig2f-low-rate-less-stable | blocked (methods_underspecified) | Cell 34: under G2 (a) part 1 fails and part 2 fails for categories 7 and 8, so not reproduced. Under G2 (b) part 1 holds but part 2 fails for categories 1, 3 and 7, so partial. The claims file blocks a claim when the two readings disagree. |
| extfig3f-layer-enrichment | blocked (methods_underspecified) | Cell 46: under G2 (a), L5 has no significant positive E-score in categories 1–3. Under G2 (b) all three parts hold. |
| fig2g-pfc-regular-enrichment | blocked (methods_underspecified) | Cell 38: under G2 (a), 4 of 6 subregions qualify (partial); under G2 (b), 6 of 6 (reproduced). |
| fig2g-ila-pl-category1 | blocked (methods_underspecified) | Cell 40: under G2 (a), ILA's category 1 E-score is −3.1* and PL is not significant. Under G2 (b), both are significantly positive (9.1*, 6.0*). |
| fig2g-bursty-orbl-mos-aiv | blocked (methods_underspecified) | Cell 42: under G2 (a), none of the three is significantly positive. Under G2 (b), ORBl and MOs are, AIv is not (p 0.07–0.105), so partial. |
| fig2g-th-hpf-bursty | blocked (methods_underspecified) | Cell 44: the claim's own readings disagree in every case. "All of 6, 7, 8" is False and "at least one" is True for both TH and HPF. |
| fig2i-ibl-replication | blocked (data_missing) | IBL data are not in 001260 (checked on the archive). The data are public and the notebook did not attempt them. |
| extfig5g-nw-enrichment | not_reproduced | Cell 48: under both G1 readings, ILA, PL and ACAd/v are not significantly enriched in the regular category (5), and ORBl is not enriched in the bursty category (1). |
| fig2j-nw-ww-correspondence | not_reproduced | Cell 50: the mean r between ww 1–3 and nw 5 is −0.001 to −0.077 under every G1 and G2 reading. 21 regions were used; the paper used 9. |
| fig3a-harris-regular-positive | not_reproduced | Cell 54: category 2 r is −0.17 under G2 (a), and 0.39–0.40 (p ≥ 0.135) under G2 (b). It is not significant under any reading. 15 areas were used; the paper used 17. |
| fig3b-harris-regular-positive-ibl | blocked (data_missing) | Dataset IBL is not attempted. |
| fig3c-harris-bursty-negative | blocked (methods_underspecified) | Cell 56: under G2 (a), category 6 has r = +0.39, so the claim fails. Under G2 (b) all of 6–8 are negative, category 6 has r = −0.57 (p = 0.027), and it is stronger than any of 1–3. |
| supptable5-no-hierarchy-within-pfc | reproduced | Cell 58: no category has p < 0.05 across the 11 PFC subregions under any reading. With n = 11 this is a weak claim of absence. |
| fig4b-dataroi-parcellation | reproduced (at the tolerance edge) | Cell 62: 001260 + 000473 give 38 dataROIs under both bounds, against 42 ± 4. 001260 alone gives 22. |
| fig4cd-dataroi-enrichment | reproduced | Cell 64: holds for all 8 combinations of reference, G1 and G2. The "most ventral" part is not tested, as the claims file says. |
| fig4e-activity-modules | not_reproduced | Cell 66: both ILA dataROIs share a module, but that module holds 2 of 6 ILA dataROIs, so it fails both "ILA-specific" readings. This uses only 22 dataROIs, 2 of them in ILA. |
| fig4g-gao-category1 | not_reproduced | Cell 70: r = 0.20–0.33, p = 0.086–0.31, n = 29 (paper 30), under every reading. |
| extfig7n-gao-category6 | blocked (methods_underspecified) | Cell 72: under G2 (b), r = −0.54 to −0.62 (p ≤ 0.002). Under G2 (a), r = +0.03 to +0.11. |
| fig4g-pl-orbl-extremes | partially_reproduced | Cell 74: under G2 (b), ROIs 20 and 41 are in the top three. Under G2 (a), ROI 23 is lowest in 3 of 4 combinations of reference and G1. Reference (b) with G1 (b) and G2 (a) gives not reproduced, so strictly G2 disagrees in that one combination. |
| fig5b-tone-categories | reproduced | Cell 78: under both training readings, category 8 is the largest. The largest onset IQR in categories 1–4 (35.8 / 26.3 ms) is below the smallest in 5–7 (90.7 / 102.4 ms). |
| fig5cd-tone-maps-cross-subregions | not_reproduced | Cell 80: no ORBvl dataROI is significantly enriched in tone category 1 under any of the 8 readings. |
| fig5e-tone-responsive-patches | reproduced | Cell 82: enriched dataROIs fall in 5 or 6 subregions, and ACAd, MOs (and PL under G1 a) hold both an enriched and a depleted dataROI. |
| fig5g-tuned-unit-counts | blocked (data_missing) | IBL data are not in the dandiset. |
| fig5g-tuning-maps | blocked (data_missing) | Same as above. |
| fig5h-choice-gao-hierarchy | blocked (data_missing) | Same as above. |
| extfig9e-tone-responsive-no-hierarchy | reproduced | Cell 84: r = 0.05 / −0.002, p = 0.83 / 0.99, n = 25 (paper 29). |
| fig5i-map-similarity | not_reproduced (dataset part) | Cell 86: the tone-responsiveness map is most similar to category 1 under G2 (a) and to category 5 under G2 (b); both are the same cluster. It is never most similar to category 8. The IBL parts are untested. |
| fig5j-tone-responsive-high-rate | not_reproduced | Cell 88: the criterion fails under all 12 readings. Either spontaneous category 6 has a negative sum, or tone-8 is positive in at most 3 of 5 categories. There are 3,921 units against the expected 6,681 (001260 only). |
| fig5k-task-tuning-category4 | blocked (data_missing) | IBL data are not in the dandiset. |
| methods-settings-no-difference | blocked (methods_underspecified) | The paper names no test. The variant only (cell 90) shows significant setting effects, for example Aversion on FR (p = 0.002) and on B (p = 9e-5). |
| zenodo-unit-link | reproduced | Cell 60: all 20,374 of 20,374 units match. Location labels agree for 98.6% and ww/nw labels for 97.0%. |

### B. Problems

1. **[affects a conclusion]** The sleep-like detector over-detects (`offperiod_sleep`, `offperiod_sleep_code`, cells 9 and 22).
   - I ran it on stationary Poisson populations with no true off periods. It flags 100% of the time with 10–20 cortical units at 3 Hz and 47–51% with 50 units; only from 150 units does it flag 0%.
   - Several probes rely on few cortical units and come out mostly sleep: PL055-probe0 (29 units) 155 sleep / 0 active, 732714-probe1 (38) 308/9, 250252 (59) 248/0.
   - The result is 20% sleep-like time against the paper's 6%, and 80 tone epochs per file against 188.
   - This decides extfig1-epoch-counts. It also lowers every unit count (dataset-ki-counts, fig1h, and the 7,184 and 6,681 expected counts), and it changes which epochs enter every metric.
2. **[affects a conclusion]** Which epochs count toward the 12-epoch rule (cell 14). The Unit quality control passage, which is the source of the 24,248, says ≥4 ISIs in 12 epochs without restricting to active epochs. The notebook runs this only as a "variant", but it is a reading the paper allows, and under it dataset-ki-counts holds. The fig1h counts were not computed under it.
3. **[affects a conclusion]** All analyses except the counts and fig4b use 001260 alone (74 of 99 recordings), although 000473 is loaded and its units carry Zenodo flatmap positions.
   - This gives 15 Harris areas against 17 (fig3a) and 22 dataROIs against 42, with only 2 in ILA and 2 in ORBvl.
   - The paper's own 42-dataROI polygons are loaded in cell 62 but not used.
   - fig4e, fig5cd and fig5i rest on this coarser map and could change.
4. **[affects a conclusion]** The G2 reading (a) is applied to a retrained SOM (`category_maps`, `CODE_SORTER`).
   - Reading (a) gives category 1 to a cluster with log10FR 0.717 and category 2 to the highest-rate cluster (1.058) (cell 26). This contradicts the text's "1–3 low-rate".
   - This is what blocks 7 claims under the claims file's rule. That is the claims file's own rule, not a misreading of the paper, so I apply it.
   - Whether the code's permutation is applied in the right direction cannot be checked: on a toy input I confirmed that the cluster of memory rank r gets category [2,4,5,1,8,3,6,7][r]. Under the other plausible direction the labels change.
   - The claims file suggests projecting units onto the paper's trained Zenodo SOM as a variant; the notebook does not run it.
5. **[does not affect a conclusion]** The E-score test "P < 0.05" is two-tailed at 5% per tail, as the claims header specifies. On synthetic null data I measured a false-positive rate of 8.4%. Readers should know that significance here means a 10% two-sided test.
6. **[does not affect a conclusion]** Mixed models use a REML Wald test, not the Kenward-Roger F test (`mixed`). All p-values are far from 0.05 except setting effects, which only feed the variant.
7. **[does not affect a conclusion]** The cell 81 markdown says "references as above", but cell 82 runs only one reference. The fig5e criterion needs only one.
8. **[does not affect a conclusion]** The ww SOM has 425 nodes, not 400 (cell 26). The 8 PCA components explain 94.1% of variance, not over 95% (cell 76).
9. **[does not affect a conclusion]** extfig5g compares category medians of the node prototypes with the unit-level median log10FR (cell 48). Only two categories are above it, so "regular" and "bursty" are forced complements. The chosen regular category has lower M than the bursty one (0.018 vs 0.091).

Helpers I checked on synthetic inputs, with no defect found:
- `epoch_metrics` matches a direct calculation (maximum error 3e-8).
- `escore` recovers a planted enrichment (E = 12.9, P = 0).
- `stability` and `coincidence` behave as expected.
- The clock check in cell 11 is convincing.

### C. What I could not check, and which output would settle it

- **Sleep-like detection.** A per-probe table of sleep-like fraction against the number of cortical units and their mean rate, plus an EMG or LFP check of a few detected periods (the Methods say every period was reviewed visually), would show whether problem 1 is the detector or the data.
- **fig1h counts under the Unit-QC reading.** Counts of ww, nw and unclassified units for 001260 + 000473 under "12 spontaneous epochs, ≥5 or ≥6 spikes", with and without the Zenodo quality flags, would decide the counts.
- **G2 numbering.** E-scores using categories from the paper's trained ww SOM on Zenodo (units projected onto it) would settle the 7 blocked claims. So would the code's `relabel_clusters.py` lines that apply `label_sorter`.
- **fig4g-pl-orbl-extremes hierarchy ranks.** The Gao table's highest scores are ROIs [5, 24, 3, 2], not 19, 20 and 41 (cell 74). The ranks of 19, 20, 41 and 23 among the 29 analysed GaoROIs, and their unit counts, would show whether the IDs are right.
- **Map claims (fig4e, fig5cd, fig5i).** These analyses run on all of dataset KI, and on the paper's 42 Zenodo dataROI polygons, would show whether the outcomes survive a parcellation like the paper's.
- **fig2j.** The outcome for a region threshold that leaves about 9 regions would show whether the result depends on using 21.
- **IBL claims (6).** I confirmed on the archive that 001260 holds only the 74 KI files, with no IBL data. They can only be tested from the public IBL Brain Wide Map release, which this attempt did not try.
