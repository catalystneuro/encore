**Verifier report, round 2: Komori et al. (2026) on DANDI:001425 0.250705.0947**

The claims file has 24 claims and the attempt record has 24 outcomes: 6 tested and 18 blocked (data_missing).

**The main problem in this round.** Almost every number in the "Result" cells, the attempt record's notes and findings, and the README differs from what the executed notebooks print. The same thing happened in round 1. The kept ICs are different too:
- The record says IC selection "removes ICs 24 and 29". Decoding cell 2 and features cell 4 print `removed for VIF: [29, 2]`.
- The SHAP notes match ICs 2, 25 and 6. Features cell 15 prints `matched: {'medial anterior (IC7)': 19, 'RSP (IC6)': 16, 'MOs (IC4)': 15}`, and IC 2 is not even kept in this run.

The text was written from a different run than the one executed.

### 1. Outcomes

| Claim | Stated | Agree? | Basis in the printed outputs |
|---|---|---|---|
| rest-decoding-above-null | partially_reproduced, seed_sensitive | **Outcome yes, stated basis no** | The record rests the outcome on R4 b + R5 b: "0.500 against 0.417, p = 0.0053". Features cell 19 prints **0.614 vs 0.576, p = 0.412**, and 0 of 5 seeds are above null. Two other combinations do show the model significantly above null: R4 b + R5 b + R3 b, 0.641 vs 0.473, p = 0.0025 (features cell 19), and R5 b + R8 b, 0.558 vs 0.529, p = 0.031 (decoding cell 21). Both means are far outside 0.82 ± 0.082, so the outcome is partial, but on different evidence. Each of those two was run at one seed only, so `seed_sensitive` is not shown for either. R4 b + R5 b, the combination that was run at five seeds, is never significant. |
| rest-loss-accuracy-vs-null | not_reproduced | Yes | R5 a: loss p = 0.90, accuracy p = 0.376. R5 b: loss p = 0.326, accuracy identical to null (decoding cell 24). 0 of 16 combinations have both. |
| rest-needs-0-1-hz | not_reproduced | Yes | 0.1 Hz is never above null: main p = 0.149, R5 b p = 0.246, 0 of 10 seed runs (decoding cells 27–28). The main 2 Hz AUC is 0.674, far from the paper's 0.51. The cutoffs were not run in the two combinations that are above null. |
| rest-ic-count-and-window | partially_reproduced | Yes | Under R5 a, reading (b), 10 ICs have the highest median (0.717, against 0.602 and 0.703). No reading puts 1.5 s highest (features cells 7–8). |
| rest-vif-below-10 | not_reproduced | Yes | The 10-IC maxima are 27.91 (validation, uncentred), 7.31 (centred) and 10.90 (training); none is within 9.0 ± 0.9 (features cell 11). On training samples, reading (a), the comparisons match the paper (7 ICs lower, Holm p = 0.024; 13 and 15 p = 0.19), but the 10-IC maximum does not hold. |
| rest-shap-medial-anterior-first | not_reproduced | **Not supported as reasoned** | Features cell 16, reading (b) (peak) under R5 a: the medial anterior IC peaks at −0.10 s and MOs at −0.067 s under both SHAP readings (`precedes: ['MOs (IC4)']`). That is the criterion's partial case. Under R5 b with the code's SHAP reading it "precedes both", but that peak sits at the window edge (−1.5 s) with a mean SHAP of −7.7e-9, a degenerate peak I would not count. Not reproduced can only hold through the criterion's "no IC matches" clause: IC 19 has 0.288 of its weight in the midline band against 0.374 in MOs (features cell 15). The record does not make that argument. On the attempt's own matching rule the outcome is partially_reproduced. |
| 18 claims on stimulation data | blocked (data_missing) | Yes | Unchanged from round 1. |

**Assumptions.** Every tested outcome has `assumed: true` and states its assumptions as deviations: R1 a (first three mice and sessions), compact-map IC selection, pupil cleaning, the hemodynamic variant, R5 b as the better-supported reading, ICs fixed across cutoffs, and per-epoch "experiment" for SHAP. They are stated and reasonable. Two deviation texts contradict the outputs: "removes ICs 24 and 29" and "the third [restart] shares 4 of 10". Features cell 20 prints `matched_to_main` = 10, 10, 10.

**Misreading in the claims file (reported, not corrected).** R5 says "for resting data it states no rule". The paper says such sessions "were therefore excluded from all datasets" (Results, somatosensory, paragraph 1), so this still stands.

### 2. Sentences the printed numbers do not support

