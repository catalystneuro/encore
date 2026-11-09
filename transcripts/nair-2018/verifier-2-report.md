**Round 2 verification: Nair et al. 2018 (doi:10.1073/pnas.1712431115) on CRCNS bf-1**

Counts come from the claims file and the attempt record. There are 28 claims and 28 outcomes, with matching IDs:
- reproduced: 4
- partially reproduced: 4
- not reproduced: 2
- blocked, data_missing: 16
- blocked, metadata_insufficient: 2

The notebook's cell indices have shifted since round 1, so all indices below refer to the re-executed notebook.

**1. Outcomes**

I agree with all 28 stated outcomes.

- **fig3a-bf-gamma-reduction: partially_reproduced.** Agree. The paired t test gives p = 0.012 with the home cage higher in 6/6 rats. The reduction is 46.8–48.1% under all 12 readings, against 35 ± 3% (cell 15).
- **fig3a-each-hemisphere-significant: reproduced.** Agree. 13/13 comparisons give p < 0.01 under all three epoch readings (cell 20).
- **fig3b-arena-gamma-unrelated-to-movement: reproduced.** Agree. Every test gives p > 0.1, including the normalized one-way variant (p = 0.117 / 0.325) and the movement-shifted variant (cells 23, 27).
- **fig3b-home-cage-gamma-increases-with-movement: not_reproduced.** Agree under the criterion: one-way p = 0.817 / 0.774 (cell 26). The outcome rests on the claims file's choice of test (point 3).
- **fig3b-matched-movement: not_reproduced.** Agree under the criterion: p = 0.070 (cell 31). Same caveat.
- **fig3c-home-cage-above-both-sessions: partially_reproduced.** Agree. With the session-order part set aside, the outcome rests only on the home-cage part. That part holds only under the criterion's named variant, Bonferroni-corrected paired t (p = 0.038 / 0.035). It fails under the named standard reading, Tukey (p = 0.30 / 0.19, cell 34). The notes report both numbers but do not say plainly that the outcome rests on the variant. It is reasonable, because Tukey here ignores the pairing within rat, but the record should state it.
- **fig3d-gamma-rises-with-time-in-arena: partially_reproduced, `assumed: true`.** Agree.
  - The assumption (1-min bins) is stated, and it is reasonable because the criterion itself names 1 min.
  - Cell 38 shows the arena-entry anchor does not change the outcome.
  - The criterion defines no partial outcome; "test holds, size off" is a judgement call that I accept.
- **figs2-bf-low-frequency-bands: reproduced.** Agree. All four bands hold in the stated directions under all 12 readings (cell 42).
- **figs3-unimodal-states: reproduced.** Agree under the criterion, which tests raw power: every test gives p ≥ 0.102 (cell 45). On log10 power, one per-session test gives p = 0.035, so the absence is fragile to scale.
- **figs5-arena-excursions: partially_reproduced.** Agree. The gamma rise is significant in 12/12 readings, theta p > 0.1 in 10/12, and the count and duration miss in every reading (cell 48).
- **The 18 blocked claims.** Agree, for the archive reasons I gave in round 1.

**2. Text against printed outputs**

- **Cell 51 (Summary):** "fig3d-rapid-switch-to-home-cage and 16 claims on behaviour, objects, units, ACC and VC". That reads as 17 claims, but the data_missing total including fig3d-rapid is 16, so it should say "and 15 claims". The README's "(16 claims)" is correct.
- **Cell 40 and record notes for fig3d:** "30-s bins 0.744 and 0.747 (within tolerance)" is offered as the only within-tolerance case. The 20-s bins with the end anchor give r = 0.662, p = 6.9e-5, which is also inside 0.648–0.792 (cell 38). This case goes unremarked.
- **Record notes for fig3d:** "In 9 of 12 arena files the first minute has more movement than the middle, consistent with entry near t = 0". This drops the notebook's "but not proof of it" (cell 40). Several of the differences are small, for example 403.9 against 389.2 (cell 38).
- **Record notes for fig3a-each-hemisphere:** "Rat 3's arena session 2 … p < 1e-100 either way" holds only for 2-s epochs as delivered. With the peak-to-peak rule the p-values are 7.1e-80 and 4.7e-93; with 10-s epochs they are 6.2e-30 and 6.8e-33 (cell 20).
- **Record finding (data_missing):** it lists "bipolar recordings" as data not in the data set, but the bipolar claim is blocked as metadata_insufficient. This is a minor inconsistency.
- **README:** "It takes under a minute" has no support in the printed outputs. Only the 3-s streaming time is printed (cell 1).
- **Everything else checks out.** All other numeric statements in cells 18, 21, 24, 29, 32, 35, 43, 46 and 50, the Summary, the README and the record notes match the outputs.
- **My round-1 reasons:** the record states them faithfully in my own words, merged with the relevant numbered problems. Two caveats:
  - The fig3d reason says I "asked for" movement values at the file edges and r against bin width. In round 1 these were suggestions under "what I could not check", not requests.
  - The fig3d reason repeats my own round-1 error, "files span 620–780 s". Cell 3 prints 526–780 s; rat 2's arena session 2 spans 526 s.

**3. Round-1 points**

- **Problem 2 (session order): resolved.** The session-order part is not judged, and a metadata_insufficient finding was added.
- **Problem 3 (time anchor): resolved.** The end-anchored window and the movement at the file edges were added, and the outcome is the same under both anchors.
- **Problem 4 (Tukey ignores pairing): resolved** as a note in the record. It now bears on the fig3c conclusion (see section 1).
- **Problem 5 (boxcar zero-padding): resolved.** `bflfp.boxcar` now divides by the count of values that exist; the fix is checked in the code.
- **Problem 6 (histogram intersection): resolved enough.** The docstring notes the early-crossing case, and the KDE variant gives similar counts.
- **Problem 7 (dip test on raw power only): resolved.** The log10 variant was run and reported.
- **Problem 8 (cell-4 text): resolved.** No issue was found. Problem 9 needed no change.
- **"Could not check" items:** the bin-width sweep and the scale-free rise/threshold comparison were added. Rise/threshold is 0.39–0.44 against the paper's 0.215, shown and not judged.

What remains that bears on a conclusion:

1. **Problem 1, unresolved by design.** The claims file's one-way ANOVA on per-rat means, without normalization, decides both fig3b not_reproduced outcomes. Every within-rat test finds the effect:
   - repeated measures, home-cage rise: p = 2e-5
   - normalized one-way, home-cage rise: p = 1.6e-9
   - paired t, matched movement: p = 0.007

   It has been put to a reader and to the paper's authors. Until it is answered, those two outcomes reflect the choice of test more than the data.
2. **fig3c depends on which post hoc test counts.** It is partially reproduced only under the Bonferroni-paired variant, and the record should say so.
3. **fig3d depends on bin width.** It is partially reproduced at the criterion's 1-min bins but would be reproduced at 30-s bins under either anchor, and at 20-s bins with the end anchor. This should be resolved by the question to the authors, not by the attempt.
