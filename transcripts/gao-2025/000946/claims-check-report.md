The file is ready for an attempt (`ready: true`). I made 16 corrections, two problems remain open, and nothing was committed.

**Checker result:** `33 claims, 33 quotes, 83 statistical values, 0 problems`. It said 82 before my edits; the new value is the p = 1.0 entry added to fig5b.

**Changes, by claim**
- **Header, test against baseline:** I took out reading B3 (a paired signed-rank test on raw rates). The paper names a two-sample Wilcoxon test, so a paired test is not a reading of it. B3 stays as a variant that decides nothing.
- **Header, dSTTC:** The formula was presented as the paper's, but it was rebuilt from Cutts and Eglen (2014). It is now named as reading D1 and flagged for checking against the PDF. Two more details were agent choices and are now named as open readings:
  - what each test counts: the pair's mean over trials, or every pair-trial;
  - the window length: 67 ms bins, or 50 ms bins (the only other bin the paper names).

  I also added the Kruskal-Wallis step that comes before the post hoc tests.
- **Header, STTC:** The 20 ms window is not stated for the STTC, so the file now says it is taken from the dSTTC. Mean and median are both readings for ranking STTC changes, since the Fig. 10 legend doesn't say which it shows.
- **fig5b:** Added the p = 1.0 results the paper reports, as fig5a already had.
- **fig6c:** The criterion now also requires 30 and 300 Hz to show no delayed response. The text says delayed responses start at 1500 Hz.
- **fig7b:** The direction of the 0.6% versus 30% difference was a guess; the legend gives none. Both directions are now tested.
- **fig10a:** Added the legend's finding that the other two directional correlations did not change during sonication.
- **fig10b, fig11c, fig11d:** These now run every dSTTC reading. fig11d accepts a change in either direction for the FSUs, which the legend calls bidirectional. fig11c reads the legend's 1421 pairs two ways.
- **fig10c, fig10d:** Windows and normalization now follow the header's readings. fig10d ranks by mean or median, not median only.
- **fig10e:** "Changes most" took the absolute value, which means nothing for a ratio. The readings are now the signed change and its size, defined separately for differences and for ratios.
- **pathway-follows-local-prf:** The criterion demanded the same single best PRF, which is stricter than the paper. The Discussion says "the same PRF range" (1500 and 3000 Hz), so both best PRFs now only need to fall in that range. The Discussion is added as a source.
- **fig11b:** The statement's "least response at 300 Hz" is now actually tested. The post hoc tests are marked Bonferroni-corrected, as the Methods state.

**Still open**
- The dSTTC equation is missing from the text I read. Reading D1 should be checked against the PDF.
- The Discussion says high PRF with 90% DC lowers activity (Fig. 7). It has no claim, and I added none because the paper reports no test for it.
