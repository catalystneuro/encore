I wrote `claims/001530/10.1038-s41467-026-73622-y.yaml`. The quote checker reports 28 claims, 28 quotes, 52 statistical values and 0 problems. Nothing was committed.

**Text read.** The version of record from Europe PMC (PMC13346651), marked as corrected. It has the main text, figure legends and Methods. Missing: the Supplementary Information (Supp. Figs. 1–19), the Source Data and the text of the correction notice, and there was no PDF. I went ahead because every main finding is stated with its numbers in the main text, as earlier claims files in this repo did. For the three findings the main text cites to supplementary figures (Supp. Figs. 3, 17, 18), the claim is written from the main-text sentence and its method from the code that draws that figure.

**Code read.** Only the code files of the paper's Zenodo record (doi:10.5281/zenodo.17973874), pulled out of the 21 GB zip by range requests, without opening any data file. The GitHub copy (LSENS-BMI-EPFL/Ghaderi_et_al_NCOMMS_2026, commit 20cf10c) is byte-identical for the analysis code.

**Claims.**
- **Coverage:** behaviour (Fig. 1c, 1f, the quiet-trial fraction), optogenetics (Fig. 2: three windows, wM2 against ALM, other trial types), unit counts, Figs. 3 to 8 and Supp. Fig. 18.
- **Quotes:** all 28 have one.
- **Statistics:** 12 claims have them (52 values).
- **Expected values:** 16 claims have them; tolerances are the paper's ± SEM where given, otherwise 10%.
- **Criteria:** all 28 have one.
- **Outside data:** 2 claims (fig4b, fig5c) are `with_inputs`. They need the paper's cluster labels (Zenodo `processed_data/Data_Clustering.mat`), because a new clustering would not number the clusters the same way. The lick-direction claims use `Lick_times.mat` from the same record; whether the dandiset holds those lick times is the author's to check.

**Where the paper and its code disagree.** Methods first, code as a variant, unless noted:
- **Quiet-trial threshold:** Methods say median absolute deviation; the code's `mad()` default is the mean absolute deviation. Both are run.
- **Optogenetics bootstrap:** 1,000 iterations in the Methods, 10,000 in the code. Only 10,000 can produce the reported p = 0.0003.
- **Clustering:** Methods describe 10 ms bins and a Gaussian similarity; the code uses 100 ms bins and exp(−d/σ). The reported σ is the code's 100 ms value, so I followed the code there.
- **Context coding direction:** trained on 20% of trials (Methods) against 30% (code).
- **SVM:** the Methods name a grid search; the code uses libsvm nu-SVC with no search. The baseline is −1 to 0 s (Methods) against −0.8 to 0 s (code).
- **PCA (Fig. 6a):** the legend says the PCs are fitted on two trial types; the Methods and code use four.
- **FDR families (Figs. 7b, 7d):** per area in the legends, pooled over all areas in the code.
- **Session count (paper inconsistency):** the Results say 35 sessions; the Methods say 34.

**Details the paper leaves open, with the readings named:**
- **Movement latency, "time to 20% max" (Fig. 1f):** no code computes it. Readings: per-session mean trace, or per trial.
- **Opto "reduction":** absolute percentage points or relative percent; and whether the ± is SEM or SD.
- **wM2 against ALM opto comparison:** not in the code. Readings: 9 sessions resampled per area, or all sessions; the FDR family is unknown.
- **"Little impact" on other trial types:** the paper's bootstrap test, or a 13-point threshold taken from the smallest significant effect.
- **Fig. 8b pairwise p-values:** which three comparisons each context's three p-values are is not stated; I read them as that context's lick group against the three no-lick groups.
- **Supp. Fig. 18 "effect size":** Cohen's d, or the Kruskal-Wallis statistic.
- **Vague wording:** "mostly" and "widely distributed" (cluster composition) and "immediately" and "rapidly" (decoding time course) are given explicit thresholds in the criteria.
