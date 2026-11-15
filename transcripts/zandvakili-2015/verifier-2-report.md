**Round 2 verification: Zandvakili & Kohn (2015) on CRCNS v1v2-1**

The claims file has 26 claims, and the attempt record gives an outcome for all 26: 5 reproduced, 6 not_reproduced, 2 partially_reproduced and 13 blocked (7 data_missing, 2 metadata_insufficient, 4 other). My round-1 header said "tests 14 and marks 12 blocked", which was a miscount; the correct split is 13 tested and 13 blocked. I found no place where the claims file misreads the paper.

**1. Outcomes**

I agree with these:
- **Reproduced:** fig4c-broad-ccg-peaks, fig6a-coordination-before-v2, fig7a-above-shuffle, fig6-slow-both-sides.
- **Not reproduced:** fig4c-narrow-peak-sites, fig5-narrow-pairs-rare, fig5b-v1v2-latency, figs3-efficacy, fig7a-threefold, fig6b-not-after-v2.
- **Partially reproduced:** fig7d-time-course.
- **Blocked:** all 13, each with the reason given.

On fig7a-above-shuffle: in 2 of 20 reading-and-window cells, one of five shuffle realizations is above the bound (cell 40). The criterion compares one shuffled value, and the mean of the five passes, so "reproduced" stands.

On fig7d-time-course: the criterion's phrase "for at least four of the five windows" could cover the "no after or distant epoch" condition as well as the peak condition. Read that way, the main, s-b and r-b readings under p-b would be reproduced, since only the 80 ms window fails (cell 49). The record should name this scope reading. The global reading the notebook uses is defensible.

I disagree with two:
- **fig5b-intra-areal-zero-lag (`assumed: true`).** The criterion defines no partial outcome: "Reproduced when the test finds no difference from zero in both areas." Under the assumed Wilcoxon test, V1-V1 gives p = 0.016 (cell 21), so the outcome is not_reproduced; under the sign test it would be reproduced. My round-1 "partially_reproduced" was wrong, and I withdraw it. It is also inconsistent with the record's own grounds for changing fig5b-v1v2-latency and fig7a-threefold ("the criterion defines no partial outcome").
  - The assumption is stated in the deviations. It is reasonable but weak: MATLAB `signrank` is a plausible default. However, at 1 ms resolution 742 of 2620 V1-V1 lags are exactly zero, so the Wilcoxon test here does not behave as it would on the paper's 0.1 ms lags. The deviation should say so.
- **figs4-partner-not-needed.** The criterion asks for each subset to be above control "at a majority of windows". Under e-b2 with p-b, the subset without a partner passes at 2 of 5 windows (p-b 0.364, 0.054, 0.064, 0.001, 0.004; cell 52). That reading fails the first condition and so gives not_reproduced. The claims-file header requires readings that give a different outcome to be named, and the record and cell 53 do not name this one. "Reproduced" can stand only with that reading named, noting that e-b2 is one side of an e-b reading that cannot be formed and that e-b3 gives 4 of 5.

**2. Sentences the printed numbers do not support**
- **README:** "Non-middle-layer, offset-RF, single-unit and V2 relay analyses (seven claims)". Those are six claims (fig7b, fig7e, fig7c, figs2a, figs2b, figs5); fig4-narrow-peak-depth has its own row. With "seven" the table adds up to 27 claims.
- **README:** "It takes about 27 minutes". Cell 56 prints 1530 s, about 25.5 minutes. This is minor.
- **Cell 55 (Summary):** "Narrow V1-V2 peaks are found at about half of the sites … so the deposited sessions are a selection the documentation does not describe." The same applies to the `selection_undocumented` finding ("They differ from the paper's sample in a measure the paper reports"). Nothing in the notebook separates sampling from method as the cause: 1 ms bins, the analytic jitter expectation, and the SD of the flank noise at 1 ms. The excess appearing in every session (cell 8) fits either cause. "Consistent with" (cell 16, fig5-narrow-pairs-rare notes) is supported; "so" is not.
- **Cell 20:** "The two-sided tests do not depend on which unit of a pair comes first as long as the order is fixed." Another fixed order, for example by electrode, flips the sign of a subset of lags and can change both p-values. Only reversing every pair leaves them unchanged.
- **Cell 35, fig6b and fig7d notes:** "p-a is near its nominal level". 13 of 150 epochs is 8.7% against 5% (about 2 SD above 7.5), and the 5 ms window has 5 of 30. This is mildly liberal at p < 0.05. The conclusion drawn from it does hold: the null gives 0 Bonferroni-significant epochs, against 10 to 19 per window under p-a in the data.
- **Cell 32:** "1.50 or more" rests on a printed 1.5 (animal 105, 5 ms, cell 31). This is trivial.

Every other sentence I checked matches the printed outputs. That covers the "**Result:**" cells 9, 12, 16, 19, 22, 25, 32, 35, 38, 41, 44, 47, 50 and 53, the Summary, the README table and the record's notes and findings.

The attempt record gives my round-1 reasons faithfully, close to my own words, with each numbered point attached to the right claim. The `agrees: false` entries correctly mark the three claims where the first record differed from my outcome.

**3. Round-1 points**

Resolved:
- 1: simulations are now blocked as other, not attempted.
- 2: the null check of p-a and p-b was run.
- 3: the ordering effect and same-tetrode sensitivity are reported.
- 4: the 1 ms smear of the epoch is stated.
- 5: the 3.54 ms smoothing floor and the "2 ms or more" meaning are printed.
- 6: fig7d and figs4 now run under every reading.
- 7: the epoch at the spike is counted apart.
- 8: four more shuffle realizations were run.
- 9: the own-trial jitter pool is stated.
- 10: the V1 rfInfo mapping is checked against permutations.

Section C requests met: the file fields and sort codes, calibration, the V1 RF mapping, the shuffle spread, and the extra readings.

Partly resolved: point 11. The excess is now shown per session, but the record treats it as a deposit selection without separating it from method, as in section 2.

Remaining points that bear on a conclusion:
1. fig5b-intra-areal-zero-lag should be not_reproduced under the assumed test (my round-1 error). The deviation should also mention the zero-lag ties at 1 ms.
2. figs4-partner-not-needed: e-b2 under p-b fails the criterion's first condition and must be named, or the outcome qualified.
3. The `selection_undocumented` finding and the Summary attribute the narrow-peak excess to sampling without excluding the method differences.
4. fig7d-time-course: the criterion's scope ambiguity should be named. It does not change "partially_reproduced" under the global reading.
5. The README count ("seven" should be "six") needs correcting.

I still read only the text outputs, not the rendered figures.
