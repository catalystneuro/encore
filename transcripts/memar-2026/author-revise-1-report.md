## Round 1 revision of memar-2026-01

No outcome changed. The verifier agreed with all 20, and the re-run gives the same outcomes: 7 reproduced, 1 partially reproduced, 3 not reproduced, and 9 EEG claims blocked. `entry.py check` reports 0 errors. Five outcomes are now marked `assumed`, because they rest on a reading I could not run or on one preprocessing reading: cross-ieeg-mean, cross-below-intra-ieeg, table2-ieeg-cross-subjects, fig5a-coverage-ieeg and surrogate-order-ieeg.

**What I fixed or added**
- **Event times (problem 5).** This was a real error in the first run. In sub-01 ses-7, sub-04 ses-3 and sub-06 ses-3, every time in the `reaches` table is later than its `ReachEvents` time by exactly the gap between 19:00 of the previous day and the session start (8.1 to 8.5 h). A high-gamma check at both sets of times shows that `ReachEvents` is the one on the recording's clock: sub-06 gives |t| 9.28 at `ReachEvents` times against 2.90 at `reaches` times. All trials are now built from `ReachEvents` (7957 trials), and I raised finding 1 to `critical`, which the round-2 verifier will review.
- **Preprocessing reading (b) (problem 2)**, now run for:
  - cross-subject: 0.315 to 0.318, outside the tolerance, so cross-ieeg-mean now rests on reading (a);
  - coverage: Local 0.569 against Non-local 0.571, still failing;
  - surrogates: IAAFT is still lowest;
  - the two ends of the mask sweep, and the full-mask claim.
- **End-matched phase surrogates (problem 3).** One 900-sample segment per series, as the verifier proposed. The phase average drops from 0.202 to 0.196, still above IAAFT (0.184), so surrogate-order-ieeg stays not reproduced.
- **Speed check (problem 4)** now covers the lagged, Local and surrogate fits on sub-07: running to 1000 epochs changes each score by at most 0.0002. The median best epoch is printed for every model.
- **Other outputs the verifier asked for:**
  - `starting_time` of every file (all 0);
  - counts of the epoch labels per subject;
  - trial overlap (no two trial windows overlap);
  - SD across electrodes for intra and cross, discussed against Table II;
  - the iEEG half of the two blocked EEG comparisons: cross/intra ratio 0.58 to 0.59, difference about 0.25.
- **Speed and memory.** Each subject is now fitted in its own process with one linear-algebra thread, and memory is released before the processes are started.
- **Record.** Round 1 is recorded under `verifications`. The verifier found no misreading of the paper, so I added no question for a reader.

**What I did not do, and why**
- **Movement plus rest trials (event reading b), not run.** Neither the paper nor its code defines a rest trial, and the dataset only labels coarse behaviour such as "Sleep/rest" or "TV", so any rule for picking rest trials would be invented. The outcomes that need this reading to fail are the ones marked `assumed`.
- **Cut for time** after a run was lost:
  - the round-rule variant;
  - the middle steps of the mask sweep under reading (b);
  - the lagged model under reading (b);
  - end-matched surrogates under reading (b).
- **EEG block reason kept as `not_runnable`**, not the verifier's `data_missing`. The claims file marks these claims as data held elsewhere (BNCI Horizon 2020), and the protocol does not allow `data_missing` for those. The disagreement is recorded under `response`.
- **No run stamp.** Two runs were lost:
  - a detached `entry.py all` was killed when its tool call ended (the sandbox kills child processes);
  - the first full run of the main notebook lost a parallel worker (probably out of memory) and stopped.

  The whole entry also takes longer than one tool call allows. So I ran the three notebooks one at a time with `entry.py`'s own nbconvert command and environment: 45, 37 and 50 minutes, peak memory 8.7 GB. I then wrote the conclusions and summaries into both the notebooks and the executed copies, changing no code or outputs. The next `entry.py run` will execute everything again, and `executed/memar-2026/result.json` still holds the round 1 timings.
- **Untracked dotfiles** (`.bashrc`, `.idea` and others) at the repository root are not mine. I left them alone, and they should not be committed.
