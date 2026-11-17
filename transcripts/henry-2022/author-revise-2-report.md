I've worked through all four points of the round-2 report and re-run the entry with `python tools/entry.py all entries/henry-2022`. Both notebooks pass (40 and 39 min) and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes.** None changed and nothing is under `proposed`: 19 reproduced, 8 partially reproduced, 2 not reproduced, 3 blocked. Round 2 is recorded under `verifications`, agreeing on all 32 claims, with the verifier's reasons in its own words and what I changed under `response`.

**Analyses added, as the verifier asked:**
- **20 single random half splits** (point 3), for fig5-terms-covary and fig5de:
  - The V4 correlation ranges from -0.893 to -0.639, median -0.683. The stored-order split gives -0.682, so it is typical, and the criterion holds on all 20 splits. Only the selection by reliability averaged over 20 splits gives -0.459.
  - For fig5de, the reading that was used (recorded trial counts against the Figure 2C slopes over all neurons) is near its limit: it holds on only 11 of 20 splits.
  - Compared against the fitted neurons' own slopes, it holds on all 20 splits, on the stored-order split and on the averaged selection. Under that reading the outcome no longer depends on the selection, so fig5de's `assumed: true` is arguably no longer needed. I left the flag as verified, since in round 2 I didn't want to alter what the verifier agreed with, and the notes explain the situation.
- **Decoders with no nonzero coefficient** (point 2). For each such fold, the variant uses the next larger C that has a nonzero coefficient, on the same folds, so the main results are unchanged. It barely moves anything:
  - Mean decoding performance changes by at most 0.007.
  - V4 threshold elevation is 6.91 and 2.55, against 7.30 and 2.61 in the main run. The large CA value at 1.3 degrees stays (10.46).
  - V1 is 1.688 and 1.575, still outside the paper's values, with the same significance pattern.
  - In Figure 7, only 15 of 880 fixed decoders were all-zero, and d′ changes by at most 0.008.

  These decoders do not explain the gaps from the paper.
- **Figure S6 fraction.** The notebook now prints the fraction driven by targets over the 10 usable populations: 0.817 (V1) and 0.871 (V4).

**Text corrected:**
- **Permutation null (cell 77, fig2f-v1).** The text now says the null is shifted much further than the no-crowding calibration. Whether the V1 elevations count as significant depends on which null is used, so the V1 outcome rests on the values, which fail.
- **fig4a notes.** Under pooling within orientation, both far values are outside tolerance.
- **figs6.** The Figure S6A agreement came only from averaging in 12 zeros; over the 10 usable populations the fractions are above its range. "No unit responds" is now "no unit exceeds the blank mean plus 1 SD".
- **Summary.** It no longer says the all-zero decoders are not a choice made here; their rate depends on the penalty grid's lower bound.
- **Findings.** `methods_unavailable` (5) now says outer folds where it said decoders, and `metadata_error` now gives the distractor-only z range (-0.29 to 0.37) as well.
- **README.** The fig5-terms-covary and fig5de rows now say they rest on the assumed even/odd selection.
- `entry.yaml` runtime for the main notebook goes from 34 to 41 min.

**Not done:**
- The pseudo-population notebook and the shuffled decoding runs were not repeated with the all-zero variant. That variant was run on the recorded-population estimates, which are the reference for both comparisons, and changes them little.
- The report raised no new misreading of the claims file, so I added nothing to `questions/henry-2022.yaml`.
