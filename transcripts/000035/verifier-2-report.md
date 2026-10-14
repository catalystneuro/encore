**Round 2 verification report: 000035-scala-2021-01**

**1. Outcomes**

The claims file has 17 claims and the attempt record has 17 outcomes: 9 blocked for missing data, 1 blocked as not runnable, 5 reproduced and 2 partially reproduced.

| Claim | Outcome in record | Agree? |
|---|---|---|
| fig1-ttype-coverage, fig2-rrr-prediction, ed5-rrr-ion-channels, fig3d-families-separate, fig3d-morphology-combined, fig4c-distance-correlation, fig4d-it-depth, fig5a-ttypes-between-families, fig5b-ttype-variability | blocked (data_missing) | Yes, all nine |
| ed6-cohort | reproduced | Yes (cell 10) |
| ed6-stimulus-protocol | partially_reproduced | Yes (cell 13: 174/185, 94.1%) |
| ed6-it-et-overlap | reproduced | Yes. The criterion is met (58.3% in cells 16 and 19d). The variants in cells 18 and 19 show the overlap is one-sided and partly an imbalance effect, and the record now says so. |
| ed6-it-et-ap-threshold | reproduced | Yes. Rank 2 of 17, p = 0.00035 (cell 23). |
| link-cells | partially_reproduced | No, as in round 1. The only mismatch is the one-to-one PT/ET renaming. After renaming, agreement is 1.000 (cell 26), and the claims file itself treats PT as ET. The record states my disagreement correctly. |
| link-features | reproduced | Yes. 16 of 17 features ≥ 0.9, lowest 0.877 (cell 29). |
| ed6-sst-temperature | reproduced | Yes. Both parts hold (cell 34) and the variants agree (cell 35). |
| ed6-sst-transcriptomic-distance | blocked (not_runnable) | I agree it was not tested. I do not agree with the reason: this run's own output contradicts it (see 2a). |

**2. Statements checked against the printed outputs**

a. The statements that are not supported all concern ed6-sst-transcriptomic-distance. Cell 39 printed: "download rate from Zenodo in this run: 149 kB/s over 1.0 MB; the member would take about 10 minutes."
- README table and cell 0 table: "the reference expression data cannot be fetched within the time limit". At this run's rate the fetch takes about 10 minutes, inside the 30-minute limit.
- Summary (cell 41): "Blocked: not runnable, the reference data cannot be fetched within the time limit". Same contradiction.
- Attempt record notes: "In the three runs of this revision it was 27, 114 and 44 kB/s, about 55, 13 and 33 minutes for the member, beyond the ten minutes a run should take in every run and beyond the 30 minute limit in two."
  - None of those rates is this notebook's 149 kB/s.
  - This run comes to 87.9 MB ÷ 149 kB/s ≈ 9.8 min, so "beyond the ten minutes … in every run" is false for the run delivered.
  - The verification response repeats the same three rates.
- Cell 40 contains no false number, but its premise is that the transfer time blocks the test. Its own output shows the transfer would have fit.

b. Everything else matches the outputs:
- Result cells 11, 14, 21, 24, 27, 31, 37 and 40.
- The other Summary bullets.
- The README's description of the data and the outcome table, apart from 2a.
- The record's notes and measured values. I checked every number: counts, ladder endpoints, 58.3/0/10.5/12.4/33.4/36.5%, 0.83/0.78, all p-values, the AUCs of 0.84/0.85/0.73, all shifts and Spearman values, the 0.895–0.995 range, and the distance range 1.54–5.24.

c. Minor slips that do not affect a conclusion:
- The comment in cell 17 says "IT and ET cells come from three mice". Its own crosstab shows four: MITSU, SCEAC, UEQOU and WPOGH.
- The README says the run takes about four minutes. The execution timestamps span about 2.5 minutes (13:03:43 to 13:06:15).

d. The record states my round-1 reasons faithfully. It condenses them and folds my problems 1–6 and the section C requests into the right claims. The link-cells disagreement and its reason are recorded accurately.

**3. Round-1 points**

All my round-1 points are resolved except the last one:
- Problem 1 (paper's 184 cells): resolved. The 184-cell kNN and Mann-Whitney results are in cells 19d and 23, with the same conclusions.
- Problem 2 (balanced variant with k = 10 ties): resolved. Cell 18 now uses k = 9 and k = 11 on the same subsamples.
- Problem 3 (confounding by mouse): addressed. Within UEQOU, the kNN gives 33.3% ET as IT and 20.0% IT as ET, and the logistic regression gives 0.78 (p = 0.025), in cell 19e. The threshold gap within UEQOU gives p = 0.094 (cell 23). The record now says the within-mouse threshold gap is not significant.
- Problem 4 (tie rule in `knn_family_confusion`): resolved. The rule is now in the docstring (`scala34.py:462`).
- Problem 5 (step timing): resolved. Onsets and offsets are now checked per sweep, and all 14,054 sweeps are 0.1–0.7 s (cell 13).
- Problem 7 (units): resolved. It is recorded as a finding.
- Section C requests: the per-cell feature CSV is now printed (cell 6), and the ED6i electrophysiological distance matrix is computed (cell 39).
- Problem 6 (ed6-sst-transcriptomic-distance): only partly resolved. A fetch attempt is now shown, but it undercuts the blocking reason.

Two items remain that bear on a conclusion:
1. **ed6-sst-transcriptomic-distance.** The reference data are public. This run measured a fetch of about 10 minutes, and the electrophysiological half is already computed. The claim is testable and should be tested, not blocked. The README, cell 0, the Summary and the record's notes and response need to be corrected to the rate actually observed, or brought in line with a run that performs the test.
2. **link-cells.** I still disagree with partially_reproduced, for the reason above. The disagreement is recorded, and it changes no other claim.
