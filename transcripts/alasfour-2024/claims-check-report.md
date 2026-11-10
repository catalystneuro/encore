I've checked and corrected `claims/alasfour-2024.yaml`. It is ready for an attempt. Nothing is committed.

**Checker result:** `claims/alasfour-2024.yaml: 30 claims, 29 quotes, 3 statistical values, 0 problems`. Before my edits it passed with 10 statistical values; the 7 entries I removed account for the difference.

**Changes, by claim**
- **Seven claims had thresholds recorded as results:** `fig2-rois-three-bands`, `fig2-inferior-temporal-all-bands`, `fig2-beta-temporal-only`, `fig2-single-band-rois`, `fig5-gamma-higher-talking`, `fig5-theta-alpha-lower-talking` and `fig5-pre-postcentral`. Their `statistics` entries were the false discovery rate cutoff (Benjamini-Hochberg, 0.01) that decides which features count as significant or consistent. That is a method, so I removed them; the criteria still apply the test through M6 and M8.
- **table1-participants:** removed the rule that 13 of the 15 minute values were enough, which the paper doesn't give. All values must now be within tolerance.
- **fig6-sign-consistency:** the tolerance of 0.9 allowed only a count of 9, while the criterion accepted 8 to 10. I set the tolerance to 1 (10% of 9, rounded to a whole count) and wrote down the reason.
- **Header O4 (artifact rule):** the file had fixed which span "the SD of the channel" covers and called it a standard choice. That choice can change which blocks are dropped, so I named two readings: the whole recording, or that day's recording.
- **Header O10, anova-roi-band-effects, anova-no-interaction:** the paper doesn't say what the ANOVA's observations are. I named two readings: the fold accuracies, or the participant means.
  - The no-interaction claim is judged on fold accuracies with type II sums of squares, marked as resting on an assumption, with the other choices as variants.
  - I noted that reading the paper's printed "p = 0" as p < 0.001 is the file's own reading.
- **fig5-pre-postcentral:** the sign for alpha was cited to Discussion paragraph 2, which gives only theta and gamma. It is now cited to Results 3.1, paragraph 6.
- **fig7-exceeds-group:** the comparison of Figure 7 with Figure 2 was fixed one way, but the paper doesn't say which values are compared. I added a second reading: each curve against the same band in its top region.
- **Header, outside data:** the eight region names are now credited to Results 3.1 of this paper, not to Peterson et al. and the legends.

**Still open**
- **Participant numbering:** the figures name a Participant 3, who isn't in Table 1. The paper doesn't say whether the figures number the five participants 1 to 5 or use Table 1's numbers.
- **No PDF was supplied:** values shown only in figures (the chance level, per-feature accuracies and intervals, per-participant matrices, the Figure 7 curves) can't be checked. The claims rest on the text and legends.
- **Vague words:** several criteria use the file's own rules where the paper gives none, such as "generally", "regularly" and "multiple". Each criterion says so.

The paper's main findings all have claims, and no claim comes from another source.
