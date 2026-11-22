No outcome changed. All 33 claims are still `reproduced`, and the verifier agreed with all of them. The entry was re-run from a clean environment with `python tools/entry.py all entries/du-2026`, and every notebook passed. The values are the same as before, and the checks report 0 errors.

**What I changed in reply to the report**
- **maze-gain:** its outcome is now marked `assumed: true`. A new deviation says the reproduction rule (every value within its tolerance) is borrowed from rtt-gain, because the criterion gives none. `07_mc_maze.ipynb` says the same.
- **maze-gain tolerance:** the tolerance is narrower than the rounding of the paper's printed −0.00004. I added this as a question for a reader in the new file `questions/du-2026.yaml` and left the claim unchanged. Notebook 07 now also prints, for each seed, whether the replacement gain falls within that rounding. Only the paper's seed does.
- **The verifier's doubt about step 1.4:** it could not see the protocol, so the response on maze-gain quotes the step's passage. It says data-elsewhere claims are tested on those data and are never blocked as `data_missing`.
- **02 cell 36 and the nested-replacement-negative notes:** cell 35 now prints, for each seed, whether each SBP value is within tolerance. Both are outside at +1000, history only at +2000, geometry only at +3000, and neither at +4000. The text now says exactly this.
- **Velocity finding and the 02 summary:** "exactly" and "1.000 in all 18" are gone. They now say 17 sessions give 1.000 and 2021-10-15 CO gives 0.987.
- **README and 05 summary:** the seed-sensitivity sentences now match the outputs. Most confirmation values fall outside under other seeds, but not all. For MC_Maze, the replacement gain and the lowest map gain fall outside under every other seed, and the main gain under one.
- **Finding about the paper:** it now names the four exceptions the verifier listed, where the paper's values are not matched at printed precision.
- **Solver comparison (estimator-family-link):** I added an option to choose the solver in `du2026.py`. Notebook 03 now runs the paper's solver (lsqr) and the faster one this attempt uses (Cholesky) on one session. They pick the same penalties and give gains of 0.0261224 and 0.0261222. I removed the earlier figures that had no printed output: 0.0261219, the 58 min run time, and the claim that a full lsqr run gave the same signs.
- **07 data check:** notebook 07 now prints the count of missing values in the analysis arrays, which is 0, and its summary says so.
- **Round 2 record:** written under `verifications`, with the verifier's reasons and my response for each of the 33 claims. No finding is rated `critical`, so there is nothing under the round's `findings`.

**What I did not do**
- **Full lsqr run:** I tried lsqr on all 18 sessions, but it went over the one-hour cell limit and cost about two hours of the run. So only the one-session comparison is in the notebook, and the record says the other sessions were not run under lsqr.
- **Other analyses the verifier noted as open:** reading (b) of the nonlinear context in estimator-family-link is still not run (about 9 h). The block, nonlinear-context and `decoders_nested` ports are still not compared against the paper's own code. The verifier said neither bears on a conclusion.
- **Stray files:** the repo root has untracked files such as `.bashrc`, `.mcp.json` and `scripts`. They are not real files: the sandbox put them there before this run started, and I left them alone.

Nothing was committed, as instructed.
