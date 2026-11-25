**Round 2 verifier report: gonzalez-2024-01**

**1. Outcomes**

The claims file has 30 claims and the attempt record has 30 outcomes: 16 reproduced, 5 partially reproduced, 9 blocked. The round-1 verification lists all 30.

- **I agree with 28 outcomes as stated:** fig1d, fig1-switch, fig1-training, fig2c to fig2h, fig2-controls, fig3d, fig3e/f/g (blocked, other), fig4c, fig4d, fig4ef, fig4gh, fig4-controls, fig5, fig4s5, fig4s7, fig6cd, fig7b (blocked, data_missing) and fig7de/f/g/h (blocked, other).
  - Changing fig7de to fig7h from data_missing to other is correct now. These four were testable with the paper's matches, and the notes say so.
- **fig4s6-incorrect-coding-overlap (reproduced, seed_sensitive):** I now accept it. The criterion is applied under the claim's seed and on the unit set of the code's figure function, and `seed_sensitive` is set. It is fragile: with MUA, 5 of 12 KS tests have p < 0.05, and 2 of the 4 other seeds fail (cell 67).
- **methods-lookahead-encoder-best (partially reproduced):** I now accept partially_reproduced over my round-1 not_reproduced.
  - The "highest mean R2" part holds under every run (cell 82).
  - The "p < 0.05" part fails on the only reading that has pairwise tests (p = 0.98 and 0.36).
  - The notes say this plainly.
- **Assumptions:** only fig1-switch-performance carries `assumed: true`. Its assumption, the claims file's 10-point "similar" threshold, is stated in the notes and deviations and is reasonable.
  - Caveat: `pct_sw_correct` is biased downward (my round-1 B5) and the fix was not run. The true Switch accuracy is therefore higher than 73.8%, so the Switch minus non-Switch difference is larger than 2.4 points.
  - Pooled, the gap is already 9.2 points (80.8 against 71.6, cell 18). So the "similarity" part sits closer to the threshold than the notes say.
  - The outcome is unaffected, because the trial count (69 against 54 ± 5.4) fails anyway.

**2. Sentences the printed numbers do not support**

- **fig4s7, cell 72 and the record's notes:** "coefficient 0.146, LRT 4.04, p = 0.045", and "Two of the four LRTs are close to 0.05 (0.045 and 0.042)".
  - Cell 71 prints `lrt_incorrect 4.115, p_incorrect 0.04251`, so the value should read LRT 4.12, p = 0.043.
  - The outcome does not change.
- **fig3d, record notes:** "0.050 to 0.067 under the other seeds and 10 folds".
  - Cell 76 prints p = 0.073 for 10 folds and 0.04993 for seed+3000.
  - Cell 77's narrower "under the five seeds" is correct. The outcome rests on the Mann-Whitney (U_Z) reading, so it does not change.
- **Figure 7 blocks, README:** "Unit matching and the analyses of matched units (Figure 7, five claims) | Blocked: data missing".
  - Notebook cells 0, 88 and the Summary (cell 89) also give fig7de/f/g/h as "blocked, data_missing (depends on …)".
  - Both contradict the record, which now has `blocked_by: other` for these four and calls the data_missing block wrong. The notebook is the first run's, but the README should have been updated.
- **fig4c, record notes:** "the dandiset lacks 11 recorded sessions with 65 isolated units".
  - Cell 6 lists 12 missing sessions. The 65 isolated units are in 8 of them, and 11 of the 12 have trials.
  - The wording should match the second finding (12 sessions).

Every other "**Result:**" sentence, the rest of the Summary, the README table and the record's notes match the printed outputs. I checked the following explicitly:
- the seed ranges for fig2d/e/f/g and fig4d/ef/gh;
- control p bounds and slope ranges (cells 46 and 61);
- the fig4c counts and tolerances;
- the fig4s6 Fisher tables and KS counts;
- the fig6cd values;
- the per-subject taus.

**Round-1 reasons in the record:** the record states my reasons in my own words. For fig7g and methods-lookahead it combines the reason with the matching problem text (B1 and B3) faithfully.

**3. Round-1 points**

**Resolved:**
- B4: the df convention is explained from paper_stats.py, and the paper's df is given in the notes.
- B6: sent to a reader in questions/.
- B7: the code's `compute_velocity` does not smooth, so the port matches the code.
- B9 and B10: now in the notes.
- B11 and B12.
- The head-direction column was checked against the code, though not in the notebook.

**Not resolved, bearing on a conclusion:**
- **B1:** fig7de, fig7f, fig7g and fig7h are still untested, although they can be tested. They are now honestly labelled.
- **B2:** fig3e, fig3f and fig3g are still untested. The decoders were ported but not run, so no fig3f chance-level comparison exists.
- **B3:** there are still no pairwise Wald contrasts on the mean-R2 reading for methods-lookahead. The contrasts were written but not run.
- **B5:** the Switch-accuracy bias is acknowledged but not fixed. It affects only the "similar" part of fig1-switch.
- **B8:** only partly addressed. The fig4s6 notes and deviation keep the claims file's reading of the table but do not say that the liberal "incorrect in one only" and "correct in one only" groups are the same units by construction (609 = 609 and 186 = 186, cell 67). The response says the point is recorded, but its substance is not in the notes. This bears on how much the liberal Fisher test supports the outcome.
- **The new misquotes in section 2:** the fig4s7 LRT value and the README/Summary block type should be corrected. Neither changes an outcome.

**Still not checked:**
- the session selection that would give 110 and 54 trials;
- the per-session blanking distribution;
- the counts of the paper's Figure 7 matches in the dandiset.

**4. Critical findings**

No finding in the record's `findings` is rated `critical`. Of the nine data findings, findings 1 to 3 are rated major and 4 to 9 minor or none; the three paper findings carry no severity.

None of them should be critical:
- **Finding 6 (`Cl_T3g_121418_0`):** a second recording with different trials and units, not a duplicate. The code excludes it, and so does the notebook.
- **Finding 4 (one-sample, 20 ms track offset):** the track's own clock column shows the offset.

I agree with the ratings as given.
