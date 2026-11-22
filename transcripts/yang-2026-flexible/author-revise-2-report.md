Round 2 is done: no outcome changed, nothing is proposed for a third round, and the corrections are recorded under `verifications` in the attempt record. The entry ran twice with `tools/entry.py all`, and both runs passed (about 55 minutes each). The numbers were identical in both runs, and `entry.py check` reports 0 errors.

**Outcomes.** The verifier agreed with all 30 (21 reproduced, 2 partially reproduced, 7 blocked), and they stay as they are.

**What I corrected or added, point by point from the report:**
- **Split-half range (cell 36):** now 0.1071 to 0.1107.
- **A_t, table2 and ttype-beyond-cre (cells 41, 42, 45, the notes and finding 6):**
  - I removed the claim that the machine's sort causes the offset, and the wrong note about the first version's numbers. "Equals" is now "within 0.0005".
  - I added a variant that ranks ties with a stable sort. It moves A_t by at most 0.0021 and A_t minus its null mean by at most 0.0003, much less than the 0.016 gap to the paper's printed values. The record now says what causes that gap is not shown.
  - The values moved slightly in this run, whose CPU has AVX-512 where the previous run's did not (A_t is now 0.0337, 0.0278, 0.0137), so I updated `measured` and the notes. The notes mention the comparison with the previous run as one made outside the notebook.
  - Finding 7 has no text about machines, so I left it alone.
- **Sst-IRES-Cre (cell 51 and notes):** now two Cre lines of the join with the Ai14 and Ai167 reporters, which the files' genotypes count as one driver. The count of lines with p < 0.05 now matches this run's output: 11 of 15. It was 12 in the previous run.
- **join-link quote (cell 10):** now the claims file's exact statement, with "genotype".
- **Summary and README:**
  - I took out the wrong 78-minute and "45 to 78 minutes" figures; the text now points at the times the notebook prints.
  - "One cell each" now says two files hold the same recording.
  - The README and the entry description no longer call all 4,435 cells interneurons.
  - `runtime_minutes` is now 55.
- **NeMO server answers:** corrected to what each run printed: three 502 errors in the earlier run, then one 502 and two time-outs in this revision's final run.
- **Critical finding 1:** cell 9 now prints the duplicated pair's feature count: 94 IPFX features in each file, all equal. The finding now says 94 (it said 93). The verifier agreed it is critical, and that is recorded under the round's `findings`.
- **Round-1 reasons:** I added the verifier's problems 6 and 8, which it noted appear in no reason, to the join-link and fig1b reasons.

**Not done:**
- No question went to a reader, because the verifier found no place where the claims file misreads the paper.
- The seven transcriptomic claims stay blocked: the NeMO server still did not answer.
- The cause of the gap between the code's own draws on the paper's scores and the paper's printed A_t is still unexplained.

Nothing is committed. The untracked dotfiles and the `scripts` folder in the checkout are not mine, and I left them alone.
