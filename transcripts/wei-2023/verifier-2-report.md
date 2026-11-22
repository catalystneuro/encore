**Verifier report, round 2: Wei et al. 2023 on DANDI:000021 (0.251116.2246)**

The claims file has 49 claims, and the attempt record has 49 outcomes: 24 reproduced, 12 partially reproduced, 12 not reproduced and 1 blocked. Fifteen of the outcomes carry `assumed: true`.

### 1. Outcomes and assumptions

**Outcomes I agree with.** I agree with every outcome except the three below. That includes the changes to fig2-fs-rs-counts, fig3a-isi-fs-rs, fig3a-rs1-excitability, fig3a-rs23-visual-responses, fig3c-fs-more-phase-locked, figs6c-fs-stronger-across-depth, fig7g, fig7h-pvalb-higher-cv and fig6cf. I also accept `not_runnable` for figs8.

**Outcomes I do not agree with:**
- **figs3b-fs-faster (partially_reproduced).** I would keep not_reproduced. The criterion defines only a reproduced outcome, and no reading puts both medians in tolerance (cell 20). The record already notes this disagreement.
- **figs5-depth-distribution (not_reproduced).** The claims file's method is the CSD computed here. Under it the Kruskal-Wallis test gives p = 0.044 under reading (c) and 0.011 under reading (a), which meets the criterion (cell 41). The outcome instead uses "the paper's layer 4 centres", and the outputs do not support that this is a per-probe CSD placement. Cell 41 shows the code's centre is 2740 µm on 8 of the 13 probes, 2460 on 4 and 2380 on 1, which looks like a fixed offset rather than a CSD sink. The paper's own labels give p = 0.36 and 0.34. I would rate it partially_reproduced (inconclusive), as in round 1.
- **fig7e-pvalb-sst-one-channel (not_reproduced).** This rests on one tagged set, isolation (c)/(a) with the per-unit exclusions, where TPW gives p = 0.013. The claims file's isolation readings give TPW and REP both below 0.01 in every other set (cell 106): reading (b) with or without exclusions, and reading (a) without them. I would rate it partially_reproduced.

**Assumptions:**
- **Reading (c)**, reading (a) plus at least 100 spikes in the first 5-min gray screen.
  - It is stated, and the data support it: it keeps all 603 reading (a) units of the code's tables and adds only 27 (cells 8, 11).
  - It is not one of the claims file's two readings, and the record says so.
  - It drops 79 of the 566 Source Data units (cell 11).
  - It decides several outcomes. Under the claims file's reading (a):
    - fig2-fs-rs-counts would be not_reproduced.
    - fig3a-isi-fs-rs would be not_reproduced (FS 15% off).
    - fig3a-rs1-excitability would be reproduced.
    - fig3a-rs23-visual-responses, fig3c-fs-more-phase-locked and figs6d-rs3-supragranular-beta would be partially reproduced.
    - figs6c-fs-stronger-across-depth would be partially reproduced with the CSD depth.
  - Using one reading throughout is defensible, and the cells print all readings.
- **The code's layer 4 centre as "the paper's CSD placement"** is stated but weakly supported (see figs5 above). It is not the method the figs5 criterion names.
- **Tagged-unit exclusions** are stated and reasonable.
- **FS forced to K = 3** is stated. However, fig3a-fs-visual-absent rests on it and lacks `assumed: true`, unlike its sibling claims.

### 2. Sentences the outputs do not support

