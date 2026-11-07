I've made the round-1 revision and re-run the entry: it executes cleanly in about 9 minutes and `tools/entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **table1-bursting-sessions:** not reproduced → partially reproduced, marked as resting on an assumption. With the new main population (below), the main burst reading gives 40/47, 1/6, 7/7, 6/7, 7/8, 3/7 and 0/7. Six of the seven counts equal Table 1's; the only miss is one 3 dB session that bursts where the paper has none.
- **table1-isolated-spikes:** partially reproduced → not reproduced. The verifier gave not reproduced. Only 4 of 7 values are within tolerance, below the five of seven at which the other Table 1 criteria call a result partial.
- The other 24 outcomes stay as the verifier agreed.

**Main changes in reply to the report**
- **Session selection (problem 1):** the notebook now shows the counts per protocol under each exclusion the verifier named. Leaving out sessions under 98 trials and sessions sorted off-line keeps 89 sessions, 47/6/7/7/8/7/7 per protocol against the paper's 43/6/7/7/8/7/8. It also leaves exactly the paper's seven protocol-5 sessions. I made this "selection (c)" the main population from table1-bursting-sessions onward, recorded as an assumption, and the first round's 115 sessions are shown beside it. The paper gives no basis for leaving out the off-line sorted sessions; I put that question to the paper's authors in the findings.
- **data-sessions-and-trials and table1-sessions-per-protocol keep their outcomes.** Selection (c) is not one of the criterion's readings, and it was chosen partly from these same counts.
- **Trial blocks and `firing_rates` (problem 10):** spikes after 1.2 s occur only in off-line sorted sessions, at pause-level rates. No block restarts its times or holds twice the usual spike count, so the trial counts stand. The `firing_rates` file matches the trial counts in 136 of 138 files and is not a selection.
- **Latency search (problem 2):** the nBTA maximum is now searched before burst onset as the main reading. The mean latency still falls with n (5.80, 4.23, 3.32, 2.67 ms) and none is negative.
- **Burst minimum (problem 3):** the two-burst minimum is now stated as an assumption, with results for 20 and 50 bursts shown. fig8e still fails at both.
- **σ bias control (problem 4):** a size-matched control and per-n ratios are added. They show sigma-n-below-sta-sigma is not a sample-size effect: 94.3% of sessions pass against the size-matched σ.
- **Burst reading (a) (problem 5):** a new peak reading starts the search after the refractory plateau. It gives 61 of 89 bursting sessions, close to the main reading's 64.
- **Information bias (problem 6):** a baseline with each trial's burst onsets shifted at random gives a larger I_n(1) slope (2.59 bits) than the data (2.22). The rise of I_n(1) with n is therefore estimator bias. The criterion fixes the method, so fig7ab stays partially reproduced, and the notes say this.
- **fig10 counts (problem 8):** the per-session flags for both widths T are printed side by side. The two widths change about 2% of the matches, which never moves the peak position on the 41-point grid, so the counts come out equal.
- **Record and docs:** round 1 is recorded under `verifications`, quoting the verifier's reasons, with a `response` for each claim. Notes, measured values, deviations, findings, README, summary and `entry.yaml` (runtime) are updated.

**Not done**
- **Problems 7 and 9:** no change. The criterion specifies the ANOVA, and fig3 is already marked as resting on the prominence threshold. The texts now say so.
- **Questions file:** I added nothing to `questions/crcns-ia-1.yaml`, because the verifier found no place where the claims file misreads the paper.

Untracked dotfiles (`.bashrc`, `.mcp.json` and others) and a `scripts` folder are at the repo root. I did not create them and left them alone; the workflow's commit should leave them out.
