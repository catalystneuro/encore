**Verifier report, round 2: 001326-kauvar-2025-01**

Counts below are taken from the claims file and the attempt record. The claims file has 54 claims. The record gives 54 outcomes: 31 reproduced, 11 partially reproduced, 3 not reproduced and 9 blocked (4 `other`, 5 `too_large`). The README's counts match these.

**1. Outcomes**

I agree with every tested outcome. The category of each still holds on the numbers the notebooks now print. For six outcomes, though, the stated reasons do not match those numbers (section 2).

- **Round-1 disagreements I now withdraw:**
  - **fig5e-rapid-unchanged (reproduced):** the criterion judges an absence on the paper's test, and on the main reading q = 0.105–0.113 (main nb cell 53). One caution: on that same reading the late fall is not significant either, so this absence carries little weight.
  - **figs30-correlation-structure (partially reproduced):** the RSP rise (9/10 sessions) and ORB rise (5/7) hold under both windows. The within-region rise is significant from the file's infusion time (p = 0.010). The between-region fall is absent (cell 80).
  - **figs29-rsp-oscillations (reproduced):** now counted as 7/9 and 5/9 sessions (cell 83).
- **Outcomes resting on an assumption (`assumed: true`):**
  - **fig6d, fig6h, figs34d, figs34g, fig6j (sub-5 is the excluded animal):** the assumption is stated in the deviations. It is reasonable, since only this exclusion gives table S3's 7 tone sessions from 7 mice (cell 30).
  - **figs33 (Methods window taken as main):** stated. Under the sub-5 assumption alone, tauP is best in all 8 readings (cell 62).
  - **fig2g (the elbow is where the marginal gain drops most):** stated and reasonable, but weak. The chord rule gives 8 factors, and the held-out R² keeps rising up to 22 factors (iEEG cell 5).
- **fig2i, fig3b (reproduced):** I agree. The recomputed loadings equal the deposited ones, and all three networks have q = 0.0039 under all three permutation seeds (iEEG cells 8, 11).
- **fig1f, fig2d, figs14g, figs4 (blocked, `other`):** I agree. The search now covers 66 files and is computed, not a hard-coded print (behavior cell 3).
- **fig6c, fig6e, fig6g, fig6i, figs12 (blocked, `too_large`):** I agree they are untested, but the label is wrong. The record itself says they are "Blocked for time, not for lack of data", and the files are 0.2–0.4 GB each.

**2. Sentences the printed outputs do not support**

Main notebook, clustering and regional timing. The printed partition is the one I reported in round 1: the cell 16 output is ρ = −0.023, p = 0.9469. The conclusion text describes a different partition:
- **Cell 11:**
  - "only 7 of the 12 … sizes … within tolerance: the largest (941 against 1070), the 9th to 11th (526, 392, 187)". Cell 10 prints sizes 1019, 730, 681, …, 394, 192, with only 4 within tolerance.
  - "decay 0.10 and 0.24 s". Printed: 0.12 and 0.20.
  - "0.34 of the peak". Printed: 0.38.
  - "Four clusters decay after more than 1 s (1.03 to 1.21 s), … peaks at 0.51 and 0.53 s". Printed: three clusters, at 1.26, 1.30 and 1.37 s.
  - "within 12 ± 1 in 6, at most 8 sizes". Cell 19 prints 7 and 10.
- **Cell 14:**
  - "under both FDR thresholds … and both rankings … PAG … in clusters 4 and 6 and VPM in cluster 2". Cell 13 prints PAG in cluster 5, and VPM in clusters 2 and 8 at 0.05 but only cluster 8 at 0.01. The condition holds in 1 of the 4 combinations (cluster-mean ranking, FDR 0.05).
  - "ACAv5", "ORBvl in clusters 1 and 9". Printed: ACAd5, and ORBvl in clusters 3 and 7.
  - "VPM … in only 3 [seeds]". Cell 19: all four combinations hold in 4 seeds (1, 4, 7, 8), and VPM holds in 9 seeds under cluster-mean ranking at 0.05.
- **Cell 17:**
  - "rho = 0.127 (p = 0.71) … 0.209 (p = 0.54)". Printed: −0.023 and −0.018.
  - "cosine distance 1.43 and 0.70". Printed: 1.003 and 0.115.
  - "rho −0.10 to 0.33" over seeds. Printed: −0.183 to 0.273.
