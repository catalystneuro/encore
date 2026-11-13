**Verifier report, round 2: wirth-2017-01**

Counts come from the claims file (28 claims) and the attempt record (28 outcomes).

## 1. Outcomes and assumptions

| Claim | Outcome in record | Agree? |
|---|---|---|
| gaze-anticipates-action | reproduced (assumed) | Yes, with a new reservation (3a). The sign assumption is stated, and it is now reasonable: it rests on the slow-phase velocity during turns at the centre (cell 28), not on eye position. |
| gaze-anticipates-landmarks | reproduced (assumed) | Yes. I now agree with this outcome. In round 1 I said partially reproduced because the test was circular; it no longer is, because the sign comes from velocity at the centre. The criterion asks only on which side the eyes lie, and that is met (cell 31). The record correctly says the test cannot separate anticipation from the shift in eye position that comes with optokinetic nystagmus (OKN) whenever the view rotates. That limitation is in the claims-file criterion. It follows the S2C legend, so it is not a misreading of the paper. |
| learning-trials | reproduced | Yes |
| learning-to-90 | reproduced | Yes |
| probe-transfer | not_reproduced | Yes. Monkey K's two means fail on their own. |
| probe-faster-criterion | blocked (methods_underspecified) | Yes |
| cells-recorded | partially_reproduced | Yes |
| responsive-cells | blocked (metadata_insufficient) | Yes |
| state-space-most-responsive | not_reproduced | Yes |
| multi-space-coding | blocked (metadata_insufficient) | Yes |
| direction-center-vs-periphery | partially_reproduced (assumed) | Yes. The stand-in for reading (b) is stated. |
| direction-tuning-not-maintained | not_reproduced | Only if marked assumed (3b). |
| state-space-ic-higher | partially_reproduced | Yes |
| sparsity-state-vs-direction | reproduced (assumed) | Yes. Both claims-file windows keep the returns: reading (b) is the notebook's toreward_ret. So the assumption is weaker than the record makes it sound. |
| sparsity-state-vs-position | not_reproduced | Yes |
| sparsity-gaze-vs-state | blocked | Yes |
| state-space-selectivity | not_reproduced (assumed) | The assumption is stated, but I would grade it blocked (3c). |
| landmark-identity-distance | not_reproduced | Yes. The upper bound over all cells fails. |
| landmark-identity-center | blocked | Yes |
| path-selectivity, gaze-aligned-dynamics, latency-skew, eccentricity-modulation, foveation-selectivity, gaze-map-landmarks | blocked (metadata_insufficient) | Yes |
| fields-per-cell, dimensionality-control | blocked (methods_underspecified) | Yes |
| spatial-selectivity-fraction | blocked (metadata_insufficient) | Yes |

## 2. Text against the printed outputs

Almost every number in the Result conclusions, the Summary (cell 67), the README and the record's notes and findings matches the outputs. I checked every range, p-value, count and bound against cells 6–66. The median probe gain of 0.30 is not printed, but it follows from the table in cell 23. These do not match:

- **Cell 29 and the gaze-anticipates-action deviation:** "The median eye velocity from 0 to 600 ms after the code is positive during right turns and negative during left turns, in 40 of 40 sessions of K and 20 of 20 of S."
  - Cell 28 prints only right > left per session (40/40, 20/20) and the pooled medians (0.539 / −0.432 and 0.470 / −0.857).
  - The sign of each turn type within each session is not printed. It should say "higher during right turns than left turns in 40 of 40 sessions".
  - This does not change the conclusion.
- **Cell 7:** "ke20140207 spans only -126 to 90 degrees because its headings (18, 90, 234 and 306 …)."
  - Cell 6 prints heading sets as counts over sessions, not per session, so this session's set is not shown.
  - Minor.
- **README table:** it drops qualifiers that the record carries as assumptions.
  - "State-space selectivity in the centre | Not reproduced" leaves out "permuted chunks; open under shifted chunks".
  - "Direction maps … IC and sparsity partially reproduced" leaves out the three-space stand-in for reading (b).
  - The Summary in cell 67 keeps both qualifiers.

**My round-1 reasons in the record:** the verifications section states them faithfully and in substance as I wrote them. Problems 1, 2, 3, 4, 5, 7, 8 and 9 sit under the right claims. Problems 6 and 10 appear in the "reviewed" text. Nothing is misattributed.

## 3. Round-1 points

**Resolved:**
- 1: the circular sign, now set from velocity (cell 28).
- 2: the overlapping shift surrogates are replaced. In the synthetic check (cell 34), 3.3% of trains with no coding come out p < 0.01, against 100% before.
- 3: both tails are stored, and at most 3 cells are significant on the low side.
- 4: three move typings are run.
- 5: state-space-ic-higher now has its own section, with all readings shown.
- 6: the toreward_ret window is added.
- 7: start-arm sequences and variants are shown.
- 8: type III sums of squares are shown.
- 9: signed-rank tests across sessions are added.
- 10: the layout is checked per file.
- All section C requests are answered. The eye sign was settled by velocity, not by the side on which landmarks appear.

**What remains that bears on a conclusion:**

a. **gaze-anticipates-action.** Every code 1 or 2 in a trial is used, so the 500 ms before a turn can fall inside the previous rotation.
   - A turn of about 28° takes 600 ms (cell 26), so a 72° rotation lasts more than 1 s.
   - In monkey K, eye velocity in the 500 ms before the code already differs between right and left turns with the in-turn sign: 0.250 against −0.189, 38 of 40 sessions, p = 2.3e-9 (cell 28).
   - The right-minus-left position difference is already −0.21 to −0.30 at −1.0 to −0.8 s (cell 27).
   - So K's effect may be the OKN position shift of an ongoing rotation, not anticipation. Monkey S does not show this: 9 of 20 sessions, p = 0.40.
   - Output needed: the orientation change in the 500 ms before each code, and the test restricted to turns with no rotation in that window (or to the first turn of each trial).

b. **direction-tuning-not-maintained.** Reading (a) fails firmly on the number of cells tested (40 and 28 against 56 ± 5.6). The outcome therefore rests on reading (b), where the three-space set stands in for the paper's responsive set.
   - That set is only a lower bound, and the count of low cells is not fixed by it.
   - Under the bounds logic the attempt uses elsewhere, adding just 2 gaze-responsive cells that both have low correlations gives 61 tested, 18 low and 4 high, which meets the criterion.
   - The outcome should be marked `assumed: true`, as direction-center-vs-periphery is, or be blocked.

c. **state-space-selectivity.** Under permuted chunks it fails firmly: the low count over the three-space set is 6 or 7 against 3 to 5 (cell 56). Under the now-valid shifted reading the bounds include the targets in 8 of 9 combinations.
   - For spatial-selectivity-fraction the record applies "met under any one reading" and blocks the claim because some readings are open. Applied the same way here, this claim should also be blocked.
   - The permuted reading rests only on the wording "randomly shuffling periods", which is weak support. Either justify grading this claim differently or grade it blocked (metadata_insufficient).

d. **gaze-anticipates-landmarks.** Not an error in the attempt, recorded for the reader: the claims-file criterion, which follows the S2C legend, is met by the OKN shift in eye position alone. The reproduction confirms the S2C pattern but not the anticipation the claim states.
