The checks entry is added and the file is ready for an attempt. Nothing was committed or pushed.

**Checker result:** `28 claims, 28 quotes, 0 statistical values, 0 problems`. Before my edits it was 27 claims with 0 problems.

**Changes, by claim**
- **Header:** the 28 cultures were credited to Figure 2B, which the header itself says could not be read. That number comes from the dataset's own description; the paper only gives the 435 recordings. Common detail 3 now also says the paper doesn't state which set of comparisons the false discovery rate correction covers. One panel is used, and the whole figure is shown as a variant.
- **culture-counts:** the expected quantity said "modal" but the criterion judged the median. Both are now listed as readings of "most recordings ... approximately 100". The 5th to 95th percentile test of the firing rate range is now marked as a choice the paper doesn't make, and the minimum and maximum are reported.
- **Thresholds the paper doesn't give, now marked as choices:**
  - fig5f-network-state-poisson-keeps-complexity: the 5% bound
  - fig7c-cb-curvature-no-peak: the 0.02 window
  - fig8-subsampling-exponents: the 10% bound
  - eq4-relation-randomized: the one SD bound
  - fig10a-complexity-randomization and fig10b-susceptibility-randomization: "Poisson among the two largest decreases"
- **fig11ac-fit-range-randomization:** the Figure 11A,C legend says the fit ranges fell under every randomization except 10-bin jitter, which is wider than the Results text. The criterion now also reports those other randomizations.
- **fig11bd-exponents-randomization:** the criterion accepted 4 of 5 randomizations, which the paper doesn't say. The legends say the exponents increased under randomization with no exception, so all five are now required, and the result is partial when only some increase.
- **Added fig8-exponents-match-literature:** a main finding with no claim. The paper reports that the sub-sampled exponents agree best with values published by Mazzoni 2007, Pasquale 2008 and Friedman 2012. Those reference values are only in the cited papers, so the claim is marked `data: with_inputs`.

**Still open**
- The Figure 8 means and SDs, the Figure 10 and 11 significance stars, and the Figure 2B exclusions appear only inside the figures. No PDF of the main article was supplied, so those claims are judged on direction only.
- Methods 2.4 prints p_trans steps of 0.05, which can't place a peak at 0.265. The two step-size readings (0.005 and 0.01) stay.
- The paper doesn't say how many avalanches a recording needed to be kept.
- The Figure 7 legend puts the complexity and susceptibility peak near 0.25, while the Results say 0.265. The claim follows the Results.
- In the Bethe lattice claim, the paper doesn't say how network states are built or how many runs were made. The claim relies on the earlier reader's reading of the toolbox file `bethelattice.m`, which I couldn't re-check.

**Ready:** yes (`ready: true`).