- **Cell 22:**
  - "−0.002 s". Printed: −0.0045 and −0.0069.
  - "31 of 35 … 29 of 31". Printed: 30 and 28.
  - "+0.006, −0.007 and +0.000". Printed: +0.0055, −0.0072, +0.0027.
  - "31 to 34 regions". Printed: 30–33.
  - "averages 0.06 … 0.24". Printed means: 0.065 and 0.262.
- **Cell 25:**
  - "−0.16 to −0.17 s". Printed: −0.179 to −0.188.
  - "−0.118 s (29 of 35) … −0.092 s (32 of 36) … −0.058 s (26 of 36)". Printed: −0.130 (30), −0.105 (32), −0.063 (29).
- **Cell 28:** "0.51 … 0.52 … 0.29 … VPM (0.53 s) and MD (0.57 s)". Printed: 0.488, 0.532, 0.311, 0.541, 0.590.

Other cells in the main notebook:
- **Cell 42:** "610 s with pooled weights". Cell 41 prints 853.339.
- **Cell 54:** "Under the code's 3 to 4 s target window the early difference is significant (q = 0.023 to 0.048)". That holds only with per-unit variance and unit-vector scaling. With pooled variance, q = 0.059, 0.135 and 0.220 (cell 53).
- **Cell 85 (Summary):**
  - "the default seed decides the outcomes". The default-seed partition was not the same across runs, so the seed does not fix it.
  - The table leaves out the assumption marks the record gives figs33 and fig6j.
  - "14 of the 30 puff series" is not shown per series in any output. Cell 5 prints counts only.

Attempt record:
- The notes of fig4de (including `measured`), figs31b, fig4g, fig4i, fig4h and fig4h-decay-anatomical-progression repeat the unprinted numbers above.
- fig6h repeats "610 s".
- fig5g gives "0.13 to 0.38"; printed minimum is 0.122.
- `verifications.reviewed` says my numbers "differ from those of the record and of this revision's runs … a different Leiden partition in the copy it reviewed". The re-executed notebook prints my round-1 numbers, so this statement is wrong. The same claim is repeated in the responses for fig4de and fig4g.

No problems found elsewhere:
- Every Result sentence in the behavior and iEEG notebooks matches their outputs, and so do the README's counts.
- The `reason` fields state my round-1 reasons faithfully. Each is my table entry with the relevant problem text added.
- fig6d's reason adds problem 10, which I had marked as not affecting a conclusion.
- Problem 4 is attached to no claim, but it is answered in cell 5.

**3. Round-1 points**

Resolved:
- **1 (figs33):** variance explained is now scored on the Ketamine series only.
- **2 (fit variants):** bounded, mean-removed and median fits were run, and degenerate fits are counted.
- **3 (figs30):** the variant from the file's infusion time was run.
- **4 (series 23 timing):** series 23 starts ≥ 235 s after the infusion in every session (cell 5).
- **5 (fig4h, fig4i weighting):** NaN weights, renormalization and a 20-replicate Pre set were run. The direction holds on the printed numbers.
- **7 (fig5d, figs32c):** the checks now use the criterion's interval wording.
- **8 (fig4b, fig5b):** outcomes changed, and the normalization question is put to the paper's authors.
- **10 (leakage):** a held-out check was added for fig6d.
- **11, 12, and the "Not checked" items:** tone and light contamination, the replicate control, and the sub-H files (fig2g, fig2i and fig3b are now tested).

Partly resolved:
- **6 (figs31b ranking):** both rankings are now shown, but the conclusion misreports which ones hold.
- **9 (fig1m):** unchanged; it does not affect a conclusion.

What remains that bears on a conclusion:
1. **Leiden partition:** it is not reproducible across runs. The conclusions and record for fig4de, figs31b, fig4g, fig4i, fig4h and the fig4h progression describe a run that is not the one printed. They need to be rewritten from the printed outputs, and the statement about my "different partition" withdrawn. Alternatively, pin the PCA/neighbor steps, or report these results as run-dependent.
2. **figs31b:** in the printed run, the result holds only under the criterion's cluster-mean ranking at FDR 0.05. Partially reproduced still fits, but for different reasons than the text gives.
3. **sub-5 assumption:** fig6d, fig6h, figs34d and figs34g change outcome if sub-1 or sub-3 was the excluded animal. The assumption is stated and reasonable; the question is open with the authors.
4. **Five human iEEG claims:** they are labelled `too_large` but are blocked for time, and the data to test them are deposited.
5. **fig2g:** "elbow at six" depends on the rule chosen. The chord rule gives 8.
