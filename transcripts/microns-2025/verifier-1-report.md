**Verifier report, round 1: doi:10.1038/s41586-025-08790-w on DANDI:000402 (0.230307.2132)**

The claims file has 36 claims: 16 on the dataset, 3 `with_inputs` and 17 `elsewhere`. The attempt record was not in my materials, so I took the count of 15 blocked `elsewhere` claims from notebook cell 0 and could not check it.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| scans-14-p75-p81 | reproduced | Cell 8: all 14 scans of Extended Data Table 1 are present, on 6 days, at ages P75–P80; each scan is 1,200 x 1,100 um with depths 80–570 um. The dataset holds 19 files. The exact mask totals in cell 12 confirm the choice of 14. |
| scan-configurations | reproduced | Cell 10: 11 / 2 / 1 scans in the three groups. The depth spans of the 11 scans are 280–420 um, all within 270–440 (reading a); the median is 420 (reading b). |
| masks-125413-somatic-115372 | reproduced | Cell 12: exactly 125,413 masks and 115,372 somatic, with 8.01% excluded. Reading (a). |
| unique-neurons-75909 | blocked (data_missing) | The dandiset has no stack coordinates. Plane `location` lists all four areas, and DANDI `variableMeasured` lists no stack. |
| area-split-half-visp | blocked (data_missing) | Cell 3: every plane's `location` is "VISp,VISrl,VISlm,VISal", so no mask carries an area. |
| z-drift-under-10um | blocked (data_missing) | The raw frames are in the dandiset, but there is no structural stack to register them into. |
| structural-stack | blocked (data_missing) | No stack among the 19 assets, and none in the asset metadata. |
| stimulus-composition | reproduced | Cell 14: all 14 scans match every count. Duration is 83.76 min (reading a) or 84 min (b). Categories split 2 / 30 / 48 per category. |
| stimulus-conserved-across-scans | partially_reproduced | Cell 16: the clips and the Monet2 seeds pass. Trippy seed 6831 (same condition hash) occurs in two scans, 6-4 and 7-5. The criterion requires each remaining seed to occur in one scan only. |
| oracle-same-order | reproduced | Cell 18: in every scan, 10 repeats of the same 6 clips with one order. The largest gap inside a repeat is 0.63 s, so no Monet2 or Trippy trial falls inside a repeat. |
| spontaneous-periods | partially_reproduced | Cell 20: every scan lies inside the widened ranges, which is the criterion's test. But the expected upper bound of the monitor-on period (5.5 ± 0.55 min) is not met: the 14 scans reach only 4.84 min. The 19 files match all four bounds (0.145, 5.54, 8.26, 21.19 min), so the paper's range was probably taken over all 19 recordings. |
| monet2-directions | partially_reproduced | Cell 25: the period is within tolerance in 560 of 560 trials (median 937.1 ms). 16 distinct directions in 556 of 560 trials by the 10° rule, or 554 of 560 after snapping to the 22.5° grid. The criterion requires every trial. The failures may be measurement error (problem 4), but that is not shown. The directions are measured from the stimulus video, a proxy; the trial table holds no per-period direction. |
| fig3f-oracle-reliability | reproduced | Cell 32: under both readings all 115,372 somatic masks are scored, the scores at the three percentiles increase, and the 99th-percentile score is above 0 (0.702 and 0.465). The score is on fluorescence, as the deconvolved traces are missing. The criterion is nearly automatic (problem 5). |
| fig3g-direction-tuning | reproduced | Cell 35: the fewest units on any direction is 5,203 under (a) and 5,113 under (b), against the 5 required. The test cannot fail (problem 6). The informative number is the split-half variant: 0.629 of units, against 0.5 expected without tuning. |
| behaviour-recorded | partially_reproduced | Cell 22: treadmill rates 57.0–100.2 Hz and eye rate about 20 Hz are within tolerance, and the treadmill covers all 14 scans. Eye and pupil data cover only 13 of 14: in scan 4-7 they end 968 s before the last frame (coverage 0.848). |
| photodiode-89pct | blocked (data_missing) | No photodiode signal in the dandiset or its asset metadata. |
| manual-coreg-19181 | blocked (other: no CAVE token) | No public copy of `coregistration_manual_v4` turned up. BossDB has only the 2021 `func_unit_em_match_release.csv`. Cell 38's variant (8,863 ROIs with an EM root id) uses only 52 of 104 fields and cannot be compared. |
| ed4-matched-higher-signal-correlation | blocked (other) | Part of it could be tested from the dandiset alone (problem 9). |
| fig6k-target-responses | blocked (other) | Needs the coregistration table. A public synapse export exists (problem 8), but the target-to-unit match still needs the coregistration table. |
| nuclei-144120 | reproduced | Cell 41: 144,120 detections, z range 14,834–27,871, which is inside subvolume 65. |
| cell-classification | reproduced | Cell 43: 89,056 neuron calls, inside 74,022–90,472 but 8.3% above 82,247 (problem 10). 69,957 well-segmented, exact. Cell 44: precision 0.955 and recall 0.996 against the column labels. |
| the 15 other `elsewhere` claims | blocked (other), not verified | I could not see the attempt record. For several of them, the stated reason (a token is needed) does not hold (problem 8). |

### B. Problems

