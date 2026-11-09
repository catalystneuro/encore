**Verification report: Martel et al. 2025 (DANDI:001174), round 1**

All counts below come from the claims file, which lists 23 claims. No attempt record was among my materials.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| zenodo-descriptors-link | not_reproduced | Only 86 of 313 matched cells (27.5%) have rate and amplitude within 1% (cell 12). Per cell and condition, the rate agrees in only 40.9%. Both are under the 50% bar. Cell identity does match (93.8% of centroids within 3 px, cell 11); the descriptor values do not. |
| cell-counts | reproduced | Reading (i) gives 61/129/63/37/23, all within tolerance (cell 15). Reading (ii) fails for 4 of 5 sites. But the reading (i) counts are the row counts of the paper's own Zenodo table, not counts taken from the dandiset (problem 1). |
| cells-tracked-18pct | blocked (metadata_insufficient) | The Zenodo table lists each cell only at its first occurrence, and the dandiset has no global cell IDs; the archive metadata shows no extra tables. The bound in cell 17, 0.141 to 0.281, contains 0.18 but cannot decide the claim. |
| fig1d-rate-no-change | reproduced | Under every grouping and both FDR families, q > 0.26 (cell 22). Reading D(ii) could not be run, so the result rests on D(i), the Methods' "first session" rule. |
| fig1e-ieicv-no-change | reproduced | Every reading gives q > 0.33 (cell 24). Same D(ii) caveat. |
| fig1f-amplitude-u-sma-spont-higher | reproduced | U SMA: n=44, p=0.0017, q=0.020 (family a) and 0.0068 (family b). Spontaneous median is higher (3.41 vs 3.17), and higher in all 5 sessions (cell 26). |
| fig1d-rate-m1-above-sma-u | reproduced | Both conditions give p < 1e-5, uncorrected and corrected, with the M1 median about 10× the SMA median (cell 28). |
| fig1f-amplitude-m1-above-sma-u-task | not_reproduced | Task amplitude: p=0.099 uncorrected, 0.198 corrected, though the M1 median is higher (cell 28). The paper's own Zenodo values give p=0.014 (cell 29), so the gap comes from the deposited events, which differ from the paper's. |
| fig2-q-sma-modulated-34pct | blocked (data_missing) | No TTL or trial data and no raw traces. I checked the archive's `variableMeasured` for all 45 assets: only ImagingPlane, OpticalChannel, PlaneSegmentation, ProcessingModule and OnePhotonSeries. No part can be tested from the dandiset. |
| fig2c-q-sma-direction | blocked (data_missing) | Same reason. |
| fig2-q-magnitude-no-difference | blocked (data_missing) | Same reason. |
| figs1-u-sma-direction | blocked (data_missing) | Same reason. |
| figs1-u-m1-target-onset | blocked (data_missing) | Same reason. |
| figs1-u-m1-movement-onset | blocked (data_missing) | Same reason. |
| fig3-synchronized-pairs-exist | reproduced | Every region × condition has sessions with \|Z\| > 1.96: SMA spontaneous 18 of 20, all others every session (cell 37). The chance level is 0.05; SMA task's median, 0.065, is barely above it (problem 9). |
| fig3ab-synchrony-not-distance | reproduced | Under both Pearson and Spearman there are U SMA and U M1 sessions with no significant correlation in either condition (4–5 SMA, 4 M1; cell 39). |
| fig3c-sync-no-condition-change | reproduced | SMA p=0.151 and M1 p=0.219 (cell 42). The 10-shift SMA variant gives p=0.077, near the paper's 0.07; the paper's own table gives 0.067. |
| fig4a-example-sequences-q | not_reproduced | The only 40-cell session (2022-09-15) gives 157–196 spontaneous and 176–311 task sequences across readings; with the documented dedupe, 5 and 2–5. None is within tolerance of 13/17 (cell 8). See problem 4. |
| fig4b-example-three-segments-q | not_reproduced | The Zenodo table identifies the session as 2022-12-06 (8/13/9). Here it gives 331–386 / 613–746 / 111–174, or 3–10 / 9–10 / 10–13 with the documented dedupe; 0 of 12 readings are within tolerance (cell 11). |
| fig4d-sequence-measures-vary | reproduced | All 6 readings differ across segments and sites (cell 13). The criterion is close to automatic, and the values do not match the paper's table in scale (cell 14). |
| fig4c-sequence-cells-not-clustered | blocked (methods_underspecified) | Reading (i), centroids, finds no difference (p ≥ 0.68). Reading (ii), pair distances, finds a difference under every 0.05 s reading (KS p ≤ 0.002, MW p ≤ 0.0002; cell 16). The readings disagree. |
| histology-lens-placement | blocked (other) | The histology is on Zenodo, not in the dandiset (all 45 assets are ophys NWB), and judging it needs an anatomist's reading. The notebook's reason "not_runnable" is not one of the protocol's reasons. |
| histology-gcamp-not-gabaergic | blocked (other) | Same reason. |

