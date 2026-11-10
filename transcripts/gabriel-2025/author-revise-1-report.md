I went through every point in the round-1 report, re-ran the entry with `python tools/entry.py all entries/gabriel-2025` (0 errors, notebook passed in 35 min), and recorded the round under `verifications`. Nothing is committed.

## What changed in the outcomes

| Claim | Before | Now | Why |
|---|---|---|---|
| fig1g-freezing | reproduced | blocked (methods underspecified) | I agree with the verifier: the two Sidak families give different results on the clock windows, and the paper doesn't say which it used. |
| fig1h-latency | reproduced (assumed) | blocked (methods underspecified) | Same reason. |
| fig1r-mixed-exit-day1 | reproduced (assumed M2) | partially reproduced (assumed M2) | Day 1 is significant only in the main run. With three other shuffle seeds p = 0.10 to 0.15, and with the paper's tone bouts p = 0.106. |
| fig2-day2-tone-further | reproduced (assumed H1) | partially reproduced (assumed H1) | Exits hold in every run. Entries hold only in the main run (other seeds p = 0.11 to 0.58). |
| data-registered-cells, both fig1o claims | blocked (data missing) | blocked (not runnable) | The minian files do hold the cell outlines (footprints) a registration would start from. Redoing it needs CellReg, which is MATLAB. |
| fig4b-hybrid-model-best | reproduced | reproduced, now marked as resting on the clock tone windows | With the paper's tone bouts, the two T1 readings fail (GG p = 0.097 and 0.11). |

Where I kept my outcome over the verifier's, the disagreement is recorded with the reason:
- **fig3a (two claims) and fig3b:** I kept the Methods' coding (success as the positive class, min-max F1), because protocol reader step 2 puts the Methods before the code when they disagree. On the clock windows, fig3a holds in all three cohorts tried.
- **fig1r and fig2-day2:** I kept the assumed readings M2 and H1.
- **The 13 CILDS claims and figs2:** they stay blocked as `not_runnable`, not as "other: not run". No Python CILDS exists (pip finds none), and writing one would substitute a different model.

## What I added

- **Data check:**
  - Every Behavior.mat field and minian variable is now printed. Behavior.mat has no jumping, rearing or escape fields, and Params.mat holds only the freezing classifier's settings.
  - The hand-scored `avoids` is printed beside the code's rule. They agree on 228 of 252 trials, so 1 means success.
  - A new check shows calcium and camera share a clock in all 30 sessions: calcium follows the freezing labels by 0.9 to 3.8 s.
- **Paper tone bouts:** every ROC, Figure 2, Figure 3 (all cells), RW and figs3gh result is now also shown on the paper's tone bouts.
- **Shuffle seeds:** the whole-session ROC is re-run with three more seeds, and the mean-activity and Figure 2 tests are repeated on each. Several results sit right at p = 0.05.
- **Event-call counts:** I tried other event windows, platform bouts cleaned of brief flickers, and other seeds. None brings the tone-onset or platform-event counts up to the paper's. This is recorded as a finding.
- **Decoding cohorts:** three cohorts are run: all 9 shocked mice, the 7 shocked mice without F1 and F2 (the two with no day 2 recording), and the mice whose training folds hold both outcomes.
- **Rescorla-Wagner update:** the Methods' version of the update (using the current trial's outcome) is run as a variant, plus fits from four extra start points. The hybrid model is still lowest, but only just below avoid-only.
- **Questions file:** `questions/gabriel-2025.yaml` asks a reader whether the claims file misreads the update as using the next trial's outcome.
- **New finding:** a question for the authors about the Sidak family. The notes for problems 6, 7, 9 and 10 are added as deviations.

## What I did not do

- **Modulated and non-modulated cell sets on the paper's tone bouts:** not decoded, to stay within time. Only all cells were run on that reading.
- **Escape part of figs2:** not run.
- **Notebook text not re-executed:** I edited the conclusion and summary text after the run and copied it into the executed copy. The code cells there are identical to the source, so I did not run the 35 minutes again.