- **Cell 66 and record, fig3c-fs-more-phase-locked:** "Reading (a) … gives 3 to 5 significant bands." Five bands occur only with LFP (c), which cell 64 says is not a reading of the criterion. Under the criterion's readings it is 3–4 (cell 65). The outcome is unaffected.
- **Cell 75 and record, fig3c-fs-stronger-earlier:** "LFP (b) the same pattern." Under LFP (b) only high gamma is significant; low gamma has Holm p = 0.091 (cell 74).
- **Cell 87 and record, figs6d-rs3-supragranular-beta:** "Reading (a) gives a beta ratio of 1.26 with p = 0.045, still outside the tolerance." Reading (a) with low gamma p = 0.014 meets the criterion's partial clause (cell 86). The text leaves this out, unlike the parallel cells.
- **Record, fig7h-pvalb-theta-sst-later deviation:** "(22.3, 54.5, 60.7)" are the round-1 values. Cell 104 gives 19.0, 57.1 and 67.7, whose mean, 47.9, is the measured value.
- **Cell 108:** "only isolation a without exclusions is above 0.05." This holds only with the 6 ms baseline; with the 10 ms baseline p = 0.0063 (cell 106).
- **Cell 51:** "against about a third with permuted labels." On the Source Data labels the permuted accuracy is 44.5% (cell 50).
- **Cell 9 and record, source-data-units-link:** "none of the 638 units of the other 12 sessions is in the dandiset." Cell 8 searched only the 13 held wild-type sessions.
- **Summary (cell 156), cell 0 and finding 1:** "the paper's other 12 wild-type sessions belong to the Functional Connectivity set." No printed output shows the sessions' stimulus set.
- **Cell 42, record figs5, figs6c, figs6d and figs6c-granular:** "the paper's layer 4 centres" and "the paper's own CSD placement". Cell 41 shows only one constant per probe, the same on 8 of the 13 probes.
- **Finding 10:** "NaN on every channel in 6 of the 24 sessions." Cell 5 counts sessions with any NaN.
- **Summary table:** fig3a-isi-fs-rs lacks "(assumed)", though the record sets `assumed: true`.
- **Stale method text (not Result lines):** cells 94, 114 and 126 say "reading (a)", but the code uses `labels["c"]`.
- **README:** consistent with cell 5.
- **My round-1 reasons:** the record states them faithfully in its own paraphrase, with the problems attached to the right claims.

### 3. Round-1 points

**Resolved:**
- 5: `name_by_overlap` is fixed, and the reading (b) counts now sum to 373 FS and 1447 RS.
- 6: permutation and split-first baselines are added.
- 8: the tagged-unit exclusions are applied.
- 9: CV direction and both periods are printed for every tagged set.
- 10: the classifiers are now run on reading (b).
- 11: spikes go to the nearest LFP sample (helper `nearest_sample`).
- 12: LV now uses only pairs within one interval (helper `isi_stats`).
- 13: reading (b) includes the 465 noise units.
- 14: missing-value counts are printed.
- 15: the fig6g p-value discrepancy is noted.

**Partly resolved:**
- 1: reading (c) addresses the unit set, but outside the claims file.
- 2: the feature mismatch is shown to be spread over all sessions. Clustering the paper's own features gives K = 3 (cell 27), so the mismatch is what breaks fig2d. Its cause is still not diagnosed.
- 3: a per-probe table and CSD plots are added, but the replacement depth is not validated.
- 7: the unit's own spike waveform is ruled out, but the 75–93% spontaneous locking is still unexplained.

**Unchanged:** 4 (FS forced to K = 3).

**What remains that bears on a conclusion:**
- The unit set, reading (c), is outside the claims file, and outcomes flip between it and reading (a).
- The feature mismatch is undiagnosed, which affects fig2d and every FS1–FS3 claim.
- Neither depth source is reliable, and figs5 and the figs6 claims are decided on one of them.
- FS1–FS3 rest on the forced K = 3.
- Spontaneous phase-locking is unexplained, which affects figs7's theta percentages. RS percentages are also above the paper's tolerance (cell 65).
- **New:** 9 of the 10 Pvalb units in the main tagged set come from one session (797828357), and the 5 Sst units from two sessions (cell 98). fig7g and fig7h therefore rest essentially on one Pvalb mouse.
- **New:** fig7h-pvalb-higher-cv passes only on within-presentation CV. Its Sst median there (1.025) is far from the Source Data median (1.624). Block CV, which matches the Source Data better (Spearman 0.848, cell 56), gives p = 0.31 (cell 102).

### 4. Critical findings

No finding in the attempt record is rated `critical`. I agree with that. Findings 1 (sessions missing) and 10 (CCF coordinates NaN, or y equal to z) are rightly `major`.
