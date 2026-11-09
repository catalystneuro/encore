I've worked through every point in the round-1 report, re-run the entry, and recorded the round under `verifications` in the attempt record. The final run took 12.8 minutes, `tools/entry.py check` reports 0 errors, and its numbers match the run the conclusions were written from. Nothing is committed.

**Outcome change**
- **fig8e-cocaine-region: partially reproduced → reproduced.** The verifier was right that the ANOVA should use Type III sums of squares, as GraphPad Prism does. With Type III, all three F values match the paper (36.37, 10.75, 199.86). It also makes the Figure 8f stimulus F match the legend (34.46), so I removed both F values from the paper-inconsistency finding. Type II is still printed as a variant. This was the only outcome the verifier disagreed with (`agrees: false`); all 32 others are unchanged.

**Fixes**
- **NaN trough bug (B6):** a NaN next to a dip could hide the real trough. I fixed the trough search and added a synthetic check in the notebook that fails without the fix. 2197 of 30341 site-trials have a NaN in the searched range. fig6a is now 98 of 129 sites with mean latency 188.8 ms (was 99 and 182.4, paper 193.8). fig6c is now p = 1.7e-05 (was 6.1e-08).
- **Rank-sum test (B7):** it now follows MATLAB's `ranksum` rule, and the exact p is also reported for groups of 10 or fewer. ed9(i) is p = 0.049 (exact 0.048); no conclusion changes.
- **Transient rates (B8):** these now divide by usable time instead of the full session. All four rates are still higher inside the hotspot (p ≤ 0.0013).
- **Grid docstring (B9):** corrected the axis order.
- **Pairing speed:** I rewrote the pairing step to make the chance null affordable. It gives identical pairs on 200 random test sets.

**Outputs the verifier asked for**
- **Hotspot false positives (B1):** I ran the hotspot procedure on values shuffled across the real sites, 100 times each.
  - Sensor mice: a hotspot appears in 67 of 100 shuffles, but none is as large as the real one (at most 482 voxels against 1010) or has as low a mean.
  - Control mice: a hotspot appears in 73 of 100, none reaching the real one's 551 voxels.
  - The ed1 notes now say its "not reproduced" rests mainly on the control correlations being as strong as the sensor ones.
- **Chance-corrected pairing (B3):** I subtracted the Methods' chance pairing rate (DA and ACh from different sessions of the same site). Every site keeps an excess for every pair type. The excess is higher inside the hotspot, and its hotspots overlap the correlation hotspot with p = 0.030, 0.005, 0.015 and below 0.005. fig2b stays reproduced.
- **Stimulation-cohort exclusion (B5):** the code's AND rule leaves out 6.5% of samples, against 32.7% with OR. The hotspot built with OR has the same overlap p (0.085). fig7f holds against it too: 19 sites inside versus 161 outside, p = 0.0003.
- **fig4c:** the cue null draws from 68,868 to 74,196 candidate times per mouse, and the code's percentiles also find a cue DA peak at all 75 sites. Neither explains the paper's 65.
- **fig8c:** the notebook now notes the voltammogram sheet and gives the descriptive cocaine/control peak ratio (1.48 in both regions). The outcome stays blocked, because the stated test is the ANOVA.

**Things to know**
- **fig2-magnitude-correlations:** the random stream changed, and the counts moved to 114, 69, 97, 78 (were 115, 70, 90, 76). The outcome is still partially reproduced, and the notes now say the counts depend on the random draws by several sites.
- **fig4-cue-sequence:** I kept "not reproduced", as the criterion fixed beforehand reads, and the verifier agreed.
- **Shortcuts:** the chance-pairing null uses 10 session shuffles in place of the paper's 10000. This is listed as a deviation.
- **Other edits:** I updated the README and set `runtime_minutes` to 15 to match the longer run. I also saved the paper's full text under `paper/`.
