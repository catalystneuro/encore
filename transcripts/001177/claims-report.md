I wrote `claims/001177/10.1093-brain-awaf312.yaml`, and the quote checker passes it: 43 claims, 42 quotes, 85 statistical values, 0 problems. Nothing is committed.

**Text read.** I read the version of record from Europe PMC (PMC12597312), full text including Methods. I also read its one supplement, `awaf312_supplementary_data.pdf`, which holds Figures S1 to S8, the Supplementary Methods and the statistics table (Table 1). I opened two supplement PDF pages, Figures S5 and S8, only to read pie-chart percentages that the text does not hold. The main paper's figures were not available as images, so main-figure values come from the legends.

**Code read.** The paper links two behaviour repositories:
- `UCSF-Nelson-Lab/ICD-Cognitive-Analysis`, tag ICD, commit 5528e22. `Summary_Cognitive.m` settles how A, K and AUC are computed: a per-mouse mean over sessions, a least-squares fit starting at A = 1, K = 0.5, and AUC by trapezoids at 0, 3, 6 and 9 s.
- `UCSF-Nelson-Lab/ICD-Cognitive-Arduino`, commit f7cff8b, which runs the operant boxes.

No code is linked for the electrophysiology; the paper says it was analysed in NeuroExplorer and Prism.

**Claims.**
- 43 claims: 42 have a quote and 1 is `inferred` (the per-session counts in the Figure S8 legend).
- 38 have statistics, 40 have a criterion and 8 have expected values.
- 14 claims use the dandiset: the electrophysiology in Figure 4, Figure S5, Figure 6F–I and Figure S8.
- 29 are `data: elsewhere`. The paper deposited the behaviour, histology, rotarod, locomotion and slice data on Zenodo (doi:10.5281/zenodo.15258978), not on DANDI.

**Details the paper leaves open, with the readings named:**
- **Putative MSN classification:** no thresholds are given. Readings are (a) a label the authors deposited with the units, or (b) the criteria of the two papers it cites (Berke 2004, Gage 2010).
- **Optical tagging:** the bin width, the baseline window for the 99% interval and the waveform test are not given. Readings are (a) a deposited label, or (b) 1 ms bins, the pre-pulse baseline and waveform correlation.
- **Response-type test:** the paper names a signed-rank test but not how the 1 min bins are paired. Readings are (a) the 30 baseline bins paired in time order with each 30 min post epoch, or (b) an unpaired rank-sum test on the same bins. A unit significant in only one epoch is counted as "no change" and reported.
- **Session for Figure 4 and Figure S5:** (a) each mouse's first PPX session, or (b) all PPX sessions pooled.
- **Figure 4 inset denominators:** the printed percentages fit 13 control dMSNs and 11 parkinsonian iMSNs, but the legend says n = 12 and n = 16. Both denominators are named as readings.
- **Figure 4H–K "normalized response":** (a) ratio to baseline, or (b) change over baseline. The paper reports no test for these panels.
- **"Immediate" suppression in healthy mice (Figure 4D–E):** no window or test is given. Readings are 0–30 min and 0–60 min, using the paper's within-unit test.
- **Figure 6H–I measure:** (a) the post-drug rate, (b) the change from baseline, or (c) the ratio to baseline.
- **Which PPX sessions form "PPX" in Figure 1:** (a) the first session, or (b) the mean of the four, as the code averages.
- **Test name conflicts:** for Figures S2I–K and 5J–L the legends and Methods name a Friedman/Dunn's test, while Table 1 names a one-way ANOVA or Wilcoxon signed-rank. Both are named as readings.
- **Baseline window for A77636 locomotion:** not given; the 20 min before injection, the window the paper uses for CNO, is used.

**Inconsistencies recorded in the claims:**
- Figure 1G p-values: legend "<0.0001" and "<0.0087" against Table 1 "0.0001" and "0.0087".
- Figure 2E: the text says "at every delay" but reports p = 0.57 at 0 s; the claim follows the numbers.
- Figure S1E: N = 7 in the legend against 8 in Table 1.
- Figure S4: N = 16 in the legend against 28 in Table 1.

**Missing from the paper that a claim needed:**
- No p-values are printed for the CNO locomotion in Figure 5C–F.
- No PPX open-field file is named in the Zenodo deposit.
- No numeric A, K or AUC values are reported anywhere, so those claims rest on tests and directions only.
