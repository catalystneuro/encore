No outcome changed. The round-1 verifier agreed with all 32 outcomes: 27 reproduced, 1 not reproduced (`ed1-monkey-d-no-change`) and 4 blocked. I re-ran the entry with `python tools/entry.py all entries/001773-fujimoto-2026`: it passed in 41 s, `check` reports 0 errors, and every number in the conclusions is the same as before.

**Outputs the verifier asked for, now in the notebook:**
- **`ed1-monkey-d-no-change`:** the notebook now prints the FigE1 script's row selection. Its ANOVA uses only group 1 (monkeys N and T); monkey D's rows (group 2) appear only in the plotted means. So the paper never tested monkey D, and the outcome stays not reproduced under the claims file's test. The notes say this.
- **`fig4c-network-sorted-reduction`:** a new section prints the Fig. 4 script's label, reordering and circular-plot lines, and every text cell of the connectome workbook. None of them assigns ROIs to networks: the only text cells are block titles, and the plot uses one colour for decreases and one for increases. The claim stays blocked (`methods_underspecified`), and the record now points to this cell.
- **`fig6c-monkey-d-cc1-no-change`:** the notebook prints the sheet's columns and the Fig6C `ttest` lines. Each of the 28 rows holds a distinct section and field, with both hemispheres' counts.
- **Seed maps (problem 3):** the data check shows one value per voxel per session (the `date` column) and prints the Fig5BCandE9 lines that load the sheet.

**Corrections:**
- **"Concatenated runs":** I removed the inference that the seed maps come from concatenated runs. The notebook, its summary, the deviations for `fig5a-pre-scc-connectivity`, `fig5b-scc-decreases` and `ed7-decreases-both-monkeys`, and a new `methods_unavailable` finding now say the maps are one per session. The paper does not say whether runs were concatenated or averaged.
- **Tukey-Kramer far tail (problem 2):** the helper's docstring, the notebook text and summary, and the `fig5b` deviation now say SciPy's P values lose accuracy below about 1e-7 (1.1 to 3 times the paper's values), not only below the 1e-11 floor. No outcome depends on such a P.
- **LIM with or without area 25 (problem 1):** I added a question to `questions/001773.yaml` asking whether the reading without area 25 should be dropped from the criteria of `fig5c-dmn-lim-cen-decrease` and `fig6e-monkey-d-no-network-reduction`. The Fig. 6e voxel counts (438 and 383) and the Fig. 5c count (821) fit only the reading with area 25. The `fig6e` cell now prints these counts. The claim is unchanged and both readings are still run. `fig6e` stays blocked either way, because with area 25 the sham-side and both-sides scopes still disagree. I also updated the `fig6e` notes and its `methods_unavailable` finding.
- **Round 1 in the record:** it is under `verifications`, with the verifier's reasons in its own words and my response for each claim.

**Not done:**
- Problems 4 and 5 (the CC1 sheet errors and the behavior legend coding) were already recorded as findings, so nothing new was needed.
- `fig5a-nonsurgical-no-reduction` and `fig6d-monkey-d-scc-local-increase` stay blocked for missing data. The ROI-level look the verifier mentions is not the criterion's test, and it would fail `fig6d` anyway.

Nothing is committed, as instructed.
