# Verifier report, round 3: Valero et al. 2022 (doi:10.1126/science.abm1891) on DANDI 000568 v0.230705.1633

The claims file has 22 claims and the attempt record has 22 outcomes. Only one outcome has a `proposed` change: fig3g-spatial-information, from reproduced to partially_reproduced. I agree with it. I downloaded no new paper text this round; the text saved in round 2 is still under `paper/`.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig3g-spatial-information | partially_reproduced | Yes | | See below. |

**How I checked fig3g**

1. **The numbers come from the data.** Cell 59 prints every number in the reason:
   - Time-matched control, place fields: n = 70, rho = 0.501, p = 1e-05, median increase -0.10 bits/spike.
   - Time-matched control, unmasked fields: n = 14, rho = 0.609, p = 0.021, median increase -0.17 bits/spike.
   - Kruskal-Wallis on the increase, unmasked against place: p = 0.3.
   - The two rho values are Spearman correlations of the matched-control SI with the light SI, as the criterion asks.

2. **The choice was not made to get this result.**
   - The time-matched control is built in cell 51, with a fixed seed (30). For each cell it draws as many 20 ms control windows as the cell has light windows during laps. Cell 51 prints a matched-to-light time ratio of 1.0.
   - It was added in round 2 as a variant for fig3f and fig3g, before this proposal, and it is not tuned for fig3g.
   - It is the fairest comparison for spatial information. Skaggs SI is biased upward when a map has little time and few spikes. The main dark-window control has about 19 to 20% of lap time, while the light maps have about 11 to 12% (cell 35, round 2). So the main analysis favours light SI, and most of all for the sparse unmasked maps.
   - The matched variant also fits the paper's own statement best: "random intervals (20 ms) between the light pulses served as control epochs" (Results).
   - The reason is also right that the dark-window control already replaces the criterion's "time when no uLED is on". So it has no prior standing to decide the outcome.

3. **The criterion is applied as written.**
   - Part 1 (positive Spearman correlation at p < 0.05 in both groups) holds under both the dark-window control (cell 59: 0.655, p = 7.6e-10; 0.574, p = 0.032) and the matched control.
   - Part 2 (larger increase for unmasked than for place fields, Kruskal-Wallis p < 0.05) fails under the matched control: both medians are negative and p = 0.3.
   - Under the main control, part 2 rests on p = 0.039. The selection of unmasked fields (a light field and no control field) also favours it.
   - Under the criterion, only one part holding gives partially_reproduced.

**One minor wording point, which does not affect the outcome**

- The record's fig3g notes list the matched increases as "-0.17 and -0.10" without saying which group each belongs to.
- The proposed reason gives them in the other order, "-0.10 and -0.17", also unlabelled.
- Cell 59 gives place -0.10 and unmasked -0.17, and cell 60 labels them correctly. The record should label them the same way.
