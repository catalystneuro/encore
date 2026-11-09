I answered the one question and changed the claims file.

**figs3-neutral-unmodulated: changed.** The question was right. Supplementary Table S11 counts NEUTRAL cells by protocol: 4 in Evoked, 20 in Evoked/Ongoing and 12 in Ongoing, 36 in all. The paper's n = 32 is therefore 20 + 12, which is also the NEUTRAL set the ongoing analyses use ("NNEUTRAL = 32").
- **What changed:** the criterion now takes the NEUTRAL units of the 'evoked/ongoing' and 'ongoing' files instead of all files. Table S11 is added to the source. The counts with all 36 units are still reported.
- **What did not change:** the statement, the quote and the expected values (32, 69 and 70) stay as they were.
- **Answer:** recorded in `questions/001708.yaml` with `answered: 2026-11-05`.

**Quote check:** `tools/claims_check.py` found every quote word for word. It reports one problem, in a different claim: the value -0.27 in `fig2g-switch-times` is not found in the main text. I did not touch that claim, and I ran the check on the main text only, not the supplement.

Nothing is committed or pushed.
