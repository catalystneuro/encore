The claims file is ready for an attempt, after fixes to 12 claims and the header. Nothing was committed.

**Checker result:** `46 claims, 44 quotes, 0 statistical values, 0 problems`. It reads the same before and after the changes. The paper reports no tests, so no claim has `statistics`.

**Changes, by claim:**
- **fig1f-koh-stability:**
  - The "~10% to ~65%" sentence is in the Methods and covers the whole optimization. Figure 1F's two groups also differ in gel recipe as well as KOH, so the statement no longer credits KOH alone. The source now starts with the Methods.
  - "~10%" of 9 probes can only mean 1 of 9 (11%), which the old tolerance (0.10 ± 0.01) ruled out. It is now recorded as 1 of 9, exact.
- **methods-revision-probe-stability:** the paper defines stability only for dipping, so applying the 25 µm rule to slice and in vivo recordings is now stated as a reading.
- **fig1h-crosstalk-pairs:** the source now starts with the Methods, where the quote is. The Methods' 1-minute filter window decides; the code's 10 frames are a variant.
- **figs3e-tau-on-under-one-minute:** the legend does not say whether "under 1 minute" refers to the dF/F0 fits or the concentration fits. Both are now readings; if they disagree, the claim is blocked.
- **figs2c-stabilization:** added the Methods' limit of the cross-correlation to voxels at least 50% likely to be a cell at the first timepoint.
- **figs5d-pvh-ne-alone:** the criterion had said the 190 and 102 nM thresholds don't decide the claim. The Methods set one threshold per dataset, so they are the PVH thresholds and now count, with their tolerances.
- **fig2h-lc-ne-da-peaks:** "DA peaks before NE" was judged only by rise time. I added a second reading, the time of each trace's maximum, with blocking if the two disagree.
- **fig2jk-lc-robust-counts:** the criterion used the code's threshold method as the main one, which goes against the protocol. The Methods now decide and the code's method is shown as a variant. Which recordings form the "dataset" is now open: LC alone, or the code's LC plus DRN recordings, which the paper never mentions.
- **fig4-ex-vivo-elevations and figs6j-serum-dipping-matches-elisa:** "Reproduced when both readings hold" would have counted a split result as not reproduced. A split now blocks the claim.
- **fig4-ex-vivo-two-orders-lower:** removed the statement that 5-HT in CSF was below detection, which the paper does not say. The 5-HT ratio is now taken from the Figure 4H values, or from the detection limit if the values fall below it.
- **fig6c-ip-5ht-reaches-chp-fast-enough:** the only reading of "fast enough" fails on the code's own printed values. I added a second reading, threshold-crossing onset, with blocking if the two disagree.
- **Header:**
  - The threshold definition now notes that the Methods don't define "dataset".
  - Added two inconsistencies in the paper: the Figure S4D legend's panel names, and the IP 5-HT dose for choroid plexus imaging (3 vs 2 mg/kg).

**Still open (logged in the `checks` entry):**
- **fig5ab-spontaneous-5ht:** the paper gives no rule for detecting a spontaneous rise, and the code picks the 3 recordings by hand. The file's rule is its own reading, and the 3 of 7 count may depend on it.
- **Single readings of vague words:** "modest", "similar", "diverse kinetics" and "most probes" each have one reading, with thresholds the file chose.
- **Findings without a claim:** "10 of 16 sensors reliable" and the Discussion's "all ligands in CSF within 15 min". Neither is a main finding.
- **Code not checked:** the paper's code repository was not available in this run, so the notebook cells and printed values the file cites were not checked against it.
