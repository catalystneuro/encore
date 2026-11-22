I've worked through the round-2 report. No outcome changed, but three outcomes now carry a proposed change for a third verification round. I re-ran the entry with `python tools/entry.py all entries/russo-2025`: both notebooks pass and the checks show 0 errors. Nothing is committed.

**Proposed outcome changes** (the verified outcome stays until round 3 reviews them)
- **speed-threshold-robust:** proposed not reproduced (currently partially reproduced). The criterion has no partial clause and needs EEG, LFP and CSD to pass at every threshold. A check added to cell 27 shows LFP fails at 5 cm/s and CSD fails from 0.5 cm/s.
- **fig2fg:** proposed not reproduced (currently partially reproduced). The criterion needs all six signed-rank tests to pass, and a check added to opto cell 8 shows 5 of 6 do. The SM-TH test of 75 against 125 ms light gives p = 0.20.
- **figs10a:** proposed reproduced (currently partially reproduced). Under reading (c), the one the criterion fixes, FS gives p = 0.35 and TRN p = 0.88. The partial outcome rested on a within-session check that is not in the criterion and that I had applied to this claim only. I followed the verifier's recommendation to judge both claims by the criterion. A new table in cell 55 shows fig3a, FS and TRN under the pooled and within-session tests; within sessions, fig3a gives p = 0.19 and FS p = 1.3e-08.

**Added or corrected**
- **figs8b:** I added a table of every pair of the five mice, since the paper reports two. All six means fall within tolerance in only 6 of the 10 pairs, so "no choice of two mice changes the outcome" was wrong. The notebook and notes now say the outcome depends on which two mice the paper used. The outcome stays reproduced.
- **Model timing:** the three runs in this revision gave 121 to 123 s on one thread and 82 to 83 s on four per simulated second, about 2.3 h for four single-thread runs at once. Cell 102, the notes for all five model claims and the round-1 responses now give these figures, along with the 158 s and 113 s from the run the verifier saw.
- **Round-1 `agrees` flag:** for the five model claims it is now false. The round-1 verifier had given blocked (other) and called the blocking unsupported.
- **Text fixes:**
  - The `waveform_duration` range in cell 8 now quotes the printed 0.110 to 2.074.
  - The artifact wording in the Summary and in finding 4 now says within 0.2 ms in the EEG and 0.6 ms (1.5 samples) in the LFP, on trial-averaged signals.
  - The 569069 FS result (p = 0.0033) is added to cell 56 and the notes.
  - In opto cell 17, the claim that the rising VPM units are GABAergic is replaced by the three possibilities the verifier named, and the stray "**" is removed.
  - The README and both summary tables mark the three proposals.
- **Round 2 in the record:** it is under `verifications`, with all 39 results in the verifier's words and my response to each.

**Not done, and why**
- **Round-1 point 8 (artifact mask span):** no code change. The helper already states the -3.2 to +2.4 ms span, and it lies outside every analysis window.
- **No `findings` entries for round 2:** the record rates no finding critical, and the verifier saw none that should be.
- **No new questions in `questions/russo-2025.yaml`:** the verifier found no new place where the claims file misreads the paper.
