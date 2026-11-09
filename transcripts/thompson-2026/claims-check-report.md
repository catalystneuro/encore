The file is ready for an attempt. I checked it against the paper and against the linked code at the commit it names (cf3c0b7). The quotes, sources, p-values and expected numbers all match the paper, and the paper's main findings are all covered by claims from this paper alone.

**Checker:** `16 claims, 16 quotes, 16 statistical values, 0 problems`, both before and after my edits.

**Changes, by claim**
- **Opening comment, the population test:** the file let two versions of the test decide outcomes. One was the code's signed-rank test against zero; the other was a rank-sum against a list of zeros, which the file made up because the paper names a "rank-sum test". I made the signed-rank test the only one that decides outcomes, and kept the rank-sum version as a variant that can be shown. The reasons:
  - the paper's stated hypothesis (median = 0) is one-sample;
  - the code uses only the signed-rank test;
  - the code's printed p-values equal the paper's for Figure 2 rows 2, 3, 4 and 6 in Oz;
  - the rank-sum version appears nowhere in the paper or the code.
- **Opening comment, other details:**
  - I added the code's "legacy" removal of two rows from its unit table. It leaves 61 Ci units, and it also leaves 50 Ci sessions where the paper has 51.
  - I corrected the 8 SD trial exclusion: it applies to the raw evoked rate, not the baseline-subtracted one.
- **fig2-row1, fig2-row4:** decided by the signed-rank test alone.
- **fig2-row2, fig2-row3:** decided by the signed-rank test alone. Both readings of "maximum change" in evoked pupil are run, and the claim is blocked when they disagree; the file had not said how the two combine. Row 3 now shows the code's 50 Ci sessions as a variant.
- **fig2-row5:** the signed-rank test is the test; I added the rule for when the two evoked-pupil readings disagree.
- **fig2-row6:** the criterion left two outcomes undefined (Oz significant but Ci not; both significant with opposite signs). Both now count as partially reproduced.
- **figs1-raw-baselines-similar:** signed-rank test only; the rule for the two evoked-pupil readings is now stated.
- **figs2-llr-pupil-baseline-evoked:** added the code's 50 Ci sessions as a reading (the code prints 6/50). This matches how the file already handles the two removed units in figs2-llr-lc-baseline-evoked.
- **fig3-pooled-within-epoch:** the Methods and the Figure 3 legend z-score pupil per session. That is now the main reading when the stored trace is not z-scored; the code's use of stored values is a variant.
- **fig3-pooled-cross-epoch-null:** fixed a wrong citation. The test split by unit group is in `plot_S1_combined.m` (raw baselines), not `compute_manuscript_stats.m`. The Figure 3 script itself is missing from the repository.

**Still open** (recorded in the check entry)
- The author must establish from the data whether the stored pupil trace already has the Methods' preprocessing (z-score, fixation-onset mean subtraction, 151 ms smoothing), and whether trial start equals fixation onset.
- The Results text says the range analysis is per session; the code does it per unit, and the claims follow the code. The two coincide wherever a session has one unit.
- For the Ci range test, the code's own output (rho = 0.05, p = 0.688) differs from the paper's (0.07, 0.589). The claims keep the paper's numbers.

**Ready:** yes, recorded as `ready: true` in the new `checks` entry. Only `claims/002034/` was modified, and nothing was committed.
