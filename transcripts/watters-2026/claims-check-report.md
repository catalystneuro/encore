I checked the claims file and made seven corrections. It is ready for an attempt.

**Checker result (after my edits):** `26 claims, 26 quotes, 16 statistical values, 0 problems`

I read the whole paper and the linked code at the commit the file cites. The code agreed with the file on everything I spot-checked:
- **Model comparison test:** the significance brackets come from a two-sample t-test over session-by-split values, and the code draws them at p < 0.01.
- **The 100-unit cut:** it counts the units that entered the models, written as "> 100". No session has exactly 100, so ≥ and > give the same result.
- **Printed numbers:** 22 of 24 sessions with Gain best, 4,688 units, and the behavioural performance values.
- **Other details:** 5,000 bootstrap resamples for the AUC p-value, and seeds 3 to 7 for the synthetic-data check.

None of the claims comes from the other paper in `paper/`. Each main finding has a claim.

**Changes, by claim:**
- **fig1c-reaction-times:** added a second reading with Triangle and Ring trials pooled, because the Fig. 1 legend says panel c includes both. Trials under 180 ms are now left out, as the legend says. The pass thresholds are now marked as the agent's own choice.
- **ext1-misbinding-errors:** when the two readings disagree, the claim is now `methods_underspecified`, as the protocol requires. Before, it was judged on whichever readings agreed.
- **ext2-stimulus-delay-activity:** added a third reading: more than half the units are also above 1 Hz in the stimulus phase. A correlation of rates across units does not by itself show that units are active in both phases. I also noted that the second half of the statement comes from the panel b legend title, and set the rule for disagreeing readings.
- **ext3c-decoder-orthogonality:** the file fitted the Ring data on the three Triangle sessions. It now uses three Ring sessions, as the legend implies (the code uses Perle 2022-06-09, 06-10 and 06-11). I also set the rule for disagreeing readings.
- **ext11-kappa-tuning:** the old rule ignored the "consistent across models" test whenever it failed. Failing that test now gives "partially reproduced". I also named which unit count is used for the link between unit count and kappa.
- **fig5ab-ring-behavior:** the source now notes that the Results cite "Extended Data Fig. 8a–b", but the per-monkey Ring figure is the ninth Extended Data legend.
- **fig5h-gain-rt-ring:** the code leaves the trial itself out of the neighbourhood mean, while the Methods say "all trials". The Methods' version is now run as a variant.

**Still open:**
- **fig4a-gain-best-triangle and fig5f-gain-best-ring:** the recorded p < 0.05 for Gain against each other model rests only on the legend's description of the brackets. There is no PDF of this paper, so I couldn't see which pairs actually carry a bracket.
- **ext8-slot-switching-behavior:** the panel a statistics are garbled in the text. Also, the paper's own Switching-model values for accuracy (R = 0.65 and 0.34) are higher than the Gain model's, so "weaker" can only be judged on reaction time, as the criterion already says.

**Ready:** yes. The `checks` entry records `ready: true`. Nothing was committed.
