The file is ready for an attempt (`ready: true`). Only `claims/001968/10.1038-s41593-026-02260-w.yaml` changed, and nothing is committed.

**Checker:** `claims/001968/10.1038-s41593-026-02260-w.yaml: 43 claims, 41 quotes, 90 statistical values, 0 problems` (it read 42 claims and 0 problems before my edits).

**Changes, by claim:**
- **Header:**
  - **Response threshold:** I removed the P < 0.01 reading. Supplementary Table 1 gives p < 0.05, and the 0.01 in Fig. 2b is just the example cell's result. The window for classing a cell is now the odor period, as Extended Data Fig. 5, Supplementary Fig. 3 and the table say.
  - **Photometry windows:** these now come from the paper itself: 1 to 4 s for comparing strains, 2 to 4 s for testing against the precue period.
  - **How readings combine:** I added a paragraph on this. Before, a claim passed if any one combination of open method details worked. The protocol requires those readings to agree, and blocks the claim as `methods_underspecified` when they don't. Readings of what a reported number counts can still match under any one of them.
- **ed5-more-odor-a-cells:** the chi-squared p (5.5e-4) was recorded as covering T1, T3 and T5, but it is T1 only. I split it into three entries with the paper's chi2 and p values, and added the Odor-A post hoc p at T1 and T3.
- **Criteria that were looser than the paper ("at least n of m"):** fig2i, ed9 (also added the T1b p), fig6h and fig6i now require every timepoint the paper states. Missing ones give a partial result.
- **ed8-t1-a1-decrease:** the APP-KI half of the statement is now tested.
- **ed7-decoding-correct-error:** I removed three things the paper doesn't give. The linear kernel is now a recorded standard choice, and the normalization is left open. The "within 10 points of chance" rule is dropped.
- **ed1-abeta-onset:** I replaced an invented Spearman test with the paper's ANOVA and Tukey test, and added the SNc ANOVA. The paper has no test for the onset ages, so they are reported only.
- **fig4f-error-sessions-no-difference:** the criterion required no strain main effect, which the paper's own table fails (p = 0.047 and 0.0061). It now tests what the paper's "NS" rests on: the interaction and the Tukey comparisons.
- **figs7-odor1-specific-decrease:** I dropped a rank-order pairing reading that nothing in the paper supports.
- **fig4b, fig4c, fig4d, figs6d:** windows are now set as above. fig4c gets readings for the unstated 39% denominator, and the window in figs6d is no longer fixed by the claims writer.
- **fig2k-per-mouse-distance:** the FDR family now follows Supplementary Table 1 (T1, T3, T5) and adds correction across the six odor pairs as a reading.
- **ed10-th-cells-spared:** added the strain main effects.
- **fig6k-ps19-ldopa-rescue:** added the Fig. 6l t-test.
- **fig2g, fig2f:** criteria now use the readings rule.
- **New claim, figs9b-odor2-stimulation-impairs-wt:** Supplementary Fig. 9b reports this finding with its own tests, and nothing covered it.

**Still open:**
- I couldn't render the supplement PDF here (no PDF tools installed). I checked which group each shuffle threshold in Supplementary Table 1 belongs to from the text order only; it agrees with the file.
- I didn't re-read the lab's code page. I took the writer's account that the code doesn't cover this paper's analyses.
- Mouse counts conflict within the paper for figs9a, figs11 and the new figs9b claim. I left them as the paper prints them.
