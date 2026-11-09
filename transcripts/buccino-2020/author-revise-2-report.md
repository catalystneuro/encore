No outcome changed in round 2. The verifier agreed with all 24 outcomes: `recordings-as-described` reproduced, `fig4a-curators-agree` partially reproduced, and the other 22 claims blocked as `not_runnable`. Nothing needed to go under `proposed`. The entry was re-run twice with `python tools/entry.py all`: both runs passed with 0 errors, and `tools/entry.py check` passes on the updated record.

**What I corrected, by report point:**
- **Stale read-time numbers:** the blocked notes, the round-1 responses and the streaming finding now quote the final run. That is 72 MB/s, 1.4 to 6.5 min per whole recording, 0.087 to 0.155 s per chunk and 6.2 to 16.9 h chunk by chunk. These numbers change from run to run, so they are not the ones the verifier asked for (85 MB/s, 1.2 to 5.5 min, from their run). The record says so.
- **Mouse value scale:** the Summary's "and not with microvolts" is softened to say the file cannot show whether the values are counts or microvolts. The cell 13 labels no longer call the values microvolts.
- **Minimum-score scan (cell 25 and the fig4a notes):** these now say the ratio stays inside its tolerance up to match_score 0.7 but falls below it at 0.8 (56.79%, against a lower bound of 57.78%), and that the criterion fixes the default of 0.5. In this run the count at 0.8 is 209, not the 208 the verifier saw; the round-2 response records both.
- **Cell 0:** it now names the fig4a curator counts as tested from the curations alone.
- **Kilosort2-only claims:** cells 0 and 22, and the notes for fig2e-ks2-unit-types, fig2e-ks2-curated-unit-types and fig3s2, now say these three need Kilosort2 alone, which still needs MATLAB and a GPU.
- **Statements with no printed output:**
  - Cell 3 now prints the archive's species summary (only house mouse), which backs that finding. Cell 4 and the Summary mention it.
  - I removed the pip results (Tridesclous, SpyKING Circus, HerdingSpikes) from the record's notes. Cell 22 still mentions them as "not run here", which the protocol allows.
- **Old cell numbers:** the round-1 `reviewed` text now says its cell numbers refer to the round-1 notebook, and gives the new numbers for the link check (18), software check (21) and fig4a (24).

**Round 2 under `verifications`:** each claim has `agrees: true`, the verifier's outcome, its reason paraphrased from the report, and my response. The points not tied to one claim are listed under `reviewed`.

**Not done:** the README is unchanged, because the verifier found every sentence in it consistent with the outputs. Nothing was committed, as instructed.
