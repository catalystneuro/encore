I've worked through every point in the round-1 report. No outcome changed: fig1d-sessions-blocks and fig1ef-reward-rate are still reproduced, and the other 31 claims are still blocked as too_large. The verifier agreed with all 33 outcomes. The entry re-ran cleanly with `python tools/entry.py all` (328 s, check 0 errors), and the conclusions match the new numbers.

**What I added, as the report asked:**
- **Per-session table** (data check): log header, forage-assist lines, blocks, rewards per block, and arms entered in the log and in the DIO beam breaks.
  - **The 9- and 3-reward blocks (problem 1):** both follow a closing trial that was a rewarded visit to the new goal. The closing-trial rule keeps that reward in the old block, so the new block shows one reward fewer than the number printed (10 and 4). The text that said only programmed values occur is corrected.
  - **Forage assist (problem 2):** no log names more than one arm in a `CURRENTGOAL` line, the five logs without a header included, so no epoch uses forage assist.
  - **jaq day 6 epoch 4 (problem 3):** the DIO confirms arm 6 was never entered, including after the last logged trial. It is the only jaq session with fewer than eight arms, in the log and in the DIO.
  - **Extra sessions (problem 4):** which jaq and despereaux epoch the paper didn't count still can't be identified. I list the likely ones and show that leaving out any one more epoch keeps all counts within tolerance (jaq 82 to 87 blocks, despereaux 100 to 108).
- **Trial counts against the figure legends:** search and correct repeat trials are within 5% and 4% of the legends. Error trials are 11 to 24% more than Figure 5B's, so the error labelling or its selection is not the paper's. Only blocked replay claims use it.
- **fig1ef-reward-rate:** printed the per-trial p, S.E.M. and n for trials 1 to 15, and added the plain reading of "rises" (trial 15 above trial 1), which holds in every subject. The conclusion now says jaq and roquefort start below chance, and that my own test of "rises" is stricter than the criterion (problem 6).
- **fig6b-visits-decay (problems 7 and the table):** I computed the behavioural half; the claim stays blocked because the replay half can't be tested.
  - It holds in jaq, despereaux and montague (last significant trial +2 or +3).
  - In roquefort a single late trial, +29, is significant with the tie-corrected rank-sum test (p = 1.6e-4) but not without the tie correction (p = 0.074). So that half holds or fails depending on the form of the test.
  - The claims file only says "Wilcoxon rank-sum test", so I added a question to `questions/000115.yaml`.
- **Arm adjacency (problem 5):** not changed in code, because no test uses the error subtypes. The helper's docstring now says so, and says arms 1 and 8 are not treated as neighbours because the claims file doesn't say which arms are.

**In the attempt record:** I updated the notes for fig1d, fig1ef and fig6b, two findings, and the streaming rate (now 8.4 MB/s), and added `verifications` round 1 with the verifier's reason and my response for all 33 claims.

**Not done:** I didn't commit, as instructed. Some untracked files I didn't create (`.bashrc`, `scripts`, `.idea` and others) are in the repo root; I left them alone.
