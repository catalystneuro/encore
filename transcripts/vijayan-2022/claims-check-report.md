I checked `claims/vijayan-2022.yaml` against the paper, made 18 corrections, and the file is ready for an attempt.

**Checker result:** `claims/vijayan-2022.yaml: 45 claims, 45 quotes, 11 statistical values, 0 problems`. Before my edits it gave the same line with 10 statistical values; the new one is the `fig4b` p-value below.

**Changes, by claim** (each is also logged under `checks`):
- **leave-higher-stay-lower:** Dropped the reading that pools this paper's own chambers. The sentence cites ref. 16, and its 1205 + 2744 = 3949 searches match the 3979 eggs from the three ref. 16 chambers in fig. S3.
- **fig1d-no-substrate-marking:** Marked the "CI above 0.5" bound as set by the file, since the paper reports no test.
- **fig1f-tarsi-proboscis:** The first statistics entry wrongly covered all three comparisons at P < 0.005. It now covers the first two; the third is P < 0.001. The legend's Bonferroni correction for seven comparisons among eight groups fits one control against seven groups, so that is now the reading taken.
- **fig2-earlier-merge-three-choice:** The text compares against Fig. 2A to C, not the 0/200 chamber alone. I added a reading that includes the Fig. 2B and 2C chambers, and noted that the CS 0/200 curves never merge (Fig. 5A legend).
- **fig2efg-inhibit-200-after-0:** The stated reason for leaving out bins below 5 s misdescribed the paper, which says rates start low for the first 10 s. I corrected it and added a 10 to 30 s window as a variant.
- **fig3c-bounce-faster:** The text does not name the bin marked with an arrow in Fig. 3C. It is now marked open, with readings 5 to 10 s and 0 to 5 s.
- **fig3d-dwell-before-fast-eggs:** The order of the gray shades is settled by the Fig. 3F legend (918 eggs, "two less than (B)"), not just by the text's wording.
- **fig3e-rate-after-long-absence:** The 240 s split was not one of the M4 bin edges. I set the bins so it is.
- **fig3f-motor-program-not-faster:** The legend does not say whether the fast-egg trace pools the three chambers, so both readings are listed.
- **fig4b-faster-middle-preferred:** The legend's "also <0.001" implies the main comparison is also P < 0.001. I added it as a statistic and raised the criterion from p < 0.05 to p < 0.001. Whether the gray reference curves are pooled is now marked open.
- **fig6b-softer-preferred:** Marked the 0.1 bound for "little effect" as set by the file.
- **fig7a-screen-ddc-hits:**
  - The statement now says the 110 are lines tested in the control condition, not "controls".
  - Ranking by fold change matches the order of Table S2 and fig. S5.
  - Each ranking is also run on only the lines with at least 5 eggs per fly, as the Fig. 7A legend does.
- **fig7ik-not-egg-number-or-motor:** Replaced an invented Spearman test with the paper's own test for groups of flies (eggs per fly, 31 C against 18 C). The correlation is kept as a variant.
- **fig7l-dopamine-gal80-rescue:** Noted that which comparisons are displayed is only in the figure, so the ones used are a reading.
- **fig8a-d1-receptor-mutants:** The expected value named the first mean (40) as CS, while the criterion says the order is only in the figure. It is now "first group, CS assumed".
- **fig8k-agarose-intact:** This is a claim that there is no effect, and it was judged at p < 0.001, which makes finding no effect easier. It is now judged at P < 0.05, the level the paper states (Fig. 1F legend); p < 0.001 is kept as a variant.
- **figs2-search-definition-robust:** Added `fig3c` and `fig5c` to `depends_on`, since their chambers are in fig. S2. Clarified that only the last two alternative definitions are cut at the previous egg plus 1 min.

**Still open (logged, not settled):**
- Paragraph numbers in the sources can't be checked, because the text file has no paragraph breaks.
- In `fig7a`, the default 10% tolerance on 110 and 111 lines allows up to 115, which says almost nothing for a count of lines. I kept it because the paper gives no spread.
- Numbers printed only inside the main figures (bin p-values, merge arrows, group order in Figs. 1F, 7L to N and 8A) can't be read, because the main-text PDF is not under `paper/`.

Every main finding has a claim. All claims come from this paper; the leave-higher numbers rest on ref. 16 data, but this paper reports them with its own p-value.

**Ready:** yes (`ready: true`). Nothing is committed or pushed.
