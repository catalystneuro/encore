I changed one outcome. I answered every point in the report and added each output the verifier asked for except the Calb1 processing parameters, which I couldn't supply. The entry was re-run from a clean environment (pass, 578 s). Round 1 is recorded under `verifications` in `attempts/001933-chen-2026-02.yaml`. Nothing is committed.

**Outcome changed**
- `fig3d-rim-binds-unphosphorylated` goes from reproduced to partially reproduced, as the verifier said. RILPL2 is found only in the p-RAB3A pulldowns, so the paired test the criterion names has no pairs and cannot score it: 3 of 4 comparisons hold. The criterion lists the imputation as a variant, so it can't decide the outcome. The notebook now decides on the paired test and shows the imputation (4 of 4) as a variant.
- The verifier agreed with the other 17 outcomes and they stay as they were.

**Added or corrected**
- **Spontaneous transient values:** The new fit (part 4b) shows the published 6F/S8C values are exactly 0.005 × the trapezoid integral ÷ the number of samples in the transient. They are not the transient mean, as the record said before. This holds to 2.2e-15 in all 15 Anxa1 mice and matches none of the 12 Calb1 mice.
  - With this measure, Anxa1 gives p = 2.747e-177, the paper's value. The per-mouse panel gives the paper's 6 of 8 (3743 and 4651 not significant) with the legend's p-values.
  - Outcomes stay as they were because the criteria fixed integrals. With this measure, `source-data-link` would score 0.556 on part 4, which would make it partially reproduced; the notes say so.
  - I corrected the `code_mismatch` finding to describe this measure.
- **Calb1 spontaneous (supp8c):** I printed p with each end of the exclusion window moved by up to 10 samples. p runs from 0.040 to 0.079 and is below 0.05 in 59 of 121 windows. The outcome stays reproduced, and the notes, summary and README now say it is fragile.
- **Fig 2B volcano table:** On the 4340 peptides with all six values, the table's Difference equals MLi-2 minus vehicle, as the samples are labelled, plus a constant (to 1.6e-06). Its p-values are close to a t-test's but not equal. The data still can't tell whether the labels or the figure's direction are swapped.
- **Fig 4D synaptosome images:**
  - I now read each image's channel order from its own metadata: 165 of 168 confirm the order. Three images give 488 nm for all channels, recorded as a new `metadata_error` finding.
  - The threshold alone gives a median of 1186 VAMP2 objects per image, near the paper's "about 1000". The size limit cuts this to 193, and 183 particles are kept after the shape limit.
  - I added a per-image table and an overlay of one image. Part B's null result is now described as weak evidence.
- I updated the notebook conclusions and summary, the README and the record notes to the new numbers. I also set the runtime to 10 minutes.

**Not done**
- The dandiset holds no further Calb1 processing parameters, and no recomputation from the raw signal matched a published Calb1 trace. The cause of the Calb1 difference stays open.
- `tools/entry.py all` stops at the check step on 8 errors, all in the earlier record `001933-chen-2026-01.yaml`. That record must stay as it was, so I ran the notebook with `tools/entry.py run`. The check reports no errors for the `-02` attempt.
- I did not rebuild a handover, because round 2 reviews the full executed notebook in `executed/001933-chen-2026/`.
