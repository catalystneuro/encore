No outcome changed in this round. The entry ran from a clean environment in 11 minutes, twice, and gave the same numbers both times; all results that were already there match the previous run exactly.

**Where the verifier disagreed.** The verifier gave three outcomes that differ from the record. I kept all three as blocked and recorded the disagreement:
- **pt-upper-persistent:** the verifier says not reproduced.
- **pt-cohort-control:** the verifier says partially reproduced.
- **pt-types-differ-in-timing:** the verifier says partially reproduced.

The verifier judged each one on its own test. The claims file makes each depend on a blocked claim (pt-upper-early-preparatory, or pt-upper-persistent through it), and the protocol blocks a claim whose dependency is blocked. The notes now give what each claim's own test shows. The other 28 outcomes agree with the verifier.

**Added to the notebook** (output the verifier asked for):
- **A new section re-running the measures on the paper's processed data for only the 100 units the dandiset holds.** This separates the two causes of failure:
  - The failures of counts and tests come from the missing sessions: unit counts, the spike-rate test (p = 0.03 on these units too), decoding counts, late-delay counts, PTupper persistence (p = 0.060 and 0.066) and the PTupper CDgo onset.
  - The files' clock raises every unit's baseline rate, by a median of about 1 Hz. That moves the rectified PTlower decoding mean out of tolerance (56.20% against 56.84%).
- **CDgo onset over 0 to 0.1 s.** The PTlower onset is 37.5 ms in the files, the same units processed, and all the paper's units. So its distance from the paper's 24 ms comes from the shared method, not the data. I did not test which part of the method causes it.
- **Lick-aligned window cut.** Only 0.16% (PTupper) and 0.17% (PTlower) of unit-trials have a last lick more than 2.5 s after the go cue, so the 3.0 s cut does not bear on pt-lower-movement-termination.
- **AA0134.** None of its axon nodes lies in the superior colliculus.
- **The 150 tagged units.** They are the paper's 143 of good quality plus 7 Fair-quality PTlower units, which the code's filter leaves out.
- **Anatomy.zip images.** Each folder's image count and file sizes, read from the archive's directory.

**Text corrected or added:**
- The conclusions now state the one-bin margin in pt-cd-change-at-go-cue and the opposite direction of the cohort difference in pt-cohort-control.
- The summary, the README, the claim notes and one dandiset finding (the raised baseline rates) are updated to match.
- The round is recorded under `verifications`, with the verifier's reasons and my responses.
- I added two questions to `questions/000006.yaml` for a reader:
  - whether the count criteria should be judged as fractions when units are missing;
  - whether the cohort-control test should count a difference in the opposite direction as a failure.

**Not done:**
- **Reassigning spikes to trials by stored order.** A trial boundary shows only where the time steps backwards, so the assignment would stay ambiguous. The verifier offered the processed-data comparison as an alternative, and I added that.
- **Opening the anatomy images in the notebook.** The entry check forbids reading images. The pixel size I found while preparing (8600 by 6200, greyscale) is mentioned as not run in the notebook and decides nothing.
- **The earlier record.** `tools/entry.py check` reports 22 errors, all in that record (`attempts/000006-economo-2018-01.yaml`), which lacks the newer claims. They were there before my changes, and I left that record as it was.

There are also untracked files in the working tree that I did not create (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others). You may want to make sure the workflow doesn't commit them.
