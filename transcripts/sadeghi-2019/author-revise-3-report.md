The verifier agreed with both proposed changes in round 3, so I applied both. No proposals are left standing.

**Outcomes changed**
- **fig9a-optimal-resolution**: reproduced → partially_reproduced.
- **fig10-vocalization-background**: reproduced → partially_reproduced.

I removed `proposed` from both and changed no other outcome. `python tools/entry.py check` passes with 0 errors.

**What the re-runs found.** The verifier said my reasons quoted the wrong machine's numbers. Its notebook had a three-way tie at 100, 141 and 283 ms. Both of my re-runs gave 81.0% at 100 ms, so the tie was at 141 and 283 ms only, as in my round-2 run. Across the five runs in rounds 2 and 3, three gave the two-way tie and two the three-way tie. So whether 100 ms ties changes with the machine.

**Text.** The Result cells for fig9a, fig9b-accumulation-rate, fig9c and fig10, the Summary, the README and the record notes now give both kinds of run. They say plainly that with 100 ms taken as the first of the tie, fig10's difference is −21.1, inside −20 ± 2. That value is set aside because the data do not single out 100 ms. The `measured` values are those of the final run (fig9a [141.4, 141.4], fig10 [94.8, 98.3, −23.2]). I also updated the classifier-methods finding (optimum 100 to 283 ms, reduction 1 to 37 points).

**Round 3** is recorded under `verifications`: `agrees: true` and `partially_reproduced` for both claims, the verifier's reasons in its own words, and my responses.

**Run not complete.** I ran `python tools/entry.py all` twice. Both times the tool's 2-hour limit stopped it during the model notebook, after the classifier (46 and 45 min) and neural (54 min) notebooks had finished. The model notebook did not change in this revision, and its executed copy is from just before round 3. So there is no clean-run stamp, and the record says this. After the last run I made one markdown-only edit, correcting the run count in the fig9a Result cell from four to five, so that cell in the executed copy still has the old wording.

As instructed, I did not commit or push.
