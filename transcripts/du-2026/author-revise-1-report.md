I've answered the round-1 report. Two outcomes changed: maze-gain and rff-maze went from blocked to reproduced, marked seed sensitive. All 31 other outcomes are unchanged, and the verifier agreed with them. The final run passed for all seven notebooks, `check` reports 0 errors, and every conclusion matches the new numbers. Nothing is committed.

**Outcome changes**
- The verifier agreed with blocking maze-gain and rff-maze, but gave the reason as data missing. The protocol (author step 1.4) says a claim whose data are elsewhere must be tested on the archive that holds them, never blocked as data missing. DANDI:000139 is public, so I ported the release's `mc_maze.py` into a new notebook, `07_mc_maze.ipynb`.
- **maze-gain:** with estimator seed 20260726, all four values are within tolerance: context R2 0.90533, gain 0.000513, MSE reduction 0.542%, replacement gain -0.0000371. The interval (0.00026 to 0.00076) and the RMSE (81.76 to 81.53) equal the paper's. With seeds +1000 to +4000, the replacement gain falls outside its tolerance under all four, and the gain under one of them (-0.000138).
- **rff-maze:** the three map gains are 0.0000448, 0.0000772 and 0.0001386, so the lowest and highest are within tolerance. With the other estimator seeds, the lowest falls outside its tolerance under each.

**Added or corrected, per the report**
- **Port against the release code:** `07_mc_maze.ipynb` fetches the release's estimator modules at commit b042fbe and runs them on the same arrays as the ports, on MC_Maze and on one LINK session (2021-10-15 CO). Every value is identical.
- **MC_Maze half of estimator-family-nlb:** now reported. Block-penalty gain is 0.000455 and nonlinear-context gain -0.000243, both below 0.01 in absolute size. The outcome still rests on MC_RTT, as the criterion says.
- **rtt-gain:** the release's conditional interval is now computed (500 resamples, the script's default) and equals the paper's, 0.05371 to 0.08478.
- **Problem 1 (representative-trial):** reading (c) is now the position in trial order among the held-out trials, 41 counting from 0. The old value was an index into the shuffled split order. Readings (a) and (b) still give 123.
- **Problem 2:** the context feature counts in notebook 04 are now computed from the data: 141, 351, 151 and 361.
- **confirm-replacement:** the notebook now prints, for each of the five seeds, how many sessions have gain above replacement: 20, 20, 19, 20 and 20. The summary had said "every session" under all seeds; I corrected that to "19 or 20 of 20".
- **Later 001201 versions:** a new cell shows both later versions list the same 312 paths with the same sizes as the pinned one.
- **Attempt record:** I added the round-1 `verifications` block, the two new inputs (DANDI:000139 and the release modules), and updated findings for MC_Maze units and seed dependence.

**Not changed, and why**
- **Problem 3 (solver):** kept, since it was already stated as a deviation.
- **Problem 4 (seed dependence):** already recorded with `seed_sensitive`.
- **Problems 5 and 6:** no change needed.
- **Nonlinear-context reading (b) of estimator-family-link:** still not run. I estimated about 9 hours, and the criterion needs only one reading.
- **Questions file:** the verifier reported no misreading of the paper by the claims file, so I added nothing to `questions/du-2026.yaml`.

**Registry listing:** DANDI:000139 holds data this paper analysed, but the registry does not list the paper on it. That is how the claims file has it, so I kept it as data elsewhere and did not add it to the record's `datasets` (it is under `inputs`). It is a dataset this paper reuses, not one the authors deposited, so whether to list it is the registry's call.
