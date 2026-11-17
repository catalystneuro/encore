I've finished the round-2 revision. No outcome changed and nothing goes under `proposed`: the verifier agreed with all 29 outcomes (23 reproduced, 2 partially reproduced, 3 not reproduced, 1 blocked). Two things need your attention: the fit-check notebook was executed outside `entry.py`, so there is no run stamp, and `entry.py check` fails on two errors I could not fix.

**How the re-run went**
- `python tools/entry.py all entries/hazon-2022` can't pass right now. The uncommitted `tools/entry.py` in this checkout requires `about:` on findings of kind `other`, but `schemas/attempt.schema.json` doesn't allow that field. Either way the check reports 2 errors (findings 2 and 5). I left both tool files alone.
- I used `entry.py run` instead, but it hit the 2-hour limit on a single command after about 2 h 10 min of work.
  - The first two notebooks finished in the fresh environment it built.
  - The fit-check notebook was stopped partway. I then executed it with the same nbconvert command in that same environment (42 min). So all three executed copies match the current entry, but `.clean-run.json` is missing and the workflow may need to run the entry again.
- Most numbers came out the same as the last run. Three differ slightly, which means some fits are not exactly repeatable from run to run: the uncapped place-field width is 37.8 cm (was 37.6), the fig2ef p-values are 3.6e-17 and 5.4e-15, and one I0 is 231 (was 230). I corrected the text to match these outputs in both the entry and the executed copies.

**Added or corrected, per the report**
- **Mislabelled assumption:** the other decoding outcomes that use the SVM (fig2cd, fig2ef, suppl7b, saturation, suppl11c, suppl8, suppl6) are now marked `assumed: true`, like fig2d and suppl11b.
- **New printed outputs:**
  - the session with the 51.88 cm error (Mouse2011 105556, one of the sessions whose events don't track position);
  - the IMSE curves of all six such sessions (73 and 97 rise slowly; they are not flat);
  - each animal's N in the variant without those sessions and without degenerate fits;
  - reading (a) without degenerate fits: Mouse2028 drops from 886 to 327, which states the session-19 problem;
  - which trials hold negative positions;
  - event rate by quarter of the joined session (38.6 rising to 103.1).
- **Fit-check notebook:**
  - Mouse2023's session refitted with 40 subsets: N goes from 716 to 474, so its 5% slope point is 1,646 neurons, still outside tolerance.
  - N refitted with C = 0.1, C = 10 and the paper's loss-weighted decoding on 9 sessions. The two C values change N by median factors of 1.25 and 0.97; loss-weighted decoding by 0.71.
  - This needed an optional loss-weighted mode in `hc30.OvOLinearSVM`. I checked it on synthetic data; the default (voting) is unchanged.
- **Rewritten sentences:** "reduced repetitions do not explain the failure" and the decoding summary's "likeliest reason" now hold only for the animals checked. The saturation and suppl8 results now say they may reflect this attempt's decoder.
- **Other text fixes:**
  - Findings: the misaligned-session I0 values, "flat" (now four of the six sessions), "far outside the track", the joined-session rate, and question 4 (at most two values, three without the cap).
  - Removed the fig4a "preparatory run" sentence.
  - Added the verifier's point on suppl11b to its notes.
- **Record:** round 2 is recorded under `verifications`, with the verifier's reasons and my response for each claim.

**Not done**
- Mouse2022, which sets the lower saturation bound, was not refitted with more subsets. Doing it properly would take about 5 CPU hours, and the entry has to run within two hours. A test run outside the entry gave 207 → 200, but it is not in the record because no saved output backs it.
- The saturation range was not recomputed with loss-weighted decoding, which would mean re-running the whole decoding notebook. Since that decoding lowers N, the saturation and suppl8 failures may come from this attempt's decoder; that is stated, and a new attempt would have to test it.
- No questions were added to `questions/hazon-2022.yaml`, because the report found no place where the claims file misreads the paper.

Nothing is committed.
