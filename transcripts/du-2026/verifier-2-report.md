**Verifier report, round 2: du-2026-01 (doi:10.64898/2026.08.04.742876)**

The claims file has 33 claims and the attempt record has 33 outcomes, all `reproduced`. No outcome is marked `assumed: true`. Cell indices below are those of the re-executed notebooks; in 02 they have shifted by about two from round 1.

**1. Outcomes**

I agree with all 31 outcomes I agreed with in round 1. The numbers in the re-executed notebooks are unchanged.

- **maze-gain and rff-maze (blocked → reproduced):** I agree, provided the protocol's author step 1.4 says what the response says. I cannot see docs/protocol.md.
  - maze-gain: 07 cell 4 gives 0.90533, 0.000513, 0.542% and −0.0000371, all within tolerance, and the interval 0.00026 to 0.00076. 07 cell 13 shows the release's own code gives identical values.
  - rff-maze: 07 cell 7 gives 0.0000448 and 0.0001386, both inside the widened range, with all three map gains positive.
- **maze-gain needs an `assumed` flag.** Its criterion states no reproduction rule ("Not on this attempt's datasets"). The rule used, all four values within tolerance as for rtt-gain, is the author's (07 cell 3). It is reasonable, but the outcome rests on it, so it should be marked `assumed: true`.
- **maze-gain's replacement tolerance is too tight (claims-file problem, reported, not corrected).** The tolerance (±0.000004) is narrower than the rounding of the paper's printed −0.00004 (±0.000005). Under the other four estimator seeds the replacement gain is −0.0027212, +0.0000294, −0.0000190 and +0.0000075, so it changes sign. The `seed_sensitive` marking is warranted.
- **estimator-family-nlb:** I agree. The MC_Maze part is now reported (07 cell 10: 0.000455 and −0.000243) and correctly kept out of the outcome.

**2. Sentences the printed outputs do not support**

- **02 cell 36** says "so two of those seeds put both SBP values outside their 10% tolerances". The attempt record (nested-replacement-negative) says "with seeds plus 1000 and plus 3000 both SBP values fall outside". Per 02 cell 35, only +1000 has both outside (−0.00887 and −0.00496). At +3000 the history value, −0.00428, is inside [−0.00448, −0.00366]. The outcome at the fixed seed is unaffected.
- **Finding 1, 02 Summary (cell 61) and the finding about the paper's data checks** say velocity is "exactly" the forward difference, with "correlation 1.000 in all 18 development sessions". 02 cell 5 shows 2021-10-15 CO second component at 0.987 (SD ratio 0.99). This is probably the session with the 1094 ms gap. Minor.
- **README** says "The MC_Maze gains … move outside the tolerances under others". Per 07 cell 4, the gain stays within tolerance under 3 of the 4 other seeds; it is the replacement gain (07 cell 4) and the lowest map gain (07 cell 7) that move outside under every one.
- **README** ("under other split seeds … the values move outside their 10% tolerances") and **05 Summary (cell 17)** ("the 10% tolerances do not hold under other split seeds") overgeneralize. Per 05 cells 6 and 9, at seed +3000 the geometry mean 0.02070 and the history mean 0.00818 are within tolerance.
- **Finding about the paper** says the code "reproduces its reported values at their printed precision for every claim tested". Not all:
  - 02 cell 29: date intervals 0.02401 against the paper's 0.02404, and 0.00711–0.01591 against 0.00709–0.01594.
  - 02 cell 59: rff-link reading (b) fails.
  - 02 cell 53: representative-trial matches under one tie reading only.
  - 04 cell 5: temporal-offset reading (a) fails under the fully nested estimator.
- **Attempt record, estimator-family-link deviations:** "0.0261224 and 0.0261219", "lsqr took 58 min" and "a full lsqr run … gave the same signs" have no printed output. 03 cell 6 also states the 5e-7 agreement without output.
- **07 cell 14:** "none of the analysis windows reaches a gap" is only indirectly supported. 07 cell 2 shows every trial runs at least 959 ms past movement onset, longer than the 800 ms window. Unlike 06, it prints no NaN count for the analysis arrays.

Every other conclusion and Summary sentence, and the rest of the README and the attempt record's notes, match the printed outputs. That includes:
- the counts in 05 cell 13 (20, 19, 20, 20);
- "three outside" in 05 cells 7 and 10;
- "mostly outside" in 05 cell 16 (7 of 12);
- the MC_Maze values;
- finding 2: SBP 0.0437 to 341 (05 cell 2) and TCR 0 to 11 (02 cell 4);
- finding 3: the 1094 ms gap (02 cell 4);
- finding 4: 15 NaN bins, none in the analysis arrays (06 cell 2).

The README claim counts (3+17+1+2+4+4+2 = 33) agree with the claims file.

The attempt record states my round-1 reasons faithfully and in my words, lightly edited ("CI" became "interval", problem numbers folded in).

**3. Round-1 points**

Resolved:
- Problem 1: reading (c) is now the position in trial order, 41 (02 cell 53).
- Problem 2: feature counts are now computed (04 cell 3).
- Problem 4: confirmation outcomes are marked `seed_sensitive`.
- Problem 5: now reported as finding 1.
- Part C, ports against release code: 07 cell 13 shows identical values for `evaluate_fully_nested_audit` and `evaluate_nonlinear_neural_audit`. The block, nonlinear-context and `decoders_nested` ports were not compared.
- Part C, confirm-replacement under other seeds: now printed (05 cell 12).
- Part C, later 001201 versions: now listed (02 cell 2).
- Part C, MC_Maze: now tested.

Unchanged, and not bearing on any conclusion:
- Problem 3, cholesky in place of lsqr; the supporting numbers are still not printed.
- Problems 6 and 1 needed no change.
- Reading (b) of the nonlinear context in estimator-family-link is still not run.

Still open and bearing on a conclusion:
- maze-gain's reproduction rule is the author's and should be flagged `assumed: true`.
- maze-gain's replacement tolerance is tighter than the paper's rounding, and the value changes sign across seeds.
- Both MC_Maze outcomes depend on protocol step 1.4 allowing data-elsewhere claims to be tested, which I could not check.

**4. Critical findings**

No finding in the attempt record is rated `critical`. The four rated `minor` are correctly rated. The data checks (no duplicates, one clock, the 9/18/375 structure, labels agreeing) show nothing that would be critical.
