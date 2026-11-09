I answered every point in the round-2 report. No outcome changed and I proposed no changes, so a third verification round isn't needed. The entry re-ran cleanly with `python tools/entry.py all` (0 errors, notebook passes, 11.5 min), the numbers match the earlier run, and `check` passes after the last edits.

**Outcomes:** all 21 stay as verified. The verifier agreed with every one, including the two it had disagreed with in round 1.

**The `assumed` flag I could not add.** The verifier asked for `fig4d-evoked-increase` to be marked `assumed: true`, since it rests on each session being one condition. I added the flag (and on the two claims that depend on it), but `entry.py check` rejected it: the attempt schema allows `assumed` only on an outcome that stands, not on a blocked one. I took the flags out and stated the assumption in words instead:
- in that claim's notes and its deviation;
- in its section and conclusion in the notebook.

They now say the outcome rests on one condition per session, and that if session 15:04 held two conditions (its trials split five below zero, five above) the outcome could change. The record's response explains why the flag is missing.

**Text corrected to match the printed numbers:**
- **Cell 12:** onset intervals are now 12.2 to 56.6 s.
- **Steady-baseline conclusion:** now "at most 6.64 against 13.60 or more" (the channel 3, window b reference).
- **Speckle conclusion:** the 12:49 episode times are now given by phase (27.5, 60.3 and 99.6 s in phase 1; about 27.5, 41.6 and 99.6 s in phases 2 and 3).
- **Speckle notes in the record:** the spectrum "peaks at its longest period (30 s), a slow drift with no regular rhythm", not a 30 s rhythm.
- **Single-pulse variant (notebook and record):** the "no response to individual pulses" statement now applies to channel 4 only. Channel 3 is significant in 14:59 (p = 0.023) and 14:50 (p = 0.039), so the variant does not decide the claim.
- **Runtime:** the README now says 9 to 12 minutes (8.6 and 11.5 in the last two runs), and `runtime_minutes` in `entry.yaml` is 12.

**Output added:** a new data-check cell prints the archive's versions (one published version, plus the draft with the same 35 assets and 29.39 GB, last modified at publication) and the version's summary (1 subject). This backs the statements in cells 0 and 4 that had no printed output. Cell numbers from cell 4 on are now one higher than in the verifier's report.

**Recorded:** round 2 is added under `verifications` for all 21 claims, with the verifier's reasons in its words and my response to each.

**Not done:** the verifier found no place where the claims file misreads the paper, so there was nothing to add to `questions/001559.yaml`. Some untracked dotfiles and folders (`.bashrc`, `.idea`, `scripts` and others) appeared in the checkout; I didn't create them and left them alone. Nothing is committed.
