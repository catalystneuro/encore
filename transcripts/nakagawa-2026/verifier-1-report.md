**A. Outcomes** (45 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| link-unit-mice | partially_reproduced | All 27 of 27 tetrode mice are matched (cell 20). Two strain labels disagree (01398 and 01431 are "AD" in the file names but young WT in the paper), and two sexes disagree (00703, 00789). By the criterion, ≥90% matched with some disagreeing is partial. |
| link-photometry-mice | partially_reproduced | 10 of 11 mice are matched; 00163 is missing. Sex disagrees for 00265. The mice present account for 9 WT and 8 APP-KI hemispheres, against the paper's 10 and 8 (cell 22). |
| units-recorded | not_reproduced | Under reading P, young WT has 635 units against 479±48, so it fails; APP-KI has 891 against 846±85, so it passes. Under reading F both fail (cell 24). The criterion needs both. |
| ed4a-spike-type-distribution | blocked (data_missing) | The files hold no waveforms, so the three-class NS/RS/WS table cannot be built. Part of the claim could be tested (problem 4). |
| ed4b-spike-width | blocked (data_missing) | The files hold no spike widths. |
| ed4c-higher-firing-rates | reproduced | Reading (a), groups P: principal cells Z=−7.18, p=6.8e-13; interneurons Z=−2.21, p=0.027; APP-KI is higher in both (cell 26). The result also holds under groups F. Reading (b) cannot be computed. The rate used in (a) matches the source `meanFR` (r=0.998). |
| fig2d, ed5, fig2j, fig2g, fig2f, fig2i, fig2k, fig2l, ed8, ed9, ed7, fig6h, fig6i (13 claims) | blocked (data_missing) | The unit files have no trial, odor or lick times (cell 3). The archive confirms this: the version's `variableMeasured` lists only Units and ProcessingModule, and 43 sampled asset records agree. Only the cell-count expectations can be compared, and they are off: old WT 796 principal cells against 671±67, L-DOPA 199 against 144±14, saline 217 against 132±13; old APP-KI 663 is within 618±62. |
| fig3b, fig3d, ed10, ed1 | blocked (data_missing) | The archive holds no histology; all 3855 assets are NWB files with Units or ProcessingModule. |
| fig4b-wt-dopamine-t1 | partially_reproduced | With sessions as units and reading B2, the G2 T1 means are 1.29, 1.67 and 0.55, all within tolerance. With the rank-sum test every significance condition holds. With the signed-rank test, Odor-1 at T5 is not significant (p=0.084). With mice as units, the signed-rank test cannot reach p<0.05 (cell 37). |
| fig4c-app-dopamine-delayed | not_reproduced | The error share is 40.0% under B2, within tolerance. But under sessions as units, Odor-1 in correct sessions is already significant at T2 (p≤0.0005), and Odor-A in error sessions is not significant at T1 (p=0.15 and 0.42). Under mice as units nothing reaches significance (cell 40). |
| fig4d-app-odor1-dopamine-decreased | not_reproduced | In window G1 the interaction gives p=0.23 (sessions) and 0.16 (mice), and the T1 Tukey test gives p=0.17 and 0.059 (cell 43). Only the G2 variant passes, and the criterion fixes G1. |
| fig4e-correct-sessions-odor1-decreased | not_reproduced | The Odor-1 interaction gives p=0.08 to 0.33 and the T1 Tukey test p≥0.33 under every reading (cell 45). |
| fig4f-error-sessions-no-difference | reproduced | Every odor and reading gives interaction p≥0.05 and no Tukey comparison at the same timepoint below 0.05 (cell 47). The absence carries little weight: there are only 1 to 3 WT error sessions. |
| figs7-odor1-specific-decrease | partially_reproduced | Sessions as units: Odor-1 exceeds A (p=0.0013) and B (p=0.0008). Mice as units: A against 1 p=0.0031, B against 1 p=0.055 (cell 49). Neither proxy is the paper's hemisphere unit. |
| figs6d-dopamine-behavior-correlation | blocked (methods_underspecified) | The required readings disagree. Only SD (a), window G2, window mean, Odor-1 trial count gives r=0.73 with p=0.025, which passes. SD (a) with G1 gives r=0.60. SD (b) keeps 0 or 1 sessions (cell 51). |
| fig1d-young-new-association-impaired | not_reproduced | On the 10 photometry mice the interaction gives p=0.26 (B1) and 0.13 (B2), and the 1/2 Tukey test p=0.36 and 0.21. The WT means are 87.3 and 88.8, outside 90.6±0.9 (cell 31). This uses 10 of the paper's 27 mice, so the test has low power. |
| fig1d-prelearned-retrieval-intact | blocked (data_missing) | There is no behaviour for old mice. The young half holds on the subset: A/B Tukey p=0.9999 and 0.997 (cell 31). |
| fig1e-young-correct-sessions | not_reproduced | B1: both means within tolerance, but p=0.25. B2: p=0.046, but WT is 90.0, outside 77.5±6.1 (cell 33). |
| fig1g, fig1h, figs1c, figs1f, fig5c, fig5d, figs9a, figs9b, fig6b, fig6c, fig6k, figs11 (12 claims) | blocked (data_missing) | There is no behaviour for old, prelearning, optogenetics or L-DOPA mice. None of the optogenetic or PS19 animal IDs from Supplementary Table 2 is among the 37 subjects. |

Totals: 2 reproduced, 4 partially_reproduced, 6 not_reproduced, 33 blocked.

**B. Problems**

1. [affects a conclusion] Cells 34–49 and `per_unit`: the photometry unit of analysis is not the paper's. The paper uses hemispheres, which the files do not identify (asset metadata: "brain region: not provided"; Supplementary Table 2 says most mice were recorded bilaterally). The notebook uses sessions or mice instead and prefers sessions. Sessions count each recording more than once: APP-KI has 30 sessions from 8 hemispheres, giving df 195 against the paper's 80 and 116 against 28. The stated reason for preferring sessions is partly that it lets the test reach significance. The outcomes of fig4b and figs7 change between sessions and mice; fig4c fails under both.
2. [affects a conclusion] Cell 37 (fig4b): the claims file asks for both the rank-sum and the signed-rank test without saying how to combine them, and here they disagree (T5 Odor-1: p=0.0025 against 0.084). The rank-sum test compares the window means with precue values that are near 0 by construction, so it is not a paired test.
3. [affects a conclusion] Cells 31 and 33: fig1d-young and fig1e are tested on 10 of the 27 mice (5 against 5, df 8 against the paper's 25). A failed test here is weak evidence against the claim.
4. [does not affect a conclusion] ed4a is marked blocked, but the RS/FS labels in the file names allow a two-class test. From the cell 24 counts I get χ²=38.2, p=6e-10, with more FS cells in APP-KI. The notebook does not report this.
5. [does not affect a conclusion] `is_correct` and cell 33 count session 00266_20190405, whose B1 performance is undefined (NaN), as an error session. With that session excluded, WT B1 is 83.3% and p=0.067, so the outcome stays the same.
6. [does not affect a conclusion] Cell 17: the near-zero contrast in the precue window is forced by the per-trial z-scoring over samples 0–999, so it does not check where the cue is. The 1 kHz rate and cue-at-sample-1000 assumption rests only on the spectrum and the post-cue contrast.
7. [does not affect a conclusion] Cell 51: reading (b) sets the threshold from the SD of every sample of every trial, which no window mean reaches, so 0 or 1 sessions are kept. Readings (a) already disagree, so the outcome does not depend on this. The mean-based readings keep only 9 to 11 sessions, against the paper's 21.
8. [does not affect a conclusion] `two_way` uses type II sums of squares; MATLAB's `anovan` defaults to type III. The interaction terms are identical; only the reported main effects differ. `tukey_cells` matched statsmodels' `pairwise_tukeyhsd` on a synthetic unbalanced test.
9. [does not affect a conclusion] Cells 20 and 24 do not explain the surplus young WT units (for example 01398: 203 principal cells against 112), nor the ABCCDD-type sessions (126 WT and 307 APP-KI units).

I found no place where the claims file misreads the paper. Its Supplementary Table 2 animal IDs, sexes and hemisphere counts match my own reading of the supplement PDF.

**C. Not checked, and what would have allowed it**

- Whether the unit files hold waveform or electrode columns. `_read` stores `unit_columns` but the notebook never prints them. Printing the units columns, and the contents of acquisition, stimulus, processing and scratch for one unit file, would settle ed4a/ed4b and the event-time block.
- Hemisphere identity of the photometry files. Printing each file's processing-module or fiber metadata would show whether the paper's hemisphere unit can be rebuilt.
- Cue onset. A plot of the mean trace per odor around sample 1000 would test the cue-at-1000 assumption.
- I did not re-run anything. All the numbers above come from the saved outputs, apart from the two small recomputations noted in A and B.
