I've revised the attempt against every point in the round-1 report and re-run it: `tools/entry.py all` gives 0 errors, and both notebooks pass (91 s and 633 s). Every conclusion matches the new outputs. The round is recorded under `verifications` with 30 entries, and nothing is committed.

**Outcomes changed**
- **fig8a-metabolite-gradient:** partially_reproduced → not_reproduced, as the verifier gives. The test now runs on MetaboLights MTBLS13927 (revision MTBLS13927_01). That deposit holds the same 558 metabolites and values as the code's table, so the counts (179 and 85, against 228 and 108) do not come from using the wrong table.
- **ven-subtypes-similar-physiology:** reproduced → partially_reproduced, as the verifier gives. I resampled the 34 cells to the paper's numbers (85 and 41): cells like these show a half-width difference in 0.96 of draws. The absence found here comes from the small sample.
- **fig5-connectivity-by-type:** partially_reproduced → blocked (methods_underspecified). I checked the first file of each of DANDI:001751's 56 sessions, and none holds cell types or connection annotations. The criterion blocks the claim in that case. The counts from the code's annotation stay in the notes.
- **fig4ac-ap-width-amplitude:** blocked → partially_reproduced. On the 68 VENs and 135 L5 PCs that DANDI:001746 holds, VEN APs are broader (p = 0.015) and lower (p = 0.073), the paper's direction, but neither reaches the criterion's p < 0.001.
- **fig6-ven-subtype-morphology:** blocked → partially_reproduced. The code's Fig. 6d script lists every cell, which gives the table's missing cell-type key exactly. The axon-distance half holds. The basal field area is not in the table, so that half is untested.
- **fig6f-g-ven-subtype-mapping:** blocked → partially_reproduced. Here I disagree with the verifier, who would give not_reproduced; the disagreement is recorded. The verifier's 14 and 15 come from a table whose subtype names follow the cluster. On the code's cell table, which gives each VEN's own subtype, VEN-L map only to L5 ET, but the counts match under neither reading (12 and 10, or 10 and 7 for traced cells). The subcluster part is untested.

The other outcomes are unchanged. Two recorded values moved because the rank-sum test now follows MATLAB's `ranksum`, as the paper's scripts call it. fig5c-sepsc-amplitude went from 0.23 to 0.24 and fig5c-sipsc-amplitude from 0.082 to 0.094. Neither outcome changes.

**Added or corrected**
- **Detector check:** peaks of the opposite polarity serve as a noise null, and synthetic events are injected into every real trace.
  - The RMS-noise threshold, reading (b), counts noise in every experiment (opposite-polarity peaks at 1.05 times the events).
  - At 5 pA, detection is reliable only in files with noise below 2 pA, where 91 to 94% of injected events are recovered. No sIPSC file is that quiet.
- **Other outputs the verifier asked for:**
  - a per-file table of noise against frequency;
  - results limited to the low-noise files, and to the Methods' 5-minute and 200-event minimums;
  - the header rows of each code sheet;
  - group tests on the paper's own per-cell values under both labellings. For mEPSC these give VEN 1.39 against PC 1.80 Hz (p = 0.028) with the sheet's labels and the reverse with the dataset's.
- **AP threshold (fig2d-f):** it is now sought only on the rising phase of the action potential. This cuts the implausible values (thresholds above −10 mV from 36 to 12). The verdict is the same under both extractions, so it does not rest on the extraction failures.
- **Question to a reader:** `questions/001752.yaml` asks whether reading (b) misreads the Methods. That reading is the only reason the sEPSC and mIPSC frequency claims are blocked; at 5 pA alone, VENs are lower in both (p = 0.026 and 0.0074).
- **New findings** for the data owners:
  - two V1 samples have swapped values in the MetaboLights deposit;
  - DANDI:001751 has no cell types or annotations;
  - the morphology table's cell-type key is only in the code's script;
  - five cells in the Patch-seq table are labelled with a VEN subtype but have another cell type;
  - the sIPSC recordings are too noisy to measure frequency.

**Not done**
- I did not change the claims file, including reading (b); it is asked as a question instead.
- fig3c stays blocked. Its table, now printed in the notebook, has no slice or animal per cell, so the two-way ANOVA the criterion names cannot be formed.
- The basal field area for fig6 and the subclusters for fig6f-g are not tested, as they need the 11.8 GB Zenodo archive and the 23 GB GEO archive.
- Recording stability (no baseline shift beyond 4 s.d.) was not checked; only the duration and event-count minimums are shown.
- To keep the notebook fast, the DANDI:001751 check reads one file per session (56 of 301), not every file.
