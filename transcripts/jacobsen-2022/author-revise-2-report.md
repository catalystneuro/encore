No outcome changed. All 28 stay as the round-2 verifier agreed: 7 tested and 21 blocked as data missing. I wrote no `proposed` changes, because nothing in the report argues for one. I re-ran with `python tools/entry.py all entries/jacobsen-2022` and it passed. `tools/entry.py check` reports 0 errors. Nothing is committed.

**Corrected or added, by report point**

- **First TTL event length:** Cell 3 now prints the length of every TTL event over 5 ms and where it starts. There are ten such events, lasting 44.8 to 1872.9 ms, and all start at an epoch start. The "0.6 to 1.9 s" claim was wrong: the 44.8 ms event is in day 15 session 1 of mouse 70375. I corrected it to "45 ms to 1.9 s" in cell 4, the Summary, the deviation for fig5c-responsive-grid-cell, the `format_error` finding and the helper docstring.
- **LFP timestamps:** cell 6 now says they run backwards "2 to 4" times per file, matching cell 5.
- **`waveform_mean` scale:** cell 25 now also prints the peak-to-trough for the units of mouse 58313 (34 to 243). The Summary and the `metadata_error` finding now give both mice.
- **The "first 275 pulses" variant (figs3):** cell 27, the record notes and the `selection_undocumented` finding now say this is not a rule the paper applied to every session. For day 15 session 1 (278 pulses), the printed 68.71% fidelity is what all pulses give; the first 275 give 69.09%. The selection that matches day 14 session 2 only works for that session. I left my round-1 response as written; the round-2 response corrects it.
- **Day-17 laser epochs (B3):** the conclusion in cell 23 and the record notes now give each unit's firing rate in each epoch. They also say these rates do not show the laser power of either epoch.
- **README:**
  - The table now marks figs3 and figs4 as "(resting on an assumption)".
  - The run time now reads "about three minutes". This run printed 180 to 184 s, of which the two shuffle runs take 83 s each.
- **Round-1 cell numbers:** the round-1 entry now notes that its reasons cite the old cell numbers and maps them to the current cells (13, 18, 21, 26, 29, 32, 35). The reasons themselves stay in the verifier's words.
- **Round 2 record:** added under `verifications`, with the verifier's agreement, outcome and reason for each of the 28 claims, and my response.

**Not done, and why**

- **No question added:** the verifier found no place where the claims file misreads the paper, so nothing went into `questions/jacobsen-2022.yaml`.
- **Open points still waiting on the paper's authors:** the shuffle interval (B2), which laser epoch Figure 5C uses (B3), and what the head direction score and the 9.02 Hz peak are (figs4). These are already recorded as questions under findings. Nothing in the data can settle them.
- **Rate maps:** the verifier still can't view the rendered maps. I made no change, because the grid and border calls rest on the printed scores.
