I made no outcome changes and proposed none. The verifier agreed with all 43 outcomes in round 2, and the new check it asked for leaves the whisking result outside the tolerance, though only just. `python tools/entry.py all entries/peron-2015` passes (the notebook runs in 33 s) and `check` reports 0 errors.

**The new whisking check.** The verifier asked for reading (a), the per-trial angle range, with tracking jumps lasting three or more samples removed. A new cell (34) and new masks in `ssc1.py` do this two ways:
- **Jump mask:** a step of more than 30° in one 2 ms sample that comes back within 25 samples, plus five other step and duration values.
- **Running-median filters:** windows of 11 and 21 samples.

What the numbers show:
- **Where the jumps are:** nearly all in an229717. They are in 116 of its 183 trials, against 9 of 764 and 4 of 496 in the other two mice. Its 99.9th percentile step is 34.5°, against 4.5° to 7.0° in the other sessions.
- **Reading (a) without the jumps:** 69.7 to 70.1 with the jump mask, and 69.2 with all the error masks together. The upper bound is 68.8.
- **What brings it inside:** only the 21-sample median, which gives 68.6 (68.3 with every mask). That filter also cuts real whisk peaks. It flags 79 trials of an197522, a mouse with no jumps (largest steps 9.1° to 11.3°), and lowers it from 70.1 to 69.0.
- **Conclusion:** under every cleaning that removes only tracking errors, the result misses by 0.4° to 1.3°, so `not_reproduced` stands. The notes now say the miss is narrow, and that whether a cleaned reading lands inside depends on a choice the paper does not describe.

**Text corrected in the notebook, README and attempt record:**
- I removed the sentences the verifier found unsupported: "71.7 to 74.1", "tracking errors do not explain the miss" and "most of reading (a) is real whisking".
- They now give the steady fall with the angle threshold: 74.1 at 88°, 72.4 at 85°, 70.3 at 80°, 67.4 at 70°.
- "29.0 to 77.0" is now "28.6 to 77.0".
- The summary and the tracking-error finding now list the multi-sample jumps.
- The question to the paper's authors now cites 69.2.
- I removed the unsupported "45 TIFFs and nothing else" from the fig2e note. It now says only what the data description says about the imaging archives.

**Recorded:** a round-2 entry under `verifications` in `attempts/peron-2015-01.yaml`, with the verifier's reasons for all 43 claims and my response to each.

**Not done:**
- **No question added to `questions/peron-2015.yaml`:** the verifier found no misreading of the paper. It noted the degree signs in the claims file are garbled, but the numbers are legible and the criterion is unaffected.
- **Imaging archive contents (point C5) not listed:** that would mean streaming a multi-GB archive, and it bears only on the wording of the fig2e note, which I changed instead.

Nothing is committed, as instructed.
