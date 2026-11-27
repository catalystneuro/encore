The file is ready for an attempt. I made eight changes and three problems remain open.

**Checker:** `claims/jarzebowski-2026.yaml: 30 claims, 30 quotes, 45 statistical values, 0 problems`. I got the same line before and after my edits.

**Changes, by claim:**
- **fig3a-low-gain-suppresses-errors:** This was a real error. The criterion compared bursts at the default L4 of 60 nS. The Methods set that value to give a single spike, so High gain would not burst there either and the comparison could not show anything. It now compares at the L4 values where High gain does burst, and reads "rarely" as below one half.
- **fig3b-gain-lowers-burst-threshold:** The Results read the omission probability off Figure 3B. So it is open whether that simulation keeps the prediction inputs while L4 varies. Both readings are now named.
- **fig3c-gain-keeps-release-delay:** Added that the legend plots latency against L4 for the Figure 3B simulation, so the release delay is read at L4 = 0.
- **fig2a-weak-sensory-silenced:** The "below 0.1 spikes per run" threshold is now marked as our choice, not the paper's.
- **fig4ef-compensation-restores-latency:** The "at least 20 nS" L5 IT level is now marked as our choice, since the paper gives no range.
- **figs1-post-omission-bursting, figs1-novel-image-bursting:** How the change in burst fraction is measured is open (a plain difference, or the paper's modulation index). Both are now named, as fig6c already does.
- **fig7c-running-leaves-omission-bursting:** Added the recording counts from the legend (35 L2/3 and 94 L5) next to the cell counts. The criterion now says these counts don't decide whether the claim holds.
- **Header note O6:** Added that the Results call the Figure 5C model "linear" while its legend says only "mixed-effects model".

I checked these against the paper and left them as written: all statements, quotes, statistics, expected values and tolerances; the common methods (D1 to D9) against the Methods; and the Figure 5C reading of seven differences per cell (1860 = 266 × 7 − 2). Every main finding in Figures 1 to 7, S1 and S2 has a claim, and none comes from outside the paper.

**Still open (also listed under `checks`):**
- Figures S1 and S2 and their legends are missing from the text. The tests for the five claims on those figures are read from the Methods and may not be the paper's.
- The code repository linked in the paper still returns 404, so no method could be checked against code.
- The printed Figure 5C slopes contradict themselves: the L5 slope has a positive t but a negative interval, and the L2/3 interval's centre is positive while its t is negative. The claims follow the Results text and the intervals; only the authors can settle which is right.

Nothing was committed or pushed.
