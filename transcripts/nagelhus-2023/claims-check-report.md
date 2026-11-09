The claims file for EBRAINS:Q0FG-1X8 is ready for an attempt. I corrected 14 claims, added 2, and left 5 problems open; they are listed under `checks`. Nothing is committed.

**Checker:** `57 claims, 57 quotes, 69 statistical values, 29 problems`. Every quote matches the text word for word. All 29 problems are p-values the checker could not match because the text garbles "×10⁻ⁿ" into "3 10�". I confirmed each one by reading: 25 in the text, and 4 on PDF pages 46 and 49, which I rendered with a temporary PyMuPDF install. Page 46 holds the Supplementary Figure 7 legend, which is only an image; page 49 holds Supplementary Table 1.

**Changes, by claim**
- **fig1c-object-tuned-fraction, fig1h-cross-day-stability, figs4-object-traces:** the binomial tests were one-sided, but the Methods say every test was two-sided. Made them two-sided.
- **fig1h-cross-day-stability:** also noted that the Figure 1H y axis runs to 62 cells while its legend says 35.
- **figs4-object-traces:** also added that a cell counts when any of its fields passes, since the legend tests each field.
- **fig1g-no-experience-effect:** the criterion pooled every cell-day, but the legend says each of the 62 dots is a cell. Which day's score stands for a cell is now named as open, with three readings.
- **figs2d-traces-no-interference:** the claim said only one way of removing traces was possible; the paper does not say how. Added a second reading (trace bins set to zero).
- **fig3b-decode-presence, figs5a-decode-no-from-no-prime:** the "99th percentile of shuffles" threshold is not in the paper. Now judged against 0.5 and the mean of the session's shuffles.
- **fig3d-number-of-cells:** the rule based on the spread across subsets was made up. Replaced it with the paper's test for correlations (Pearson).
- **fig4c-each-session-decreasing:** made explicit that every session is judged under the same reading.
- **figs6-behaviour-decoders-flat:** removed a made-up "accuracy below 0.6" condition; the medians are now only reported.
- **tables1-without-bin-1:** added p = 1.50e-5, read from the table on PDF page 49.
- **fig6ab-single-cell-distance-tuning:** a tolerance of 0.013 had no stated reason; set it to the default 10%.
- **fig6d-reorganization-grows-with-cells:** the criterion allowed the peak at 400 or 500 cells; the Results say 500, so it is 500.
- **fig7-single-cell-properties:** the statement says the correlations were significant, so p < 0.05 is now required.
- **New claims:** `figs5jk-walls-no-pivot` (the walls do not act like the object, Supplementary Figure 5J and 5K) and `figs8eh-least-tuned-smaller-datasets` (Supplementary Figure 8E to 8H). These were findings with no claim.
- **Opening comment:** updated for the table read from page 49 and the Figure 1H inconsistency.

**Still open**
- **figs5ghi-fields-and-rates:** the paper reports no test for these panels. The tests in the criterion are of the paper's kinds but were chosen by the writer.
- **fig1d-field-distances:** the paper says fields cover "the entire azimuthal range". The criterion's "a field in every 45° sector" test is not from the paper.
- **fig2-fraction-changed-no-o:** the paper does not say how the paired values for its signed-rank test are matched; pairing by repetition is assumed.
- **figs5jk-walls-no-pivot:** the Methods do not describe the position decoder, so readings are named.
- **fig5b-words-more-informative:** the printed U ≥ 439 is impossible for 16 against 16 sessions (the largest possible rank sum is 392). Which samples were compared stays open.

**Ready:** yes. The final checks entry says `ready: true`.
