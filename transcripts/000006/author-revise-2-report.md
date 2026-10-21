No outcome changed in this round. The verifier agreed with all 31 outcomes, and nothing I found calls for a proposed change, so no claim has a `proposed` entry and a third round isn't needed for this attempt.

**Text corrected to match the outputs:**
- **README:**
  - The dependency sentence now names the three claims blocked because they depend on a blocked claim, and says their own readings agree with each other.
  - The processed data for the same 100 units now give "most" of the dandiset's counts and test results, not all. Two differences are given as examples: 97 selective units against 99, and a PTupper CDgo onset of 82.5 ms against 77.5 ms.
  - The baseline rise is now "a median of about 1 Hz (0.14 to 6.47 Hz)".
  - It now says spikes are given to trials by time window, and the stored order is used only for the last licks and the trial boundaries of the bursting measure.
  - The run time is now "about ten minutes".
- **Summary (cell 124):** the unidentified units are now given per cohort: 232 against the paper's 495, and 430 against 511.
- **Cell 92, cell 124 and the record notes for pt-upper-decoding-rectified:** the PTlower mean is out of tolerance on the files (56.20%) and within it on the same units processed (56.84%). The higher baseline may explain this, but the notebook does not show it is the cause.
- **Cell 112 and the record notes for pt-lower-movement-termination:** the paper's units match the dandiset's pattern for PTlower only. For PTupper, CDgo selectivity on the dandiset is significant before and after the last lick, and on the paper's units in no bin.
  - The verifier wrote "4 to 10 bins" after the last lick. The printed table gives 4 to 13 with the code's selection, so I used that and said why in the response. Its own words stay in its reason.
- **Round-1 record:** problem 3 now carries the verifier's rating "does not affect a conclusion", and its caveat that it didn't download the Figshare sequencing and axon files is added.
- **Round 2 under `verifications`:** all 31 claims are recorded with the verifier's reasons and my responses. For the dependency rule it couldn't read, the response quotes docs/protocol.md, Author step 1.5: "A claim that depends on a blocked claim is blocked for the same reason."

**Re-run:** `tools/entry.py all` still stops at the check, as in earlier rounds. All 22 errors are in the old `-01` record, which lacks outcomes for claims added later, and I left that record as it was. The `-02` record passes the check. I ran `tools/entry.py run` directly, twice, the second time after the last text edit. Both passed (598 s and 611 s), and every number I used matches the outputs.

**Not done:**
- **Problem 2:** the unit-count criteria that 100 units can't reach still wait for the reader's answer in questions/000006.yaml.
- **Problem 8:** I didn't look further into what in the method makes the PTlower CDgo onset late. It doesn't change the outcome.

Nothing is committed. The untracked dotfiles and `scripts` in the working tree are not mine and I left them alone.
