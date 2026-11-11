I checked the file and made eleven changes. After them the checker still passes: `claims/drieu-2018.yaml: 35 claims, 34 quotes, 87 statistical values, 0 problems`. The count of statistical values went from 86 to 87 because I added one. The file is ready for an attempt.

The quotes, sources, p-values and expected values match the paper. Where the two printed versions give different bounds, the claims use the version of record's, as the file's header says. Every main finding has a claim, and none comes from anything but this paper.

**Changes, by claim**
- **fig2cd-spike-bursts-slower:** the criterion matched P < 10^-6 to the Active vs Passive 1 comparison and P < 0.02 to Active vs Passive 2. The Fig. 2D legend does not say which goes with which, so either assignment now counts. The other reading (an overall Kruskal-Wallis plus one follow-up comparison) is now written out.
- **figs4de-precession-range-similar:** the criterion said its definition of the precession range came from ref. 26. The paper never defines the range, so it is now marked as an assumption.
- **fig3e-joint-score-slope-theta, fig4d-joint-score-slope-replay:** the bounds used for "high-value" events (above the 95th percentile of shuffled scores, slope above 3 m/s) are now stated as choices made here. The paper gives none.
- **fig3c-proportion-significant-theta:** added the legend's binomial *P < 0.05 as a statistics entry; only the P < 0.001 level had been recorded.
- **fig2b-theta-power-reduced:** stated that the 12–20 Hz band used for the first harmonic is not the paper's.
- **figs1-travel-similar, figs4b-proportions-oscillating-precessing, fig3b-average-theta-reconstruction, fig3c-proportion-significant-theta:** removed rules that let some expected values miss (7 of 9, 5 of 6, 4 of 6). The paper gives no such allowance, so a full reproduction now needs every value within tolerance, and a partial outcome covers the rest.
- **figs2c-track-coverage:** the result at 100% coverage, the literal reading of "entire", is now reported as well.

**What remains open** (also recorded under `checks`)
- **figs2c-track-coverage:** the 95% threshold for covering the "entire" track is not from the paper, which gives no number.
- **fig3e and fig4d:** the high-value region is not defined in the paper, so their outcomes rest on an assumption.
- **figs5b-per-rat-reconstruction:** which of the three P values in fig. S5B belongs to which measure comes from the order of the extracted text. It cannot change the outcome, because the criterion requires all three to be below 0.05.
- **Paragraph numbers in sources:** they follow the author manuscript, and the version of record merges some paragraphs, so a number may be off by one. Each source also names its figure panel.

Nothing was committed or pushed.
