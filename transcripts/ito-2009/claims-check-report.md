I made 11 corrections to the claims file and marked it ready for an attempt (`ready: true`). Nothing was committed or pushed.

**Checker:** `claims/001641/10.1523-jneurosci.6157-08.2009.yaml: 46 claims, 43 quotes, 23 statistical values, 0 problems`. It passes the same way before and after my edits.

**What checked out:**
- All quotes, sources, p-values and expected values match the paper.
- The supplement confirms what the file says about the model: 5000 particles, the choice rule, and parameters that drift with no bounds.
- I recomputed the region-comparison p-values from the paper's neuron counts (0.031, 0.0038, 0.58). They match the paper's 0.03, 0.004 and 0.59, which supports how the file reads that test.
- Each main finding has a claim, and no claim comes from another paper.

**Changes, by claim:**
- **block-structure:** the criterion required the bounds to be exactly 5 and 12, contradicting its own tolerance on 12. Now the most blocks in a session may be 11 to 13.
- **fig2c-reward-effects-fade:** a 0.02 slack and a 0.05 bound were made up. It is now judged on the order of the paper's own values (0.68 < 0.72 < 0.74), with the last within the default 10% of 0.75.
- **fig2d-switching:** a made-up rule (the 99% interval excludes 0.5 in six of eight cases) is removed. The intervals are still reported.
- **fig2e-persevering:** a made-up 0.02 slack is removed, so the rise must be strict, as "gradually increased" says.
- **table1-lsq-parameters:** the tolerance on the reported 0.00 was 0.05, justified by a wrong reason (Table 1 is printed to 0.01). It is now 0.01.
- **table2-ml-parameters:** it counted as reproduced with only 13 of 16 values matching, and the split, search and bounds choices could each be picked to fit. Now all 16 must match, and the outcome must hold under every reading of those three choices.
- **fig5-fq-dfq-beat-all-models:** the paper does not say whether the tests are one- or two-sided, so both are now readings.
- **fig5-fq-dfq-no-difference:** side not given. The test is run two-sided, with the one-sided p shown as a variant.
- **table3-parameter-averages:** the paper does not say what the averages are taken over. Pooled trials and per-session means are now both readings.
- **fig4-strategy-tracking:** a persevering episode was defined as a run of unrewarded choices. It is now a run of choices of the worse side, as the paper describes it. The run lengths (5, 10, 15 trials) are readings that must all agree.
- **Opening comment:** added the p-value recomputation as support for its reading of the region test.

**Still open (recorded in `checks`):**
- **Test side for the no-difference claim:** a one-sided test would roughly halve the paper's p = 0.067, and the difference would then be significant.
- **Thresholds for vague words:** the earlier writer chose these, and the paper gives no number:
  - the information-curve claims: within 0.5 s, a fifth of the peak, twice the median;
  - suppdata1-choice-vs-q-difference: a Spearman correlation above 0.9;
  - fig4-strategy-tracking: kappa2 within 25% of kappa1.
- **Missing supplement data:** Supplemental Data 1 and 3 are not in the text. suppdata1-choice-vs-q-difference and core-shell-no-difference are judged on guesses at their methods.
