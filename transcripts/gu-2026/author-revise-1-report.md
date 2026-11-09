I've revised the attempt for the round-1 report. The entry re-ran with `python tools/entry.py all` and passed in about 14 minutes (it was 26). A second run gave identical numbers, and the entry and the attempt record pass the checks. Nothing is committed.

**Outcome changes:**
- **Figure 3 claims (4):** blocked becomes partially reproduced for all four (`fig3b-extended-before-stopping`, `fig3b-distance-predicts-com`, `fig3c-distant-after-stopping`, `fig3d-distant-vs-inbound`). The verifier agreed these were blocked. But when I matched the `scratch/triggered` tables' trigger times to this entry's events, as it asked (B6), 720 turned out to be triggered at COM times and 353 at outer pokes. They hold the decoder's MAP position in windows around those events, and they are the inputs of the paper's own Figure 3 code. I read them with that code (Gu2026 at commit 0f0c9a7, now listed under `inputs`), so the claims could be tested:
  - **fig3b-extended-before-stopping:** COM greater with p < 0.01 in 4 of 5 rats; rat E has p = 0.053.
  - **fig3b-distance-predicts-com:** the fold change is 1.047 or 1.079 per cm depending on the reading. Both are within tolerance, but neither reaches p < 1e-20.
  - **fig3c-distant-after-stopping:** 4 of 5 rats; rat J fails, with only 26 events.
  - **fig3d-distant-vs-inbound:** the whole-track tables come in pairs from two decoders, and the files don't say which is the paper's. With the smaller of the two the claim holds in part, with the larger in full. I kept the partial result and marked it `assumed`.
- **`figs7b-no-swr`:** blocked becomes reproduced (`assumed`). I detect ripples on the deposited LFP, in short windows only, run in separate processes.
  - Under the criterion's reading (iii), COM is below both trial ends in both windows, with and without the reference subtraction.
  - It rests on three choices the files force: all tetrodes in the file are used, since the electrode table has no locations; the reference channel is in the file on some days only; and the session baseline is sampled from 20 windows per epoch.
  - Ripples come out rare, 0.13 to 0.34 per second of immobility.
  - A new clock check shows LFP theta amplitude tracks head speed with no time shift.
- The other 15 outcomes are unchanged. All 29 rounds are recorded under `verifications`, with figs7b as the one disagreement.

**Corrections and added outputs:**
- **Reading (b) threshold (B3):** now 0.1 of the paper's 96 cm arm, i.e. 9.6 cm. Still 4 of 10 counts within tolerance.
- **COM time (B4):** now the first reversal after the head passes the threshold. No count changed.
- **Sessions under 20 trials (B5):** now left out of figs1f, fig1g and fig1h. Both thresholds now run for the run-through claim.
- **Trial shortfall (B2):** added trials per day. Rat M's missing sixth day explains its shortfall. K and L have the days shown in Figure 1C, so where their trials went can't be told from the files.
- **Chance level (B7):** added the 1/3 chance comparison for fig1c.
- **fig1h variant:** added the version that adds one to both counts so no day is dropped. It would reach the partial bar (J, K, L at p < 0.01). I kept not reproduced, because the claims file itself says to drop undefined days.

**Findings:** I rewrote the triggered-table finding and added four. Two are about the metadata: no electrode locations, and the LFP unit given as volts. Two are methods questions for the paper's authors, on which decoder made the Figure 3D tables and how SWR detection was set up.

**Not done:**
- No claims-file question added; the verifier reported no place where the claims file misreads the paper.
- In fig3b, the readings for all moments and for the 5 s before stopping can't be run, because the deposited tables don't hold those data.
- Some triggered tables match none of this entry's COM times or pokes; these are many of rat J's and are left out.
- Untracked dotfiles and a `scripts/` folder appeared in the repo root during the run. I didn't create them, so I left them alone.
