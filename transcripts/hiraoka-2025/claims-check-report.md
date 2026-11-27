I checked the claims file against the paper and made seven changes. The file is ready for an attempt.

**Checker result after my changes:** `claims/hiraoka-2025.yaml: 14 claims, 14 quotes, 0 statistical values, 0 problems`. Before my changes it was the same but with 2 statistical values; I removed both, for the reason below.

**Changes, by claim**
- **Opening comment, O4 (the grid of timescales):** the file said a grid with ratio 1.8 "cannot change a claim's outcome". That does not hold.
  - The δ′ labels in Figure 2 step by about 1.82, but the burst-size labels (55, 140, 370, 940, 2400, 6300 ms) step by about 2.55. That is not a whole power of 1.82, so the paper's grid is finer than the labels.
  - The grid's density changes any criterion that counts timescales or pairs ("more than half").
  - O4 now names two grids, both to be run. It also records the relevant range of about 55 to 6300 ms, which the legend implies ("span the entire range of relevant timescales").
- **fig2-neuron-burst-size-heavy-tail:**
  - I removed the `statistics` entry (p < 0.05). In the legend that value is the threshold that decides whether each exponent gets a filled or an open circle, so it is a counting method, not a reported result.
  - I cut the statement to the paper's words, "heavy-tailed across different timescales". The paper's text never says the power law is supported over an exponential.
- **fig2-neuron-merging-heavy-tail:** I removed the `statistics` entry for the same reason.
- **fig2-wikipedia-beta:** I corrected the source from Section III paragraph 2 to paragraph 3. Paragraph 2 describes the neuronal data.
- **fig2-wikipedia-beta and fig2-earthquake-beta:** the statements include heavy-tailed merging numbers, but the criteria judged only the exponent β. They also used the 3000 ms bound, which the paper gives for the neuron alone.
  - The criteria now also judge the merging numbers.
  - They name two readings of the range of δ: the whole relevant range, or the timescales where β at δ′ is below γ (Section III, paragraph 9).
- **fig4-model-heavy-tails:**
  - I added the timescale pairs from the Figure 4 legends, which differ by series and were missing.
  - I marked the "more than half" and 0.5 interquartile-range thresholds as the registry's readings.

All 14 quotes are word for word. Every main finding has a claim, and nothing comes from outside this paper.

**What remains open**
- There is no PDF, so I could not see which exponents in Figures 2 and 4 are filled circles, or the β and γ values at each δ.
- The paper gives no thresholds for "most", "several", "relatively constant", "collapse" or "statistically equivalent". Each criterion uses one chosen by the registry and says so.
- The paper does not say which parts of the session (O2) it used. The only way to decide is whether the spike count matches Figure 2's n = 228 356.

The `checks` entry at the end of the file has `ready: true`. Nothing is committed or pushed.
