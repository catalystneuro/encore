No outcome changed and nothing is proposed. The round-2 verifier agreed with all 45 outcomes, including fig4h as reproduced, which it had disputed in round 1. I re-ran the entry with `python tools/entry.py all entries/zhai-2025`: 0 check errors, the notebook passes, and every number cited matches the new output. Nothing is committed.

**Added**
- A new notebook cell, `somatic-last-sweep`, runs all 14 somatic tests (rheobase and summed spikes) using the first and then the last sweep of a repeated step. U and P are identical in every test, including the fig6c summed-spikes variant (P = 0.45). The somatic deviation, repeated in 10 outcomes, now cites this cell instead of the unsupported "every somatic result is the same".
- Three reader questions in `questions/zhai-2025.yaml`:
  - **link-dendritic-cells, Figure 6D letter:** the letter matches the file's cell number (16 of 16 cells) better than the cell's place in the day (14 of 16). The outcome is reproduced either way.
  - **link-dendritic-cells, row order:** the criterion says the somatic link checks the row order. It does not, because the somatic link uses best matches.
  - **link-sr-cells:** the criterion names `lid.detect_events`, which does not exist in this attempt.
- The round-2 entry under `verifications`, with the verifier's reasons in its own words and my response for each of the 45 claims. No finding is rated critical, so the round has no `findings` list. The verifier would rate none of the 8 findings critical.

**Corrected**
- **fig4h:** I removed the claim that the paper's per-cell counts support the "nearest run" choice of sweeps. That was in the notes, the deviation, cell 78 and a code comment. The text now says the support is weak: for 2023-04-06 cell 1 the two possible runs give 93 and 89 events against the paper's 73. It also says the outcome is fragile and rests on the paper not having used that cell's first 10 sweeps; with those, P = 0.049 instead of 0.064.
- **README:** the Sr2+ row now says the iSPN frequency claim depends on which sweeps are used.
- **Notebook text:** the Sr2+ claim headers now list every sweep variant the code actually runs.
- **Summary:** "Seven claims rest on the paper's own tables" is now eight.
- **link-somatic-cells notes:** "most of them" is now "6 on-state dSPNs and 3 sulpiride iSPNs" (9 of the 18 cells).
- **GRAB finding 6:** "seven regions" with a short acetylcholine trial is now six. The 2024-05-24 Slice1Roi1 region is listed only because it lacks a tetrodotoxin trial; its acetylcholine trials last 4.6 and 5.2 s.

**Not done**
- **Claims file:** unchanged, as the rules require; the three points the verifier raised about it are now reader questions.
- **fig1i-dspn-dendritic-sch-lower:** stays not reproduced. The verifier agreed this comes from the pair missing in the data, and asked for no change.
