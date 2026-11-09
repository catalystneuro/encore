**1. Outcomes** (23 claims in the claims file, 23 outcomes in the attempt record: 15 reproduced, 2 partially reproduced, 2 not reproduced, 4 blocked)

I agree with all 23 stated outcomes.
- session-link, trials-per-session, blocks-per-session, session-duration, block-min-30, fig1c-20-rats, fig1c-context-selection, fig4-converging, fig4-loc-frq-uncorrelated, ed3g-halfsplit, units-per-rat, fig3h-neural-uncorrelated: reproduced. I agree; the printed numbers meet each criterion (cells 11–12, 18–19, 22, 25, 27, 38, 42, 45, 51, 55).
- ed1e-switch-four-trials: reproduced. I agree (cell 30). The position-4 reading is thin: the switch to location reaches 0.9 in only 0.678 of bootstrap resamples. The position-5 reading, which the criterion also allows, is firm (0.956 and 0.977).
- ed2g-learning-2-5-months: reproduced. I agree (cell 33): 17, 19 and 17 of 26 rats.
- fig5d-behaviour-neural: reproduced. I agree under the criterion's main reading (cell 60: r = −0.697, p = 0.0056). It stays fragile (see 3).
- subjects: partially reproduced. I agree (cell 15, 0.913).
- ed4-bilateral-fof-impairs: partially reproduced. I agree (cell 48: 2 of 3 and 2 of 4 rats under every reading).
- neural-link: not reproduced. I agree (cell 52): at most 0.958 of cells match one session, from 110 to 115 sessions against 199.
- choice-axes-parallel: not reproduced. I agree (cell 57): mean 4.73°, no rat within 1.44–1.76°. This matches my own round-1 recomputation.
- The four blocked claims: I agree that they are blocked. I accept `not_runnable` for fig1f, fig3a and fig5c in place of my round-1 "other".

**2. Statements the printed outputs do not support**

- README: "It takes about 7 minutes: 2 to read …, 2 to read the paper's neural files …, and 3 to fit the kernels." Cell 36 prints a kernel fit time of 280 s (about 4.7 min) and cell 62 prints "total run time 782 s" (about 13 min).
- Cell 49 and the ed4 notes: "nor is P127 (4 sessions, 0.603 against 0.634, p = 0.55)" and "P127 not lower (0.603 against 0.634, p = 0.55)". 0.603 is lower than 0.634. The supported statement is "not significantly lower".
- Summary (cell 63): "links one to one to the paper's published per-session tables … with identical trial counts, outcomes, strengths and pulse timing". Cell 12 shows the 50 ms pulse bins agree on 0.99996, not all of them. The per-trial fields could not be compared in the 627 sessions whose record in the paper's tables is empty. Cell 11 lists 6 dandiset sessions that are not in the paper's tables, so the link is not one to one.
- Summary (cell 63): "the stored generative log rate ratios, which give the paper's own per-session values". Cell 11 shows the relative weights agree in 0.898 of sessions. Of the 692 that still differ after capping at 1, only 632 have a missing value, so about 60 sessions differ with both values present.
- session-link notes: "632 have a missing value on one side". Cell 11 counts a missing value on either side, and its printed rows show both sides NaN. Cell 13 states this correctly as "one side or both".
- Cell 13: "(sessions where a feature does not vary or the fit has too few trials)". No output shows this. The printed H113 rows that are NaN on both sides have 473 to 914 valid trials.
- choice-axes-parallel notes and the claims file: "The reported test against 0 is in neither the Methods nor the code". This is not a notebook number, but the paper's Methods ("Estimating the choice axis", saved in `paper/PMC11903320.txt`) describe it: a per-rat permutation test that shuffles context labels and recomputes the two axes.
- Summary: "match 112 dandiset sessions (115 …)". These are the gap-tolerant counts. Under the criterion's contiguous rule cell 52 gives 110 (113). This is minor.

Every other sentence I checked matches the printed outputs. That covers all "**Result:" cells, the rest of the Summary, the README table and the attempt-record notes.

The attempt record does state my round-1 reasons in my own words, for all 23 claims.

**3. Round-1 points**

Resolved:
- Point 1, the choice-axis port. The projected, folded angle is ported, its values equal my recomputation, and the criterion's description of the code is corrected and the correction noted.
- Point 3, the neural-link search. Every TaskSwitch protocol is now searched and the per-rat table is added.
- Point 4, ed4 laser connection. The crosstab shows every trial with an epoch has the laser connected, and the connected-only test changes nothing.
- Point 7, ed1e robustness. No fits are dropped, and the bootstrap is added.
- Point 8, dates of birth. Each rat's age at its first session is now shown, and P189 is flagged.
- Point 9. The unused variable is removed and the 13 unreadable sessions are added to readings c and d.
- Section C, per-trial comparison beyond the sample. All 14,650 sessions with a per-trial record are now compared.
- Point 5, relative-weight mismatch. Mostly resolved; about 60 differing sessions remain unexplained (above). It does not affect a conclusion.
- Point 6, cross-validation folds. Acknowledged and left as the criterion fixed them. It does not affect a conclusion.

Remaining items that bear on a conclusion:
- fig5d (point 2). The reproduced outcome rests only on the main reading, 0.04 inside the tolerance edge. The better-powered variants for P049 and P059 (−0.830, −0.834) fall outside the tolerance on the negative side, and leaving out one rat at a time keeps only 4 of 7 values inside. This is disclosed, and the outcome holds by the criterion.
- ed4. Which three rats the paper analysed is still unknown. The result is partial under both readings, so the outcome does not change.
- choice-axes-parallel. The Methods' permutation test behind "not different from 0 in 6 of 7 rats" exists but was not run, and the record says no such test is described. The mean angle decides the outcome, so the outcome stands, but the notes, the criterion and the code_mismatch context should be corrected.
- Minor, outside any criterion: the paper says neural differential pulse responses "only displayed positive (or zero) slope indices". Cell 55 gives P049 location −0.221, P101 location −0.045 and P095 location −0.007, and the record does not mention it.
