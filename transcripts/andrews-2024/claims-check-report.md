I've checked the claims file against the paper and corrected it. It is ready for an attempt. Nothing is committed.

**Checker result:** `claims/andrews-2024.yaml: 29 claims, 29 quotes, 51 statistical values, 1 problems`. The one problem is the cluster 10 p-value (3.634e-04). The checker can't match that form, but ST5 and the Fig. 5 legend both print it, so it is correct.

**Changes, by claim:**
- **fig3a-spontaneous-reduction:** the statement said firing "recovers after light-OFF". The paper doesn't say that, and in ST2, pre against OFF is significant for 3C. It now says the OFF rate is higher than the light-ON rate, which is what the criterion tests.
- **chr2-increase:** "returned to baseline" isn't in the paper. It now says pre against OFF was not significant, as Extended Data Fig. 8 reports.
- **zero-mg-isolated-bursts:** the paper names two different second slices. Extended Data Fig. 9 shows 10F and 9E; the Extended Data Fig. 5 legend shows 10F and 11G. The claim fixed 9E but cited Fig. 5g, so both pairs are now readings. The criterion now says its burst thresholds and the 1-minute spacing are not from the paper.
- **fig4-firing-propagation:** "activated in sequence" became "suggested a progression", the paper's words. The criterion now says the Spearman test is an assumption. The window, the 3 SD threshold and the 5 s baseline match the propagation notebook at the cited commit.
- **ka-rhythmic-bursts, ka-theta-coherence, opto-cluster3-profile:** each criterion now says which of its tests, bounds and rank rules are assumptions and not taken from the paper.
- **waveform-gcl-association:** the symmetric tolerances conflicted with the rule that the odds ratio must fall inside ST5's asymmetric 95% CI. The criterion now says the CI decides.
- **opto-waveform-association:**
  - I removed the residual's "p < 0.05" entry. The paper reports z = 3.28 against a critical value of 3.23, which is a threshold and not a reported p-value. The z stays as an expected value.
  - The Methods' formula, (O − E)/√E, and their term "standardized residual" (R's `$stdres`) are different quantities, so both are now readings.

**Still open (recorded in the checks entry):**
- The paper also says spike events in 0-mg media did not stop completely during light-ON in two slices. That finding has no claim; I judged it minor.
- I couldn't check the paragraph numbers the sources give for the Discussion, because the text has no paragraph breaks.

All other values check out against the text, the supplement and the code at commit 6865bf6: p-values, CIs, odds ratios, unit counts, Table 2 percentages and the Supplemental Fig. S3 p-values.
