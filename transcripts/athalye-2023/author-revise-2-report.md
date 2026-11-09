No outcome changed and nothing is under `proposed`. All 29 outcomes stay as the verifier reviewed them: 20 reproduced, 6 partially reproduced, 1 not reproduced, 2 blocked. The entry re-ran cleanly (main notebook 928 s, simulations notebook 498 s), the numbers came out the same as before, and `tools/entry.py check` reports 0 errors.

**Sentences corrected (the five the verifier flagged):**
- **fig3e notes:** now say three or four of the six fractions are within tolerance, not four in every case. It is three with the shuffle null and neurons over significant tuples.
- **Main notebook, cell 7:** the Monkey J figure is now 98.9 to 99.6%, not 98.7.
- **Simulations notebook, cell 4:** now says 0.967 to 1, not 0.98 to 1.
- **Simulations notebook, cell 9, and fig6d notes:** no longer say the result "holds only in part" under the summed 5 ms gain. They now say that under that reading the criterion would give not reproduced, and that the outcome depends on which Monkey J decoder is used.
- **Main notebook, cell 54, and figs3 notes:** now say the variant fitted on rates in Hz leaves only the full model's counts unchanged. The decoder-null counts are not tested under it.

**Other additions to the notes, answering the verifier's remaining points:**
- **fig5c:** the outcome depends on scoring the same pairs the paper's code scores. On that reading the shuffle 95th percentiles (0.0543 and 0.0527) match Table S1's 0.055 and 0.053.
- **fig4f and fig5h:** both now state that their partial verdict is a judgment the criterion does not provide for.
- **Round 2 record:** added under `verifications`, one entry per claim, with the verifier's reasons in its own words and my responses.

**Not done:**
- **figs5f is still blocked.** I rechecked the install with uv 0.13.6: building `ssm` still fails with "No module named numpy". The registry installs every entry's environment with a plain `uv pip install -r` of the lock file. The workarounds the verifier suggests would mean changing the registry's tooling, which the entry cannot do. Running the rsLDS comparison would also be a new analysis, which the protocol leaves to a new attempt (about 3 h on one core for Monkey J alone). The record says all this.
- **Monkey J's condition classes and outside target list:** the verifier could not check these, and there is nothing in the entry to change for it. The target list and its source were already recorded under `inputs`.
- **No questions for a reader:** the verifier did not report any place where the claims file misreads the paper, so I added nothing to `questions/000404.yaml`.

Nothing is committed, as instructed. The untracked dotfiles, `.idea`, `.vscode` and `scripts` in the working tree were there already and I did not touch them.