**Decoding cell 22**
- "0.669 against 0.688 … (paired t = -0.78, p = 0.477), and with R5 b 0.556 against 0.468 (p = 0.209)". Cell 16 prints 0.720 vs 0.725, p = 0.863, and 0.558 vs 0.583, p = 0.578.
- "R5 a is never above null (p = 0.48 to 0.91)". Cell 19 prints p = 0.26–0.86.
- "R5 b is above null at one seed of five (claim + 3000, 0.708 against 0.494, p = 0.0475; the others p = 0.18 to 0.98)". Cell 19 prints claim+3000 as 0.515 vs 0.557, p = 0.67, and no R5 b seed is above null.
- "The five other readings … (p = 0.11 to 0.77)". Cell 20 prints 0.41–0.94.
- "nor are any of the 16 combinations … (p = 0.11 to 0.94)". Cell 21 prints 1 of 16 significant (a a a b, p = 0.031).
- "training AUC is 0.746 under R5 a and 0.516 under R5 b". Cell 16 prints 0.802 and 0.593.
- "under R5 b four of the five stop at their first or second training epoch". Cells 16–17 print model epochs [4, 7, 8, 10, 4].
- The 12.8% and 48% shares are supported.

**Decoding cell 25**
- All four means and p-values are wrong. Cell 24 prints loss 0.610/0.613 (p = 0.90), accuracy 0.652/0.674 (p = 0.376), and for R5 b 0.689/0.683 (p = 0.326) and 0.551/0.551 (no p).
- "No seed gives either test significant (the smallest p is 0.065…)". Cell 24 prints R5 a claim+1000 loss p = 0.048, with the model higher.
- "the five readings under R5 a (p >= 0.12)". Cell 24 prints R2 high-pass accuracy p = 0.017, with the model higher.

**Decoding cell 29**
- "0.702 against 0.716, p = 0.845" and "0.480 against 0.416, p = 0.523". Cell 27 prints 0.668/0.726, p = 0.149, and 0.552/0.441, p = 0.246.
- "R5 a p = 0.63 to 0.84; R5 b p = 0.14 to 0.53". Cell 28 prints 0.15–0.65 and 0.18–0.84.
- The 2 Hz values "0.637 against 0.608, p = 0.227; … 0.475 against 0.494, p = 0.885". Cell 27 prints 0.674/0.694, p = 0.642, and 0.590/0.482, p = 0.244.
- "No cutoff is above null … (p >= 0.23)". Cell 27 has a minimum of 0.149.
- "the one where the 0.1 Hz decoder is above null": wrong combination, as in §1.

**Features cell 9**
- "reading (a) cannot reach 13 ICs (11 are kept, 4 removed)". Cell 7 prints 3 removed.
- "reading (b) keeps 6, 8 and 9". Cell 7 prints 5, 8, 10.
- "10 ICs (0.591; 7 ICs 0.540, 13 ICs 0.486)". Cell 7 prints 0.717, 0.602, 0.703.
- "reading (a) at 13 ICs (0.694…)". Cell 7 puts reading (a) highest at 7 ICs (0.761).
- "under R5 a 10 s is (0.695 …)". Cell 8 puts 5.0 s highest (0.745).
- R5 b "0.497, … 1.0 to 10 s at 0.495". Cell 8 prints 0.577 and 0.572–0.5725.
- "smallest p 0.15". Cell 7 prints 0.073.
- "none of these models is above its null model (p = 0.07 to 0.96)". Cell 7 prints R5 b, reading (b), 7 ICs at p = 0.045, with the model higher.

**Features cell 12**
- "60.1 … (per model 20.5 to 60.1; 35.8 under reading b)". Cell 11 prints 27.91 (13.07–27.91) and 19.79.
- "Holm p >= 0.29". Cell 11 prints 0.095.
- "With an intercept … 5.58 … 7 ICs … lower (p = 0.024) and 13 and 15 … (p = 0.62)". Cell 11 prints 7.31 with Holm p = 0.45, 1, 1.
- "14.05 (reading b 11.79)". Cell 11 prints 10.90 and 8.05.
- "4.5e6 and 3.7e8". Cell 11 prints 1.5e9 and 1.2e7 (paper VIF), 1.7e9 and 6.3e6 (centred).
- "9.58 for the 10 kept ICs". Cell 4 prints 9.48.

**Features cell 17**
- ICs "2 … 0.164 … 25 (RSP, 0.473) and 6 (MOs, 0.793)". Cell 15 prints ICs 19 (0.288), 16 (0.239) and 15 (0.683).
- "smallest p 0.094". Cell 16 prints 0.072.
- "the medial anterior IC peaks at 0.0 s, after RSP and MOs (-0.03 s)". Cell 16 prints −0.10 s, before MOs (−0.067 s).
- "explains 0 or 1 samples". Cell 14 prints 0 for every model.
- "only the RSP IC differs from null (-1.1 to -0.7 s, p = 0.033 and 0.044)". Cell 16 prints RSP p = 0.87 and 0.63.
- "the medial anterior IC peaks at 0.0 s, last". Cell 16 prints −1.5 s.
- "R5 a 0.669 against 0.688, R5 b 0.556 against 0.468". Cell 14 prints 0.720/0.725 and 0.558/0.583.

