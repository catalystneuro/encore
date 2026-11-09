I wrote the claims file at `claims/crcns-nac-1/10.1523-jneurosci.1107-21.2021.yaml`: 34 claims, all with quotes. All 34 quotes pass `tools/claims_check.py` and the file matches the schema. The checker still reports 44 problems, all of the "VALUE NOT FOUND (confirm by reading)" kind. In the extracted text, minus signs and the "× 10^" in p-values come out as a replacement character, so the checker can't match those values. I checked each one against the text by reading. Nothing was committed.

**Text read**
- The version of record (the journal PDF's text under `paper/`): Methods, Results, figure legends and Discussion.
- Not read: Extended Data Figures 1-1, 1-2 and 2-1 (per-rat suppression ratios, session-by-session suppression ratios, alternative clusterings) are not under `paper/`. No claim rests on them alone, because the Results state the numbers used.
- No PDF renderer was available, so I read figures only through their legends and the Results.
- Code: the paper links only http://mcdannaldlab.org/resources, and that page returns 404, so no code was read. I read the data descriptor only for what the data set holds.

**Statistics and criteria**
- 117 statistical values: F and t tests, Pearson correlations, Fisher r-to-z, Hartigan's dip, Pitman–Morgan, and 46 bootstrap confidence intervals. All recorded as printed.
- Every claim has a criterion. Where the paper gives a CI, the tolerance is the distance from the mean to the nearer bound; otherwise it is 10%. Counts of deposited units, sessions and rats must match exactly.
- Absence claims are judged on the paper's own test: a CI containing zero, p ≥ 0.05, or the Bonferroni level 0.05/9.

**Details the paper leaves open, with the readings named**
- **z-scoring:** over four trial types, or three with uncertainty collapsed. How uncertainty is collapsed: mean over all eight trials, or mean of the shock and omission traces.
- **Per-trial normalized firing** (Figures 7 and 8): three readings, mainly which baseline is subtracted, plus z-scoring each trial over the unit's bins.
- **Suppression ratio when a trial has no pokes (0/0):** leave the trial out, or set it to 0.
- **Sessions for Figure 1G:** the 82 sessions with a cue-responsive unit, all 95, or the 79 sessions of the main populations.
- **Cue-responsive screen:** uncertainty tested as one cue, or shock and omission trials tested separately.
- **k-means:** clustering on normalized firing (Results) or firing in Hz (Methods). No seed or replicate count is given, so either the best of 100 starts or the most frequent partition. k = 5 is fixed, with the paper's rule for choosing it run as a variant.
- **Population labels:** the paper's own labels if the data set holds them, otherwise the reproduced clusters.
- **Tuning curve:** one regression on the 10-s cue mean (Methods), or per-1-s-bin betas averaged (Results).
- **Fear output regression:** one model with both regressors, or a separate model for each.
- **Reward and nose-poke windows:** which ITI events qualify (two readings) and how the trace is normalized (two readings).
- **Comparing two correlations:** Fisher r-to-z for independent correlations, or Steiger's test.
- **Figure 6 between-population test:** p < 0.05 (legend) or 0.0056 (Methods).
- **Coefficient of variance:** spikes from the baseline periods, or the whole session. The dip-test implementation isn't named.
- **Narrow/wide waveform boundary:** taken as the lowest point between the two modes of the 172-unit histogram, because the figure's dashed line couldn't be read.

**Missing from the paper**
- Some degrees of freedom imply fewer units than the stated n, with no reason given: Figure 8 (25, 54 and 86 units against 26, 55 and 91) and the Figure 9 reward ANOVA (165 of 172; 87 of 91 Bidirectional Valence). This is recorded as a reading.
- The Figure 1C acquisition claim needs the eight pre-surgery sessions. The data set's description lists only the 95 recording sessions, so they may not be there.
