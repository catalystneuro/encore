No outcome changed. In round 2 the verifier agreed with all 37 outcomes, so nothing needed to go under `proposed`. The outcomes are still 35 blocked, fig11-ac-unit-counts not reproduced, and fig11b-ac-prf-responses partially reproduced (resting on the O2a assumption). I ran `python tools/entry.py all entries/000463-gao-2025` twice. Both runs passed with 0 errors (about 3 minutes each), and every number matched the previous run.

**Corrected, as the report asked**
- **fig11b, 30 Hz:** cell 30 and the record now say 30 Hz is significant during sonication under three of the six readings, not four.
- **fig11b, 4500 Hz:** the record now gives the corrected p range during sonication as 2.4e-6 to 0.009.
- **fig11b, paper values:** "responses of 106 to 159%" is now "responses reported at 123 to 159% in the Results text". I checked the four values in `paper/`.
- **Duplicate files:** the Summary no longer says the duplicate files differ in session start time. Cell 8 shows that is true for only 27 of 731 groups.
- **Trial counts:** the first finding now says mostly 500 trials per recording (691 of 814; the others 400 to 499).
- **AC unit counts:** I removed the sentence in the notes about duplicate copies doubling the counts, since no output showed it.
- **STTC files:** the notes for the 10 STTC-based claims (fig10, fig11c, fig11d) and the untyped-pairs cell (cell 19) no longer state a dimension order. They now say:
  - the opened file's arrays are 4-D while its description lists five dimensions, so the order is not established;
  - only one file was opened, an M1 against S1 file.

**Added output**
- Cell 18 now lists the `general/notes` of all 370 STTC files. 364 of them name AC, POm or M1 against S1, so the area pairs I described are now shown, not assumed.

**Verification record**
- **Round 1:** I removed the fig11-ac-unit-counts entry, because the verifier never gave that agreement. The round's `reviewed` text now says this claim, like methods-insitu-pressure, had no counterpart in the verifier's claims file.
- **Round 2:** added for all 37 claims. It records agreement, the verifier's outcome, its reasons paraphrased from the report, and my responses.

**Not done**
- I added no new question on O2b. The question the verifier refers to, whether O2b stays a valid reading, is already in `questions/000463.yaml`. fig11b keeps its verified outcome until a reader answers it. If O2b is kept, the claim would become blocked (`methods_underspecified`), and that would need a new round.
- I left the round-1 `response` texts on the STTC arrays as they were written, since they are history. The round-2 responses record the correction.
- Untracked dotfiles plus `.idea`, `.vscode` and `scripts` are in the checkout. I did not create or touch them, and nothing was committed.
