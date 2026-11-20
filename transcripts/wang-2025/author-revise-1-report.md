I've revised the attempt for every point in the round-1 report, re-run the entry (`python tools/entry.py all entries/wang-2025`: 0 errors, notebook passes in 42 min), and recorded round 1 under `verifications`. No outcome changed; one block reason did, on 27 claims. Nothing is committed.

**Outcomes**
- **link-authors-deposit:** reproduced, as before. The verifier agreed.
- **data-scale:** still reproduced, but on a new count; the verifier would give partially reproved. Its objection was that the 17 areas nest inside each other, which is right. I now count each unit once in its main Allen brain division, using the authors' own structure tree from their deposit, with cortex split into ALM and the rest of cortex as the claim's own list of areas does. That gives 13 structures under every filter and session set, so more than 12. The margin is one structure and depends on that split; the notes say so. The verifier's disagreement is recorded.
- **fig6e-marker-clustering:** still partially reproduced, and the verifier agreed. The main set is now the authors' 106 sessions. The session AUC is now the average of the per-fold AUCs, as the paper's Methods do for their other cross-validated measures; the pooled AUC is kept as a variant.
  - Main result: clustering score 6.83 against chance 1.03 ± 0.42, p < 0.001, with 4 nose-type and 5 jaw-type mice.
  - The paper reports 12.57 ± 1.26; all 72 variants give 3.52 to 7.91, none in tolerance.
  - Across the five seeds the score is 6.68 to 7.82.
- **The 27 blocked claims:** the reason changed from `too_large` to `data_missing`, as the verifier said. Only 34 of the authors' 106 sessions have video in any version; the other 72 have none. For the 34, reading the video alone would take about 49 h, so `too_large` stays in the notes as a second reason.

**Added or corrected**
- **Unit locations:** 92,769 of the 154,948 `unit_quality` good units have no brain-area location. The notebook and the record now say so.
- **Zenodo deposit:** every file is listed with its size. `session_latents.pkl` holds 16 images per session, not per-frame embeddings.
- **What the deposit does hold:** the authors' own per-neuron explained variances and AUCs. These are results of the paper's analysis, not data, so I don't use them; the notebook says why.
- **Google Drive embeddings:** the notebook now says these are excluded by the protocol's rule that outside data must be pinned, not by a judgment call.
- **Marker half of fig6-marker-vs-embedding-decoding:** now computed, not as an outcome. The better of jaw and nose gives a response-epoch AUC of 0.754 ± 0.006, and all three markers 0.819, both below the paper's 0.88. The claim stays blocked because it compares the markers with the embedding.
- **Smaller fixes:**
  - The docstring now says decoding runs every 20th frame, stated as an assumption.
  - Outlier cleaning no longer takes velocity across the gaps between trial videos.
  - The text on what the later version adds is corrected: raw electrophysiology in 169 files, video in 71.
  - The link claim is described as added to the claims file by this attempt.
  - The summary now gives 27 blocked claims, not 25.
- **Findings:** findings 4, 6 and 8 are updated with the new numbers; their order is unchanged and none was added. In the claims file, fig6e now has `data: with_labels` and depends on link-authors-deposit, because its main set comes from the deposit. Its statement, expected values and criterion are unchanged.
- **Housekeeping:** I added `openpyxl` to read the deposit's structure table and re-locked, and deleted `entries/wang-2025/p.out`, a stray profiler dump nothing uses.

**Not done**
- **Marker arm of fig2-ordering-across-methods:** not run. It needs every neuron's firing rate in every session and decides nothing without the other two methods. The notes say it could be computed and why it wasn't.
- **New seeds for the marker half of fig6:** it runs under the claim's seed only, since it decides no outcome.
- **Questions for a reader:** none added; the verifier found no misreading of the paper in the claims file.
