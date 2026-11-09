No outcome changed. The round-2 verifier agreed with all 22 outcomes (10 reproduced, 6 partially reproduced, 6 blocked), and I'm not proposing any change. The entry was re-run with `python tools/entry.py all entries/001878-sun-2021`: the check reports 0 errors, the notebook passes and ran in 4.4 minutes. All the numbers the conclusions rest on came out the same as before.

**The three statements the verifier said the outputs did not support:**
- **Cell 32, flagged frames in mount:** Cell 31 now prints the flagged frames by label: mount 304, investigation 212, other 141, out of 657. Cell 32 now says mount holds the largest share (304 of 657, 46%), not most of them.
- **Cells 13 and 14, Task 1 test recordings in Task 3 training:** Cell 13 now prints how many distinct recordings the six Task 3 training sequences come from. It is 5, and one recording appears as two sequences. Cell 14 and the matching finding in the attempt record now say five Task 1 test recordings appear as six Task 3 training sequences.
- **Cell 4, frame counts of the other two NWB files:** The sanity cell now prints the pose series, frame counts and related publications of all three NWB files, through a new helper `pose_overview` in `calms21.py`. The output shows 71,524 and 14,991 frames and the other DOIs, so cell 4's statement now has printed support.

**Other changes:**
- **Run failure fixed:** The first two re-runs failed. CaltechDATA sometimes handed out a signed download URL that had already expired, and the request was refused with a 403. `caltech_url` now checks how long the URL has left and, if it is under 30 s, waits for a fresh one. The seek in `_HTTPRange` now raises on an HTTP error, so a refused request shows its real status.
- **README:** It said the notebook takes about three minutes; it now says about four and a half, matching the 4.4 minutes printed.
- **Attempt record:** Round 2 is recorded under `verifications`, with all 22 claims marked as agreed. The reasons are in the verifier's words and each has a response. The cell 4 point does not belong to any claim, so I recorded it under `link-mouse071` next to the related point about duplicate recordings.

Nothing from the report was left undone. Nothing was committed or pushed.
