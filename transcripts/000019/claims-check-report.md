I checked the claims file against the paper and changed ten things; I think it is ready for an attempt, with four problems left open.

**Checker result:** `claims/000019/10.1038-nature11911.yaml: 22 claims, 22 quotes, 17 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim:**
- **Header, consonant labels:** The file said the labial, coronal and dorsal labels came from Fig. 4c, a main-text figure the file itself says was never available. Its second reading also put /h/ in the dorsal set, which nothing in the paper supports. The labels are now read from the place features of Supplementary Figure 12. /w/ and /j/ are added to /h/ and /r/ as consonants no sentence places, and /h/ is left out under both readings.
- **fig1f-h-phonetic-contrasts:** Added citations for two choices it made without sources: the Fig. 1h legend ("active lip electrode for /u/") for picking an electrode with a positive lips weight, and Fig. 4b for the +250 ms vowel time.
- **fig2a-lips-dorsal:**
  - The Methods' "associated p-value" was taken as the whole-model F-test only; it is now open, with the articulator's own coefficient test as a second reading.
  - The weighted mean position was not the paper's measure; it is now open, with the median position of the top 10% of weights (from the Methods) as a second reading.
  - The paper states the lips-above-tongue finding for the map averaged over subjects, so it is now judged on the three subjects pooled, not required in every subject. Each subject is still reported.
- **fig2b-somatotopic-sequence:** The criterion now says plainly that its rule for reading the dorsal-to-ventral order is the file's own and not the paper's.
- **suppfig3f-dv-sequence:** Added the legend's convention that values above the dashed line are dorsal-posterior shifts. The paper does not say which map of each pair is shifted, and swapping them swaps the two sides. So the claim is now judged on the size of the sign change, and the side that comes out positive is reported.
- **fig3d-timing-sequence:**
  - Whether the mean + 2.5 SD threshold is computed per subject or pooled is not in the Methods; it is now open.
  - The second onset reading was only "shown"; both readings are now run.
  - The paper gives no acoustic-onset threshold; a standard choice is now named and labelled as such.
- **suppfig7-no-latency-difference:** Named as open which electrodes are compared (71 + 67 is fewer than the 266 vSMC electrodes). Added a second reading of "across the geunon".
- **pca-nine-components:** The time range is a method choice, so the result now has to hold under each reading. It previously said "under one reading", which goes against the file's own header rule.
- **fig5c-separability-timing:** Added the four consonant groups of the Fig. 5a legend (labial, coronal, dorsal, sibilant) as a reading of the clusters.
- **suppfig9-pc-articulator-weights:** The legend's "over jaw and larynx (P < 0.001 for each)" may also cover tongue; both readings are now named.

**Still open, and recorded under `checks`:**
- The baseline window in the first baseline reading (-1000 to -500 ms) is the file's own choice. The paper says only "baseline data".
- fig4c-d-hierarchy decides the consonant tree with a two-thirds purity rule the paper does not give.
- fig3d tests "jaw and larynx aligned to the CV transition" only as their onsets coming after those of lips and tongue. That is a weaker test than the sentence, but the paper gives no measure of alignment.
- I could not check the figure readings (Supplementary Figures 1d and 12, and the significance marks on Supplementary Figure 5), because no PDF renderer was available in this run.

All of the paper's main findings have claims, and every claim comes from this paper.

**Ready:** yes (`ready: true`). Nothing was committed.
