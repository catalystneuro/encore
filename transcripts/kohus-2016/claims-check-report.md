The file is fit for an attempt, and its new check entry says `ready: true`. Nothing is committed.

**Checker:** `44 claims, 43 quotes, 43 statistical values, 0 problems` (before my edits it was 43 claims and 0 problems). Every quote matched word for word, including the one in the new claim.

**Changes, by claim**
- **Header comment:** it said the extracted Table 4 had lost its type-parameter columns. It hasn't, so the comment now gives the values and notes two places where Table 4 and the Figure 11 legend disagree: CCK+BC to PC τr (71 ms against 12.9 s) and PV+BC to PV+BC τe (23.7 against 2.37 ms).
- **M6:** I worked out by hand that the p-values 9.42e-4, 0.0175 and 0.0181 come from an uncorrected 2 × 2 Pearson chi-squared test on the Figure 3A counts. The note now says so, and the tests are to be run that way.
- **table4-model-parameters:** CCK+BC τr changed from 12.9 s to 71 ms, Table 4's value for the best model, which is the model this claim tests. The legend's 12.9 s stays as a named variant. The statement and the `inferred` note are corrected to match.
- **fig13-pvbc-pc-recovery-halftime:** tolerance changed from 147.8 to 152.2 ms. Both quartiles lie 152.2 ms from the median.
- **table2-pvbc-aac-features:** added the Table 2 p-values for input resistance (1.0e-4) and rheobase (6.0e-4), two features the statement names.
- **fig3-cp-pv:** the paper's counts give p = 3.2e-4, or 1.2e-3 with Yates correction, not the printed 6.21e-4. Both are now shown.
- **fig2b-pvbc-aac-clusters:** noted that the paper's counts give 80.8%, not its 83%. The accepted range covers both.
- **fig6-pv-trains-depression:** the statement says IPSCs stay synchronous under EPI, but the criterion never tested it. I added a test that uses the onset rule of `fig6-cckbc-async-onset`.
- **fig5db-recovery, fig6, fig9 (two claims), fig10bd-be, fig11-model-pv-udr:** several tests and margins were not from the paper (the Spearman tests, the 10% and 20% margins, 0.95 at the 11th AP, the 10% error gain). They are now marked as standard choices.
- **fig10-cck-cck-heterogeneity:** added a second reading of which trains count, from the Fig. 10Ac legend: release above 10 Hz, so 20 Hz and up.
- **fig13c-optogenetic-swr:** the window with no evoked SWR is 100 ms in the Results and 200 ms in the Figure 13 legend. Both readings are now named.
- **New claim `sipsc-continuum`:** the finding that the spontaneous IPSCs form a continuum (Results, IPSCs onto interneurons are more rapid than on PCs, paragraph 5) had no claim.

**Still open**
- I could not find the contingency table behind the 6.21e-4 in `fig3-cp-pv`; none built from the paper's counts gives it.
- Figure 8A labels the CCK+DTI pair example n = 3, while the Results say n = 4. The claim keeps n = 4.
- Values printed only inside figures were not read, because the PDF could not be rendered here either. These include the Figure 5Db asterisks, which would show at how many intervals PV+BC and CCK+BC differ.

`git status` also shows untracked files I did not create (`.bashrc`, `.idea`, `scripts`, among others). I left them alone.
