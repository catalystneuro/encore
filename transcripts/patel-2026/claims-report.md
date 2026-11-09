I've written the claims file for DANDI:001454 at `claims/001454/10.1038-s41593-026-02413-x.yaml`. The quote checker reports 60 claims, 60 quotes, 64 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (PMC13633117, Europe PMC): main text, figure legends, Extended Data Fig. 1–10 legends, Methods, and the one supplement file fetched, which is the reporting summary. There is no PDF of the article, so no figure could be read; no claim relies on a figure image. I also read the bioRxiv preprint (v1) to compare Methods. It is cited once, for the 3-s baseline used for drinking bouts.

**Code.** The paper links no code ("available upon request"), so no repository or commit was read. All methods come from the Methods, legends and reporting summary.

**Counts.** 60 claims: 60 have quotes, 44 have statistics, 60 have criteria and 8 have expected values. They cover Fig. 1–6 and Extended Data Figs. 1–9; the opening comment notes that Fig. 1 and Extended Data Fig. 1 behaviour may not be in the dataset.

**Details the paper leaves open, and the readings named.** Seven shared method notes in the opening comment (M1 to M7) hold most of these:
- **Bout gap for calcium analyses:** measured from the last lick of the previous bout (from the preprint), or onset to onset as a variant.
- **Baseline for social bouts:** 3 s or 5 s.
- **Matching bout counts:** cut to the smallest count with bouts taken at random, or the first bouts.
- **Response measure:** mean z-score from 0 to 3 s; responsive neurons by ±1.98, with Wilcoxon as a variant.
- **Decoding:** which frames of a bout are sampled (whole bout or 0–3 s), the signal (raw trace or z-score), and how chance is shuffled (training labels or bout labels). The SVM's C is left at the library default, and five folds with one repetition is used, both stated as choices.
- **Spike detection:** upward crossings of 0 mV or of −20 mV. The 26 current levels (0 to 500 pA) and the repeated-measures design are read from the F degrees of freedom.
- **Input resistance window:** last 100 ms or last 50 ms of the step.
- **Fig. 1d time blocks:** two ways of splitting the 11 isolation days into four blocks.
- **Extended Data Fig. 4 factor levels:** UMAP clusters or time bins; UMAP settings are not given.
- **Bonferroni families:** two or four tests (Extended Data Fig. 1 and 6, Fig. 3).
- **Fig. 6 sidedness:** the printed P values match two-sided tests although the legends say one-sided, so both are named.
- **Extended Data Fig. 9:** the co-registration denominator, the 50-point time window, the number of decoding folds (10 implied by the degrees of freedom), and the chi-square table.
- **Absence claims with no named test:** these use the tests the Statistics section names.

**Inconsistencies in the paper, recorded in the criteria.**
- Extended Data Fig. 8g, h and j say there is no effect where Fig. 5d, 6c and 6f report one.
- Extended Data Fig. 1n has males drinking more alcohol, while the Results describe a trend toward higher female baseline intake.
- The Results cite the rank panels of Extended Data Figs. 2 and 3 the wrong way round.
- In Extended Data Fig. 9g, the error degrees of freedom (7350) do not fit 199 neurons.

**Missing.** The values of Supplementary Tables 1 and 2 (input resistance and firing threshold by housing and by rank) are not in the text. The two input-resistance claims therefore have a direction and test but no numbers. The paper also has no figure images and no code.
