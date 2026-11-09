**Verifier report, round 2: Skromne Carrasco et al. 2026 on DANDI:001676, 0.251205.2137**

The claims file has 32 claims and the attempt record has 32 outcomes: 18 reproduced, 6 partially reproduced, 3 not reproduced and 5 blocked. Cell numbers below are those of the re-executed notebooks.

### 1. Outcomes and assumptions

I agree with all 32 stated outcomes. Five need a comment.

- **edf2-no-registration-confound (reproduced).** I agree. Pooled over all CellReg scores with Bonferroni ×4, both absence tests are non-significant and displacement against score gives p 0.0011 (cell 42). Two problems remain:
  - The outcome rests on reading "all cells" as every CellReg score. With score > 0.8 only, displacement against score is 0.67 and 0.055, so the claim would not reproduce. The record does not set `assumed: true`, and the Summary (cell 98) says "no (both HDI readings agree)".
  - Under raw HDI the minimum score is −0.10 (cell 42), which is not a valid CellReg score. It may feed the raw-HDI regression (p < 0.0001). The n is 49 or 108 against the paper's 72.
- **edf4ij-pv-decay (reproduced).** I agree under the main reading. The claims file requires the mean at the longest interval to stay above 0. Under raw HDI mouse 5 gives −0.00 and −0.19 (cell 55), so the outcome rests on the HDI reading, and cell 56 itself says that part "holds in 4 of 5 there". The record does not set `assumed`, and the Summary says "no".
- **edf2ab-jaccard (not reproduced, assumed).** In round 1 I had it as reproduced. I now accept the record's position: one HDI reading applied to every claim is reasonable, and the record states that the outcome rests on it.
- **fig2g-environment-classifier (reproduced, assumed).** The criterion is met. The new controls show that cell-pair presence alone reaches 0.70 against 0.28 (cell 77). The shuffle used permutes all features, so it also destroys the presence pattern. The criterion's "more accurate than shuffles" is therefore met by presence alone. The record says the data do not show that the classifier reads correlations, which is accurate.
- **fig1k (blocked, too_large).** This is defensible on the printed numbers: 51 min of fits for the partial reading, plus roughly 9 min to load 97 sessions, against a 60 min limit. Fits run 4 at a time, while loading uses 12 workers.

The other `assumed: true` flags are stated and reasonable. Three small inconsistencies:
- edf9 is flagged `assumed`, but the Summary says "no".
- edf1h is listed in the Summary as resting on the normalization reading but has no `assumed` flag.
- The sign convention for edf10b and edf10c is now justified independently from Fig. 1g: 5 of 5 signs match as computed and 0 of 5 reversed (cell 24). It is reasonable.

### 2. Sentences the printed numbers do not support

- **Attempt record, fig1k notes and the fig1k response; README; main cell 0; main cell 98; decoding cell 13:** "2.39 s each, an estimate of 75 minutes … and 47 minutes" / "estimated at 75 minutes". Decoding cell 12 prints 2.57 s per fit, 81 min and 51 min. The conclusion stands, since both are over the limit.
- **README:** "It takes about 25 minutes". Main cell 99 prints 40.7 min.
- **Main cell 2:** "About 16 minutes". Cell 3 prints 1992 s.
- **Main cell 98:** "Every HD cell claim is also run with raw HDI; it changes the outcome of edf2ab-jaccard, fig2h-coherent-remapping and edf4c-previous-session." This omits two claims:
  - fig1f: under raw HDI no mouse with 18 sessions matches (cells 21 and 22).
  - edf4ij: mouse 5 is ≤ 0 under raw HDI (cell 55).

  The record's methods_unavailable finding has the same omission.
- **Main cell 98, Summary table:** "edf4ij … no (raw HDI: decay in 5 of 5)" and "edf2 … no (both HDI readings agree)". Both rest on a reading (see section 1).
- **Main cell 98:** "unsigned pairwise offsets, the only reading whose shuffle medians (39 to 57 degrees) match the paper's 51 to 57". For edf4g, mice 3 and 1 give 39 and 48 (cell 49), below the paper's 51 to 54.
- **Main cell 96:** "The medians are about half the paper's (18, 12, 27, 15)". The medians 6, 6, 9 and 6 are one third to one half of those values.
- **Main cell 10:** "Every claim below that rests on HD cells is also run with raw HDI". edf1h (cell 58) uses smoothed HDI only. This does not bear on an outcome.

Every other sentence I checked in the conclusions, the Summary and the record's notes matches the printed outputs. The verification `reason` fields state my round-1 reasons faithfully, mostly in my own wording. They combine the outcome rows with the relevant problems (2, 3, 4, 5, 6, 7, 8, 9, 10) on the right claims. "26 of 32 agree" matches my round-1 report: I disagreed on 6 claims (edf2ab, edf2, edf4f, edf9, edf10b, edf10c).

### 3. Round-1 points

Resolved:
- 1: sign of the change, now printed both ways with a justified convention.
- 2: raw HDI is now run for the claims I listed.
- 3: cell 10 now states the conflict with the Extended Data Fig. 1e proportions.
- 4: edf2 is rerun over all scores with Bonferroni ×4.
- 7: the looser test-session rule for the decoders.
- 8: autocorrelated bins in edf1h.
- 9: edf4ef fragility.
- 10: the dates identifying the probe week (cell 80).

Partly resolved:
- 5, fig2g: the controls were added. A shuffle that keeps the presence pattern and permutes only the values was not run. It would show whether the correlations carry environment information at all. This bears on how the claim is read, not on the criterion.
- 6, fig1k: fits now run in parallel and the estimate is recomputed. The stated figures are stale (section 2), and the partial reading is near the limit at 4 concurrent fits.

New, bearing on a conclusion:
- `assumed` is missing for edf2 (the all-scores reading) and edf4ij (the HDI reading), and the Summary marks both "no".
- The raw-HDI edf2 cell set includes a CellReg score of −0.10.

Claims file: I still found no place where it misreads the paper.
