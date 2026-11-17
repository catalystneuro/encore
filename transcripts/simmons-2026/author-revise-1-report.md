Round-1 revision is done. The entry re-ran cleanly with `python tools/entry.py all entries/simmons-2026` (0 check errors, notebook 14.1 min), and every conclusion and note now matches the executed numbers.

**Outcome changes**
- **fig5d-shrna-higher-rate:** changed from reproduced (assumed) to blocked, `metadata_insufficient`. I agree with the verifier: the dataset identifies neither control reading the criterion names. The comparison against gabazine-alone cells stays in the notebook as a variant only, and it now says two of those control subsets were picked after looking at the data.
- **fig5f-aldh-inhibitors-higher-rate:** changed from not reproduced to blocked, `metadata_insufficient`. This goes against the verifier's outcome for this claim. It follows from its problem 5 and its own fig5d outcome: the same unlabelled stand-in controls cannot decide one claim and not the other. Round 2 will review this.
- **fig6c-snc-gi-dreadd-no-snr-change:** kept blocked, with the disagreement recorded. The claims file makes it depend on figs3 (the SNc recordings, which are missing), and the protocol blocks a claim whose dependency is blocked. Its own test now runs on the 8 SNr cells: P = 0.81, no change.
- **All other outcomes are unchanged.**

**Added or corrected, by verifier point**
1. **Collapsing cells (problem 2):** the notebook now prints every cell's rate at thresholds 6, 8 and 12 (27 of 171 cells have a condition that differs by more than 25% between 6 and 12). The helper now records spike amplitudes, and one rule (rate falls below a quarter of the previous condition) finds 7 cells. Their time courses show the spikes shrinking to noise level, in several cases already during the control file, so these are failed recordings, not drug effects. Every affected claim is also run without them, and no outcome changes. fig3b becomes significant under both readings (P = 0.0097 and 0.0014) but stays at 8–14% against the expected 25%.
2. **fig2c (problem 3):** now also run on quinpirole sweeps from 6 min. P = 0.078–0.11, so still not reproduced.
3. **fig4a (problem 4):** now measured on the mean of sweeps without spontaneous action currents, with each cell's sign taken from its clean control sweeps, plus an overlay of the mean traces. The current falls in all 4 cells by about 49%, but P = 0.11, and 49% is more than 10 points from the quinpirole reduction. Still not reproduced.
4. **fig4b:** the notes now name the two cells behind the threshold dependence. The P = 0.036 at threshold 12 comes with one cell's spikes being mostly missed at that threshold.
5. **fig5g (problem 6):** a power calculation shows 3 cells would detect an effect of the paper's size only 25% of the time (58% with 5), and the conclusion says the absence carries little weight.
6. **Gap-free pairing (problem 8):** the files are printed by cell. The drug file follows its control within 5 to 80 s.
7. **File 0023 of subject 9019 (problem 9):** it holds a 225 pA evoked current like its neighbours, so it is not a gabazine recording.
8. **Record:** I added a finding about the seven failed recordings and recorded the round under `verifications` for all 39 claims, with the verifier's reasons quoted and my responses kept separate. The README and the notebook's header and summary now show the new outcomes.

**Not done, and why**
- The verifier found no place where the claims file misreads the paper, so I added no question to `questions/simmons-2026.yaml`.
- I left two choices as they were, as the helper already states them: the drug's application time is taken as the start of its file, and the control in reading (b) uses all control episodes (problem 7).
- Nothing is committed, as instructed. The repo root has untracked `.bashrc`, `.gitconfig`, `.mcp.json`, `scripts` and similar entries. They appeared at 02:10, before this run started, and appear to be sandbox placeholders (character devices, not real files). I left them alone, and they should not be committed.
