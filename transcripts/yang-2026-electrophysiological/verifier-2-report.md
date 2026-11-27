**Round 2 verification: Yang & Xiao 2026 on DANDI:000020 (attempt yang-2026-electrophysiological-01)**

The claims file and the attempt record both have 21 claims. The notebook tests all 21 and treats none as blocked.

### 1. Outcomes and assumptions

I agree with all 21 stated outcomes:
- **Reproduced (16):** fig1d, fig2b, fig2d, fig2c, fig2e, fig3a, fig3b, fig3d, fig3e, fig4a, fig4b, fig4c, fig4e, fig4f, disc-brief-gain, fig5a, fig5b and fig5d-f (fig5b, fig5d-f and the two disc/fig4f gain claims included in that count).
- **Partially reproduced (2):** fig1c and fig5c.
- **Not reproduced (1):** fig2a.

Every outcome with `assumed: true` states its assumptions, and they are reasonable. Points on specific claims:
- **fig2b, fig3b, fig4b:** The scatter and density plots are now rendered (cells 23, 38, 50), and I inspected them. Each shows one cloud with no gap. The ramp cloud has a sharp lower edge, which is an artefact of the collinear recruitment and latency features, not a separation between groups. The continuity judgement is now supported.
- **fig5b:** The outcome rests on the suprathreshold long-pulse sweeps and on Spearman's own p-value. The claims file names that test, so using it is correct. The Mantel variant, however, gives p 0.0088–0.021 for every within-tolerance combination, none below 0.001 (cell 68). The outcome is fragile, and the record says so.
- **fig5b deviations:** They list the "main long-pulse reading" assumption alongside the suprathreshold one, but the outcome does not rest on the main reading. That entry is misleading and should be removed or marked as context.
- **fig2a:** The record has `assumed: true`, but the Summary table (cell 79) says it rests on no assumption ("no (no reading matches)"). The two should agree.

### 2. Sentences the printed outputs do not support

- **Cell 33, and the fig2e notes in the record:** "Pvalb median 3.70, Vip -1.84". Cell 32 prints main-reading medians of Pvalb 2.26 and Vip -1.04 (means 2.20 and -1.06), and so does cell 23. The ordering conclusion is unaffected.
- **Cell 69, the fig5b notes and the fig5b verification response:** the Mantel p is said to be "0.0088 to 0.0111 for the 32 combinations within tolerance". Cell 68 prints 0.0088 to 0.0213: rows 259, 262, 283 and 286 give 0.0213 and 0.0209, and several others give 0.0123–0.0136. The conclusion that none reaches p < 0.001 still holds.
- **Cell 57:** "readings (a) give |r| of 0.93 to 0.99". The Pearson values in cell 56 run from 0.953 to 0.986; 0.93 is the Spearman minimum. The record's "0.95 to 0.99" is correct.
- **Cell 79, Summary table:** the fig2a "rests on an assumption: no" contradicts the record, as noted above.

Every other "**Result:**" sentence, the Summary prose, the README and the record notes match the printed outputs. That includes the counts, the 24/60/15/20-of-66 tallies, 80 of 192, 32 of 576 (16 with dV/dt), 42 settings with values 0.005–0.911, 24 of 84, the five-seed spreads, and the 13% and 16% incomplete-trace rates.

The record states my round-1 reasons faithfully and in my own words. Its additions are drawn from my section C: the per-cell table request for fig1c, and the unconfirmed Figure 4C mapping for fig4c. The fig2a reason also links problem 9, which I had rated as not affecting a conclusion; that is acceptable. The fig5b entry has `agrees: false` because I disagreed with the round-1 outcome of partially_reproduced. The record has now adopted my outcome.

### 3. Status of my round-1 points

**Resolved:**
- **Point 1:** Pairwise 11 lines are now used for brief response vs gain, giving 0.795, with 0.700 for the 8 lines shared by all three protocols as a variant.
- **Point 2:** Balanced resampling now runs on the alternative long and ramp readings: in 42 settings at most 3 of 6 medians fall within tolerance.
- **Point 4:** Thresholds, command bins, count scale and fast-response windows of 1, 2 and 5 ms are all varied. No outcome changes.
- **Point 5:** The plots are rendered.
- **Point 6:** The LP-named sweeps are included in fig5a and fig5b.
- **Point 9:** Spike counts per second were run as a variant.

**Resolved as far as the data allow:**
- **Point 7:** The shared lines are now derived from the data and match the paper's 8. The largest-lines inclusion rule is stated as an assumption.
- **Point 8:** The Mantel test was added as a variant.

**What remains that bears on a conclusion:**
- **Point 3: readings are not jointly consistent.** It is disclosed (cells 71–72), but it is not resolved. fig3a holds only with all 14 ramp features, while fig3d holds in full only with the 8 features of Figure 3D. fig5b holds only on the suprathreshold sweeps, and on those fig2d and fig2e fail and fig5a fails (r -0.08 to 0.32). No chain of readings holds more than 5 of these 8 claims. Each outcome is legitimate under the claims file's "under a reading" rule.
- **fig5b under Mantel:** the reproducing readings fail p < 0.001 under the Mantel test (above).
- **fig1c long-pulse count gap:** 3276, 1957 or 1881 cells against 2270 ± 227 is still unexplained. It may be linked to the fig2a failure (PC2 at 18.7% or more in every reading) and to which long-pulse reading fig5b needs. It is properly raised as a question for the authors.

### 4. Findings rated `critical`

**Finding 1 (duplicate recording) is the only one rated `critical`.**
- **Cell 6 shows it.** Sessions 680563483 (subject 673135474, Vip-IRES-Cre;Ai14) and 680897463 (subject 673135516, Ndnf-IRES2-dgCre;Slc32a1-IRES2-FlpO;Ai65) have identical per-sweep summaries: stimulus, amplitude to 2 decimals and peak to 4 decimals. They also share the same first-sweep fingerprint, with 2 duplicates found.
- **The exclusion is real.** Cell 8's code sets both sessions' line labels to None.
- **`critical` is the right rating.** This is one recording deposited as two sessions, under two subjects and two genotypes, and nothing in the files shows which genotype is right. An analysis that takes the files as given would count one cell twice, under two lines. Its effect on these results is negligible (one cell per line), but the rating depends on the defect, and the defect fits the definition.

The other findings are rated appropriately: finding 2 (driver line parsed from the genotype) and finding 3 (zero-padded sweeps) as `minor`.
