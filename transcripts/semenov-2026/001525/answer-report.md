I answered the one open question, and the claims file changed. `tools/claims_check.py` reports 27 claims, 27 quotes, 9 statistical values and 0 problems.

**fig7b-test-pulse-unchanged-to-760 (changed).** The paper settles which test it used. Three passages point to an unpaired test:
- The Fig. 7B legend tests "the difference from the undamaged membrane (gray area between horizontal dashed lines)", which compares each point with the control group and its spread.
- The Methods name only "Student's t-test and one-sample t-test".
- The paper writes "paired" when it pairs (Fig. 2D legend, "2-tailed paired t-test"), but not for Fig. 7B or in Results 3.7.

What changed in the criteria:
- **fig7b-test-pulse-unchanged-to-760:** the paper's test is now the unpaired two-sided t-test against the control group. The paired test and the one-sample test are only variants, and the methods_underspecified rule is gone.
- **fig7b-test-pulse-reduced-1200-1400:** uses the same unpaired test as the main test. Only the pole readings are still open.
- **fig7a-test-pulse-cosine-up-to-1000:** refers to that single test instead of to "readings" of it.

No statement, quote, source or expected value changed. I marked the question `answered: 2026-11-02`. Nothing is committed.
