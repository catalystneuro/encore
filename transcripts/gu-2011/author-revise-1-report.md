I've worked through every point in the round-1 report. Two outcomes changed, and the rest stay as they were. The entry re-ran cleanly with `python tools/entry.py all` (notebook runs in 49 s, 0 check errors), and the conclusions match the new numbers. Nothing is committed.

**Outcomes that changed**
- **fig7c-narrow-preferences: not_reproduced → partially_reproduced**, as the verifier proposed. The proportions match and the improvement grows as the range narrows, but the best improvement is 4.83%, below the paper's 8 ± 0.8%.
- **fig4dh-lateral-more-sensitive: blocked → reproduced, on a subset (problem 2).** I tested it on the 129 units from two trained monkeys, using the claims file's Fisher threshold and its readings. The paper's ANOVA has a training factor, which can't be included because there are no naive units.
  - Lateral units have lower median thresholds under every reading, in both conditions.
  - One of the 8 readings reaches p < 0.001 (p = 1.9e-07), which is what the criterion asks for.
  - The result is fragile, and the notes say so:
    - In that reading, the vestibular condition alone gives p = 0.040.
    - With spline-peak preferences, no reading reaches p < 0.05.
    - Neither monkey shows a significant vestibular difference on its own.

**Corrections and additions**
- **Problem 1:** `pref_vector_sum` now weights each response by the angle it covers. A synthetic check in the notebook shows it recovers preferences to within 3°; the old version put 30° at 16°.
  - fig8ab is still not_reproduced. The weighted vector sum gives p = 0.80, and the opposite-sign result (p = 0.0006) is gone.
  - I added the share of choice probabilities above 0.5 (71.7%) as a check on how they are signed.
- **Problem 3 (fig8cd):** the notebook and notes now state the conflict with the claims file's point-count rule. The outcome stays reproduced, judged on the trained pairs.
- **Problems 4, 6 and 7:**
  - The header's random-numbers statement is corrected.
  - The notebook prints the largest difference in signal correlation between the two simulation readings (5.6e-07).
  - The two behavioural thresholds for fig2a are stated against the 0.9–3.3° plateau range.
- **Items the verifier couldn't check:**
  - fig5-intercept: bootstrap intervals for each group's intercept, which still overlap.
  - fig7a: the point where trained/naive crosses 1, at rsignal = −0.0216.
- **Attempt record:** notes and the affected findings are updated, and round 1 is recorded under `verifications` for all 35 claims (agrees false for fig7c and fig4dh). The README table is updated.

**Not done, and why**
- **Problem 8 (six pairs in one recording):** not explained. The six pairs are all pairs of four units, and nothing in the data set accounts for the paper's maximum of five. It stays a finding.
- **Problem 5:** no change needed; the verifier said it does not affect a conclusion.
- **Questions file:** no questions added, because the verifier reported no place where the claims file misreads the paper.
