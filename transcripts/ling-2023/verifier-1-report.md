**A. Outcomes** (19 claims, from the claims file; I had no attempt record, see C)

| Claim | Outcome | Reason |
|---|---|---|
| mouse-sessions | reproduced | 7 block sessions, 4 mice, median 210 ROIs across the block sessions (215 ± 21.5) (cell 19). |
| figshare-trace-link | reproduced | Median within-trial r is 0.968 with windows counted in frames. All 198 deposited glomeruli match the same-index ROI (cell 21). With windows placed in seconds the median r is 0.307, so the paper's code counted frames. |
| fig2h-onoff-angle-mouse | partially_reproduced | All 28 values and every odor mean are above 90°, but the mean is 127.88°, outside 121.8 ± 2.98 (cell 25). The >90° result is mostly produced by the centring (problem 2). |
| fig2f-onoff-anticorrelated-mouse | not_reproduced | Median r is +0.481, with 0 of 28 values below 0. Every odor median is positive (cell 28). |
| fig4b-reference-odor-mouse | partially_reproduced | Reading (a) holds for ace only (p = 0.018, ON-ON smaller). For als the difference is significant in the opposite direction (ON-OFF 59.6° vs ON-ON 112.1°). Reading (b) holds in 0 of 28 cases (cell 30). |
| fig4d-clustering-mouse | not_reproduced | ON and OFF separate in 0 of 7 sessions, including the 198-ROI session. This holds with dF/F and with z-scored traces (cell 32). |
| fig6e-contrast-msc | not_reproduced | Solitary r 0.229 vs sequential r 0.219, one-tailed p = 0.39 over 21 pairs (cell 34). On the paper's own three sessions (see problem 6), cell 34's values give p = 0.082. |
| fig6e-contrast-ace | blocked: data_missing | In every block session each sequential block is X→msc (cell 10). The random-order sessions have no pairs 1 s apart, and the archive holds only these 12 files. Nothing is testable. |
| fig7d-persistent-anticorrelation | not_reproduced | The median r is positive in every bin from 0 to 50 s (0.48 down to 0.09), and positive with pre-block F0 too (cell 36). |
| fig7h-iti-knn-mouse | partially_reproduced | In the 318-ROI session accuracy is 0.45, above the null's 99th percentile (0.375) but below 50% (cell 38). |
| fig7j-iti-timebin-mouse | reproduced (criterion only) | In the 318-ROI session all five segments are between 0.719 and 0.885, above the null's 99th percentile (at most 0.359) (cell 40). Cell 41's no-odor pseudo-trials score 0.70 in the same session, so the accuracy cannot be attributed to the odor (problem 3). |
| figs7e-ibi-chance | not_reproduced (criterion nominally met) | The k = 50 rate is 3.8%, far below 34.8 ± 3.48 and below chance, because the k = 50 classifier is degenerate (problem 1). The only usable classifier (k = 20) gives 73–95% with permutation p = 0 in the four complete sessions (cell 43), which contradicts "no longer present". |
| figs8e-random-order-decline | partially_reproduced | Early accuracy is above the null in 5 of 5 sessions. Late accuracy is still above the null's 95th percentile in 4 of 5 (cell 45). Chance is 1/11, as in the paper. |
| figs2-pid-decay | blocked: data_missing | No file has a PID series. The acquisition groups hold only treadmill position (and respiration in one file) (cell 4), and the asset metadata (`variableMeasured`) lists no other series. |
| fig1g-onoff-angle-locust | partially_reproduced | All 11 odors are above 90°, but the mean is 104.92°, outside 106.7 ± 0.84 (cell 49). Uncentred, the mean is 58.5°. |
| figs4a-reference-odor-locust | reproduced | 4 odors are significant with ON smaller (5 ± 1), and ON is smaller on average for 9 of 11 (cell 51). See problem 10. |
| fig5e-contrast-locust | reproduced | Solitary r 0.486 vs sequential r 0.227, one-tailed p = 0.0055 (cell 53). |
| fig7f-iti-knn-locust | reproduced | Accuracy 1.000 against a null 99th percentile of 0.257; chance is 1/7 (cell 55). |
| fig7i-iti-timebin-locust | partially_reproduced | 7 of 7 odors are above the null in the last 5 s, but the mean is 0.290, outside 0.40 ± 0.04 (cell 57). |

Totals: 6 reproduced, 6 partially reproduced, 5 not reproduced, 2 blocked.

**B. Problems**

