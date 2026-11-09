**A. Outcomes** (17 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| fig1-ttype-coverage | blocked (data_missing) | The DANDI API lists 185 assets for this version, all `*_icephys.nwb` (1.66 GB), all from the 34 °C cohort. The room-temperature cells, sequencing and morphologies are not in 000035. |
| fig2-rrr-prediction | blocked (data_missing) | Same reason. No gene expression in the dandiset. |
| ed5-rrr-ion-channels | blocked (data_missing) | Same reason. |
| fig3d-families-separate | blocked (data_missing) | The room-temperature cohort is not in 000035. Cell 13 runs the same kNN on the 34 °C cells, but that belongs to ed6-it-et-overlap. |
| fig3d-morphology-combined | blocked (data_missing) | No morphologies in the dandiset (the Methods say morphologies were not recovered at 34 °C). |
| fig4c-distance-correlation | blocked (data_missing) | Needs room-temperature cells and 10x reference expression. |
| fig4d-it-depth | blocked (data_missing) | Needs room-temperature IT cells and expression. |
| fig5a-ttypes-between-families | blocked (data_missing) | Needs room-temperature cells across all families. |
| fig5b-ttype-variability | blocked (data_missing) | Same reason. |
| ed6-cohort | reproduced | Cell 9: all 11 exact counts match (185, 8, 7, 1, 177, 110/43/12/10/2, 175). 185 cells with all 17 features against 184 is within 18.4. The counts are read from labels stored in the files, so this checks consistency, not independent derivation. |
| ed6-stimulus-protocol | partially_reproduced | Cell 11: 174 of 185 cells conform (94.1%, ≥90%). Nine cells from mouse UEQOU go above 1,380 pA (up to 1,580), and two start at −180 or −100 pA. |
| ed6-it-et-overlap | reproduced | Cell 13: 58.3% of ET cells are classified as IT, above the 25% threshold. IT as ET is 0%. The paper states no chance level; the notebook's reference is an IT share of 0.78 among IT+ET. Caveat: the class-balanced logistic regression separates L5 IT from ET at balanced accuracy 0.83 (permutation p = 0.005, cell 15c). So the overlap is partial and the kNN number is driven partly by the 43:12 imbalance. |
| ed6-it-et-ap-threshold | reproduced | Cell 18: AP threshold ranks 2 of 17, p = 3.5e-4. The paper's own 34 °C code (physiological-temperature.ipynb, cell 22 output) gives the same top two features: input resistance, then AP threshold. |
| link-cells | reproduced | Cell 20: 185/185 cells match. Layer, soma depth and mouse agree 100%. Literal t-type agreement is 93.5% because the files say "L5 PT_k" where the table says "L5 ET_k". The mapping is one-to-one (crosstab), and after renaming agreement is 100%. The claims file itself treats PT as ET. |
| link-features | reproduced | Cell 22: 16/17 features have Spearman ≥0.9 and all 17 have ≥0.8 (lowest is AP CV at 0.877). Criterion met. |
| ed6-sst-temperature | reproduced | Cell 26: the two largest absolute shifts are AP width (−1.78 SD) and AP amplitude (−1.66 SD). Spearman is positive for all six features, median 0.93, over 7 t-types. Cell selection matches the paper's code: 147 room-temperature cells (143 after removing Sst Chodl) and 101 at 34 °C. The result is unchanged with the published 34 °C features (cell 27). |
| ed6-sst-transcriptomic-distance | blocked (too_large / data_missing) | Archive check: no expression data in 000035. The paper's code (cell 19) takes RNA distances from the 10x_cells_v2_AIBS reference. That file is gitignored in mini-atlas and held at NeMO. The electrophysiological half could have been computed from the dandiset: Euclidean distances between the mean standardized 17-feature vectors of the 9 L5 Sst t-types with ≥5 cells, excluding Chodl. A proxy RNA distance from the 34 °C Patch-seq counts in mini-atlas (2.6 MB) was also feasible, though it differs from the paper's method. Neither was done. |

**B. Problems**

1. [does not affect a conclusion] Cells 13 and 18 use all 185 cells. The paper excluded 20200406_sample_4 (an L5 IT cell from WPOGH, threshold about −33.6 mV) as lacking good electrophysiology, so the kNN and the Mann-Whitney test run on 43 IT cells against the paper's 42. Removing this cell would, if anything, strengthen the threshold difference.
2. [does not affect a conclusion] Cell 15(b): with k = 10, `> k_bal / 2` sends 5:5 ties to "ET". This inflates IT-as-ET (47.5%) and deflates ET-as-IT (4.1%), so the balanced variant cannot be read as symmetric. An odd k would fix it.
3. [does not affect a conclusion] Confounding by mouse is not addressed in ed6-it-et-overlap or ed6-it-et-ap-threshold. All ET cells come from two mice (MITSU 3, UEQOU 9). UEQOU is the Pvalb-Cre mouse; it has a different stimulus ladder and the lowest feature agreement with the paper (0.895 of values within 10%). Inside UEQOU, the threshold gap is smaller (−31.8 vs −29.3 mV, cell 18), and 6/9 of its ET cells are classified as IT against 1/3 in MITSU (cell 14). The criteria do not require a within-mouse test.
4. [does not affect a conclusion] `knn_family_confusion`: I confirmed on synthetic data that ties go to the alphabetically first label, so IT/ET ties go to ET. This works against the overlap finding, so it is conservative. Unlabelled and NP cells are encoded as "" and could win a majority, but every cell was counted (cell 13).
5. [does not affect a conclusion] Cell 11 (`protocol`) checks step duration only as (min offset − min onset) and (max offset − max onset), not per sweep. The onset and offset values are never printed. The markdown in cell 7 states 0.1 s and 0.7 s for every step without showing it.
6. [does not affect a conclusion] Cell 0 blocks ed6-sst-transcriptomic-distance as "could not be fetched within the time limit", but no cell shows a fetch attempt, and the partial test described in A was not done.
7. [does not affect a conclusion] Units: the files say volts and amperes with conversion 1, but the values are mV and pA. The notebook detects this (cell 7) and handles it correctly; `dvdt` gives V/s from mV.

Helper tests on synthetic traces (R = 100 MΩ, τ = 10 ms, Gaussian spikes) gave the right input resistance (100 MΩ), τ (10.0 ms), sag (1.0), rebound (0), spike counts and a rheobase within the bracket. `rheobase`, `family_of` (PT→ET, Car3→IT, NP, CT, L6b→None) and `layer_from_depth` (boundaries are exclusive, as in the paper's code) behaved as documented. I found no use of the published values in feature computation and no train/test leakage: the kNN excludes the query cell, and PCA is unsupervised.

**C. What I could not check**

- Feature extraction on the real traces: I had only the printed outputs. A saved per-cell CSV of the 17 computed features plus cell_id would have let me re-run the Mann-Whitney test, the kNN and the temperature analysis independently.
- Per-sweep stimulus onset and offset: printing the distribution of `step_onsets` and `step_offsets` would settle problem 5.
- Whether the overlap result survives the paper's exclusion of 20200406_sample_4, and whether it holds within mouse UEQOU alone. The confusion matrix on the 184 published cells, and an IT/ET comparison within UEQOU, would answer both.
- The ED6i electrophysiological distance matrix for the 9 L5 Sst t-types, and any record of an attempt to fetch the reference 10x data.
- Exact paper values for Extended Data Fig. 6 (for example the ED6i r and p): the text does not state them, and I did not use the figures.
