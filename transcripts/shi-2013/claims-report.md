I've written `claims/shi-2013.yaml`, and the quote checker passes it: 28 claims, 26 quotes, 7 statistical values, 0 problems. Nothing is committed.

**Text read.** The version of record (PyMuPDF text of the journal PDF): Methods, Results, Discussion, Table 1 and the legends of Figures 1 to 6. The paper has no supplement and links no code, so no code was read. The text prints the math signs (=, <, >, ±, minus, ~) as a broken character, and the PDF could not be rendered here. I recovered the signs from the PDF's font encodings instead; the decoded signs are listed in the file's opening comment.

**Counts.**
- **Claims:** 28, all findings.
- **Quotes:** 26. Table 1's means and its SDs have no sentence stating them, so those two claims carry an `inferred` note.
- **Statistics:** 7 entries across 5 claims.
  - The example neuron of Fig. 3: P < 0.05 for position, P = 0.52 for vision, P = 0.64 for the interaction.
  - The Fano factor permutation test.
  - The CV2 Kruskal-Wallis test.
  - The V against NV decoding t-test.
  - The aborted-trials t-test.
- **Criteria:** all 28 claims have one.
- **A reading of the paper's notation:** it prints "P < 0.05" even after results it calls not significant. I read that as the test's threshold, so it is recorded as a statistic only where the finding is a significant difference.

**Details left open, and the readings named:**
- **Trials per target:** the paper says five. Read as five per target in each condition, because the decoder trains on four trials and tests on the fifth.
- **Session averaging (behavior):** the mean of the 16 animal-by-target percentages, or pooled over all session-target pairs. Levene's test centred on the mean or on the median.
- **Table 1:** the origin of the tracker frame is not given, so values are compared directly and again after removing a constant offset.
- **Example neuron (Fig. 3):** it is not identified; any neuron matching its tuning and P values counts.
- **Movement onset:** not defined. An event code marking onset, or the time the arm leaves the start window.
- **The 9% (27/343) interaction count:** 27/343 is 7.9%, so the readings are 27 cells or 9% (31 cells).
- **The V–NV correlations:** what a response pair is (cell-by-target mean rates, or single trials paired by order). The permutation test is taken as two-sided.
- **Fig. 4 outliers:** Tukey fences over all cells, the same fences within each group, or an index above 1.5 times the IQR. For INDX2, whether outliers are removed on INDX1 or on INDX2.
- **"Adjacent" preferred location:** neighbours on the ring of eight directions, or on the 3 by 3 grid including diagonals.
- **Rate variance:** all 343 cells or the cells left after outlier removal.
- **Fano factor outliers:** the 5 cells removed for Fig. 4, or Tukey outliers on the count means or variances.
- **CV2:** intervals pooled over trials, or computed per trial and averaged.
- **Decoding:**
  - Bootstrap: 200 resamples of the cells, or resampled populations of 200 cells.
  - The cross-condition scheme: leave-one-out across conditions, or train on all five trials of one condition and test on all five of the other.
  - The t-test's samples: paired over the 8 targets, unpaired over the 8 targets, or unpaired over the 200 bootstraps.
- **Tests the paper does not name:** the first against last 400 ms decoding comparison, the cells without ANOVA effects, and the extended-hold sessions. Each takes the paper's decoding t-test (or, for the extended hold, a chi-square test of the cell counts) as its reading.
- **Eye position:** per animal, or per session.

**Missing from the paper that claims needed:**
- **Aborted trials and the 1,200 ms hold:** both rest on an abstract (Shi and Buneo 2009). The paper gives no window sizes, test units or sessions, so these two claims are probably underspecified.
- **No identifier for the example neuron.**
- **No analysis code.**
