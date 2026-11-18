I've written `claims/fujisawa-2008.yaml`: 33 claims, one of them the `channel-region-link` link check on 000067. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** The version of record (main text, figure legends, Methods) and its supplement (Supplementary Note, legends of Supplementary Figures 1 to 16). I opened PDF pages only for Figures 2d/e and 3b and Supplementary Figures 1 to 3 and 11. The paper links no analysis code; its only link is to the KlustaKwik spike sorter.

**Counts.**
- 32 claims have quotes; the link check has none.
- 4 claims carry statistics, 7 entries in all: three t-tests in Figure 2d and 2e, the permutation test for the path divergence, and the jitter test for pair 156-136.
- All 33 have criteria.
- Every claim rests on both datasets, except the link check, which rests on 000067 alone.

**Ids.** Ids from the two old files are kept and mapped in the opening comment. Two old claims are split: 000067's `fig2b-trajectory-selective` into the side-arm and central-arm claims, and its `ee188-example-session` into six session and pair claims. Two claims are new: `fig2d-layer-rates` and `fig2e-layer-discrimination`.

**Corrections to the earlier reading.**
- The text's "1172 pairs" and "n ~ 1422" are 117² and 142² in the PDF.
- Supplementary Figure 1 names the rats E, F, G and H, with F in layer 5. The earlier files did not have this.
- Figure 2d prints the unit counts: 411 in layer 2/3 and 222 in layer 5. Its pyramidal and interneuron counts (218 and 84 of 633) give 34.4% and 13.3%, not the 32.5% and 12.5% the Results state. I recorded this as a variant.

**Details the paper leaves open, with the readings named:**
- **Which dataset rat is which:** R-a, the datasets' EE, FF and GG are the paper's E, F and G (FF in layer 5, rat H missing); R-b, the names are unlinked and at most one rat is layer 5.
- **Trials:** correct trials only, or all trials.
- **Rate for widths and peaks:** occupancy-normalised (Figure 1c legend) or the Methods' density per trial.
- **Cross-correlogram bin width:** 1 ms or 0.5 ms.
- **How the "2 ms or less" peak width is applied:** the band test alone, or a pointwise run of 2 ms or less.
- **Units with both a peak and a trough:** unclassified, or left out of the denominators.
- **Which sessions:** the Figure 2a sessions, or all sessions (for the active fraction, field width, population vectors, odor, previous-trial coding and class fractions).
- **Field width:**
  - PSTH: all trials, left and right as two entries, or the side with the higher peak.
  - Width: the contiguous run around the peak, or the total length above 50%.
- **Odor and Figure 2d/e t-tests:** Student's or Welch's.
- **Figure 2d rate period:** trials only, or the whole session.
- **Figure 2e mean:** all neurons, or selective neurons only.
- **Cell-ratio average:** per session, per rat, or pooled.
- **Denominators:** for the reciprocal fraction, directed or unordered pairs; for pyramidal-to-pyramidal connections, all pairs or pyramidal pairs only.
- **Direction for the nearby pyramidal-interneuron probability:** one direction over directed pairs, or either direction over unordered pairs.
- **Session counts:** directed connections or distinct reference cells.
- **Position dependence:**
  - Trials: left and right apart, or together.
  - What counts: any significant region, or a significant region plus a non-significant one.
- **Thinning region:** positions 0.2 to 0.5, or one span per pair.
- **Facilitation and depression:**
  - Pairs: excitatory only, or all connections.
  - Peak height: the largest bin, or the sum over 1 to 4 ms.
  - Later spikes: inside a train begun after 200 ms of silence, or any spike within 40 ms.
- **Satellites:**
  - Size: two or more presynaptic cells, or three or more.
  - Count: spikes, or distinct cells.
  - The linear baseline: k times the one-spike probability, or independent summation.
- **Minor details given standard choices:** numbers of permutations and surrogates (1,000), the evaluation grid, and thresholds for "steady", "relatively constant", "small" and "several".

**Missing for the claims that need it:**
- Only three of the paper's four rats are in the data, so totals are judged as fractions or per rat.
- Task performance needs error trials. The CRCNS description lists correct trials only, so that claim may end up blocked.
- The paper does not give how soma positions are estimated (Figure 3c), so distance is measured by shank separation.
- Figure 7 reports no test.
- Fig. 2d and 2e bar heights are read off the figure, so the files report them without judging them.
