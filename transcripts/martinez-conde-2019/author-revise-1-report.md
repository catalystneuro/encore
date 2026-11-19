No outcome changed. The verifier agreed with all 19 outcomes, and nothing I found in this round gives a reason to change one. Counts stay at 8 reproduced, 1 partially reproduced, 7 not reproduced and 3 blocked. I re-ran the entry with `tools/entry.py all`: it passed, every number from before came out the same, and `tools/entry.py check` reports 0 errors. Nothing is committed.

**The two points marked as affecting a conclusion**
- **fig7c-fold-edge-equivalence, "within one step of 90%":** both readings now run. Measured from 90, the level nearest S40 (94.3) is out, and the claim is not reproduced. Measured from the level nearest 90 (90.6), it is one level away and the claim would be reproduced. I kept not reproduced and marked it `assumed: true`, with a deviation giving the reasons:
  - it is what the criterion says;
  - under reading (b) both matches are forced, since S40 is 6.66 spikes/s above every Edge level and P180 is 4.50 below every one;
  - against that, the paper calls the 0.943 level "94%" and the 0.684 level "68%", which partly supports the second reading. I say so in the record.

  I added this as a question for a reader in the new `questions/martinez-conde-2019.yaml`.
- **The Square and Edge baseline:** the single 16 DU square that matches the stored `BaseActivity` sits at (15, 129), on black beside the rectangle. Used on all 22 recordings, it still gives a baseline difference (Kruskal-Wallis p = 0.009), leaves S90 out of tolerance (8.21) and gives the same Table 1 counts. The paper's four squares, on only the recordings that store `BaseActivity`, also find a difference (p = 0.025). So the stored values themselves differ; neither the four-square method nor the smaller set of recordings explains it.

**Other fixes and added outputs**
- **Helper bug:** a window lying wholly off the map now comes back empty (synthetic test gives NaN). No number changed.
- **Corners fold direction:** the new luminance profiles showed the Corners fold running from its bright end. The helper now starts it at the dark end. Only the plotted profile changed; the Table 1 and Fig 6 summaries don't depend on the order.
- **New printouts in the data check:**
  - the zip's 155 files by kind;
  - fold lengths (150, 150, 70.7, 150 and 100 DU, as expected);
  - baseline square positions for each condition;
  - a check of the stimulus offset against the Edge (offset 1 puts it within 1 DU);
  - the 12 Star recordings used against the 16 readable ones left out, which don't differ on the overall map (p = 0.98). This is only a rough check.
- **Fig 5:** the number of recordings left out is now computed (1, in Corners).
- **Fig 7a:** a synthetic check shows that a half-black patch always has RMS contrast 1.0. The weak Square and Edge registration check is now discussed in the text.
- **New finding:** inside the region analysed, the Corners stimulus has no 0% area. Its darkest grey level is 1.01, and the Corners baseline squares sit on it.
- **Neuron-counts conclusion:** a garbled, repeated passage is fixed.
- **Record:** the round is logged under `verifications`, with the verifier's reasons and my responses.

**Not done**
- Point 10 is the claims file's note saying it is "not stated" whether S40 uses only the bright fold, when the paper does say so. The verifier called this an internal inconsistency, not a misreading of the paper. I added it as a question for a reader anyway; it can't change an outcome.
- The physical-luminance explanation for Fig 7a can't be tested, because the files don't hold the monitor calibration.
- I didn't change the claims file.
