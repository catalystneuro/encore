**A. Outcomes (25 claims in the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| counts-neurons-subjects | reproduced | Cell 16 gives 1864 unit rows (+1) and 59 distinct subject_id. Counting duplicated trains once gives 1798, also within ±186.3. |
| counts-sessions | reproduced | Cell 18: the 87 (subject, session) pairs in the files equal the 87 in Online-only Table 1. The Methods' 89 is 2 more. |
| table1-demographics | partially_reproduced | Cell 20: age and sex match for 56 of 59 subjects. C24 and H33 differ in age, H48 in age and sex, so the files have 26 F / 33 M against the table's 25/34. |
| task-structure | partially_reproduced | Cell 22: 79/87 sessions have 100 encoding trials with 100 distinct files (7 have 50, one has 97). The label split is 50/50 and there are 5 categories in 87/87. |
| new-old-label-coding | not_reproduced | Cell 24: under the stated coding (0 = old), test 1 holds in 0/87 and test 2 in 1/87. With the labels reversed, test 1 holds strictly in 79 and test 2 in 86, so both hold in at least 78/87, which is "most". |
| ttl-codes | partially_reproduced | Cell 27: 78/87 files meet every part. 9 files have extra codes (0, 4, 22, 23, 98, 99) and 7 files have trials out of order. Lengths and timestamps match in 87/87. |
| experiment-ids | partially_reproduced | Cell 29: both ids are in the stated sets in 83/87 files. The other 4 use 81/82, 82/83 or 80/82, which their data_collection field confirms. |
| session-dates | partially_reproduced | Cell 31: 86/87 dates fall on the 1st; H28_48 is 2010-03-13. H44 has year 2000, outside the H-site span (2006–2016). |
| units-table | partially_reproduced | Cell 33: the columns are present, but IsolDist is stored as IsolationDist. Each unit has exactly 1 electrode and the rate is 98.4 kHz (within tolerance). SNR is not finite for 86 units and IsolationDist is NaN for 493. |
| electrodes-table | not_reproduced | Cell 35: `imp` is empty for all 887 electrodes, which the criterion's "not reproduced" clause covers. x/y/z are also missing for 99 electrodes in 8 files. |
| isi-criterion | partially_reproduced | Cell 37: 1858/1864 units (99.7%) are below 3% with sorted times; the stored-order variant gives 1860. This is ≥95% but not every unit. |
| fig5a-mtl-locations | reproduced | Cell 39: all 1864 units are in left or right amygdala or hippocampus. |
| fig5c-auc-all | reproduced | Cell 43: mean AUC 0.753 (within 0.74 ± 0.10), SD 0.094 (within 0.10 ± 0.01), n = 87. |
| fig5c-auc-sites | reproduced | Cell 45: CS 0.760 ± 0.086 and TWH 0.688 ± 0.138. All four values are within tolerance; Welch p = 0.16. |
| fig5b-roc-asymmetric | reproduced | Cell 47: mean z-ROC slope 0.782 over 82 sessions, t-test against 1 gives p = 4.3e-9. The Wilcoxon (p = 2e-8) and pooled-slope (0.816) variants agree. |
| fig5d-confidence-accuracy | reproduced | Cell 49, fixed split: high 80.1% against low 60.9%, paired p = 3.2e-16 over 84 sessions (3 left out). The dynamic split also gives p = 1.3e-11. |
| vs-cells-proportion | reproduced | Cell 53: 332/1864 (17.8%), both within tolerance. The code's window gives exactly 343 (18.4%). The shuffled null is 4.1%; the paper states no chance level. |
| ms-cells-proportion | not_reproduced | Cell 55, main reading (Methods' window, all 50/50 trials): 118 (6.3%), outside 146 ± 14.6. Five more seeds give 108–115, so the miss is not seed noise. The code's choices (correct trials, 0.2–1.7 s) give exactly 146 (7.8%). |
| dual-cells-proportion | not_reproduced | Cell 57: 13 (0.7%) against 26 ± 2.6, about what independence predicts (21). The code-choice variant gives 25 (1.3%). |
| fig5f-site-proportions | partially_reproduced | Cell 59, main tests: none of the 3 Fisher tests finds a difference, but only 3/6 values are within tolerance (CS MS 6.2%, CS dual 0.7%, TWH VS 22.1% are outside). The code-choice variant gives 6/6. |
| twh-sessions | reproduced | Cell 61: 9 T-labelled sessions (from 8 subjects), all with institution "Toronto Western Hospital". |
| previous-release-link | partially_reproduced | Cell 63: 64/65 sessions of Faraut 2018 Table 1 are found and agree (98.5%). Session 98 (H48) is missing. Age and sex match for 39/42 subjects. |
| previous-release-additions | partially_reproduced | Cell 65: 23 new sessions and 17 new subjects are within tolerance. New neurons are 325, outside 288 ± 28.8. |
| fig4-example-vs-neuron | reproduced | Cell 67: CS58_132, channel 177, unit/electrode row 4, Right Amygdala. ANOVA p = 1.2e-22 and the top category is animals (6.75 Hz against ≤0.85 Hz). |
| fig3-example-vs-neuron | blocked (data_missing) | The paper's own Online-only Table 1 has no session 144. I checked the archive: the API lists 87 assets at 0.220126.1852 and none is named for session 144; the notebook read identifiers from all 87 files and none is 144. A candidate exists (cell 69: T103_2009 unit 2, channel 140, right hippocampus, phones preferred, p = 1.3e-9), but nothing links it to the figure's ID, so only that much could be tested. |

Tally: 10 reproduced, 10 partially_reproduced, 4 not_reproduced, 1 blocked.

**B. Problems**

1. [does not affect a conclusion] Cell 33 hard-codes the line "IsolationDist column description: 'IsolDist' (read from the files' VectorData description)". The text is a literal string and is never read from the files, so the output claims a check that did not run. units-table is partial either way.
2. [does not affect a conclusion] Cell 7 also hard-codes "stated unit 'seconds' (NWB)" without reading the attribute. The clock check in cell 13 (830 against 115 responsive units; category effect peaking at lag 0) covers the substance.
3. [does not affect a conclusion] `nomem.auc` tests `tp[0] != 0`, while calcROC_AUC.m tests `TP(1)~=1`. After `adjust_hf`, F is always ≥ 1/(2n), so both prepend (0,0) and give the same AUC. Its docstring calls it identical to the MATLAB, which is not strictly true.
4. [does not affect a conclusion] `nomem.zroc_slope` says the sixth point is (1,1); after adjustHF it is (1−1/2n, 1−1/2n). Dropping it matches calcZROCSlope.m. Cell 41 leaves out 5 sessions with fewer than 2 distinct F values, a rule of the author's own that is not stated as an assumption. It is harmless at p = 4e-9.
5. [affects a conclusion, as context only] ms-cells, dual-cells and fig5f fail only under the Methods' text reading. Under the code's reading (NWB_singleCellAnalysis_release.m, which I fetched at 1d95162: correct trials only, 200–1700 ms), VS = 343, MS = 146 and dual = 25 come out exact or within tolerance. The paper's numbers were evidently produced by the code, not by the procedure its text describes. The claims file reads the paper correctly and the notebook applies the criterion correctly, so the outcomes stand; this belongs in the report as the explanation.
6. [does not affect a conclusion] fig5f: the Fisher tests compare 77 TWH units with 1787 CS units and have little power, so "no test finds a difference" says little. The criterion prescribes these tests, so this is a remark only.
7. [does not affect a conclusion] new-old-label-coding: `reversed_1_partial` (>50% of label-1 images found in the encoding block) is a threshold of the author's own. The strict counts (79 and 86) already give "most", so the outcome does not depend on it.
8. [does not affect a conclusion] Three findings appear in the notebook outputs but not in its narrative: 7 sessions store only 50 encoding trials, and only 26–29 of their 50 old images appear in their own encoding block (cell 25); every spike time of H27_58 units 35 and 37 is stored twice (cell 37); and the institution field is misspelled. These are data findings, not analysis errors.

Checks that passed:
- **Code reading:** `bootstrap_p` matches bootstrapMeanEqualTest.m (fetched; unstudentized, varCorrection = 0, two-sided). ANOVA, window and trial selection follow the claims file.
- **Synthetic tests:** `window_rates` counts correctly with (start, stop] edges. `auc` agrees with sklearn (0.7514 against 0.7522; the difference is the 0/1 adjustment). `bootstrap_p` rejects at 5.4% under the null. `zroc_slope` returns 1.0 for an equal-variance model and 0.8 for SD ratio 1.25. `accuracy_fixed` is correct.
- **Leakage:** none applies here.

**C. Not checked**

- What `imp` holds in the files: NaN, a sentinel such as −1 or 0, or empty strings. Cell 35 prints only the empty count. Printing `el.imp.unique()[:10]` and its dtype would confirm that electrodes-table's "empty for every electrode" is real.
- The units table's actual column description for IsolationDist (problem 1). Printing the attribute would settle it.
- The 4 sessions dropped from `info` in cell 3: not checked here, because I truncated that output myself. The counts in cells 16 and 18 cover them.
- helper.dynamic_split in the Python code: I did not fetch it, so reading (b) of fig5d is unverified. Reading (a) alone decides the claim.
- The live Europe PMC table parses. Their totals rows (59/87/25/34 and 42/65/15/27) match the paper text and Faraut's abstract, but per-row parsing of Faraut Table 1 (session 98 under H48) was not cross-checked. Printing `far` in full would allow it.
- Per-unit p-values for the VS and MS sets. Saving `cells` with p-values would let the code-choice counts of 343 and 146 be checked unit by unit against the paper's code.
