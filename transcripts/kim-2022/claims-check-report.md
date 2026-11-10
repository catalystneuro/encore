The claims file is ready for an attempt. I made two changes and logged five open points.

**Checker result:**
- Before my edits: `claims/kim-2022.yaml: 24 claims, 24 quotes, 7 statistical values, 0 problems`
- After my edits: `claims/kim-2022.yaml: 25 claims, 25 quotes, 7 statistical values, 0 problems`

**Changes, by claim:**
- **fig7-charging-time-constant:** The quote ended at "520 ns". That left out the discharge fit's numbers (425 datapoints, r = 0.85, p < 0.0001), even though the statement and the statistics record them. I extended the quote to include them (Results 3.5, paragraph 2).
- **fig7-bipolar-alternation (new):** Results 3.5, paragraph 3 states that bipolar trains made the membrane potential alternate between positive and negative values, across the whole train. The file covered this only for the first pulse, in fig7-bipolar-overshoot. The new criterion tests the end of the first phase and the minimum of the second phase for each of the five pulses. The paper gives no test for this, so it uses a one-sample t-test at p < 0.05, the same rule the file applies to the other Fig. 7 claims.

Everything else checked out against the paper:
- The other statements, sources and statistics match the text.
- Range tolerances are correct: 18 to 27.5%, 27 to 55%, 1.8 to 3.3 and 2.7 to 4.4%.
- The opening comment's account of the methods matches Methods 2.1 to 2.6.
- No claim draws on another paper.
- The main findings and the highlights are covered.

**Still open (recorded under `checks`):**
- **fig2b-exponential-same-slope:** The criterion tests the slopes of exponential fits made to each dish. The paper fits the means and reports no test for the slope, so fitting per dish is the file's own choice.
- **fig2a-uptake-rises-with-field:** "Proportionally" is read as "rising with field", tested as strongest ROI against weakest. Fig. 2B shows the rise is exponential, and the paper gives no test.
- **fig6be-bipolar-khz-less-than-1hz:** "Less than at 1 Hz" is judged only at the strongest ROI. "Just marginally above the background level" is not judged at all, because the paper gives no cutoff for either.
- **File's own rules:** The ROI inclusion rule for microsecond pulses (fig4eg, fig4h) and the "mirroring" rule in fig7-unipolar-pole-polarization were set by the file, not the paper. Each criterion says so.
- **Data location:** Neither dataset's title names the experiments of Figs. 3 to 6 or the thermometry photographs of Fig. 1E. Those claims depend on 000489 holding them, which is for the author to find.

Nothing was committed or pushed.
