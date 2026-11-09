I've worked through all eleven points in the verifier's round-1 report, re-run the entry (it passes check and runs clean in 173 s), and recorded the round under `verifications`. Every conclusion matches the final run's numbers. Nothing is committed.

**Outcome changes**
- **fig3e** goes from partially reproduced to not reproduced, as the verifier said. The dCP part is the point of the claim and fails in every reading (ANOVA p = 0.21 to 0.76).
- **fig3fg** goes from blocked (`methods_underspecified`) to partially reproduced, as the verifier said. It holds with the baseline z-score and fails with the session z-score. The notebook no longer picks the session z-score as the main reading. The text now says the third window is stronger than the second, which is the reverse of the paper's legend.
- **fig4c, fig4e, fig4f, fig4h, fig5g, fig5i** become blocked (`data_missing`). The dandiset's 42-label VAME set is not the paper's 37 motifs, and the claims file says only the paper's labels can decide these claims. The analyses stay in the notebook, marked as not deciding.
- **fig5h, both fig5j claims and fig5m** stay blocked, now as `data_missing` to match fig4c, which they depend on.
- **Kept, with the disagreement recorded:**
  - **fig4b-dcp** stays partially reproduced. Anxa1 has the claimed sign in 9 of 10 recordings but p = 0.07 to 0.08.
  - **fig6j** stays partially reproduced. Arch accuracy on day 4 is below the controls' in all eight main readings, but never significantly.
  - **fig1b** stays blocked as `other`, not the verifier's `data_missing`, because the checker does not allow `data_missing` on a claim whose data are in another archive.

The totals are now 4 reproduced, 3 partially reproduced, 3 not reproduced and 28 blocked.

**Added or corrected**
- **Motif label timing (the verifier's problem 2):** this check turned up something real. Kinematics and labels both start at t = 0, and the kinematics line up with the pose. But the labels explain speed best when moved 15 to 21 frames later (median 18, about 0.6 s), so stored motif onsets come early. I recorded this as a new finding. The motif-onset numbers change a lot with the shift, which supports blocking those claims.
- **Start times:** a table per file of where kinematics, labels and photometry start.
- **What each file kind holds:** no nosepoke, reward, end-zone or trial objects anywhere.
- **GEO:** its supplementary files are only the MitoPark counts and RPKM tables, so there are no cMfn2KO counts.
- **Maze pixel scale:** the arena covers the same pixel range every day, so the scale is stable.
- **figs2 baseline:** the trace is flat before each train, so the previous train does not raise the 2 s baseline.
- **Mouse 687662 (conflicting genotype):** fig3d still fails without it; fig4b's Anxa1 result weakens to p = 0.21.
- **fig6j:** the Arch day-1 laser label is now stated as a departure from the paper's protocol.
- **Text fixes:**
  - The edgeR docstring now says it is not edgeR's default route.
  - The fig3d notes wrongly said neither part ever held.
  - The README's blocked count was 16 where it should be 15.
  - The README and `entry.yaml` now match the new outcomes.

**Not done**
- I did not check event times against the reaching videos. They are external mp4 files, the environment has no video decoder, and judging a touch means looking at the frames.
- I did not add smoothing to the maze speeds. The claims file leaves smoothing open and gives no reading, so the notes say the not-reproduced outcome rests on noisy, unsmoothed speeds.
- The post hoc tests still use separate t-tests instead of Prism's pooled error term; this stays stated as a deviation.
- The preferred limb is still taken over all of a mouse's sessions. That is the claims file's reading (i) as written, and the per-session reading is also run.
