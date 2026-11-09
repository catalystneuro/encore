The claims file for DANDI:001250 is fit for an attempt after my corrections, and I marked it `ready: true`. Only `claims/001250/10.1101-2024.12.04.626805.yaml` changed; nothing is committed.

**Checker:** `39 claims, 39 quotes, 26 statistical values, 0 problems`, both before and after my edits.

**Changes, by claim:**
- **fig5a-synthetic-mostly-single-units:** the criterion left "S 377 vs. 163" as an open comparison. The paper's own numbers settle it:
  - 163 is the synthetic simulation's multi-unit count: N = 740 is its 540 units plus Marques-Smith's 200.
  - The test is the code's chi-square on single-unit percentages, which gives the printed 4.0.
  - "Four times" is 377 against Marques-Smith's 96.
  
  I rewrote the criterion and added 163 to the expected values.
- **fig5a-single-unit-fraction-differs:** I added a third reading of "on average 41%": the mean of the Marques-Smith, NS and NS-2X fractions (48%, 36%, 38%, mean 40.7%). It also reproduces the paper's chi-square of 2.0. The NS fraction alone is 182/504 = 36%, which does not match 41%.
- **fig5a-dense-probe-more-multi-units:** added the multi-unit counts (Marques-Smith 104, Horvath 265) to the expected values, and the unit totals (200, 358, 504, 562), checked against the printed N values.
- **fig6ab-biophysical-accuracy-15-percent:** added `data: with_inputs`, because N = 3,190 includes the synthetic simulation, which is outside data.
- **fig6a and fig6ab:** the Methods leave open which sorted units enter the best match, and the code settles it, so the code's choice now decides. The all-units version is a variant.
- **fig6gh-selection-bias-layer5-pyramidal:** a unit's layer is now the matched neuron's layer, as the Results and the Fig. 6h legend say; the code's site layer is a variant. The two sorting durations must now agree.
- **Method details that had been decided "under one reading"** now need all readings to agree, or the claim is blocked as `methods_underspecified`. The protocol only allows "any reading" for ambiguity in a reported number.
  - fig5ef: the train/test split, 80/20 in the Methods against 75/25 in the legend and code.
  - fig2s-v: median against summed AP power.
- **fig3fg-wavemap-six-profiles:** fixed the "six, three or six electrodes" typo. Six electrodes (Methods) and the code's resolution now decide; the rest are variants.
- **supp4-other-sorters-firing-rates:** named as open whether "b, p > 0.15" refers to medians or variances. The Results and the supplementary legend label panel b differently, so both are run.
- **fig6c-f-accuracy-predictors:** noted that the code runs no penalty at all, while the Methods describe a lasso that selects features. Recorded as a deviation.
- **fig7g and fig7h-j:** noted that printed t values of -0.31 and 0.18 contradict "all p < 0.001".

**Still open (recorded in the checks entry):**
- Several criteria judge vague words with thresholds the earlier reader chose, not the paper. Examples: "rising with depth" allows at most one inversion, a power law needs a fit of R² ≥ 0.9, and log-normal is tested with Shapiro-Wilk. Others are in fig6gh, fig7a, fig2q, fig5cd and supp2. Each is labelled as a choice, but the outcomes rest on them.
- Which five experiments enter the chi2(4, N = 5,241) test can't be fixed without the evoked unit total.
- I did not re-read the code repository. Details taken from the code are as the previous reader recorded them.

The main findings each have a claim, and every claim comes from this paper.
