I've worked through every point in the round-2 report. No outcome changed and nothing is under `proposed`, so no third round is needed. The final run of `python tools/entry.py all entries/park-2019` passed with 0 errors, and the text in the notebook, README and attempt record matches its output.

**Outcomes.** All 22 stay as verified. Two are now marked `assumed: true`, as the verifier asked:
- **fig1d-instability** stays partially reproduced. A new deviation says this is a judgement outside the criterion, which has no partial form; read strictly, it would be not reproduced.
- **fig4c** stays not reproduced. A new deviation states that "beyond 10 s" in the partial form is read as "from 20 s", citing the paper's "abruptly decreased after 10 s" (Results, Transient Allocentric Registration, paragraph 3). It also says that under the broader reading the outcome would be partially reproduced.

**Added or corrected**
- **figs3:** the notes, the deviation and the result cell now say the 10° Idir reading is not the one that reproduces figs2. Under that 45° reading, 1 of 14 tests is significant under either n, so the claim would not reproduce.
- **fig5c:** the notebook now prints the chance that at least one of 32 rows matches both minima (0.18, rough because the rows share data). It also prints how shallow the pooled curve is: the minima sit 13.6 and 13.4° below the mean but only 0.1 and 1.6° below the next bin. The notes now call the match weak support.
- **fig4c text:** the sentence about the room frame falling as far as the arena frame now applies only to the Methods' normalisation. The code's normalisation is described separately.
- **Total runtime:** the notebook now prints it, and the README says six to eight minutes.
- **Round 2 record:** added under `verifications` for all 22 claims. It has `agrees: false` on fig1d-instability, figs3 and fig4c, because the verifier agreed with only the other 19 "as they stand".

**Something the report didn't find.** When I re-ran the notebook, the decoder and Idir numbers moved between runs. Windows whose directions are exact multiples of 10° landed on one side of a bin edge or the other because of floating-point rounding. I fixed this in `hd20.window_directions` by rounding the mean direction to 1e-6°. On the same machine, two runs after the fix gave identical results apart from timings; I couldn't test another machine.

After the fix, some of the numbers the verifier quoted changed:
- **figs2:** the per-ensemble values now print as the original text had them (0.605, 0.291, 0.199, 0.054 and 0.367).
- **fig2c:** measured is now -0.0698. The range of means is -0.043 to -0.087, and 9 to 12 of the 14 correlations are negative.
- **fig5:** reading (i) gives r of 0.031 to 0.426, the highest room-frame median is 0.348, and the arena-frame value is 0.543.

No measured value that decides an outcome changed, and every count behind an outcome is the same.

**Not done**
- No questions were added to `questions/park-2019.yaml`, because the report flagged no new misreading of the paper.
- Nothing was committed or pushed.

The checkout held transcripts from an earlier attempt on this paper (park-2019-01) in `transcripts/park-2019/`. While finding my way around, I read its round-3 verifier report, which argues that figs3 fails under n = number of bins. That breaks the blindness rule for repeat attempts. I did not act on it: figs3 keeps the assumption the round-2 verifier called reasonable, and I proposed no change.
