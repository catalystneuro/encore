**A. Outcomes** (41 claims in the claims file: 2 tested, 39 blocked)

| Claim | My outcome | Reason |
|---|---|---|
| fig3b-photometry-continuous-only | reproduced | Cell 18: with the repeated-measures ANOVA, post hoc errors pooled across frequencies and the Methods baseline, continuous gives BH p = 6.6e-5 to 9.5e-5 with Stim higher. The three train frequencies give p ≥ 0.46. With separate paired t-tests per frequency, continuous gives only p = 0.048 to 0.11 (cell 19: uncorrected p = 0.04, n = 5), so the result depends on the error term (problem 2). |
| fig3c-photometry-opsin-vs-control | reproduced | Cell 21: with pooled errors, continuous gives BH p = 0.00074 to 0.0028 with opsin larger (paper p = 0.002), and 5 to 20 Hz give p ≥ 0.66. Holds in 64 of 128 readings. With separate Student t-tests, continuous gives p = 0.098 to 0.19 and the claim fails. |
| 9 acute silicon-probe claims (fig3-optotag-counts, fig3e, fig3f, fig3g, fig3i ×2, fig3j ×2, fig3k) | blocked, methods_underspecified (the notebook says data_missing) | Cell 4: the files hold raw 30-kHz voltage and no units, so these claims need a new spike sort. The paper gives no Kilosort version and used manual Phy curation. Cells 6–7: the tagging pulses are on ADC1 or ADC2, and nothing records which laser colour each channel carries. |
| 6 chronic claims (chronic-optotag-count, fig4c ×2, fig4d, fig4e, fig4f) | blocked, metadata_insufficient plus methods_underspecified | Same sorting blocker. In addition, cell 4 shows no intervals in any file, so rotation onset and direction are absent, although the dandiset description says they are included. There are 4 chronic subjects against the paper's 3 mice. |
| 11 juxtacellular and tracing claims (Fig. 1, Supp. Fig. 1) | blocked, data_missing | The asset list I queried at 0.261103.0758 has 66 files: 34 ecephys and 32 photometry. None is juxtacellular or histology data. |
| 5 slice claims (Fig. 2a–c, Supp. Fig. 2b,c) | blocked, data_missing | No slice recordings in the dandiset. |
| 8 open-field claims (Fig. 2e–i, Supp. Fig. 2d–f) | blocked, data_missing | No video or tracking in the dandiset. |

**B. Problems**

1. [does not affect a conclusion] `vtapno.regular_onsets` drops valid 10-Hz trials. It rounds interval lengths to 0.01 s and keeps those within 0.01 of the mode. Lengths of 2.905 s round to 2.90 or 2.91 from float noise, and the difference of 0.01 fails the `<= 0.01` test.
   - On synthetic onsets taken from the files' timings, 9 to 11 of 23 trials were dropped from 10-Hz files.
   - This explains why `diff_10hz` changes between the "all" and "regular" rows (main reading 0.552 against 0.694), although only the exp-5 5-Hz file has stray intervals.
   - The 12 readings with 10-Hz p < 0.05 and the 8 with 20-Hz p < 0.05 reported in cell 18 all come from the corrupted "regular" rows. The "all" rows have 10-Hz p ≥ 0.094.

2. [affects a conclusion] Both outcomes depend on the post hoc error term, which the notebook chose (`within_opsin_tests`, `opsin_vs_control_tests`, `posthoc="pooled"`). The claims file names only "paired Pre against Stim per frequency" and "unpaired opsin against control per frequency".
   - The pooled form averages the variances of the four frequencies. Opsin continuous deltas have SD 5.28; the trains have SD 0.38 to 0.96.
   - Pooling therefore shrinks the continuous standard error and inflates the train standard errors, which pushes both halves of each claim in the claimed direction.
   - The notebook justifies this by Prism's default (Methods name Prism v10), but nothing confirms that default for a design with both factors repeated.
   - What supports the reading: the pooled p-values match the paper's magnitudes (p < 0.0001; 0.002), and the separate tests do not.
   - Under separate tests, 20 Hz is p = 0.031 uncorrected (all 5 opsin mice positive).
   - I accept the pooled reading, but the result is fragile.

3. [does not affect a conclusion] For the "plain" two-way ANOVA with pooled errors (`within_opsin_tests`), the comparison is not paired, which the claims file asks for.
   - It uses SE = sqrt(2·MSE/n) with df 32 from 5 mice.
   - Its MSE includes the Pre cells, which have zero variance by construction under the Methods baseline with mean/SD z-scores (cell 17: Pre = 0.0). That halves the MSE.
   - It gives the smallest p-values (3.8e-6). The repeated-measures pooled readings carry the conclusion without it.

4. [does not affect a conclusion] For fig3c with pooled errors, the "rm" variant uses dfe = 24, which treats each mouse's four frequencies as independent. A mixed-ANOVA simple effect would use a combined error with Satterthwaite df. The continuous margin (raw p ≈ 2e-4) is large enough that a smaller df would not change the outcome.

5. [does not affect a conclusion] The blocked reason for the 15 silicon-probe claims is given as data missing (cells 0 and 23). The raw data and light timing are present, and reading all the raw data was estimated at 1.4 h (cell 8), so the block is neither data_missing nor too_large. The reason should be the unspecified sort and curation, plus the missing laser-colour, protocol and rotarod labels.

6. [does not affect a conclusion] In 12 of 32 files the isosbestic fit has R² < 0.30 (cell 11; control-1 Cont has R² = −0.01). No variant tests whether the outcomes depend on the 405-nm correction. The continuous responses are large, so a change is unlikely.

7. [does not affect a conclusion] Cell 15 asserts that the stimulation table and the signal share a clock for control and train files without showing it. Only the opsin continuous files were checked.

I found no misreading of the paper in the claims file for the two tested claims. Every number in cells 17–22 derives from the loaded files. I recomputed the main-reading p-values from the printed per-mouse values and they match: repeated-measures pooled continuous BH p = 9.4e-5, and fig3c pooled continuous p = 9.2e-4.

**C. What I could not check**

- **Prism's post hoc error term.** I could not confirm which error Prism uses for a two-way design with both factors repeated, or for a mixed design. Printing `p_raw` per frequency for both error forms, with the error SD and df, would let a reader judge problem 2 directly.
- **Trial counts in the "regular" reading.** The notebook does not print trial counts per file for this reading. That table would have exposed problem 1.
- **Recoverability of the silicon-probe labels.**
  - Laser colour: a scan of every acute and chronic recording listing which ADC channel carries 210-pulse trains, and whether those trains differ in amplitude or order, would show whether colour can be inferred.
  - Rotarod timing: no chronic ADC channel was scanned for 2-s rotation-timed signals (only one chronic file was examined, and ADC8 of its recording1 holds an unexplained analog signal), so whether rotation timing survives in the ADC data is open.
- **Isosbestic dependence.** A variant using 470-nm dF/F without the 405-nm fit would settle problem 6.
