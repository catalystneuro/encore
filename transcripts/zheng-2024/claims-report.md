I wrote `claims/zheng-2024.yaml` and nothing else. The quote checker passes: 32 claims, 32 quotes, 43 statistical values, 0 problems. The style rules hold: no em dashes, no "rather", and the one value containing ": " is a quoted string, not a plain scalar.

**Text read**
- **Main text:** the author manuscript in PubMed Central (PMC11485410), with the STAR Methods and all main figure legends. The file's header calls it the version of record, but it is the PMC author manuscript.
- **Supplement:** the supplemental information of the version of record (mmc2.pdf, Figures S1 to S15 with legends), which is included in the same text file.
- **Code:** the paper's Zenodo deposit, doi:10.5281/zenodo.13247193. It is the authors' GitHub repository `samdeoxys1/within-session-representationl-drift`, tag v0.0, commit 93d6e33. Its notebooks keep their outputs, which give the 46 familiar and 8 novel sessions by name.

**Claims**
- 32 claims, all with quotes. 13 report statistics (43 tests), 32 have a criterion and 18 have expected values.
- Two claims (Figure 7 and Figure S15) use the two-photon imaging data and can't be tested on DANDI:000552. Those data are available from M. Bartos on request and are not deposited; both criteria say so.

**Details left open, and the readings named**
- **40% step filter:** the Methods say "max firing rate across trials", which could be the raw or the fitted maximum. The code uses the maximum of the fitted step function; the raw maximum is a variant.
- **Pool for the 212/3,184 count:** familiar and novel sessions together, or familiar only.
- **Explained deviance (20% ON, 14% OFF):** held-out cross-validated, or in-sample. The Methods say 5-fold cross-validation repeated 10 times; the code holds out 10% per split, kept as a variant.
- **Figure 4D correlation:** the legend says Pearson and the code uses Spearman, so Spearman is a variant.
- **"First passage times" (75–77% under two trials):** individual passage times or switch durations. A pure step predicts 75% under two trials only for individual passage times, so that reading is likely the right one.
- **Co-switching ("at least one trial"):** a per-session test on the count of co-switching pairs (what the code does), or a per-trial test. "Same trial" against the code's window of one trial is a variant.
- **Figure 5C units:** neurons with metrics averaged over fields (Methods), or fields matched across environments by field index (code).
- **Same-cell field pairs (781 and 41):** environments pooled or familiar only; any switch or switches of the same type.
- **Field width on one trial (Figure S13A):** the detected field's width, or the width above half the peak.
- **Switch time for the waveform control (Figure S1H):** the start of the switch trial, or the animal's entry into the field.
- **Figure S2 categories:** four switching classes, or switching against not switching.
- **Figure S5 units:** session with turns pooled (code), or session and turn.
- **Figure 1I test:** the paper names none and the code has none. The readings are per-session slopes tested with the Methods' default Wilcoxon signed-rank test, or the code's tentative regression on the median over sessions.
- **Claims with no test in the paper:** Figure 1D, 1H, 3D–F population, 4N–O, S8A–B and S14. These use the Methods' default tests (Wilcoxon signed-rank or rank-sum, Pearson), and each criterion says so. Where the paper states a contrast only in words, I set the decision thresholds myself and the criterion says it chose them (Figure 1H "twice as steep", the GLM-drop spread rule, a 0.05 absolute tolerance on r).
- **Figure S8C:** the paper's familiar p (3 × 10⁻¹¹) is significant even though r = 0.01, so that absence claim is judged on r, and the criterion explains why.
- **Figure 2E groups:** I took "Familiar" to mean the familiar sessions of the three mice that also ran a novel environment, which gives 12 sessions in the code's list, matching the n = 12 in the legend.

**Missing**
- Nothing that a claim needs from the text is missing.
- The imaging data are not public, as above.
- The code's session database and intermediate files are not in the repository, so the session list comes only from the notebooks' stored outputs.
- Numbers printed only inside figure panels were not read.
