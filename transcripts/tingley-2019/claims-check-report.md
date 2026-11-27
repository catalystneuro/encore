I checked the claims file against the paper, corrected what the paper shows to be wrong, and marked the file ready for an attempt.

**Checker result:** before my changes it reported `39 claims, 39 quotes, 13 statistical values, 0 problems`. After them it reports `claims/tingley-2019.yaml: 39 claims, 39 quotes, 12 statistical values, 0 problems`.

**Changes, by claim**
- **fig1d-phase-locking:** I removed the Rayleigh p < 0.05 statistic. It is the threshold used to count the 1840 phase-locked neurons, which makes it a method, not a result.
- **fig4d-compression:** the criterion used a cutoff at compression factor 15 and a fallback at 5, neither from the paper. I replaced them with the paper's "~20" as an expected value with a 10% tolerance (18 to 22).
- **fig5b-nrem-and-rates:** the statement now says "significantly lower", as the Results do. The NREM thresholds in the criterion are now marked as set by the writer, not the paper.
- **fig4b-pre-post-unchanged, fig4c-temporal-bias:** these presented p < 0.05 as the paper's level. The paper states no level, and the criteria now say so.
- **fig7e-content-independent:** p < 0.05 was attributed to the Figure 7E legend for the rank-sum test. The legend's level applies to the single-neuron t-tests, so 0.05 is now named as a reading.
- **fig1c-hfo-each-animal, fig2-confined-to-ls, fig5e-state-coupling, ls-spikes-not-locked-to-ca1-ripples:** windows, bounds and tests the paper does not give are now marked as set by the writer.

The other claims hold: statements, quotes, sources, expected values and tolerances match the paper. Every main finding has a claim, and all claims come from this paper.

**Still open (recorded under `checks`)**
- **dataset-composition:** the Methods attach the 62 recordings (37 with CA1, 25 with CA3) to "Figure 6", the optogenetics figure. The file reads them as the Figure 7 dataset; the content supports that, but the paper does not say so.
- **fig7e-content-independent:** Figure 7E has seven content-independent features. The text names only four, and the Methods define two more. The seventh is never named, and the main figures are not available to read it from.
- **figs2-post-rate-increase:** the file assigns the counts printed on Figure S2A (1754, 2315 and 1373 neurons) to LS, CA1 and CA3 in that order. This is inferred from the order of the supplement's extracted text, not from the figure.
- I did not re-read the code repositories the opening comment cites (DavidTingley/papers at 9f4cd48, buzcode at e615663).

**Ready:** yes (`ready: true`). Nothing was committed or pushed.
