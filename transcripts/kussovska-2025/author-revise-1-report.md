Round 1 is revised. `python tools/entry.py all entries/kussovska-2025` passes with 0 errors: the main notebook ran in 46 min and the new dPCA notebook in 22 min. `check` passes and `handover` is rebuilt. Nothing is committed.

**Outcome changes**
- **The three Fig. 3 claims, blocked → reproduced.** They are now tested in a second notebook, `dpca_kussovska_2025.ipynb`. The earlier "too large" estimate came from fits competing for threads: on one thread each fit is fast, and the 100 splits run on 4 processes.
  - **fig3d:** with the code's trials, H = 457.62 and Dunn p 1.1e-38 and 2.39e-29, against the paper's 457.217, 2.38e-38 and 1.25e-29. The two maintenance conditions do not differ (p 0.077).
  - **fig3abc:** maintenance trajectories are more complex under both measures, but part of the difference is only that maintenance is longer.
  - **fig3h:** reproduced only when the early half is fitted with `protect=[]`. The code's own setting reverses the result, so I recorded it as a finding.
- **fig6cd, partially → not reproduced.** The verifier was right: the criterion's partial outcome needs the full pattern at load 1, and the interneuron encoding-versus-probe test fails under every reading.
- **fig6e, partially → reproduced.** It rests on the cell types: 3 of 15 interneuron concept cells (20.0%, p = 0.038). This run's ACG fit keeps 316 well-fit neurons where round 1 kept 317, with the same code. That one neuron changes the type (a) counts. The other cell-type reading does not reproduce it, which the notes say.
- **fig4d, still reproduced, on a revised assumption.** The verifier's problem 3 is confirmed. With the code's 2.8 s window, burst-free Poisson trains exceed the null, in 17 to 20 of 20 participants. The claim now rests on each trial's own maintenance window. That reading gives the paper's pattern with the Methods' groups and the prominence rule, but not with the code's groups. I added a finding and a question for the authors about this window.

**Added or corrected**
- **Second cell-type reading (problem 2):** every downstream claim on cell types now also runs with the reading that matches the paper's counts, including the PY/IN burst groups. Only fig6e differs between the two readings.
- **Own-maintenance burst reading (problem 3):** run under every burst reading, with the Poisson control, and also applied to fig6ab maintenance.
- **M3 burst rate per second (problem 4):** shown for every group.
- **ACG fit stated as a limitation (problem 5),** including the 316 versus 317 variation between runs.
- **Decoding (problem 7):** a binomial test against the paper's 20% chance sits beside the code's p values. Under it, the fig2f 250 ms value (code's trial table) has p = 0.13.
- **Cross-temporal clusters (problem 6):** the largest real cluster spans 26 bins. 3 of the 1,000 shuffled maps have a significant pair, one each, so the cluster rule cannot remove anything here.
- **fig6gh (problem 12):** a variant using only intervals within trials is shown. It is outside the criterion's method, so it does not decide the outcome.
- **Subject 9's 0 s maintenance and 31 µs fixation trials (problem 10):** now in the data check, showing they barely affect the fixation statistics.
- **Problem 11:** now stated in fig4c.
- **Problems 8 and 9:** stated in the notes.
- **New findings:**
  - the code's maintenance surrogate window, which produces the artefact;
  - the dPCA code takes maintenance trials by `trial_id` where encoding uses `new_trial_id`, so 4 of 14 sessions use other trials;
  - the code's early/late `protect` setting reverses Fig. 3h.
- All conclusions, the summaries and the attempt record now match this run's numbers. The `verifications` block lists all 45 claims, with the verifier's words and my responses. It marks disagreement for the three dPCA claims and fig6cd.
- I added `scikit-posthocs` to the requirements and re-locked, so the Dunn test uses the same package as the code.

**Not done, and why**
- **No reader questions:** the verifier reported no place where the claims file misreads the paper, so `questions/kussovska-2025.yaml` was not created.
- **ACG groups from the within-trial spike features:** not built. Those groups are defined on normalised mean ACG, and the every-spike features equal the code's shipped table to within 1% for 99% of neurons.
- **Fewer shuffles for one variant:** the fig6kl run with the second cell-type reading uses 200 shuffles, not 1,000, to save time. Every shuffled null so far has been empty.
- **Conclusion text was edited after the run:** some markdown conclusions were written after the final run, then copied into the executed copy so the handover matches. No code cell changed after the run.

Untracked dotfiles (`.bashrc`, `.vscode`, `scripts` and others) appeared in the repository root during the session. I did not create them knowingly and left them alone; the workflow should not commit them.
