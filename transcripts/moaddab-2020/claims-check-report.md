I checked the 20 claims against the paper and made five changes, all inside `claims/crcns-pag-2/`. The file is ready for an attempt. Nothing was committed or pushed.

**Checker result:** `20 claims, 20 quotes, 49 statistical values, 3 problems`. The three problems are p-values the checker could not match as text: 3e-06 and 9e-06 in fig1bc, and 9e-06 in fig4de. I found all three in the paper, printed as "3.00 × 10 –6" and "9.00 × 10 –6". Every quote matched word for word.

**Changes, by claim:**
- **fig2b-baseline-poke-equivalent:** one reading of the baseline window came from a field in the dataset's own documentation, not from the paper, so I removed it. The criterion now uses the 20 s before cue onset, the only baseline window the Methods define. How sessions are combined per rat is left open, with two readings.
- **fig4c-excited-inflated-onset:** the statement said the extra firing showed "most clearly to safety". It now says there was a significant group difference to safety, which is all the paper reports; it gives no tests for the other two cues.
- **fig6-excited-firing-threat-decoupled:** added the paper's statement that the safety relationship did not differ between groups, to both the statement and the criterion.
- **fig7-inhibited-firing-fear-output:** the criterion now says which tail decides each group comparison: one-tailed for danger and uncertainty, two-tailed for safety. That is what the paper's p-values match when I recompute them (0.149, 0.076 and 0.549).
- **Opening comment:** added Fig. 4D,E to the list of tests whose degrees of freedom don't match the neuron counts.

I recomputed two other numbers and they hold. The chi-square of 5.68 is the test without Yates correction (with it, the value would be 5.17). The Fig. 6 comparison p-values are one-tailed, as the file says. The paper's main findings each have a claim, and no claim draws on another source.

**Still open (recorded under `checks`):**
- **Safety comparison in Fig. 6:** the paper gives no statistic for it, so which tail to use is a choice. I judge it one-tailed, like the other two comparisons in that figure, and the criterion also shows two-tailed.
- **Fig. 2C p ≤ 0.01:** the file format has no "≤", so it is stored as "<". The criterion still uses ≤ 0.01.
- **Supplement missing:** Supplementary Figs. S1 to S6 are not in the text supplied. The three claims that rest on them (figs4, figs5, figs6) each come from one sentence of the Results and have no statistics from the paper.
