I've revised the attempt for every point in the round-1 report. The entry passes its checks and the full run passes (`python tools/entry.py all`, 0 errors, 10.5 min). Every conclusion matches the final outputs. Nothing is committed.

**Outcome changes**

| Claim | Before | Now | Why |
|---|---|---|---|
| fig3c | partially reproduced | not reproduced | The criterion needs all three parts and has no partial clause. The Fmr1 alternation median at 100% is 0.369, below 0.5. |
| fig3e | blocked | not reproduced | Reading o2 shows no 50% effect under either ANOVA reading, and the criterion needs every reading. |
| fig4eg | partially reproduced | not reproduced | The 50% genotype effect is not significant under any reading (p 0.29 to 0.45). |
| fig7b | partially reproduced | not reproduced | The "no difference at 100%" part fails, and the criterion has no partial clause. |
| fig2b | blocked, data missing | blocked, metadata insufficient | A new cell reads all 646 unanalysed files. None is labelled as sensory-deprived, and some later 50% sessions score very low (as low as 0.0). |
| fig4b, fig4c | not reproduced | blocked, methods underspecified | See the lag outlier point below. |
| fig8b, fig8e | not reproduced | blocked (other) | See the follower-trial point below. |
| fig8d | reproduced | blocked (other) | It depends on fig8b in the claims file, so it is blocked for the same reason. The verifier had agreed with reproduced; the reason is recorded. |

fig4d stays reproduced, now marked as resting on an assumption. Its two readings now disagree at 50%. I adopted the poke-based reading: the head positions disagree with the pokes in 6 of 10 pairs, and in the pairs where they agree the position reading matches.

**What I added or corrected**

- **Follower trials (problem 1):** trials are now built as the Methods describe them: the first rat to reach a new well leads, and the other rat's next arrival is its choice.
  - Both this rule and the first round's rule were also run on a null where one rat's visits are shifted in time, so the two rats are independent.
  - The first round's rule produces the reversed effect by itself (0.18 against 0.51 on the null), which confirms the verifier.
  - The Methods rule is biased the other way: every group shows the effect in 10 of 10 rats on the null.
  - So the criterion's test is settled by how trials are built, not by the rats. I added a maximum-likelihood check for fig8e as well.
- **Pixel scale (problem 2):** the camera metadata says 0.0016 m per pixel in every file, but the processed positions of FXM105, FXM107, FXM108 and FXM109 were converted at 0.0025. The 40 px radius is now measured per video (10 cm for those four rats), with the old 6.4 cm shown as a variant; the radius changes no outcome.
- **Position check (new finding):** in 6 of 10 pairs only 39 to 62% of head positions are within 20 cm of the poked well at poke time, against 99.9% or more in the other four. Shifting poke times by up to 30 s does not help. Figure 4 results are also shown for the 189 sessions where position and pokes agree.
- **Lag outlier (problem 3):** one FXM101-FXM110 session has a mean arrival lag of 803 s. With the four sessions that have a lag over 100 s removed, the position-based reading passes in both contingencies. It then disagrees with the poke-based reading, so the criterion blocks fig4b and fig4c.
- **fig1h (problem 5):** I added the table of rebuilt against dataset match counts. I also added a test that uses the dataset's own matches for the observed value. That gives 5 of 5 WT and 4 of 5 Fmr1 pairs, still partially reproduced.
- **Record:** round 1 is recorded under `verifications` for all 35 claims, with the verifier's reasons and my responses. Findings now include the pixel-scale metadata error, the position mismatch and the unlabelled sensory-deprived sessions. The trial-definition question to the authors is rewritten. README, entry.yaml, notebook header and summary are updated.

**Not done**

- I did not run a maximum-likelihood GLMM with Laplace fitting (lme4 or glmmTMB). R is not in the locked environment and statsmodels has no Laplace binomial mixed model. The fig8e logistic check stands in partly; for the gaze claims fig7g and fig7h the verifier said this does not affect the outcome.
- I did not re-check the gaze claims (fig7e to fig7h) on the sessions where position and pokes agree; the fig7e notes say so.
- No question was added to `questions/001845.yaml`: the report names no place where the claims file misreads the paper.
