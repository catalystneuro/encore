I've revised the attempt for verifier round 1. The entry re-runs cleanly: `tools/entry.py all` reports 0 errors and the notebook passes in 305 s, up from 40 s because of the bootstrap redraws. Nothing is committed.

**Outcome changes**

One outcome changed: fig6f-k6-ppe-then-valence goes from reproduced to partially reproduced. The verifier flagged its omission CI as sitting at zero (lower bound -0.000). Over 20 redraws that CI includes zero, as the paper's does, in only 2 of 20 draws (4 of 20 with MATLAB's nested standard errors). Judged by the sign most draws give, 6 of 7 CIs agree, and the claim's partial condition holds.

The verifier agreed with all 30 outcomes, and every other outcome is unchanged. Totals are now 24 reproduced, 5 partially reproduced, 1 not reproduced, 0 blocked.

**Added or corrected**

- **Bootstrap (problem 4):**
  - MATLAB's documentation confirms the verifier: called as in the paper's code, `bootci` estimates the standard error from 100 nested bootstrap samples, not a jackknife. I corrected the helper's docstring and added the nested version as an option.
  - A new notebook section redraws all 121 CIs the criteria judge, over 20 seeds and with both standard-error methods. Each CI is now judged by the sign most draws give, and both methods give the same majority sign for every CI.
  - Only fig6f changes. fig6b's omission CI excludes zero in 19 of 20 draws, so it stays partial. fig3d's borderline k8 CI includes zero, as the paper's does, in 11 of 20 draws, so it stays reproduced.
- **The paper's code (verifier section C, problems 2, 5 and 7):** a new cell prints the cited code lines from `data.zip`, covering the normalization, the k-means matrix, run and elbow measure, the cluster map, the tuning columns including k5's bins 8 to 12, the bootstrap call, and the post-shock windows and axis of the Figure 6 traces.
- **Elbow (problem 5):** I added best-of-10 and mean-of-10 runs that follow MATLAB's random stream. 30 of 45 readings now meet the criterion. The claims file's own readings disagree with each other (z-b passes 3 of 4 with the MATLAB stream, z-a 0 of 4), so the outcome rests on the code's runs, as it already did.
- **K-means clusters (problem 6):** I ran every reading (outcome start 12, 12.5 or 13 s; three normalizations; single run or best of 10). Only the code's own combination gives the paper's sizes; no other reading gets more than 4 of 8 cluster sizes within 10%.
- **Table S3 (problem 3):**
  - The units to drop cannot be identified. Four different k3 units reproduce Table S3's F when removed, and removing any of 10 of the 18 k3 units makes the k3 interaction non-significant.
  - Table S3's partial eta squared fits 17 k3 units better than 18, which weakly suggests one k3 unit was left out.
  - Re-running the pooled ANOVA on 362 units gives F(1, 355) = 28.72 and F(13, 4615) = 4.34, against the paper's 28.57 and 4.13: close, not equal.
  - The outcome stays partial, because the claims file asks for all units.
- **Reader questions:** I created `questions/crcns-rrf-1.yaml` with two questions:
  - Problem 1: whether the k1, k3, k5 and k6 windows should follow Table S4 (0 to 4 s) or the gray boxes (0 to 8 s).
  - Problem 8: whether k4 should count in part (2) of fig4abc, since the paper describes k4 as inhibited equally to danger and uncertainty.

  While preparing, I rendered the Figure 6 page: the boxes end at the 8-s tick, and the code puts 0 s at shock offset. So the claims file reads the figure as drawn, and the conflict is between the figure and Table S4.
- **Record:** I added the round-1 verification block (verifier's reasons in its words plus my response for each of the 30 claims). I also updated the affected notes, deviations and two findings, the conclusions, the summary, the README, and the runtime in `entry.yaml` (5 minutes).

**Not done**

- No claim was changed, as instructed.
- Problem 1 does not change fig6a's outcome; it waits on the reader's answer.
- MATLAB's `'Replicates'` option is emulated by continuing one random stream. That is an assumption, stated in the helper and the notes, because the paper's code never uses replicates.
