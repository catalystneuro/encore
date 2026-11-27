I changed no outcomes. The one disagreement is now a proposal for a third verification round. The entry was re-run with `python tools/entry.py all entries/cambrainha-2025`: the notebook passed in 31 min and the checks show 0 errors. The new numbers match the earlier ones, and the conclusions match the printed outputs.

**The disagreement (figs3-exponents-stable-with-threshold)**
- The verified outcome stays not reproduced. I added a `proposed` change to partially_reproduced with its reason. The criterion asks for stability "at every grid point with at least 10 sessions contributing". When no grid point has 10 sessions, that condition holds trivially, so passive and NNI mu cannot fail. Read that way, the grid from 7 fails only for NNI z (0.083 against an SD of 0.058).
- The verdict had also rested on a convention listed only as a deviation: an exponent with no such grid point counted as not shown stable. That convention is now stated as an assumption the outcome rests on.
- A new notebook cell gives the verdict under both conventions at every start that was run. Under the literal reading the starts at 7 and at the 99th percentile give partially reproduced. The 99.9th percentile and CV (b) give reproduced.
- The same cell shows that at most 7 passive and 6 NNI sessions have a mu at any grid point, against 32 active. So mu was in effect not tested in those phases.

**Sentences corrected**
- **Notebook, "How readings decide":** the exponent result does depend on the grid start. That section, the summary and the README now say so, and that figs3 was run only at named starts (7, the 99th and 99.9th percentiles) and on the 4 to 12 grid.
- **The κ_surr_max finding (finding 3) and the "Surrogate reference" cells:** "not windows with few active units" holds only for the active maximum (34.29, 182 units). The all-phase maximum (48.34) comes from a passive dropout window of sub-545994 with 87 active and 84 silent units. The next value (36.50) comes from a window of the same session with 12 active units. With at least 128 active units the all-phase maximum falls to 34.29.
- **fig3c-scaling-hit-rate-higher notes:** under CV (c), κ_surr_max is 34.29 under both O6 readings, not 48.34.
- **figs2-strict-units notes:** the seed verdicts are those of the fig3c sub-test. The claim itself is not reproduced under every reading, because no session count is within tolerance.

**Recorded**
- Round 2 is under `verifications`: all 18 claims (17 agreed, figs3 not, with the verifier giving partially_reproduced), each with the verifier's reason and my response.
- No finding is rated `critical`. The round's `findings` still record that the verifier agreed with the ratings of findings 1 (major), 6 to 8 (minor) and 9 (none). No severity changed, and the findings keep their order.

**Not done, and why**
- **Questions file:** I added no question. The only claims-file point the verifier raised, whether aborted trials count (O5), is already in `questions/cambrainha-2025.yaml`.
- **Session selection:** the analysis still runs on 97 sessions from 68 mice, not the paper's 62 from 44. That cannot be resolved from the files, and it stays a finding.
- **Figures:** the verifier said it has still not compared the results with Figures 3A, 3C, 4A and S8. That is its own pending check, and it asked me for no output.
- **Stray files:** some untracked files appeared in the repo root during the run (`.bashrc`, `.profile`, `.vscode` and others). I did not create them on purpose and left them alone. They should probably not go into the workflow's commit.

Nothing was committed or pushed.
