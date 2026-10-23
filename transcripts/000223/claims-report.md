I wrote `claims/000223/10.1088-1741-2552-ac8765.yaml`. The quote checker passes: 13 claims, 10 quotes, 3 statistical values, 0 problems. Nothing is committed.

**Text read.** The accepted author manuscript in PubMed Central (PMC7613561), which is not the version of record. It includes the full text, Methods, figure legends, Table 1 and the one supplement (three figure supplements of Figure 1). Nothing was missing. I also read the linked code, `starquakes/mea_spineca_mapping` at commit 99c2a47: a helper module and three analysis notebooks plus an NWB-export notebook, with no saved numeric outputs.

**Claims.**
- **Count:** 13 claims, all of them findings.
- **Quotes:** 10 have quotes. The other 3 (per-spine best-R values, per-recording optimal thresholds and F-scores, per-recording network measures) have numbers only in Table 1, so they carry an `inferred` note.
- **Statistics:** 3 claims have them: the Mann-Whitney U = 12.0 (P < 0.05), and the two Spearman correlations of spike contrast and OUT/IN ratio with maximum F-score.
- **Criteria:** all 13 have one.
- **Data:** every claim uses the dataset alone.

**Readings settled by recomputing from Table 1**
- **Mean max F-score and units per recording:** 0.692 ± 0.136 and 102 ± 43 come out over 19 recordings (the two-spine recording counted once), with the population SD.
- **Spearman correlations:** the reported values come out over the 20 spine rows (the two-spine recording counted twice). Over 19 recordings they are −0.742 and 0.680. Both readings are run.
- **Accepted against rejected best-R:** the ± values are population SDs, and U = 12 is the smaller U. The two-sided p is 0.005, so a one- or two-sided test both give P < 0.05.
- **Quantile grid:** the code's 100-point grid gives exactly the quantiles printed in Table 1.

**Details the paper leaves open, with the readings named**
- **Burst threshold percentile:** "visually chosen for each data set" and not reported. Readings are the 96th to 99th percentiles, chosen per recording, with the code's default (97th) also shown.
- **Hyperactive-unit exclusion:** the Methods give two strategies, a 99.75th-percentile rate cut (the code's default) or a 15 Hz cut. Both are run.
- **Background region for the noise estimate:** the paper says only "close to the spine". If the dataset doesn't hold this region, at least three placements are fixed before analysis. If they disagree, the claim is blocked as methods underspecified.
- **Quantiles for the acceptance test:** Table 1's values, or the optimal ones re-derived from the F-score grid.
- **Spike contrast and OUT/IN:** which units enter (all sorted, or those left after excluding hyperactive units). For OUT/IN, burst periods with or without the 0.1 s / 0.5 s extensions. The time span, whole recording or imaging span.
- **Example recording of Figure 1(e):** not identified, so the claim holds if any spine shows it.
- **Random seeds:** a standard choice. Table 1 rows 3 and 18 sit near a threshold, so their accept/reject decisions are also reported over five seeds.

**Where the Methods and code disagree** (the Methods are the main reading, the code a variant):
- **Burst-edge smoothing:** the Methods smooth over 5 points; the code uses a lowess fraction of 0.0002.
- **Misidentified surrogate in the F-score test:** the Methods count it FP or TN; the code counts it FN.
- **Release probabilities:** a fresh draw per the Methods, or the stored draw in `log_release_Pr.npy`.
- **Spike retention:** the code keeps a fixed number of spikes; a Bernoulli draw per spike is the other reading of the Methods' wording.

**Missing from the paper.** There is no map from Table 1 rows to dataset files; culture ID and unit count are the only keys. The background region for the noise estimate is never specified.
