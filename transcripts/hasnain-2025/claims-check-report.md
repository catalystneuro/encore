I checked the file; it is ready for an attempt. I made seven corrections and left two problems open. Nothing is committed or pushed.

**Checker result:** `claims/hasnain-2025.yaml: 19 claims, 19 quotes, 9 statistical values, 0 problems`. The result was the same before and after my edits.

**Changes, by claim:**
- **ed3-letn-fast-switch:** the quote stopped at "movement onset", before the 105 ± 36 ms value (n = 27 sessions) that the statement and expected value use. I extended it to the end of the sentence.
- **map-session-selection:** the source said Results paragraphs 1 and 3, but the 1116 bilateral ALM neurons are in paragraph 4, the decoding paragraph. I changed it to paragraphs 1 and 4.
- **fig2e-potent-only-units:** I moved the source from Discussion paragraph 2 to paragraph 1. The text has no paragraph breaks, so this rests on the sentence following the Discussion's opening with no change of topic.
- **fig3c-network-beats-linear:** the criterion now notes that the Results give 1954 neurons and the Figure 3c legend gives 1945 units.
- **fig4e-medulla-null-lower-dimension:** the statistics recorded n = 16 sessions, but the paper gives no n for this test. The field now says so.
- **Header M7 (selectivity):** the Figure 1i legend uses an uncorrected p < 0.05 shuffle test. I added it as a variant; the Methods' Bonferroni threshold stays the main reading.
- **Header M9 (dimensionality):** ref 70 is Recanatesi et al. 2022, a scale-dependent measure of dimensionality. Reading N2 (participation ratio) is now marked as a stand-in, because the paper does not name the measure or the scale.

Everything else holds up against the paper: statements, sources, statistics (results only, no thresholds used to count units), expected values and tolerances. The criteria's methods come from the Methods, the legends, or the subspaceID code. Every main finding has a claim, and all of them come from this paper. The claims on the paper's own recordings cannot be tested, because those data are not public.

**Still open (recorded under `checks`):**
- The paper contradicts itself on the ALM and medulla sessions: 16 in the Results and Figure 4, 11 sessions from 7 mice in the Methods. It also gives 1116 bilateral ALM units in the Results and 2016 in the Methods. Both readings stay in the criteria.
- Variance-explained reading V2 normalizes by total variance, which departs from the Methods' formula. I kept it because the Results describe "78% of the variance" and the values add up. V1 is the formula's own reading.
