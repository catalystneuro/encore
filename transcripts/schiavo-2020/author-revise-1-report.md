I revised the attempt for round 1. The main change: five in vivo whole-cell outcomes are now blocked, because the deposited recordings show no current that follows the calls. The entry re-ran cleanly with `tools/entry.py all` (149 s, 0 check errors), and every conclusion matches the new numbers.

**Changed outcomes**
- **ed6ef-epsc-tuning, fig2h-epsc-enhanced-ev, fig2j-ie-ratio-tracks-isi, fig2k-ipsc-exceeds-epsc-575** were not reproduced or partially reproduced. They are now blocked as `other`.
- **fig2i-ipsc-weaker-nv** was blocked as `methods_underspecified` and is now blocked as `other`, the reason the verifier gave.
- Behind this (B2 and B3), I found a bug of my own: the call onset was wrong. The first syllable of many calls is quiet, and the onset fell a median 193 ms late (up to 644 ms) in 51 of 83 files. The helper now takes the start of the sound.
- With the corrected onset, the currents still do not follow the calls:
  - 2 of 39 cell recordings respond, against 3 of 39 before the call.
  - No cell responds in the first 300 ms after onset.
  - 13 of 110 files show any sweep-locked change, where chance gives 5.5.
  - The Methods' rule of five significant prototype responses keeps 1 of 39 cells, or none at the stricter threshold. The paper does not define a significant response; I assumed a trial beyond 2 or 3 s.d. of the cell's pre-call measure.
- The values computed on every cell stay in the notes.

**Added or corrected, by verifier point**
- **B1:** the subject link now reads the figshare item titles. All 54 match a subject and agree with the descriptions, and the 5 mice that had no group now have one. The outcome stays partially reproduced, because no file says which call each trial played.
- **B2 to B4:**
  - Per-cell trial-averaged currents by ISI, aligned to onset (a figure), and the inclusion-rule counts.
  - Ranking the largest trials by expected direction as well as by absolute size, for both the call and the pre-call windows.
  - Trial counts for the seventh experienced IPSC cell, which has only 4 or 5 trials per ISI.
- **B5:** the oxytocin section prints each file's spreadsheet label and timing. A second reading of the control window takes in all 7 controls and again shows no change. The outcome stays reproduced, resting on the assumed comparison family.
- **B6:** `sampling_interval` now takes a median, over the times printed at 0.1 ms. That gives 0.70 ms; a median over the coarser times would give 1.0 ms, which reflects the printing, not the sampling. The operant numbers are unchanged. The notebook now prints how the gap that ends a press grows with time in the session.
- **B7 and B8:** the slice pulse times are checked against the stimulus artefacts (91.8% within 1 ms), with one sweep drawn. The fig1g notes now say the two readings point in opposite directions, neither significant. Retrieval onset hours now also count from the 24 and 48 hour PRE sessions.
- **Imaging (point C):** folding single pixels shows trials recur every 40 frames (10.24 s), not the Methods' 0.1 Hz. Which call each trial played still cannot be recovered, so the imaging claims stay blocked. I recorded this as a finding.
- **Record:** the round is in `verifications` for all 44 claims, with the verifier's reasons and my responses. The README, summary and findings are updated.

**Not done**
- I added no reader questions; the verifier reported no misreading of the claims file.
- I did not try to segment cells or recover call identity from the movies. Without a stimulus order there is no defensible way to assign calls.
- The changes to `tools/runner/chain.sh` and the untracked dotfiles were there before this run, and I left them alone.
