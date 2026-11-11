I've worked through every point in the round-1 report and re-run the entry with `python tools/entry.py all entries/plitt-2021`. Both notebooks pass: part 1 in 31 min, part 2 in 18 min. The conclusions, summary, README, attempt record and questions now match the new numbers, and the round is recorded under `verifications`. Nothing is committed.

**Outcomes changed (5).** In each case I took the verifier's outcome.
- **Now not reproduced:**
  - **Session and trial counts:** the decision-mouse trial count fails under both readings.
  - **Place-cell similarity matrices (fig2eh):** the z-scored half fails.
  - **Checkerboard sessions (edf7):** R5 session 8 fails.
  - **Frequent-morph null models (edf9l):** the uniform-prior test fails.

  All four were partially reproduced before. Their criteria define no partial outcome, so one failed part means not reproduced.
- **Hebbian model's prior reconstruction (fig7g): now partially reproduced.** The signs hold, but "less closely matched than the neural data" is not shown for rare. The neural rare mean it is compared with has the wrong sign. Under the paper's code (see below) the rare-trained models' magnitude (0.349) exceeds the neural one (0.288).

**Added or corrected**
- **Prior reconstruction (fig6d, used by edf10 and fig7g).** I added the ideal-observer check the verifier asked for. Under the claims file's formula, an observer that samples the rare posterior still gives +0.547, so this formula cannot produce the rare sign on this task's design. The paper's code computes the reconstruction differently, and that code printed the paper's own values. As a variant with the 2020 code's settings it gives rare −0.421 ± 0.123 and frequent 0.500 ± 0.077, both within tolerance. fig6d stays not reproduced, as the claims file fixes the formula. I added a `code_mismatch` finding and a reader question.
- **Place cells.**
  - Using the 2020 code's signal (activity divided by each cell's 95th percentile) leaves 99.91% of decisions unchanged, so the signal does not explain the excess.
  - The fast shuffle matches a plain implementation exactly (500 of 500 counts).
- **Other variants, none deciding:**
  - fig2eh with unsmoothed maps (2020 code) meets both halves of its criterion; the claims file's smoothing decides.
  - The step share clipped at 1, and per-mouse medians: edf6 and fig3ab are still not significant.
  - edf5 with each mouse held out: only 5 of 20 clusters beat the mouse relabelings. Separability may partly reflect mouse identity; the notes say so and the outcome stays reproduced.
  - edf9k/l under both code likelihood widths: same outcomes.
- **Session numbering (edf7).** File days equal the deposit's date order for 60 of 89 files. R5's day-8 file is its session 8 under either numbering, so the failure stands. I added a `metadata_insufficient` finding about the undocumented numbering.
- **Decision-mouse sessions.** I added the per-session trial table. The 2020 code's selection (sessions 5 and later) gives 2,662 trials, within tolerance; it is shown as a variant only.
- **Smaller fixes:** the session listing now separates training and testing files; the notebooks print the number of asset paths the file-name pattern skips (0); and the edf4bc notes say the place-cell reference includes the overlap cells themselves.

**New reader questions (4)** in `questions/plitt-2021.yaml`:
- whether fig6d and its dependants should follow the code's reconstruction;
- the claims file's statement that scaling a cell does not change spatial information;
- the claims file's stated range of the Hebbian model's test stimuli (they actually span 0.04 to 38.45 f_h);
- whether the code's decision-mouse session selection should be a reading.

**Not done**
- I could not identify the two extra rare sessions (26 against the paper's 24). My rebuild of the 2020 code's selection holds more sessions than the dandiset has, and its trial totals do not match the code's printed ones.
- After the final run I only reworded the date explanation in the conclusion, summary and record, and added a docstring note to `morph.py`. No numbers changed. I applied the same text edit to the executed copy of part 2 so it matches.
- Some files I did not create are in the working tree: dotfiles such as `.bashrc` and `.gitconfig`, plus `.idea`, `.vscode` and `scripts`. I left them alone; the `tools/` changes were already there when I started.
