I wrote `claims/002034/10.7554-elife.112525.yaml` and the quote checker passes it: 16 claims, 16 quotes, 16 statistical values, 0 problems. Nothing is committed.

**Text read:** the eLife Reviewed Preprint v1 (2 October 2026, not revised), from the publisher's HTML. It has the main text, the figure legends, the Methods, and the legends of Supplemental Figures 1 and 2, which are the whole supplement. There was no PDF and I opened no figure. Nothing a claim needed was missing.

**Code read:** github.com/lwthompson2/Thompson2026_LCPupilAnalysis at commit cf3c0b7 (MATLAB). It rebuilds the analysis from the NWB files of dandiset 002034. The repository also holds the printed output of that code run on the dandiset, and some of its values differ from the paper's. For example, Figure 2 row 6 for monkey Ci gives p = 0.0105 against the paper's 0.008, and the code counts 50 Ci sessions and 61 Ci units where the paper has 51 and 63. The claims use the paper's numbers.

**Claims:**
- 16 claims, all with quotes and all with a criterion.
- 8 have statistics (16 entries): the six rows of Figure 2 and the two analyses relating each unit's correlation to the range of its evoked responses.
- 5 have expected values: the unit and session counts, Oz rho = −0.33, and the three log-likelihood-ratio (linear against quadratic fit) counts.
- Four are claims of absence: Figure 2 rows 5 and 6, the evoked-LC range analysis, and the pooled across-epoch result.

**Details the paper leaves open, and the readings named:**
- **Population test.** The paper names a "Wilcoxon rank-sum test" but states a one-sample hypothesis (median = 0). The code runs the signed-rank test. Both readings are run, and the claim is blocked as underspecified if they disagree. For the two absence claims I made the signed-rank test the main one and the rank-sum a variant, because it is the only test of the hypothesis the paper states. This departs from the protocol's "the paper's text comes first", and the second reader should check it.
- **Evoked pupil.** "Maximum change" in the Methods allows two readings: the largest increase, or the largest absolute deviation with its sign kept (as the code does). The code's own window (0 to 800 ms in 1 ms steps, where the Methods use beep to 20 ms before the end of fixation in 10 ms steps) is a variant.
- **Pupil preprocessing.** The Methods z-score, subtract the mean fixation-aligned trace and smooth. The code applies none of this to the stored trace, so the author must establish whether the dataset's trace already has it.
- **Code choices the Methods disagree with, kept as variants:** the minimum baseline before the beep (Methods 100 ms, code 400 ms and 800 ms before the record ends), and the end of the fixation-only firing-rate window (code: end of trial).
- **Code choices the Methods don't mention, followed:** dropping trials whose evoked rate has |z| ≥ 8, the code's include lists of sessions and units, and fitting drift residuals over beep and fixation-only trials together.
- **Range analysis.** The paper says the range is per session; the code takes it per unit, which I followed.
- **Log-likelihood-ratio unit denominator.** Readings: all 63 Ci units (the paper), or the code's removal of two table rows. I set the tolerance to ±1 count, because 10% of counts this small would demand an exact match; the claims file gives the reason.
- **Figure 3.** The legend draws linear fits but the code tests with Spearman, which I followed. The code's raw-baseline version is a variant.
- **"Similar" (Supplemental Figure 1) and "across monkeys".** I defined "similar" against the per-row, per-monkey pattern of significance and sign the paper reports. "Across monkeys" means significant with the same sign in both monkeys.
