**Round 2 verification: Ray, Moaddab & McDannald (2022) on CRCNS nac-1**

The claims file has 34 claims and the attempt record has 34 outcomes, one per claim: 16 reproduced, 7 partially reproduced, 10 not reproduced, 1 blocked. All population claims are judged on the primary partition, N4 (ii).

**1. Outcomes and assumptions**

I agree with all 34 outcomes. Notes on the ones that changed, or that depend on a choice:

- **units-recorded**, not reproduced: agree. Cell 10 gives 90 sessions, and the criterion's tolerance is zero.
- **fig1g-discrimination**, reproduced: agree, because the criterion accepts "under one reading". But the outcome rests on one reading: all sessions, with 0/0 suppression ratios read as 0.
  - At the median of 50 seeds the uncertainty-minus-safety CI is [0.012, 0.599], and it excludes zero in 68% of seeds (cell 23). In the CI section it does so in 3 of 5 seeds with the analytic SE and 2 of 5 with the inner bootstrap SE (cell 124).
  - Under 0/0 = 1 with the 82 sessions, which the record itself adopts for fig1h because it gives the paper's F exactly, that CI contains zero in every seed with the standard interval.
  - The outcome rests on a deviation the record names ("a tie-break the criterion does not give"), yet it carries no `assumed: true`. It should, and the note should say that the authors' 0/0 handling does not reproduce the claim with the standard interval.
- **fig9bcd-reward-pre-post**, not reproduced: agree.
- **fig10bcd-poke-cessation-pre-post**, now not reproduced: agree. With the 1-s baseline and cessations at recording pauses dropped, the Bidirectional Valence pre CI contains zero under every reading: 0.085 [-0.009, 0.207] and 0.218 [-0.038, 0.485] (cell 117). This holds in every seed, form and SE (cell 124). My round-1 "reproduced" was on the uncorrected events.
- **fig10a-poke-cessation-anova**, now reproduced: agree. Under ITI reading (b) the interval p is 0.26 and 0.12 and the interaction p < 1e-4 (cell 114).
- **ITI reading (a)** is empty by the data, not only by construction. The latest recorded poke or pellet is 33.54 s after onset (cell 6), so no 4-s window can lie after onset + 30 s. Reading (b) is therefore the only testable reading for fig9 and fig10.
- **The `assumed: true` outcomes** (partition, the script's 193 units, 0/0 = 1 for fig1h, the 0.3875 waveform boundary and the unhalved peak-valley duration, the N4 SD for per-trial normalization, the event windows) each state their assumption in the deviations. All are reasonable.
  - The partition assumption is the weakest, since the alternative partition flips fig5ab and fig7. Both flips are disclosed.
  - most-units-threat and fig3ab-rate-cv-unimodal carry no flag, which is fine: they hold under every partition.

**2. Text the printed numbers do not support**

- **Cell 33:** "Other readings give partitions whose centroids do not show the patterns (smallest cosine below 0.5)." Cell 30 shows smallest cosines of 0.73 for N4 (i), which is one of the fitting partitions, 0.65 for N1 (ii) and 0.66 for the script normalization (i).
- **Cell 33 and the record's fig2 notes:** "each found in 1 to 3 of 100 starts". The Hz most-frequent partition was found 19 times (cell 30). The phrase is true only of the normalized readings.
- **Cell 86:** "largest difference 1.3e-15". Cell 85 prints 9.09e-16.
- **Cell 105:** "Threat Inhibited post-reward firing and its rise exclude zero under both (0.67 [0.12, 1.35] and 0.58 [0.04, 1.10])". Those two values are the TI post values under (i) and (ii). The rises are 0.71 [0.15, 1.37] and 0.90 [0.32, 1.45] (cell 104). The conclusion is unaffected.
- **Summary, cell 126:** the script variant "brings several effect sizes to the paper's values (… fig9hij)". The Danger Excited R² of 0.212 is outside 0.25 ± 0.025 (cell 111). Only the Bidirectional Valence R² (0.062) is within tolerance.
- **Cell 27 and the record's fig1h-discrimination-safety notes:** "p of 1.4e-4 or less". The outputs print p only as 0.0, so this cannot be checked against them.

Everything else checks against the printed outputs: the other conclusions, the remaining Summary text, the README tallies and the record's notes and responses.

The record's verifier reasons are faithful paraphrases of my round-1 report, with problems 1–5 and 9 folded into the relevant claims.

**3. Round-1 points**

Resolved:
- Problem 1: the event baseline is now bins 4–7 (`nac.EVENT_BASE`). The script's 1–4 baseline is kept as a variant.
- Problem 2: windows outside a recorded segment, and cessations at pauses, are dropped. Cell 99 prints the counts.
- Problem 3: the CI section (cell 124) tests both interval forms, both SEs and five seeds, and the seed-1001 flags are now printed.
- Problem 5: the screen choice is stated as an assumption (cells 14–15, which repeat the same paragraph).
- Problem 6: outcome tallies now count only partitions with smallest cosine ≥ 0.7.
- Problems 7 and 8 are resolved.
- From section C: the script lines are printed (cell 8), the re-runs and dropped-event counts are done, and the per-rat session counts are printed.

What remains that bears on a conclusion:
- **fig1g:** the reproduced outcome is marginal and should carry `assumed: true`, as in part 1.
- **Problem 4, partition choice:** stated as an assumption, and the alternative partition is shown. fig5ab-the-onset and fig7-tuning-curves still depend on it.
- **Questions on the claims file**, still open (my problem 9): the 0/0 = 1 reading, normalization (the script variant matches the paper's effect sizes for fig4ab, fig4cd, fig8ef and fig9hij), and the CI form. The record says these are asked in questions/crcns-nac-1.yaml.
- **A further claims-file defect:** in fig9efg-reward-cue-correlations, the conditions for reproduced and partially reproduced overlap. The "reproduced" condition does not test the Danger Excited part of the statement, which the partial condition does. Here both are met, and cell 109 resolves it toward partially reproduced. That choice is reasonable, but the criterion should be fixed.
- **The 95-session count:** still not explained. Extended Data Figure 1-1 is not available to compare against.
