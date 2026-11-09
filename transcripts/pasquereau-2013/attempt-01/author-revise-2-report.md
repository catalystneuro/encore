No outcomes changed. The verifier agreed with all 28, and I found nothing that called for a `proposed` change. The tally is still 4 reproduced, 3 partially reproduced, 3 not reproduced and 18 blocked. I re-ran the entry after editing the notebook: it passed in 155 s, and `tools/entry.py check` reports 0 errors.

**Text corrections**, each made in the notebook and, where the same sentence appeared there, in the attempt record:
- **`velocity-matched-magnitude`** (cell 98): the paper's group sizes are now given as 22 to 33. It said 24 to 33.
- **`ptn-more-responsive`** (cell 48 and notes): both fractions are now said to be outside tolerance. The PTN value, 68.9%, is above its tolerance range too, not only the CSN value.
- **False-positive rate** (cell 39, the Summary, the `false-positive-rate` notes and the `methods_unavailable` finding): Poisson spike trains give 0.15 against the 0.22 observed. The text now says most of the excess comes from the detection procedure and about a third is not explained. It previously said Poisson "gives the same".
- **`emg-onset-unchanged`** (cell 92 and notes): I removed the untested claim that small pre-MPTP responses delay their detected onset. I added the middle-command-size onsets: 28.8 ms pre and 45.6 ms post (p = 0.18), so post-MPTP is the later one there.
- **`emg-m2-larger`** (cell 88 and notes): the median m2 is now given by command size and state, including 17.09 for pre-MPTP at the largest size (n = 5). The text says it does not rise simply with command size within a state.
- **`kinematics-slower`** (cell 80 and notes): I replaced the "8.5 to 145.3 deg/s is lower than the paper's range" statement. It now gives the 58.7 deg/s mean and says only one response comes from a session in the paper's 130 to 200 deg/s window.
- **README**: "a few minutes" is now the measured 2.4 min from this run. The verifier's run printed 1.5 min.

**Verification record:**
- **Round 2** is added under `verifications`: all 28 claims agreed, with the verifier's reasons in its words and my changes under `response`.
- **Round 1:** the `false-positive-rate` reason now includes the two points the verifier said were missing: the literal t-test reading also fails, and about 12% of detected responses are expected to be false.

**Not done:**
- **Round-1 `velocity-matched-magnitude` reason:** I left the sentence that contradicts itself as the verifier wrote it, since the record must keep its words. Its round-2 entry records the correction.
- **Paper text:** I did not download it. Every point could be handled from the report and the claims file. The verifier says it saved the text under `paper/`, but that folder is not in this checkout.
- **Figures:** the verifier did not inspect the plotted figures, and I note that in the round-2 record.
- **Untracked files:** some files in the repo root that I did not create show as untracked (shell and editor dotfiles, `scripts`). I left them alone.
