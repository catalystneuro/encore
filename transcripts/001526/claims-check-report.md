I checked the claims file for DANDI:001526 against the paper and corrected what was wrong; it is fit for an attempt.

**Checker result:** `30 claims, 30 quotes, 9 statistical values, 0 problems`, both before and after my edits. The quotes, sources (I checked each paragraph number), statistics and the paper's own tolerances are correct.

**Changes, by claim:**
- **fig1-pattern-poles-leaky:** the criterion said Figure 1 shows one cell. The legend doesn't say that, so it now says the cells are not identified.
- **fig2b-di8-bleaching-43:** the two expected values had opposite signs (+5 and −5). Bleaching lowers dF at both poles, so both are now −5%, which matches the criterion.
- **fig4a-fluovolt-limits:**
  - The midpoint for the 45 to 50% range was wrong: 47.5 corrected to 47.75, so it covers the criterion's 40.5 to 55.
  - The paper says measured and calculated IMP matched "only" at 43 and 150 V/cm, so the mismatch test now starts at 230 V/cm, not 360.
- **fig4c-equator-cosine:** the measured-to-calculated IMP ratio is now a ratio of means, taken separately for each half. As written, it would blow up near the equator, where calculated IMP is near zero, and the two halves' signs would cancel.
- **fig5c-gd-reduces-conductivity:** 2.5 ± 0.8 corrected to 2.55 ± 0.75, to match the criterion's 1.8 to 3.3.
- **fig6a-single-pulse-ca:** the criterion said 14 cells per field strength. The legend only says 14 cells, so this is now stated as not given.
- **fig7c-fast-resealing:**
  - 13.5 ± 7.2 corrected to 14.15 ± 7.85, to match the criterion's 6.3 to 22.
  - "Most datapoints" now has two readings: all datapoints, or only those with leftover conductivity. The original wording, which counted only the latter, came from the earlier writer, not the paper.
  - The statement's "no difference between the poles" had no test. I added a paired t-test as a reading, since the paper names none.

**Still open (recorded in `checks`):**
- Reference [20] is not under `paper/`. The claims marked `with_inputs` need its fit of the charging time constant against cell radius.
- Seven criteria test statements the paper judged by eye. Their windows, bins and tests are labelled readings built from the tools Methods 2.5 names, not the paper's own methods.
- **fig5b-eq2-sensitivity:** my rough calculation from Eq. (2) gives about 1.3% for a 10-fold conductivity increase, against the paper's "~2%". It may fail its tolerance.
- **fig6b-train-ca:** the paper never defines a "strong" Ca²⁺ response, so the responder fractions stay blocked.
- The abstract's 1000 V/cm weakening point for 0.3 µs pulses has no Results sentence of its own. It is covered only indirectly, by fig4d-short-pulses-same-limit.

Every main finding has a claim, and none comes from outside the paper. The new `checks` entry is marked `ready: true`. Nothing was committed or pushed.
