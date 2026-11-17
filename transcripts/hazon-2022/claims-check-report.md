I checked `claims/hazon-2022.yaml` against the paper and supplement, and spot-checked the cited code at the same commit (2057af9). I changed 11 claims and renumbered sources in 19, and I've marked the file ready.

**Checker result:** `claims/hazon-2022.yaml: 29 claims, 28 quotes, 26 statistical values, 1 problems`. The one problem is that the checker can't find the 4e-5 in `suppl11c-asymptotic-imse-vs-asymptotic-snr`. The paper prints it as "4・10-5" (Suppl. Fig. 11c), so the recorded value is correct.

**Changes, by claim:**
- **Sources (19 claims):** the Results and Discussion paragraph numbers were one or two paragraphs too high. I renumbered them to match the text, not counting figure legends. For example, Fig. 1d is Results paragraph 2, Fig. 5 is paragraph 11, and the 9.38 cm figure is in Discussion paragraph 8.
- **`suppl-table1-place-field-properties`:** which cells are averaged is now named as open. The readings are all cells, cells with more than 100 events per 10 min (Suppl. Fig. 3), and cells with minimal spatial modulation for the place-field values (Suppl. Fig. 2c and 2d).
- **`fig1d-noise-correlation-by-field-distance`:** added pooling over all pairs as a reading, because the legend counts 3,941,140 pairs, not sessions.
- **`fig3cd-signal-and-noise-growth`:** the 10% and 90% margins are now labelled as standard choices, not the paper's.
- **`fig3g-noise-slope-decreases-over-run` and `fig3h-snr-higher-at-run-end`:** the Methods limit Fig. 3g onwards to the 73 large-data sessions, while the legends say n = 110. 110 stays the main reading and 73 is now a variant.
- **`fig4b-correlations-increase-noise-signal-overlap`:** the old quote did not state the finding. I replaced it with the Suppl. Fig. 15 sentence that says correlations increased the overlap. I also added eigenvectors of the correlation matrix as a variant (Suppl. Table 2, row 2). The covariance matrix stays the main reading, from the Methods and the code (`Cloud.m` with `use_corr` false).
- **`fig5hi-nsv-predicts-noise-correlation-effect`:** corrected how the criterion describes the Results sentence. That sentence names the ratio as unmodified over shuffled, but the relation it states fits the inverse ratio.
- **`suppl-table2-nsv-best-predictor`:** the table has eleven rows, though its note says ten variables.
- **`suppl11b-i0-vs-single-cell-snr`:** the Methods define the cell SNR as a ratio of medians over bin pairs, so that is now the main reading. The code's average of per-pair ratios is a variant.
- **`suppl7b-initial-slope-lower-with-correlations`:** the legend doesn't say which I0 is lower. The statement and rule now test only the significant difference, with the sign reported.
- **`suppl6-twenty-bins-near-optimal`:** the one-SEM margin is now labelled as a standard choice.

**Still open:**
- The code citations I spot-checked agree with the criteria. I did not re-read every live-script output the criteria quote.
- The paper contradicts itself in two places, and the criteria already name both readings:
  - **Fig. 3f:** the legend says the signal slope decreases, but the code tests the reverse direction.
  - **Fig. 4c:** the legend gives Pearson 0.81, while the Results call the correlation inverse.

Every main finding has a claim, and every claim comes from this paper. A `checks` entry dated 2026-11-11 records these changes. Nothing was committed or pushed.