### B. Problems

1. **[does not affect a conclusion]** Cell 15 (cell-counts, reading (i)). The unique-cell counts are just the number of Zenodo-table rows per site, so this compares the paper's table with the paper's text. They were also used even though the link claim failed. The claims file's method C allows this, but the only count the dandiset yields by itself is reading (ii) (401 cell-occurrences), and that fails.
2. **[does not affect a conclusion]** Cells 12–13. The disagreement with the Zenodo table is never explained. Two U SMA sessions are far off: the table's rate is 20× the dandiset's for 2023-03-07 spontaneous, and 3.8× and 0.042× for the 2023-03-14 spontaneous and task files (the 20 Hz session). That could mean mislabelled conditions or truncated events. Both sessions feed fig1f-u-sma and the M1-vs-SMA tests. All 5 per-session medians agree in direction, so I judge the fig1f-u-sma conclusion safe, but this was not checked (see C).
3. **[does not affect a conclusion]** Cell 8 checks for TTL or trial data in one file only (sub-V). My archive query of all 45 assets confirms none exists.
4. **[affects a conclusion]** `sequences.detect`/`finalize`, cell 14. On the sessions it can be matched to, the port finds about 3.1× the paper's own Zenodo sequence counts, and its median repetitions (4–18) are far below the paper's (up to 120). The documented-dedupe variant finds about 0.4× the counts. Neither matches the paper's outputs anywhere. This suggests the method readings in the claims file (identify_sequences.m records no parameter values) do not include the paper's actual pipeline. The not_reproduced outcomes for fig4a and fig4b therefore reflect a method mismatch, not the data. I report this as a point about the claims file: on this evidence it could have been blocked as methods_underspecified.
5. **[does not affect a conclusion]** In `finalize`, the main count uses the "code as run" reading of double counting, in which nothing is removed. The claims file says "double counting removed as the code does." Both variants were run and neither is within tolerance. The claim that the MATLAB code fails because it writes 2 into a logical array is plausible but I could not verify it.
6. **[affects a conclusion]** Cell 16, fig4c reading (ii). Pairs are pooled over all sessions, so sessions with many sequence cells (e.g. Q 2022-12-06, U M1 2023-03-01) dominate. Field-of-view geometry differs between sessions, which confounds the comparison. A test within each session, or stratified by session, could find no difference, which would turn blocked into reproduced.
7. **[does not affect a conclusion]** Cell 16, reading (i). It compares a subset (78–91% of cells) with the set containing it, so p≈1 is nearly built in. The criterion prescribes it.
8. **[does not affect a conclusion]** Cell 34 / `binned_logical`. Each file is binned and shifted on its own rather than joined. The bin counts are 3 short of the Methods' throughout. Agreement with the paper's Jaccard table is good (r=0.95, median \|difference\| 0.009).
9. **[does not affect a conclusion]** Cell 37. Several U SMA proportions are at or below the 0.05 chance level (0, 0.026, 0.044). Synchrony "exists" only in the sense the criterion asks for.
10. **[does not affect a conclusion]** Not noted in the notebook: four sessions have more accepted cells than the paper analysed, by the Zenodo tables' cell counts. Q 2022-10-03 has 18 vs 17, Q 2022-12-01 13 vs 11, V 2023-03-09 11 vs 10, V 2023-03-16 14 vs 13.
11. **[does not affect a conclusion]** Cells 18–20. Reading D(ii) could not be run, so every Fig. 1 outcome rests on D(i).
12. **[does not affect a conclusion]** I tested the helpers on synthetic inputs. `bh` matches statsmodels. `binned_logical` smooths forward and drops the last 4 bins, as method J says. `zjaccard` matches brute-force circular shifts exactly. `descriptors` is correct. `detect` recovers a planted 3-cell sequence, and its shuffle null gives about 6% false positives on random events, frame-aligned or not.

### C. What I could not check
- Whether `PlaneSegmentation/id` (`roi_ids`, loaded but never printed) holds cross-session IDs. Printing the `roi_ids` of each file would settle cells-tracked-18pct.
- Whether U SMA 2023-03-07 and 2023-03-14 are mislabelled. Needed: fig1f-u-sma and the M1-vs-SMA tests rerun without those sessions, plus their per-cell table vs dandiset values.
- Whether the Zenodo aligned-activity record (doi:10.5281/zenodo.14976651) would allow a partial, outside-data test of the Fig. 2 classification (signed-rank test plus FDR on the paper's z-scored windows). I did not open it; listing its files and columns would decide it.
- The MATLAB and R code behaviour the helpers cite (the logical-array dedupe; whether permfun.R shifts the joined series or each part). I could not see that code.
- fig4c reading (ii) by session: KS and MW results per session, or stratified, would show whether the pooled difference survives.
- For fig4a and fig4b: sequence counts for the matched sessions under a sweep of t2 and the separation rule, against the Zenodo Fig. 4D table. That would show whether any parameter set reproduces the paper's own pipeline.
