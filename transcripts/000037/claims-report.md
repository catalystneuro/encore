I wrote `claims/000037/10.1038-s41597-023-02214-y.yaml`. The quote checker passes: 35 claims, 33 quotes, 0 problems.

**Text read**
- The version of record of the Sci Data paper, full text from Europe PMC (PMC10192216): main text, Methods, Tables 1 and 2, and the figure legends. There was no PDF.
- The only supplement, Supplementary Table 1, was read from the paper's GitHub copy (`jeromelecoq/allen_openscope_metadata` @ `0e9c7ac`).
- The two other texts under `paper/` are the separate analysis papers on the same data. I did not write claims for them.

**Code read**
- `colleenjg/OpenScope_CA_Analysis` @ `046e7fe`, and its dependency `colleenjg/util` (tag `osca_mult`, commit `2b05f95`).
- The code fixes several choices the paper leaves out:
  - Figs. 5, 7 and 9 use local sessions 1–3 that passed QC: 33 sessions from 11 mice, leaving out mice 411400 and 412933.
  - Every ROI in an NWB file is used.
  - It gives the exact SNR computation.
  - Fig. 9 uses a −2 to 2 s window and scales each ROI's ΔF/F as (x − median)/(95th − 5th percentile).
  - Gabor responses use a −0.9 to 0.6 s window, and correlations are smoothed with a 4-point moving average.
  - Dendritic matches need a minimum overlap of 0.1 or 0.2.

**Counts**
- 35 claims: 34 findings and 1 link (the dataset's ROI SNRs against the repository's Fig. 7a source data).
- 33 have quotes; the 2 table claims are marked `inferred`.
- 35 have criteria and 20 have expected values.
- No statistics are recorded, because the paper says it reports none.
- 5 claims need outside data (`with_inputs`): the Fig. 8 conflict counts, the comparison of ordering effects between somata and dendrites, and the Fig. 7a link.

**Details left open, and the readings named**
- **QC failures:** the text says two animals had failed sessions, but its own Table 2 shows three (411400, 412933, 440889). Readings: any failed session, or first three sessions failed.
- **Session span ("three to six days"):** days from first to last session, or calendar days counted inclusively.
- **ROI count ranges:** taken over the 33 analysed sessions, all passing sessions, or all 50.
- **"Theoretical maximum" of trackable ROIs:** per mouse, the smallest or the mean ROI count of its three sessions, summed per plane.
- **"Approximately 30 blocks":** counted per session, per stimulus, or per stimulus and direction.
- **SNR ">1":** the group median, the 5th percentile, or every ROI. By the code's construction, SNR exceeds 1.645 whenever an ROI's median ΔF/F is at least 0.
- **"Stable over days" (Fig. 7a/b):** the boxplot notches overlap, or each median lies inside the other sessions' interquartile ranges.
- **"Very similar" correlations (Fig. 7c):** medians and 95th percentiles within 0.05 or within 0.1.
- **0.01% of pairs above 0.8:** pooled pairs, the mean of per-session fractions, or each session; and r > 0.8 or r ≥ 0.8.
- **Fig. 9 onsets:** all grey-to-stimulus transitions (text and code), or Gabor only (legend). The transient threshold is 1 or 2 SEM.
- **Fig. 5:** panel a or panel b ROI selection. The visual-flow comparison is circular because of how ROIs are selected, so it is reported, not judged.
- **File sizes:** MB and GB as decimal or binary units.

**Missing from the paper**
- The custom-modified ROI matching code is not linked. Without it, the conflict counts can only come from the repository's matching files, and "somata vary less across session orderings than dendrites" can't be tested beyond the two example mice.
- The repository's own Fig. 7c source data give 0.018% of L2/3 dendritic pairs above 0.8. That is outside the tolerance I set for the stated "approximately 0.01%". I noted this in the file's opening comment for the author; it is not a criterion.

Nothing has been committed.
