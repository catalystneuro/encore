I've finished the round-2 revision. The final run from a clean environment passed in 21 minutes, `entry.py check` reports 0 errors, and every number cited in the conclusions is in the final executed copy.

**Outcomes.** None changed and nothing is proposed. The verifier agreed with all 47 outcomes, and I recorded round 2 under `verifications` with its reasons and my responses.

**Outputs the verifier asked for, now printed in the notebook:**
- **fig3d slow-oscillation coupling:** the deep peak frequency (`f_deep`) is now printed. It does not back the sentence the verifier questioned, so I removed it:
  - The deep sites peak above 100 Hz in only 5 of 18 mice (6 with the 0.5-3 Hz phase).
  - Over 5-200 Hz their median peak is 71 Hz, the same as the superficial peak.
  - The notes now say the deep part of the claim does not hold as stated. I kept partially reproduced: the criterion already fails on the index values and passes only on the superficial frequency.
- **fig2b six clusters:** each boundary ranges by 31 to 40 sites across mice (620 to 800 µm). The conclusion, notes, Summary and README now give this range and say the passing reading can hardly fail. The verifier called this a flaw in the claims-file criterion, so I added it as a question for a reader in the new `questions/000166.yaml`. The claim is unchanged.
- **Deepest IC counted twice:** this IC peaks at the deepest site and counts both as volume conducted and as main IC 6. It is spread over depth in 9 of 18 mice.
  - With the six ICs that stay confined in depth, fig2d still fails: the superficial mean is 0.086, outside 0.14 ± 0.04, although the superficial ICs are larger (p = 0.0089).
  - fig5b's silhouette favours 2 clusters on both feature readings, never 8.
  - fig2c's confined reading already fails for ICs 4-6.
  - The notes of fig2c, ica-volume-conduction-fraction, fig2d and fig5b now state this.

**Text corrections against the outputs:**
- **slow-gamma-superficial-wake:** now reports the −7.06 result, which goes against "superficial dominance". The criterion tests only the state order, so the outcome stands.
- **fig7 within-layer fractions:** all three fractions are outside tolerance, not two.
- **fig2b across states:** the boundaries differ by at most 3.2 sites, not 3.
- **figs2c:** three of the four tests give p < 0.01; one gives p = 0.01.
- **fig8eh:** the wording is now exact. One unlabelled cell (YMV10 unit 36, 0.74) lies below a labelled one (YMV15 unit 33, 0.77).
- **fig8cd:** the notes now say the mean rebound comes mostly from three cells the dataset labels "down state".
- **Labels:** "(assumed)" added to fig2d in the Summary and to the layer 4 row of the README.

**Not done:**
- No new analysis beyond the outputs above, since none was needed to answer the report.
- `tools/runner/chain.sh` was already modified before this run, and I left it alone.
- Nothing is committed.
