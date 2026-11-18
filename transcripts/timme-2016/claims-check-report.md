I checked the claims file against the paper and corrected eight claims and two header notes. I'd call the file ready (`ready: true`), with the open problems below.

**Checker:** `claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml: 14 claims, 14 quotes, 1 statistical values, 0 problems`, before and after my edits.

**Changes, by claim:**
- **Header, M-TE:** the reason for one-bin past states was wrong (four variables don't fix the history length). It now rests on the paper's binary spiking states (Effective Connectivity Detection, paragraph 2).
- **Header, M-CORR:** added that each Fig 5A/5B panel has 40 correlations, more than the 25 recordings, so each panel pools both time scales.
- **fig4ac-te-lognormal:** the criterion used only the full networks, though the paper doesn't say whether Fig 4A/4C use those or the sub-networks. Both are now named and reported.
- **fig5a-in-degree-uncorrelated:** the binomial test is judged on both time scales pooled, as the panel pools them. Each time scale is reported.
- **fig5b-out-degree-positive:** it required a significant skew at each time scale separately, which the paper doesn't report. It is now judged on the pooled panel.
- **fig6-information-gain-not-rising:** it passed with only one negative exponent, but the legend says both fits gave negative exponents. It now needs both negative; a positive exponent whose interval is not wholly above zero counts as partial. Whether the information gain is normalized by H(I_F) is now named as open.
- **table1-pid-examples:** the paper's table survived flattening intact, so I computed the PID terms from it. Two parts of the criterion contradicted the paper:
  - In the hidden self interaction, mutual information is 1 bit while transfer entropy is 0. The paper's point is that MI is wrongly nonzero there; the criterion said MI is zero.
  - In the single and redundant example, interaction information is -0.25 bits (minus the redundancy), not zero.
  - The tolerance was also too tight: rounding in the four-digit table entries alone gives 1.3e-4 bits. It is now 0.001 bits after renormalizing each column.
- **fig7c-degree-modified-rule-matches:** the model's runs have no past, so the synergy method used for the recordings can't apply as written. I named this as open and gave a reading. The Euclidean-distance rule is now marked as a reading.
- **fig7d-degree-rule-highest-conditioned-mi:** it required every pair of rules to differ at p < 0.001, but which pairs the figure marks can't be read from the text. The p < 0.001 requirement now applies to the degree-modified rule's conditioned MI, the result the legend notes. All pairwise tests are reported.
- **figs1-larger-model:** the criterion now covers the parts of the statement it missed: larger conditioned MI for the Hebbian and firing-rate rules, and the same connectivity ordering as fig7b. Whether the sigmoid constants (alpha, beta) are recomputed for 40 neurons per layer is named as open.

Every main finding has a claim, and all claims come from this paper.

**Still open:**
- The four model claims (fig7b, fig7c, fig7d, figs1) need equations 16 to 20 and 22 to 24, which the flattened text lost, and there is no PDF of the paper. The author must take them from the version of record or block these claims as methods_underspecified.
- The pass thresholds for fig4ac, fig4bd, fig5ab, fig5cd and fig7b are the file's own readings; the paper gives no measure for these qualitative statements.
- Bins, delays, jitter width and how the sub-networks are drawn depend on the earlier Timme et al. 2014 paper, which was not read here.
- The paper doesn't say which 40 of the 50 possible correlations Fig 5 uses.

Nothing was committed.
