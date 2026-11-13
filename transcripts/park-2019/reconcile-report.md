I've written the reconciliation into `attempts/park-2019-02.yaml`. The author was not blind. Ten of the twelve earlier findings are reported again by park-2019-02. I checked the other two in a new notebook and both are still present. Only one outcome changed, `figs3-no-head-direction-bias`, and the cause is a difference in method.

I added `entries/park-2019/earlier_findings.ipynb` and listed it in `entry.yaml`. The lock file didn't change. `python tools/entry.py check entries/park-2019` reports 0 errors, and `run` passes both notebooks (365 s and 7 s). Nothing is committed.

**1. Blind: no (`blind: false`).** The first author run saw nothing, and all 17 of its first findings and its figs3 outcome were written there. Later runs saw park-2019-01's results:
- **author-answers:** it printed `questions/park-2019.yaml`, which the answer run had copied from main. That file holds park-2019-01's two questions with its numbers: fig5 error r of 0.014 to 0.211, and one of 14 figs3 tests at p = 0.0134. It also printed the first lines of park-2019-01's author-answers and author-revise-3 reports, which had been left in `transcripts/park-2019/`.
- **author-revise-2:** it read park-2019-01's round 3 verifier report, and said so in its own report.

It kept figs3 as reproduced. The one finding it added after these runs (15, the Tukey error term) answers its own round 1 verifier.

**2. Earlier findings**

| Earlier | Status | Now | Note |
|---|---|---|---|
| 1 data missing | still_present | 1 | |
| 2 FileNameList.xlsx | still_present | 2 | The CON names on the second sheet were not reported again. The notebook shows they are still there. |
| 3 1024R157 P9C1 spikes | still_present | 4 | |
| 4 1211R039 room track | still_present | 3 | |
| 5 R029 frames disagree | still_present | 19 (on_prompt) | Checked in the notebook: 6.85 to 13.49 px between frames against 0.31 px, and the lag still grows through the trial. |
| 6 1017R035 header | still_present | 5 | |
| 7 1121R157 cl1 half trial | still_present | 7 | |
| 8 spike times vs samples | still_present | 9 | |
| 9 per-rat counts, pairs | still_present | 10 | The pair count is in finding 18. |
| 10 Idir questions | still_present | 12 | Also covered by findings 13 and 14. |
| 11 Tukey, speed, internal tuning | still_present | 15 | Also covered by 16; the speed question is not asked again. |
| 12 paper: 660 vs 133 ms, z values | still_present | 20 (on_prompt) | The paper text is unchanged; the paper's code uses a 20-sample window (666 ms). |

**3. New findings:** 6, 8, 11, 13, 14, 16, 17 and 18. Of these, 13, 14, 16 and 18 split out parts of earlier findings 9 to 11 but have no `now` pointer, so under the schema they count as new.

**4. Outcomes that changed:** only `figs3-no-head-direction-bias`, not_reproduced earlier and reproduced now. Both attempts get the same numbers: average r of 0.166, and one test of 14 below 0.05 when n is the number of bins (p = 0.0134 and 0.014). They differ in the n used for the weighted Rayleigh test, which the criterion leaves open. The earlier attempt used the number of bins; the blind one used the sum of the weights, the CircStat convention.

**5. What did not fit the protocol**
- **Earlier entry:** this branch is a shallow clone, so the `git log -1 -- attempts/park-2019-01.yaml` recipe returns HEAD, which holds the blind attempt's own entry. I fetched main and used commit 66cf4ab0 instead; its park-2019-01 record is identical to the one here.
- **Shared transcripts:** both attempts' transcripts sit together in `transcripts/park-2019/`. Leftover files from park-2019-01 (author-revise-3, verifier-3, recorder, some reports) caused part of the exposure. The audit's hits in `author-revise-3.md` belong to park-2019-01's own author.
- **Questions file:** the answer run copied the questions file from main, which got around `blind.sh hide`.
- **One `now` per finding:** an earlier finding that the new attempt splits into several, or reports only in part (the CON names in finding 2), can only be recorded in the note.
- **Paper-only finding:** "check on this version" doesn't really apply to finding 12, which is about the paper. The notebook quotes the passages and reads the window length from the paper's code.