**Features cell 21**
- "0.500 against 0.417 … p = 0.0053". Cell 19 prints 0.614/0.576, p = 0.412.
- "0.629 against 0.480 (p = 0.042)". Cell 19 prints 0.641/0.473, p = 0.0025.
- "the first holds at one seed of five (the others p = 0.19 to 0.31)". Cell 19 prints 0 of 5, p = 0.41–0.90.
- "null models below 0.5 (in 3 to 5 of the 5 folds at every seed)". Cell 19 prints 0, 2, 1, 0, 2.
- "loss p = 0.33 and 0.29". Cell 19 prints 0.312 and 0.055.
- "two keep 10 ICs that match … AUCs of 0.668 and 0.671; the third shares 4 … (p = 0.07 to 0.60)". Cell 20 prints all three matching 10 of 10, AUCs 0.706–0.720, p = 0.44–0.97.
- "2 of the 27" happens to be the right count, but it names the wrong combinations.

**Summary (decoding cell 30, features cell 22) and README**
- "partially reproduced (… seed sensitive; one combination, R4 b with R5 b)". R4 b + R5 b is not significant. The significant combinations are R4 b + R5 b + R3 b and R5 b + R8 b, each at one seed.
- README: "Partially reproduced (one reading combination, at one seed of five)". Two combinations are significant, and neither was run at five seeds.
- The rest of the Summary and README (methods differences, dataset findings) is supported.

**Attempt record**
- The outcome notes repeat every number quoted above. They also give "By mouse … 0.596 and 0.602, 0.574 and 0.551, 0.761 and 0.792"; decoding cell 18 prints 0.790/0.742, 0.512/0.508, 0.801/0.832.
- The code_mismatch finding gives "60.1 …, 14.05 … and 5.58"; cell 11 prints 27.91, 10.90 and 7.31.
- The second methods_unavailable finding gives "model 0.669 against null 0.688; … 0.500 against 0.417, p = 0.0053"; the outputs are 0.720/0.725 and 0.614/0.576, p = 0.412.
- The data findings and the hemodynamic and pupil deviations are supported (decoding cells 4, 5, 7, 8, 12, 13). The exception is "min-max normalisation of the raw trace leaves almost no dilation", which no output shows.

**My round-1 reasons in the record.** They are stated in my own words and faithfully, for all 24 claims.

### 3. Round-1 points

**Resolved**
- **B4 (VIF).** The paper's code was read, and the uncentred VIF is used and selects ICs.
- **B3.** The null-shuffle share is printed and disclosed.
- **B7.** The per-epoch "experiment" is now stated as an assumption.
- **B9.** Edge peaks are counted: 15 of 117, 2 of the 17 epochs kept by R5 b.
- **B8.** Disclosed, with the label plot.
- **B10, 1.5 s window.** Explained by the paper's 46 frames.
- **C, training curves.** Shown (decoding cell 17).
- **C, R5 b over seeds.** Run at five seeds.
- **JADE determinism.** Shown, since all restarts match 10 of 10.

**Partly resolved**
- **B1 and B2.** R5 b is run as a main reading and 16 combinations under it. But R1 b is not run, R4 b + R5 a is not run, and the significant combinations are not run at other seeds.
- **B5.** The hemodynamic check was added (median r 0.26–0.70). The compactness rule is still unverifiable.

**Remaining, bearing on a conclusion**
1. The conclusions, Summary, README and record do not describe the executed run; every numerical sentence above must be rewritten from the outputs. The record's IC list and its SHAP match point to a different decomposition than the one executed.
2. The rest-decoding-above-null partial outcome rests on R4 b + R5 b + R3 b and on R5 b + R8 b at one seed each. Both need a five-seed check before `seed_sensitive` and "weak" can be justified.
3. rest-shap-medial-anterior-first: under the criterion and the attempt's own match, the printed outputs give partial (R5 a, peak reading). Either the outcome changes, or the record must argue that IC 19 does not match (0.288 of its weight in the band against 0.374 in MOs). The old B6 point now bears on this conclusion.
4. rest-needs-0-1-hz was not run in the combinations that are above null, which the criterion asks for.
5. R1 b and the paper's possible epoch rule remain untested. R5 b keeps only 17 epochs.

### 4. Critical findings

No finding in the attempt record's `findings` is rated `critical`. I agree with the ratings:
- **Finding 1, swapped excitation wavelengths (`minor`).** The values show the swap (decoding cell 5), and the series descriptions give the right channel.
- **Finding 2, unflagged failed pupil detections (`minor`).** The values are evident (2.88e21 pixels).
- **Finding 3, six files without behaviour (`minor`).**
