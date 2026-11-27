No outcome changed, as round 2 requires. The verifier agreed with all 33 outcomes, so they stay at 24 reproduced, 7 partially reproduced and 2 not reproduced, with none proposed for change.

**One thing to know first: the last full run did not pass cleanly.** `python tools/entry.py all entries/mah-2023` passed the checks (0 errors), but the behaviour notebook failed when Zenodo returned "504 Gateway Time-out". The models and starts notebooks passed. It was already past 11:38 by then, so I re-executed only the behaviour notebook, with the same environment and command that `entry.py` uses. That run passed. All three executed copies now match the entry, but `executed/mah-2023/` has no `.clean-run.json` stamp and `result.json` still records the failure. The workflow may need to run the entry again. In the previous full run, every notebook passed and the outputs were identical.

**Changes the new numbers forced:**
- **suppfig8:** `seed_sensitive: true` is set again. This runner gives the first run's numbers: the claim's seed still gives p = 0.163, but seed +3000 gives BIC/AIC p = 0.0305. The 2-start fits differ slightly between machines, and the notes give both runs.
- **fig3l:** the one-start lambda fits also differ by machine. Wait time C at mixed to low is now p = 0.337 and initiation C is p = 0.047. The outcome stays not reproduced, and the notes give both runs.
- **fig3j and fig3f:** the notes now use this run's numbers.

**What I added or corrected, point by point:**
- **Fit starts (problem 4):** a new notebook, `starts_mah_2023.ipynb`, refits the models from 6 starts, the most that fits the time limits.
  - suppfig8 at seed +3000 gives BIC/AIC p = 0.0507, so it stays near the threshold.
  - fig3f's 6-start results are unchanged, so its failure does not come from too few starts.
- **Zenodo coverage (fig4a):** I worked out where the 1,731 unmatched sessions come from.
  - 1,718 of them belong to 49 rats and are dated after the deposit's last session for that rat. For 42 of those rats that last session falls on 21 to 23 November 2022. The other 13 are sessions with a NaN in the initiation times used to match them.
  - The 22 rats with fewer deposit sessions are all among the 49.
  - Part (2) of fig4a still fails without these rats.
  - Finding 1 and the summaries are corrected, and a new finding at the end reports the deposit's coverage.
- **fig2k, fig2l, fig5c:** the wording is now "only with the post-violation trials". The text says the data cannot tell whether rats use the repeated offer or react to the offer of the trial they violated.
- **fig3l:** the shuffle fits are now counted at both bounds of C. None is at either bound.
- **Finding 3:** the direction of the threshold difference is now printed. It is lower in all 291 rats, by a median of 5.19 s.
- **Finding 2:** it no longer says initiation times depend on the offer only in flagged sessions, and it gives S050's slopes.
- **fig3i:** the verifier's point about a size floor for the overshoot is now a question for a reader in `questions/mah-2023.yaml`. The claim itself is unchanged.
- **Round 2 record:** written under `verifications`, with all 33 results and an empty `findings` list, since no finding is rated critical.

**Not done:**
- The paper's 100 fit starts were not run, because that is far beyond the time limit.
- The supplementary PDFs could not be read here because no PDF tools are installed. The fig3i question cites the Results passage instead.

I did not commit anything.
