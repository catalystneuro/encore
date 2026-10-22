I wrote `claims/001277/10.1016-j.bioelechem.2025.109016.yaml`. The quote checker passes it: 17 claims, 17 quotes, 13 statistical values, 0 problems. Nothing is committed.

**Text read:** the accepted author manuscript in PubMed Central (PMC12331426, NIHMS2087238), with its Methods, Results and figure legends. There is no supplement; PMC lists none and the text cites none. No PDF was stored, so I could not see the figures, and numbers shown only in figures are not claimed. The paper links no code ("Data will be made available on request").

**Claims:**
- All 17 have quotes; none needed an `inferred` note.
- 6 claims carry statistics (13 entries); the remaining 11 report no test.
- All 17 have criteria; 5 also carry `expected` numbers.
- All use `data: dataset`.
- The dataset's archive description names the pulse-duration experiment (Fig. 6), which has 5 claims: the 900-ns central peak is not significantly higher; normalised profiles look similar; FWHM falls with pulse duration (p = 0.003); 600 and 900 ns each differ from 300 ns (p = 0.028 and 0.0072); and 900-ns FWHM is 1.7 ± 0.08 mm, 11.1 ± 0.6% of the gap.
- The other 12 cover packet rate (Figs 3 and 4), raised electrodes with YP against Pr (Fig. 5), burst number in CT26 and CHO cells (Fig. 7), and heating (Fig. 2).
- One mismatch for the author: the archive description gives a 10 mm inter-electrode spacing, while the paper gives a 15.3-mm diagonal.

**Details the paper leaves open, and the readings named:**
- **ROI spacing along a diagonal:** 1-mm steps (the text names positions at 0, 6 and 7 mm), or contiguous ROIs.
- **Lorentzian fit range:** half-widths of 4, 5 or 6 mm. The Methods say 4–6 mm, Results 3.1 says −4 to 4, and the Fig. 5 and 6 legends say −5 to 5.
- **Pooling the two diagonals:** averaged at each signed distance before fitting, or all points fitted together.
- **Test for the Fig. 6B peak:** Bonferroni t-tests or a one-way ANOVA. If they disagree, the claim is blocked as `methods_underspecified`.
- **Fig. 6D trend:** linear in pulse duration (legend) or linear in log pulse duration (Results).
- **Fig. 6D pairwise tests:** 2 or 3 Bonferroni comparisons. The asterisks are not tied to a duration, so both orders are accepted.
- **"40-fold" ratio:** the near-electrode position is 6 or 7 mm, and the ratio is either of means or the mean of per-experiment ratios.
- **Fig. 4B pairs compared:** each rate against 1 Hz, or all pairs.
- **Which ROI side lies along the diagonal, and which electrode footprint holds the background ROIs:** neither is stated. I treated both as standard choices unlikely to change an outcome.

**Not judged:**
- "Practically no" staining near electrodes and "just slightly larger" spot: the paper sets no threshold for either, so the values are reported and not judged.
- "2.3% of the electrode array area": the paper's numbers don't give this figure. A 1.1 mm circle over the array square gives 0.8%, so the figure is reported, not used for the outcome.

**Missing from the paper:** no supplement or code was needed. A claim did lack one thing: Fig. 4B and the Fig. 3 legend use packet rates the text does not all name. Five rates lie below 0.2 MHz, but only 1 Hz, 1 kHz and 10 kHz are named.