1. **[affects a conclusion]** Cell 20, spontaneous-periods. Only the containment test is run; the four expected bounds and their tolerances are never compared. The upper monitor-on bound fails for the 14 scans. Printing the 19-file bounds would have shown that the paper's range matches all recordings.
2. **[affects a conclusion]** Cell 22, behaviour-recorded. Scan 4-7's eye data end at 5,392.9 s, against a last frame at 6,360.8 s. That fails "all 14 scans covering the imaging period".
3. **[affects a conclusion]** Cell 16, stimulus-conserved-across-scans. The repeated Trippy seed 6831 breaks the "one scan only" condition. It is probably a chance repeat of a random seed, but the criterion has no exception for that.
4. **[affects a conclusion]** `n_distinct_directions` and cells 24–25, monet2-directions.
   - The 10° merge rule is too tight for the measurement error. The largest deviation from the grid is 7° (median) and 11° (max).
   - In my synthetic test, uniform ±7° noise on a 16-direction grid gave a false "15 distinct" in 9.5% of trials, and ±11° in 83%.
   - The two measures disagree on which trials have 15 directions. Scan 9-6 seed 6154 has 15 by the 10° rule but 16 on the grid.
   - Seed 7637 in scan 5-6 gives 15 under both measures, and its 16 measured directions are never printed. So the outcome rests on an unvalidated proxy.
5. **[does not affect a conclusion]** Cell 32, fig3f.
   - Units picked at the 34th, 79th and 99th percentiles are increasing by construction, so the criterion tests almost nothing. This is a weakness of the claims file, not a misreading.
   - The score percentiles over all masks (for example 0.21 at the 34th) match the somatic-only ones, so the 10,041 artifact masks score like somata.
   - That is consistent with a shared stimulus-locked signal in raw fluorescence (neuropil, or light from the monitor), and it was not examined. An artifact-only score distribution would settle it.
6. **[does not affect a conclusion]** fig3g criterion. Taking the argmax over 16 directions on pure noise for 100,000 units gave at least 6,111 units per direction in my test, so "at least 5 per direction" cannot fail. The split-half result (0.629) and the clock check in cell 29 (peak at +0.47 s in all 104 fields) are the real evidence.
7. **[does not affect a conclusion]** `field_responses`. It uses fluorescence in place of deconvolved traces and applies no per-unit delay. All fields share one timestamp array although they are imaged one after another within a frame. All three are disclosed and cannot change the ordering-based outcomes.
8. **[affects a conclusion]** Blocked reasons. The BossDB open bucket, readable without a token, holds:
   - `functional_data/digital_twin_properties/v2/anatomy/units.csv`, with per-unit `unit_x/y/z` and `brain_area` for 13 scans (its `metadata.csv` lists no 7-4);
   - `minnie65/synapse_graph/cave_exports/v1181/` and `v1300/` synapse exports, including `connections_with_nuclei`.

   This does not unblock the dataset claims, since the claims file limits them to the dandiset. It does undercut "needs a token" for some `elsewhere` claims, such as the synapse-detection counts, outputs-94-axons and the fig7abc count.
9. **[affects a conclusion]** ed4-matched-higher-signal-correlation. Cell 38 finds 396 EM root ids in more than one scan within the dandiset's own columns. That would allow a partial test with the dataset's matches, but it was not attempted.
10. **[does not affect a conclusion]** Cell 43. The paper's 82,247 equals 69,957 + 12,290, while the release has 89,056 neuron calls. It passes on tolerance only. The excitatory/inhibitory check in cell 44 scores the model on its own training labels, which the notebook states.
11. **[does not affect a conclusion]** Cell 18. `repeats_consecutive` is true by construction, because `iloc` slices a reset index. The gap check is what supports the result.
12. **[does not affect a conclusion]** Cell 10. `fields_per_depth` is a ratio and does not show two fields at each depth. Scans 8-5 (210 and 220 um) and 9-3 (295, 305 and 315 um) could have side-to-side depth offsets.
13. **[does not affect a conclusion]** Cell 0. The listing of the NWB groups (`other_groups` in `scan_metadata`) is collected but never printed, so the absence of a stack, deconvolved traces and photodiode data is asserted without output. The DANDI metadata agrees with the assertion. Separately, cell 39's statement that the paper's matches span the whole field of view has no source.

### C. What I could not check

- **Extended Data Table 1 scan list.** It was read from an image I do not have. Printing the table cells, or citing them, would close this; the exact mask totals already corroborate it.
- **The two Monet2 trials with 15 directions.** I could not tell whether they are real. The notebook should print the 16 measured directions and the per-period shift magnitudes for seed 7637 in scan 5-6.
- **Artifact masks in Fig. 3f.** An artifact-only oracle score distribution, and the same score on a neuropil-subtracted trace, would show whether the score measures neural reliability.
- **NWB group listing.** Printing `other_groups` for one file would confirm what the dandiset lacks.
- **Eye data for scan 4-7.** Listing every EyeTracking and PupilTracking series in that file would show whether there is a second series after 5,393 s.
- **Fields per depth.** A field-by-depth table for each scan would settle problem 12.
- **The 15 blocked `elsewhere` claims.** The attempt record was not available, so I could not check each one's reason against the public BossDB exports.
- **Raster and tuning figures.** I did not look at them; the numbers above come from the text outputs.
