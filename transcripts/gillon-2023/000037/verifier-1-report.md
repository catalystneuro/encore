**A. Outcomes** (35 claims in the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| table1-subjects | reproduced | All 13 subjects are present and sex and genotype agree for every one, 0 disagreements (cell 17). The files record no date of birth or plane; these are listed, not counted. |
| cohorts-by-plane | reproduced | 3/3/4/3 mice per group, each with at least 3 sessions (cell 19). |
| sex-split | reproduced | 7 male, 6 female, and 1 female L2/3-D mouse (cell 21). |
| sessions-total | reproduced | 50 session ids in 13 subject folders, each file in its subject's folder (cell 23). |
| table2-sessions | not_reproduced | 43 of 50 sessions agree in every recorded field, below the 45 needed for partial (cell 25). The 4 date mismatches are real in the deposited data: the archive metadata gives `startDate` 2018-10-19T00:18:29-07:00 for 765427689, and the paper's Table 2 gives 20181018. 433414's depth is 60 µm in the files and 75 in Table 2 (paper text checked). Reading the file clock as UTC gives 47, which would be partial, but the criterion has no such reading. |
| qc-failures | blocked (metadata_insufficient) | No QC field in the files (cell 27). The archive's dandiset description points to the external metadata repository for QC. The "more than three sessions" part can be tested from the archive: 5 animals (cell 27). |
| session-schedule | reproduced | Under (i)(b), 13 of 13 mice have spans of 3–6 inclusive days and no shared dates, whether dates are read as stated in the file or with the clock read as UTC. Durations are 70.06–70.53 min (cell 29). |
| imaging-depths | reproduced | 50 of 50 within the allowed values (L2/3-D 50/60/75 µm) (cell 31). |
| acquisition-rates | reproduced | Imaging 30.08–30.15 Hz, running 59.95 Hz, frames 512×512 in all 50 sessions (cell 33). |
| roi-noise-rejection | reproduced | 0 of 19115 ROIs have either property (cell 35). |
| roi-count-ranges | reproduced | Reading (a): somata 15–224, dendrites 159–1636, exact (cell 37). |
| tracked-roi-totals | reproduced | Totals are 254/261/516/129 for the 11 mice. Under reading (a) the percentages run from 32.9% to 75.0%, within tolerance (cell 39). |
| tracked-sessions-overlap | reproduced | 13 of 13 mice: equal counts, each index once per session, same index sets (cell 41). |
| fig8a-final-matches | reproduced | 136 tracked ROIs in each of 413663's three sessions (cell 43). |
| fig8a-conflicts | reproduced | Union 140 − 136 = 4 (cell 45). |
| fig8b-final-matches | reproduced | 47 tracked ROIs in each of 411771's sessions (cell 43). |
| fig8b-conflicts | reproduced | Union 49 − 47 = 2 (cell 45). |
| fig8-somata-less-order-dependent | blocked (data_missing) | Only 2 of 13 mice have `match_perm_examples` in the repository (cell 45). The NWB files hold only the final `tracking_id`, so nothing in the archive helps. The examples' ranges are 3 (2.2%) for the dendritic mouse and 1 (2.1%) for the somatic mouse. |
| gabor-sequence-structure | partially_reproduced | Order, 30 patches, A–D orientations {0,45,90,135}, U orientations {90,…,225}, and U = mean + 90 all hold in 50/50 sessions. But 13 of 340000 images in 4 sessions fall outside 300 ms ± 10% (maximum 0.604 s), and the criterion requires every image in every session (cell 47). The criterion defines no partial outcome; strictly read, this is not_reproduced. |
| visual-flow-structure | reproduced | 105 squares, flipped proportion 0.25, two contiguous direction periods in 50/50 sessions, reversals 1.99–4.01 s (cell 49). Size and speed in degrees are not recorded and are listed as untestable, as the criterion says. |
| session-stimulus-durations | reproduced | 50 of 50: Gabor 34.03–34.31 min, flow 17.01–17.04 min per direction, grey 29.98–30.04 s (cell 51). |
| inconsistent-fractions | reproduced | Means 6.96% (Gabor) and 4.68% (flow), both within tolerance (cell 53). |
| inconsistent-blocks | reproduced | Reading (b): Gabor 31.5 and flow 32.3 blocks per session, and 100% of blocks have durations in range (cell 55). |
| fig5-example-responses | blocked (methods_underspecified) | Robust-scaled readings give a partial (2/4 planes), b partial (3/4), c not reproduced (1/4). Unscaled gives partial, reproduced, partial. The readings disagree, which the criterion says makes the claim methods_underspecified (cell 57). No chance level is stated in the paper. |
| fig5-consistent-vs-inconsistent | partially_reproduced | Scaled: 2/4 planes clear under (a), 3/4 under (b). Unscaled: 2/4 and 2/4 (cell 59). Both readings give "partial", so they agree. The notebook blocks this claim only because it depends on fig5-example-responses; this claim's own criterion is fully specified (problem 1). |
| fig6-behaviour-all-mice | reproduced | 33 of 33 sessions from 11 mice have finite running (cm/s) and pupil (mm) series (cell 61). |
| fig7a-snr-above-1 | reproduced | All readings hold: lowest SNR is 2.163 over 10736 ROIs (cell 63). This is guaranteed by how SNR is defined, though (problem 4). |
| fig7a-snr-stable | blocked (methods_underspecified) | Notch reading: 2/4 planes stable. IQR reading: 4/4. The readings disagree (cell 65). |
| fig7b-signal-stable | blocked (methods_underspecified) | Notch reading: 1/4. IQR reading: 4/4. The readings disagree (cell 65). |
| fig7c-correlations-similar | blocked (methods_underspecified) | Threshold 0.05: 1/6 comparisons similar. Threshold 0.1: 6/6 (cell 67). |
| fig7c-high-correlation-fraction | not_reproduced | 0.0178% pooled (134 of 752101 pairs, identical to the repository's source data), 0.0176% mean of sessions, and per session 0.021/0.028/0.004%. Every reading falls outside 0.005–0.015% (cell 67). The notebook blocks this claim by dependency only (problem 2). |
| fig7a-source-link | reproduced | 33 of 33 sessions have the same ROI counts as the source data, and 100% of ROIs agree within 1% (largest relative difference 3e-5) (cell 69). |
| fig9-onset-offset-transients | reproduced | 12 of 12 groups show a transient at onset and at offset under every reading, k and scaling; the weakest is 2.09 SEM (cell 71). |
| file-sizes | reproduced | All four values are within tolerance in both decimal and binary units, and 50 of 50 sessions have all three versions (cell 73). |
| download-33-files | reproduced | 33 files, 14.82 GB decimal (13.8 GB binary), within 15 ± 1.5 (cell 73). |

**B. Problems**

1. [affects a conclusion] Cells 0 and 59, fig5-consistent-vs-inconsistent: the claim is marked blocked only because of `depends_on`. The ambiguity that blocks fig5-example-responses is which Gabor panel enters that claim's rule; this claim's own readings (a) and (b) are fully defined and both come out partial. One caveat: if "at least two planes under both" means planes where both readings hold at once, only L5-D qualifies, and the outcome would be not_reproduced.
2. [affects a conclusion] Cells 0 and 67, fig7c-high-correlation-fraction: also blocked only by dependency. The fraction does not depend on how "similar" is read, and every reading of the denominator is outside tolerance.
3. [affects a conclusion] Cells 6 and 25, table2-sessions: the `date_if_utc` variant drops the file's stated -07:00 offset and re-reads the clock as UTC. That is the author's own reading, not one in the criterion. It may well be correct (00:18 local imaging is implausible), but the deposited value disagrees with Table 2. Also, `start` is truncated to 25 characters in the printout, which hides the offset. Separately, the depth disagreement for 433414 (60 µm vs 75) holds under any reading.
4. [does not affect a conclusion] `calculate_snr`, fig7a-snr-above-1: my synthetic test gives SNR 2.07 for pure Gaussian noise and 1.06 only when the median is −1. So "SNR > 1" can only fail if an ROI's median dF/F is negative, and the result says nothing about recording quality. The claims file notes this; the outcome follows its criterion.
5. [affects a conclusion] Cell 47, gabor-sequence-structure: 4 sessions (759189643, 759666166, 759872185, 760269100; three of them from 411400's failed-QC sessions) contain over-long images. The criterion's "every session" rule makes the outcome partial at best.
6. [does not affect a conclusion] Cell 27: the QC search looks only at trial-table columns and subject fields, not at other NWB `general` fields (notes, descriptions). The archive's dandiset description confirms QC is kept externally.
7. [does not affect a conclusion] Cell 12: the clock check does not establish alignment in 777496949 (418779 session 1, 15 ROIs, rank 0.054), which is one of the analysed sessions. Fig. 9 still shows its onset at 4.07 SEM.
8. [does not affect a conclusion] Cell 0: the notebook says Supplementary Table 1 agrees with the paper's Tables 1 and 2 "checked while preparing this entry, not run here". I spot-checked 765427689, 777496949 and 826187862–827833392 against the paper text and they agree.
9. [does not affect a conclusion] `process_session` cell 71: `trans_scaled[:, sel]` would fail if `windows` dropped any transition. It ran, so none were dropped, but nothing asserts it.
10. I found no misreadings of the paper in the claims file.

The helpers I tested on synthetic inputs behave as documented: `rolling_mean` (last axis only), `robust_scale`, `windows` (edge drops), Pearson via a normalised dot product (differs from `corrcoef` by 1.5e-7), `select_gabor_rois` and `select_flow_rois` (recover the planted ROIs), `grey_transitions` and `flow_onsets`. The SNR port matches the source data to 1e-9 in cell 69.

**C. What I could not check**

- The ROI selection for fig5, beyond synthetic tests. Per-ROI selection masks, and the 75th-percentile thresholds for each mouse and session, would allow a comparison against the code's Fig. 5 source data (`panel_*.json`).
- The truncated outputs of the session table in cell 6 and of cells 47 and 49. My reading was limited by the 6000-character cut-off in my own dump; the summary lines were complete.
- Whether the file's -07:00 offset is a labelling error. An output of the NWB `session_start_time` string next to the stimulus or 2p timestamps' wall-clock time, or the raw value of the Allen `imaging_UTC_date_time`, would settle it.
- Whether NWB `general/notes` or the description fields hold QC text. A dump of every `general/*` field for one failed-QC session (e.g. 759666166) would show it.
