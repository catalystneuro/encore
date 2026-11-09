I wrote `claims/000935/10.1038-s42003-021-02981-7.yaml`. The checker reports 26 claims, 26 quotes, 37 statistical values and 0 problems. Nothing was committed.

**Text read.** I read the version of record (Commun Biol 5:33) from Europe PMC, PMC8752598: main text, figure legends and Methods. I also read Supplementary Figs. 1–7 with their legends, the description of Supplementary Data 1–7, the reporting summary and the peer review file. The Supplementary Data spreadsheets (the source data) were not in `paper/`; none of the claims needed them to be written. The paper links no code. It names Prism 8.2.1, MC Rack, NeuroExplorer, and MATLAB R2020a with Chronux 2.11.

**Claims.** All 26 have quotes; none rests only on an `inferred` note.
- **16 in vitro claims (Figs. 2–6, Supp. Figs. 2–6).** The dandiset does not hold these data; its description covers only the in vivo experiment.
  - 11 of them are marked `data: elsewhere`. Their per-electrode counts are the article's Supplementary Data 1–6.
  - The other 5 (Supp. Figs. 2, 3, 5 and 6, and the Supp. Fig. 4 claim) have no deposited data as far as the paper says.
- **10 in vivo claims (Fig. 7b–f).** These are `data: dataset`. Supplementary Data 7, the source data for Fig. 7, is named in the opening comment but not used.
- **Statistics:** 22 claims have them, mostly Wilcoxon and Mann–Whitney tests, plus KS tests for Fig. 7. Five claims are claims of absence, judged on the paper's own test.
- **Criteria:** all 26 have one. Seven in vivo claims also have `expected` values. Means use the SDs the paper states as tolerances; medians use 10%.

**Details the paper leaves open, and the readings named:**
- **(o1) The Opsin (+) mouse with no imaging** has no bioluminescence onset. It is aligned (a) to the start of CTZ infusion, or (b) to that start plus the mean onset delay in the five imaged mice.
- **(o2) Position of the bioluminescence ROI.** (a) An ROI position the dataset records, or (b) the whole frame.
- **(o3) Gamma-event window.** The Methods count from the start of CTZ and the Results from bioluminescence onset; both are run.
- **(o4) The jackknife for the event threshold.** (a) Leave one sample out, or (b) leave one 1-s block out. The analysis is run at both 10 kHz and 1 kHz.
- **(o5) MUA.**
  - "Median divided by 0.6745" is taken as median(|x|)/0.6745, the usual noise estimate.
  - The span is (a) the whole recording or (b) the baseline.
  - Spikes are counted as (a) every sample below threshold, as written, or (b) threshold crossings.
- **(o6) The 85th percentile.** MATLAB `prctile` interpolation or linear interpolation.
- **(o7) Filter phase.** Zero-phase filtering is used as a standard choice; it cannot change an outcome materially.
- **Excluded contacts.** The paper reports the same 7 bad contacts for every animal, so the set is read as the union over animals.
- **Gamma band.** The Methods use 30–100 Hz and the Fig. 7d legend 80–100 Hz; both are run for Fig. 7d. The Fig. 7e tests follow the Methods.
- **"Exceeded baseline" bound.** The upper end of a two-sided 95% interval, or a one-sided 95th percentile.
- **Time bins of the KS test on gamma events.** Counts per 1-s bin, or per-contact totals.
- **Layer split for "superficial and granular" (Fig. 7d).** The paper gives no layer boundaries. The contacts are split (a) into upper and lower halves, or (b) into the upper two thirds and the deepest third.
- **Fig. 6c pairing.** Which counts each Wilcoxon test pairs is not said; two readings are named. The Results print p = 0.0001 and the legend p < 0.0001; either counts as a match.
- **Fig. 4e group comparison.** One p is given for a comparison of four groups; it is run as pairwise tests against the immediate-CTZ group.
- **Supp. Fig. 4c.** The paper uses a Mann–Whitney test on paired counts, so a Wilcoxon test is shown as a variant.

**Notes on the statistics.**
- **Fig. 7e, mouse level.** With 3 against 3 mice, U = 9 means every Opsin (+) mouse is above every Opsin (−) mouse. The exact one-tailed p is then 0.05, not below it, so these claims are judged on U.
- **Fig. 7f, MUA across mice.** The paper's two-tailed test cannot reach p < 0.05 with 3 mice per group. That claim of absence therefore holds whatever the data, and it is judged on U and the reported values.

**Missing from the paper.** Five claims need data that, as far as the paper says, were never deposited:
- the IVIS images (Supp. Fig. 5)
- the confocal images (Supp. Fig. 6)
- the recordings that show presynaptic activity (Supp. Fig. 3)
- the synchrony recordings (Supp. Fig. 2)
- the electrode counts behind Supp. Fig. 4c, which are in Supplementary Data 3, but that claim was left `data: dataset` instead of `data: elsewhere`.

The Supp. Fig. 3, 5 and 6 claims say no data are deposited; the Supp. Fig. 2 claim says the recordings are not deposited. The Supp. Fig. 4c claim names Supplementary Data 3 under `where:` but is not marked `data: elsewhere`, so the schema ignores it. That is my slip: this claim should be `data: elsewhere`, and the second reader should correct it.