1. [affects a conclusion] Cell 43, `knn_neighbours` with k = 50 on 60 bins: with leave-one-out, the own class has 14 candidates and each other class 15, so the vote almost never picks the own class. On random data with 4 × 15 vectors and k = 50, accuracy is 10.7%; the notebook's own null mean is 10.8%. The ≤ 38.3% criterion is therefore met by construction. The k = 20 analysis is far above chance, but adjacent 1-minute bins of the same IBI serve as each other's neighbours, so slow drift alone could explain it.
2. [affects a conclusion] `onoff_angles(center=True)`, cells 25, 30, 49, 51: centring ON and OFF frames together makes the mean ON vector exactly opposite the mean OFF vector (cell 25 prints a cosine of −1.0 for every case). On synthetic data, ON and OFF patterns that are 11° apart uncentred come out at 157° centred. Uncentred, the mouse mean is 71.8° (26 of 28 values below 90°) and the locust mean is 58.5°. The ">90°" test follows the code but does not show inversion.
3. [affects a conclusion] Cells 38, 40, 41 (and the locust cells 55 and 57): all trials of one odor fall in one block, and blocks are 15 minutes apart. Cell 41's pseudo-trials, taken in the IBI with no odor, are classified at 70–97%. The trial-label permutation null does not keep the block structure, so a null 99th percentile around 0.35 is the wrong reference. The odor and slow drift cannot be told apart. The locust recordings were also in blocks, and the notebook has no control for them.
4. [affects a conclusion] `zscore_trials` variants (cells 28, 34, 36): z-scoring each trial over a window that contains the ON response produces negative ON-vs-later correlations by construction. Synthetic glomeruli with pure excitation decaying to baseline give r = −0.98. The fig7d z-score variant (28 of 28 negative) and the fig6e z-score variant (p = 5.6e-7) are not evidence for either claim. The deposited arrays are close to this normalisation (r = 0.927, cell 21), so the paper's reported anticorrelations may come from it.
5. [affects a conclusion] Cell 45: the later version's Table 1 (iScience, PMC13066794) lists the random-order sessions with 175, 340, 323, 306, 286, 204, 250 and 280 glomeruli. The dandiset's random-order sessions have 559, 325, 323, 306 and 403 ROIs, so only two match, and figs8e is tested mostly on sessions the paper may not have used. The odor names (2-ethylphenol, anisaldehyde) and the 0.0 concentrations of those two odors also differ from the Methods.
6. [does not affect a conclusion] Cell 34: the same Table 1 identifies the msc-contrast sessions as the 286-, 219- and 318-ROI sessions (sub-148 ses-2, sub-148 ses-3, sub-149 ses-1). It assigns the ace panel to the 73/210/153/198-ROI sessions, which the dandiset labels as X→msc. In those sessions the ace-first response correlates 0.94–0.98 with solitary ace (cell 34), which supports the dandiset's labels over the table's.
7. [does not affect a conclusion] Cell 38: k = 20 with 9 same-class candidates out of 39 also biases accuracy against the own class. The null mean is 0.17, and random data gives 0.175. The fig7h accuracy is depressed by this choice.
8. [does not affect a conclusion] Cell 30: the paired t-test is two-sided, so the als result (significant, but with ON-OFF smaller) has to be excluded by hand. The mouse ON-ON angles (85–123°) are far from the later version's 44.7°, which suggests the method differs from the paper's.
9. [does not affect a conclusion] `windows`: past the last frame it extrapolates linearly instead of failing; a synthetic test returned values 10–15 from data ending at 9. sub-124 ses-3 has trials after the end of imaging. The first-10-per-odor selection probably avoids them, but this is not checked.
10. [does not affect a conclusion, unverified] Cell 51: the set of ON angles includes the reference odor's own 0° angle, as the criterion's "11 ON angles" says. This biases the test toward ON being smaller, and bza (p = 0.052) and oca (p = 0.059) are borderline.
11. [does not affect a conclusion] `dff_pre`: F0 is the 2 s before onset, which is 53–55 s after the previous same-odor offset, a period the paper says still carries OFF activity. The pre-block F0 variant in cell 36 gives the same sign.
12. [does not affect a conclusion] Windows are placed in seconds, while the paper counts frames at a nominal 16 per second. At 17.8 Hz (sub-134 ses-22) the code's "5 s" is 4.5 s. The analyses here therefore do not use the paper's actual windows.
13. [does not affect a conclusion] Cell 28: the median-subtraction variant is identical to the main analysis by construction (Pearson r is unchanged by subtracting a constant across glomeruli), so it is not a separate check.
14. [does not affect a conclusion] Subject labels: the dandiset puts the 318-ROI session under sub-148 with the 286-ROI session. The later version's Table 1 puts it with the 219-ROI session (m4).

**C. What I could not check**

- The preprint full text. bioRxiv refused the download (HTTP 429, Cloudflare 1015). I saved the v2 abstract and the later iScience text in `paper/`, so the preprint's Fig 4B ON-ON value and its Table S1 session list are unverified.
- The attempt record was not among my materials. The counts in A come from the claims file.
- These outputs, if added to the notebook, would have let me check more:
  - IBI classification with k at or below the class size, or block-held-out validation (problem 1).
  - A control for the centring in fig2h, for example the centred median angle between the pre-odor window and the ON window, or between the two halves of ON (problem 2).
  - A null for fig7j that respects blocks, and a pseudo-trial control for the locust data (problem 3).
  - The z-score variant with the mean and SD taken from the pre-onset window only (problem 4).
  - fig6e computed on the three sessions from the paper's table (problem 6).
  - The figs4a counts with the self-angle excluded (problem 10).
  - The number of extrapolated window frames per session (problem 9).
