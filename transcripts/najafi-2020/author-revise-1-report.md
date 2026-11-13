I've revised `najafi-2020-01` for every point in the round-1 report and re-run all notebooks. 13 outcomes changed, and the entry check passes with 0 errors. Nothing is committed.

One departure: I did not use `python tools/entry.py all` itself. A full run takes about 2 h 50 min, and a single command here is cut off at 2 hours. I ran the same steps in parts with a small script: the entry check, then the same environment build and execution command, writing to `executed/najafi-2020/`. All four notebooks passed, in 19, 47, 49 and 50 minutes (each under the 60-minute limit). My first try at notebook 1 failed on a pandas error in a print line I had added; I fixed it and re-ran.

**Outcome changes**
- **Reproduced or partial → not reproduced (11):** `fig1gi`, `figs3c`, `figs3e`, `fig3b`, `figs6de`, `fig8de`, `figs13c` and `figs13ab` (their criteria have no partial band, so a failed part means not reproduced), and `figs12`.
  - `figs3c`: the inhibitory count per session is 9.819 under reading (a) and 9.883 under (b), both just below the 9.9 limit.
  - `fig3b`: with C chosen at every bin, mouse 3 still peaks at bin 6, outside the window under both readings.
  - `figs13c`: after the re-run mouse 1 is also not significant (p = 0.073).
  - `figs12` was blocked before; its running part fails in mouse 1, whatever the untestable lick part would show.
- **Reproduced on an assumption → blocked, methods underspecified (3):** `fig2bd`, `fig6bc` and `fig7`. The claims file says readings that disagree mean blocked, so I withdrew the assumptions.
- **Reproduced → partially reproduced (1):** `fig3df`. The new per-bin weights show differences in some bins of mice 2 and 4.
- **Now:** 7 reproduced, 3 partially reproduced, 14 not reproduced, 14 blocked.

**Corrections and additions**
- **16 Hz trials:** they are rewarded on a random side and always labelled "High-rate", so the side licked is unknown. Their choice is now left out of every analysis (138 trials). The per-rate table groups on rounded rates, and the 16 Hz fractions are withdrawn.
- **Trial exclusions:** the data check now lists every trial-table column. There is no flag for helped trials or for the first trials of a session, so the paper's code's exclusions cannot be applied. This is recorded as a deviation and a finding.
- **Other data checks:**
  - The check now lists the imaging (`processing/Ophys`) and behaviour groups of every file; none holds a fluorescence trace or a spout identity.
  - Every trial's start time matches the first trial's in all sessions.
- **Activity matching (`figs3d`, `fig6bc`):** median activity is zero for nearly every neuron, so the paper's matching rule mostly keeps everything in the zero bin. I now print the activity of the kept neurons and added a variant matched on mean activity.
- **Requested outputs:** exact p-values for `fig2bc`, the `figs3c` counts to 3 decimals, per-bin weights for `fig3df` (notebook 3), and a new notebook 4 that repeats `fig3b` for mice 2 and 3 with C chosen at every bin and 50 splits.
- **Question for a reader:** `questions/najafi-2020.yaml` now asks whether the claims file misreads the paper on `figs6de`. I took the Figure S6D passage from the verifier's report, because I could not render the supplement PDF here.
- **Record:** I recorded the round under `verifications` (38 claims, 12 where the verifier disagreed), with the verifier's reasons and my responses. I also updated the notes, measured values, conclusions, summaries, README and runtimes, and built the handover package.

**Not done, and why**
- **`fig8ce` per-bin C:** not run; from my subset timing it would take about 6 hours of compute.
- **Still blocked, not run:** `figs6ab`, `figs6c`, `figs2`, `figs7c` and the three model claims. The time went to the corrections, and I recorded this as the response to each.
- **`figs1b`:** kept as blocked, data missing (the verifier would say metadata insufficient), and I recorded the disagreement. A fit without the inter-trial interval would not test the claim.
- **Fewer repetitions than the paper:** the coarser C grid and the 5 (or 3) excitatory subsamples stay, as recorded deviations.
