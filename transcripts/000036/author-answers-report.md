No questions were answered, because none were asked, so no outcome changed. A problem did come up during the run: one reading behind fig4-locomotion-effect-size is missing from the copy going to the verifier. It comes from the paper's Zenodo deposit, and that download did not finish in time on this machine.

## Questions and answers

`questions/000036.yaml` does not exist. In its report the author run says, "No questions were asked: every method detail I needed was in the claims file or its stated readings." The answer run found nothing to answer and left the claims file alone, and git confirms it has not changed since the author run. So no claim had a new criterion to re-run, and every outcome is the same as before:

| Claim | Earlier | Now |
|---|---|---|
| all 27 claims | as recorded (15 reproduced, 2 partially reproduced, 1 not reproduced, 9 blocked) | unchanged |

## Lock, check, run, handover

- **Lock:** `requirements.lock.txt` came out the same as before.
- **Check:** 0 errors, both before and after my text edits.
- **Run:** the entry ran twice from a clean environment and all three notebooks passed both times. The second run took 782 s, 757 s and 1590 s.
- **Numbers:** the conclusions' key numbers come out the same as before, for example 36 of 108 parameter sets for ext3-2, AM d 0.132 for fig3b, largest d 1.111, and pupil r = 0.651 and -0.647.
- **Handover:** built in `executed/000036-mayner-2022/handover/` from the second run.

## The missing reading for fig4-locomotion-effect-size

The arousal notebook downloads the 4.5 GB Zenodo deposit in the background. It stops at a 26-minute deadline so the notebook stays under the 30-minute CI limit. The files reading (b) needs, the running parameters, come after 4 GB of dF/F.

- **Then:** in the author run they arrived after 1105 s.
- **Now:** the deadline came first in both runs, after 1527 s and after 1467 s. The second run was already in the folder that holds them when it stopped.

So the executed copy shows reading (a) only (r = 0.842, p = 0.035) and prints "reading (b): not available". The criterion requires both readings, so this copy alone does not back "reproduced". That outcome rests on reading (b)'s r = 0.844 from the author run's executed copy. I kept the outcome and did not change the entry's code, since this run was for answered questions. I recorded the gap instead, in two places:

- **Attempt record:** the fig4-locomotion-effect-size notes now give both deadline times and say where the reading (b) numbers come from.
- **Notebook conclusion:** one added sentence, which holds whichever way a run goes. It says reading (b) needs the download to reach the running parameters before the deadline, and that the output above says whether it did. I made this text-only edit in both the committed notebook and the executed copy, after the run.

The verifier will see this; whoever drives the next round may want to know that this outcome can depend on network speed. Nothing is committed or pushed, and I did not verify my own work.
