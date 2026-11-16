Round-1 revision of hazon-2022-01 is finished. The final run of `python tools/entry.py all entries/hazon-2022 --max-minutes 80` passed all three notebooks with the final text. Its numbers match the first run's, and `entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes (all three move to the verifier's outcome):**
- **fig3f-signal-slope-beginning-vs-end:** partially reproduced → reproduced, resting on the code's direction of the test. The criterion says an outcome that holds only in the code's direction is recorded that way. The notes say the legend's "decreases" does not hold.
- **pf-width-variance-not-predictive:** not reproduced → reproduced, resting on the filter that Supplementary Table 2's note describes. With intervals of 1 to 3 standard errors, p is 0.056 to 0.139 across sessions and 0.077 to 0.085 across animals. The four sessions the filter drops are four of the six whose events do not track position. Without the filter p = 0.041, and leaving out any one of 11 sessions brings it above 0.05.
- **suppl11b-i0-vs-single-cell-snr:** not reproduced → partially reproduced, resting on leaving out failed fits. The result is r = 0.750, p = 0.0125. The new check shows these fits fail with 80 subsets as well.

**Added or corrected:**
- **Problem 1 (4 subsets per size):** a new notebook, `reproduce_hazon_2022_fitcheck.ipynb`, repeats the IMSE fits with the paper's 80 subsets on steps of 10 for 16 sessions: all 15 of Mouse2011 and Mouse2012, plus one of Mouse2028.
  - Where both fits are sound (13 sessions), N changes by a median factor of 1.09.
  - The fits that make no sense come from the misaligned sessions under either setting.
  - So the fewer subsets do not explain why saturation-ensemble-size, suppl11b and suppl8 fall short; those outcomes stand.
- **Problem 2:** suppl8 is now also run without the misaligned sessions and failed fits. The path pattern holds, but two r values are outside tolerance and accuracy against trials has p = 0.064, so it stays not reproduced.
- **Fit tables (part C of the report):** the decoding notebook now prints R² for every fit (median 0.986) and the IMSE points against the fitted curve for the 7 failed unshuffled fits.
- **Problem 4:** the decoder's docstring and defaults now say C = 1, the value actually used. No number changes.
- **Problems 5 and 6 (Supplementary Table 1):**
  - The minimal-modulation rule keeps 27,715 and 27,770 of 27,898 cells, close to the paper's 27,793. It only removes silent cells, as in the paper.
  - Without my 1180 cm width cap the mean width is 37.6 cm, inside tolerance. That mean comes from 195 runaway fits (the median is 11.5 cm). The outcome stays not reproduced but is now marked as resting on the cap; without the cap it would be partially reproduced.
  - The occupancy and footnote-formula limits are recorded as deviations.
- **Problem 8:** fig4a's use of the first trials in each direction and its cut to 14 components are now recorded as deviations.
- **Other record updates:** I added a question to the authors about how the Supplementary Table 2 intervals were computed. Round 1 is recorded under `verifications` (26 agree, 3 disagree), with a response for each claim. The README and the notebook summaries are updated.

**Not done:**
- The verifier reported no place where the claims file misreads the paper, so I added nothing to `questions/hazon-2022.yaml`.
- I could not run 80 subsets on all 73 large-data sessions: that would take about 4 hours. The per-animal saturation range therefore still uses 4 subsets per size.
- The decoding notebook takes 66.8 minutes, over the 60-minute aim, so I ran with `--max-minutes 80`. The new notebook takes 37 minutes.
- I could not check the paper's MATLAB code.
