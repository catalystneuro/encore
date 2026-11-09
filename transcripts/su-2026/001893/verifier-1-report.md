**Verifier report, round 1: Su, Kosillo, Jung et al. 2026 against DANDI:001893 v0.260817.1647**

The claims file has 31 claims. The notebook tests 8, all from the Patch-seq experiment, and treats 23 as blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| patchseq-sample | reproduced | Cell 10: 96 cells and 28 mice in total, Cortex 27/8, Cerebellum 15/7, Spinal cord 54/13; "all counts match: True". There are no duplicates (cell 5: no shared start times or sweep digests). As the criterion asks, the inclusion rule is reported: 78 of 96 cells pass it (Cerebellum 11, Cortex 27, Spinal 40). |
| patchseq-transcriptome-link | reproduced | Cells 22–23: 64 of 96 cells have a library identifier. All 64 resolve, each has R1 and R2 files, the NeMO name matches, the MD5 sums match, and all are SMARTSeqSC nuclei. Only 64 of 96 cells have a transcriptome. |
| patchseq-ne-identity | partially_reproduced | Cell 25, among the 64 cells with a transcriptome: reading (a) Dbh detected in 60/64 (93.8%); reading (b) all four markers in 58/64 (90.6%). Both are at least 90% but neither is 100%. Reading (c) was not run. Reads were counted by an exact k-mer method of the author's, not by alignment (problem 4). |
| tau-table-link | reproduced | Cell 17: all 96 table rows match a file. Of the 82 cells with a value on both sides, 77 (94%) are within 10%, which meets the ≥90% bar; r = 0.992. |
| patchseq-ap-waveform-spinal-vs-cortex | reproduced | Cell 14, main reading: n = 35 and 24, t = −3.98, df 54.8, p = 2.0e-4. Code variant: n = 54 and 27, p = 0.0097. Both are below 0.01. |
| patchseq-ap-waveform-spinal-vs-cerebellum | reproduced (fragile) | Cell 14, main reading: n = 35 and 9, t = −2.25, df 14.7, p = 0.041. Code variant: p = 0.031. Both are below 0.05. The result rests on 8 wt/wt cells from two donors: without them p = 0.19 (problem 3). |
| patchseq-tau-cortex-vs-spinal | partially_reproduced | Cell 19, main reading (the Methods' sweep rule): 55.4 vs 42.9 ms, n = 24 and 35, p = 0.0071. That is below 0.05 with cortex longer, but not below 0.001. The code variant (frozen table) reproduces at p = 4.0e-5. |
| patchseq-tau-cortex-vs-cerebellum | partially_reproduced | Cell 19, main reading: 55.4 vs 37.1 ms, n = 24 and 10, p = 0.0025. The frozen table gives p = 3.1e-4, which would reproduce. |
| lc-definition, axon-density, axon-length-and-branching, single-neuron-primary-targets, markov-renewal-model, mapseq-consistent, dorsal-ventral-projection-targets, retrograde-dorsal-cortex-ventral-spinal | blocked (data_missing) | I checked the DANDI API: 105 assets, which are 96 `*_icephys.nwb` files plus 9 BIDS and metadata files. The only approach listed is electrophysiology. None of these claims can be tested here. |
| projection-and-expression-axes, behaviour-history-dependence, go-cue-response, ventral-respond-ignore, dorsal-switch-stay, cortex-input-switch, outcome-responses-spatial, rpe-predicts-choice-change, outcome-coefficients-cluster, frontal-axons-rpe, extracellular-waveform-spatial | blocked (data_missing) | The same archive check applies. There is no retrograde tracing, MERFISH, in vivo or photometry data in the dandiset. |
| snrnaseq-single-cluster, pseudospace-graded-genes, merfish-pseudospace-dorsal-ventral, retroseq-projection-gene-space | blocked (too_large / methods_underspecified), but the notebook's stated reason is partly wrong | The notebook says col-p9d5w39 "lists no files". The collection does list 5 child collections, and I found processed STAR counts in them (problem 5). Parts of these claims look testable. merfish-pseudospace also needs the Nardone 2024 MERFISH data. |

No chance level is stated in the paper for any selection.

### B. Problems

1. **[affects a conclusion] Both tau outcomes hinge on the bias part of the Methods' sweep rule, and the meaning of that field was never checked.**
   - In cell 19, dropping only the bias part gives p = 5.5e-4 and 5.1e-4. With all sweeps (no rule) p = 1.3e-4 and 2.0e-4. Both would reproduce.
   - In cell 12, the bias part is what removes most cells: 19 cells have no sweep within ±100 pA at all.
   - The dropped cells are not a random subset. In cell 20 their tau is much shorter: Spinal 23.1 vs 42.9 ms, Cerebellum 13.7 vs 37.1 ms.
   - `lcne.extract_cell` reads the NWB `bias_current` value as the applied holding current. It does not check that holding was actually switched on (the MIES "I-Clamp Holding Enable" setting) or that the value matches the pre-pulse baseline.
   - The paper's frozen table has values for 17 of these 19 cells, so the paper's own pipeline did not apply this exclusion.
   - Applying the rule follows the criterion, so the partial outcome stands as graded. But it rests on this unverified reading of the field.

2. **[does not affect a conclusion] Which sweeps the input resistance for the 15% bridge rule comes from is an assumption (`lcne.sweep_rule`, `cell_input_resistance`).**
   - 26 cells have no input resistance this way, so all their sweeps fail.
   - The "rin_all" reading tests the alternative. Tau is unchanged; the waveform test changes from 35 to 39 spinal cells, with the same verdicts.

3. **[does not affect a conclusion] 8 spinal cord cells from two donors (sub-1435396971, sub-1435397039) are recorded as wt/wt with C57BL6J sample names (cell 5).**
   - The Methods describe Dbh-Cre;Ai65 mice, and this cross-based labelling should not work in wt/wt mice, so the metadata conflicts with the Methods.
   - These two donors have the most extreme PC1 means (−1.53 and −1.67, cell 15).
   - Without them (cell 14), the main spinal-vs-cerebellum p is 0.19 and the code-variant spinal-vs-cortex p is 0.14.
   - The claims count all 96 cells, so the outcomes stand, but the waveform effects rest heavily on these two mice. At the mouse level, spinal vs cerebellum gives p = 0.063.
   - The PCA was not refitted after leaving them out, and their marker expression was not reported.

4. **[does not affect a conclusion] patchseq-ne-identity uses the author's own counting method (`rna.count_library`): exact 31-mer matches to gene bodies, in place of the paper's STAR alignment.**
   - The negative controls suggest off-target hits at the CPM > 0 threshold: Slc32a1 (a GABAergic marker) is "detected" in 46 of 64 cells.
   - Reading (b) sits one cell above the 90% line, and falls to 55/64 at CPM > 10.
   - Reading (a) stays at ≥90% under every threshold up to 10, so the outcome holds either way.
   - No cross-check against an aligned count was made.

5. **[affects a conclusion: the blocked status] Cell 27 lists only the top level of col-p9d5w39.**
   - I queried NeMO. The collection has 5 child collections: raw and Analysis sets for both the snRNA-seq and the retro-seq data.
   - The Analysis sets hold processed counts: 10x .h5ad and .npz files of 2.5–3.5 GB each, with cell-metrics files, and SSv4 STAR 2.7 CPM, exon and intron matrices as .Rdata.
   - With these, the nuclei count and the Gaussian-mixture silhouette part of snrnaseq-single-cluster may be testable, and possibly retroseq-projection-gene-space too.
   - The notebook's reason ("lists no files") is inaccurate. `too_large` may still apply.

6. **[does not affect a conclusion] The seal measurement gives negative values (minimum −1.84 GOhm, cell 10).** This suggests IPFX's `measure_seal` misbehaves on some cell-attached sweeps. It inflates the count failing the seal criterion (16 cells), which is only reported, not used.

7. **[does not affect a conclusion] Cell 5's donor_local_id check falls back to a count of non-missing values if the merged column is absent.** So "96 of 96" may not be a real comparison between `mapping.tsv` and `participants.tsv`.

8. **[does not affect a conclusion] Cell 22 does not verify that the 64 libraries belong to nemo:col-s96tk9a,** the collection the claim names.

I tested the waveform helpers on synthetic inputs (`infer_main_stimulus_pulse`, `detect_efel_peak_times`, `average_spike`, `compute_pc1`, `welch`) and they behave correctly. I compared `ipfx_tau` and `cell_input_resistance` with the current IPFX source (`time_constant` argument order, median peak time as the fit end, (−100, 0) pA range, mean over sweeps) and they match IPFX's LongSquareAnalysis.

### C. Could not check

- **What `bias_current` means.** A per-sweep table of `bias_current_pa` against `v_base`, plus MIES's holding-enable flag for the 19 cells with no sweep within ±100 pA, would settle problem 1.
- **Rheobase sweep choice.** The chosen sweep number and amplitude per cell under the main and code readings would show how much the rule moves it.
- **The 8 wt/wt cells.** Their marker CPMs (if they have a library), and how they were labelled, are not reported.
- **The five largest tau disagreements.** Per-cell frozen against computed tau with sweep counts for cells 1426070420, 1410668927 and the others, and the IPFX version used.
- **Sensitivity of the k-mer counts.** Comparing them with STAR counts for the same libraries, if the NeMO SSv4 processed matrices include the Patch-seq cells, would confirm the counting method.
- **Group sizes in the paper.** The paper gives no per-group n for the tau test, so I could not compare it with the frozen table's 22/46/14 or the main reading's 24/35/10.
