There were no reader answers to apply, so I didn't change any claim, the notebook, the conclusions or the attempt record.

**Questions.** None. `questions/crcns-hc-7.yaml` doesn't exist, and git history shows it never has. The first author run asked a reader nothing (its report says "Questions to a reader: none."). The answer run in commit 49aabf4ea1 also found nothing to answer and changed nothing.

The attempt does leave three questions open, but they are addressed to the paper's authors, not a reader. They are recorded as `methods_unavailable` findings in `attempts/crcns-hc-7-kohus-2016-01.yaml`, and no reader answer applies to them:
- how the onset of asynchronous release was determined;
- which APs gave the CCK+ pairs' single-AP uIPSCs;
- how the recovery half-time in Fig. 13B was fitted.

**Outcomes per claim.** Every outcome stays as the first author run recorded it, because no claim was amended or re-tested.

**Entry commands:**
- `lock`: the lock file came out unchanged.
- `all`: the check found 0 errors, and `reproduce_kohus_2016.ipynb` ran from a clean environment and passed in 431 s.
- `handover`: written to `executed/crcns-hc-7-kohus-2016/handover`.

Nothing is committed or pushed. The edits under `tools/` and `tools/backfill_summaries.py` were already in the working tree before this run, and I didn't touch them. If a reader was meant to have questions for this dataset, they need to be added to `questions/crcns-hc-7.yaml` and answered in a new answer run before this revision has anything to do.
