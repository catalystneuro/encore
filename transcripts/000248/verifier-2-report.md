**Verifier report, round 2: 000248-shin-2025-01**

The claims file has 40 claims. The attempt record has 40 outcomes: 14 reproduced, 1 partially reproduced, 3 not reproduced and 22 blocked (21 data_missing and supp3 too_large).

**1. Outcomes**

| Claim | Agree? | Note |
|---|---|---|
| results-npx-units-per-session, methods-npx-ic-encoder-count, ed6cd, ed2f, ed2g, ed2a, fig3a, ed7b, ed7a, ed6ef | yes | |
| fig3c | yes | Within tolerance under reading b. Under reading a, the two further seeds are within tolerance (LC 0.198 and 0.199) and the first seed is not (0.197). The criterion accepts any one decoder reading. |
| ed6b (`assumed`) | yes | The assumption is stated and reasonable. Reading b1 matches both counts exactly. |
| ed2b (`assumed`) | yes, with a reservation | The assumption is stated. It is plausible, but it was chosen partly because it gives the paper's 9 sessions, and the reproduction rests only on that session count: under either rule the units are the same 10. Rule r also lets a session count as valid with no standard trial at a position, and standard trials are what the exclusivity test uses. The record says the unit count may be partly coincidental (fig1e gives 44, not 18); I agree. |
| fig1e, fig1f, fig1g | yes | |
| fig2d (reproduced) | no; I still judge it blocked under the criterion as written | The criterion requires a higher median "under every combination". With boxcar smoothing, raw flank and number of connections, the medians are 1 and 1, so that combination fails the rule. The direction of the rank-sum test is not a median comparison. The protocol rule cited for the tie-break ("ties in a criterion") was not available to me. The substance supports the claim (P = 0.63, p = 9.8e-05, 68% against 50% of units with any connection). The outcome rests on that tie-break, but the record does not mark it `assumed: true`; it is only listed as a deviation. |
| fig3d (partially reproduced, `assumed`) | yes | The assumption is stated: decoder reading b is adopted. Reading a would meet the criterion, and the claims file does not say which decoder reading decides. Under neither reading does the set of significant areas match the paper's. Reading b, which decides the outcome, was checked over seeds only in V1 (see section 3). |
| supp3 (blocked, too_large) | yes | The printed cost is 15 h on one core, against a 30-minute notebook limit. The two SVMs agree with the linear SVM. |
| 21 claims on 2p, mesoscope and holography data (blocked, data_missing) | yes | |

**2. Statements the printed outputs do not support**

- **reproduce cell 31, and the record's fig1e notes:** "under (a), 383 units have the center as best position and at least one position passing the Holm step, and 44 of them have exactly one". Cell 30 prints `{1: 68, ...}`: 68 of the 383 have exactly one passing position. The 44 are the units whose single passing position is the center, with the smallest p. The cell 30 step label "exactly one position passes (= exclusive, reading a)" is wrong in the same way. The record's response to fig1e also says "383 and 602 passing the center step under a and b". For reading a, 383 counts units with any position passing, not the center.
- **checks cell 16:** "about 18 hours on one core". Cell 15 prints `3.60 ms per full-batch epoch … ~ 3.0 min; 300 fits … ~ 15.0 h on one core`. The record's supp3 notes ("4.4 ms per epoch … about 3.6 minutes per fit and about 18 hours") and its round-1 response for supp3 ("about 18 hours on one core, 4.5 hours on the four cores") carry the same stale figures.
- **checks cell 9:** "The fig3c and fig3d outcomes do not depend on the seed." The fig3d outcome rests on reading b, and reading b was repeated over seeds on V1 only (cell 5 says so). PM p = 0.077 and AM p = 0.083 under reading b were not repeated.
- **checks cell 12:** "The bound of the C grid of reading (b) does not exclude a better C on these data." Read literally, this says the opposite of what the numbers show, which is that no better C lies above 1. The check covers only the first outer fold of the V1 sessions, and 12 to 17 of 36 fits per C value above 1 did not converge. "C above 1 never gave a higher inner accuracy" is therefore based on partly unconverged fits. The record's fig3c and fig3d deviations repeat this claim without that caveat.
- **Record, ed7a notes:** "every significant difference has the HVA below V1 (PM and AM)". Decoding cell 20 also shows RL significantly below V1:
  - XRE accuracy, reading a: signed-rank p = 0.0137 and Tukey-Kramer significant.
  - XRE accuracy and XRE score, reading b: Tukey-Kramer significant, and XRE score signed-rank p = 0.0244.

  LM is also below V1 in XRE accuracy under reading b (p = 0.0234). The direction is still HVA below V1, so the outcome stands.
- **README:** "It streams the 12 session files (about 3 minutes)." Reproduce cell 1 prints 292 s, about 5 minutes. The decoding notebooks take 190 and 211 s.
- **reproduce cell 6:** "0.03 to 2.7 ms". Cell 5 prints a minimum of 0.014 ms. This does not affect a conclusion.

Every other sentence of the Result cells, the three Summary cells, the README and the record's notes agrees with the printed outputs.

The record states my round-1 reasons faithfully, mostly in my own wording, with the problem numbers attached.

**3. Round-1 points**

Resolved:
- 1: the status table now matches the outcomes.
- 2: reading b was run on every area.
- 4: rule r was tried and gives 9 sessions.
- 6: ed6b is marked `assumed`, with a finding asking the authors.
- 7: the quadratic and RBF SVMs were run.
- 9: the maximum variant of pupil area now gives NaN, not -inf.
- 10: the rank-sum test is now tie-corrected.
- 11: cell 58 now says 21 claims.
- Section C: fig1e now prints counts at each selection step, apart from the misstatement in section 2.

Partly resolved: point 3. Seeds were added, the C bound and one-vs-all coding were checked, and fits now converge (2 unconverged under reading b).

Unchanged: point 8, a criterion issue that now matters less because fig3d is partial. Whether XRE1 carries the same 135° bar as IC1 is still not shown in cell 14.

Remaining points that bear on a conclusion:
1. **fig2d.** The tie-break departs from the criterion as written and is not marked `assumed`. I still read the outcome as blocked (methods_underspecified).
2. **fig3d.** The outcome rests on reading b, whose PM and AM p-values were not repeated over seeds. The C-bound check (V1 only, first fold, partly unconverged above C = 1) and the one-vs-all check (changes of up to 0.024) were also not extended to PM and AM. Under reading a, AM is p = 0.0029; under reading b, 0.083. Its significance, and so whether fig3d is reproduced or partially reproduced, depends on the hyperparameter choice. The record asks the authors about this.
3. **ed2b.** Reproduced only through the post hoc session rule. The unit count agrees with the paper while the parent selection (fig1e) does not reproduce.
4. **Not checked.** The claims file's opening comment says Supplementary Fig. 3 and the code repositories were not read, and I could not check them. I found no place where the claims file misreads the paper. The fig3d criterion does not say which decoder reading decides, while fig3a requires both readings and fig3c accepts either one. Together with the brittle median rule in fig2d, these are the criterion problems already reported in round 1.
