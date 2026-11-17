I checked and corrected `claims/saez-2018.yaml`, and it is now fit for an attempt. Nothing was committed.

**Checker:** `claims/saez-2018.yaml: 28 claims, 28 quotes, 13 statistical values, 2 problems`. The two problems are the 1e-06 in `fig5-past-sustained` and the 0.0001 in `mixed-effects-robust`. Both are in the paper: the text extraction garbles the minus sign in "p < 10^-6" and "p < 10^-4", so the checker can't match them. Every quote matched word for word, and the Table S2 sums (all 16 electrode counts, 167 task-active electrodes, 20.9% mean) match the table.

**Changes, by claim:**
- **figs5d-sharp-boundary:** The direction of the one-sided KS tests was backwards. As written, a significant result would have meant stronger encoding at t-2, the opposite of the boundary the legend describes. It is now read so that t-2 shows weaker encoding than t-1.
- **fig3-present-encoding, fig4-past-encoding:** The rule "at least six of eight counts within tolerance" was made up. Full reproduction now needs all eight counts, and fewer gives a partial result. The 95th-percentile chance level is now named as a standard choice. The rise in the number of encoding electrodes (`fig3-present-encoding`'s statement) was never tested; it now is, under two readings.
- **figs4b-power-at-buttonpress:** The made-up condition "outcome peak at least 400 ms after the press" would have accepted a peak before the outcome is even shown. I replaced it with the paper's figure of about 750 ms after outcome reveal, added as an expected value with 10% tolerance. The 200-ms window is named as a standard choice.
- **fig6-past-short-lived:** The made-up "more than one regressor in five" threshold is replaced by the mean over regressors at each lag, compared against chance.
- **mixed-effects-robust:** The file stated the Bonferroni correction as over 16 regressors, but the paper doesn't say. It is now listed as a reading.
- **figs3b-no-motor-encoding, no-anatomical-gradient:** The Discussion paragraph numbers were wrong: the paragraphs cited don't mention movement or gradients. Each is now cited by its first words.
- **fig7-all-areas-similar:** Added the stepwise selection as a reading, plus a dependency on `figs6b-stepwise-similar`. The chi-square test is marked as borrowed from elsewhere in the paper.
- **hfa-more-than-fp:** n is now marked as a reading (the paper doesn't state it), and the quote is extended to "3.3%".
- **methods-electrode-trial-counts:** The timeout tolerance is now 0.998 (10% of the value). The criterion notes that 9.98% of 2,000 trials isn't a whole number, so the denominator is read as all trials recorded.
- **behavior-risk-neutral:** The statement now says patients gambled "only slightly more often than a risk-neutral baseline model", as the quoted sentence does.
- **fig1c-patients-like-controls:** Removed the wrong claim that the legend fixes the test.
- **figs2a-choice-gamble-ev, fig2-example-electrodes:** Their tests are now labelled as borrowed or standard choices, since the paper names none.
- **figs2b-rt-conflict:** Says how "comparable effect sizes" is handled: reported, not judged, since the paper gives no measure.
- **fig3-latency-duration-similar:** Notes that reading (c) is the measure used in Figure 5, whose values differ from the ones here, so it is the least supported reading.

**Still open:**
- I couldn't render the PDF (no PDF tools installed), so I couldn't count Discussion paragraphs across page breaks. That is why those two sources use first words instead of numbers.
- Table S2 contradicts itself: patient s06 has 4 in "any choice" but 0 in every choice row.
- Table S2's patient counts give a mean of 7.75, not the paper's 7.41. The claim already lists readings for this.
- The Methods give a 20% win probability for a shown 2, while Table S1 and the worked example give 80%. The opening comment already handles this.

Every main finding has a claim, and none comes from outside the paper. The `checks` entry is added with `ready: true`.
