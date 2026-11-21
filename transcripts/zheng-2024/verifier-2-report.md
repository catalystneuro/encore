**Verifier report, round 2: Zheng et al. 2024 on DANDI:000552 (0.261113.1035)**

The claims file has 32 claims and the attempt record has 32 outcomes. 29 claims are tested in full, figs1 is tested on one session, and 2 are blocked. Cell numbers are 0-based notebook cell indices.

### 1. Outcomes

I agree with every outcome except as noted below.

- **No change from round 1, and I agree:** fig1d, fig1e-novel, fig1e-later, fig1h, fig1i, switch-step-size-filter, fig2d, fig2e, fig3df (both), figs4g, fig3k, figs5, fig4-delay-zone, fig4-behavior, figs9, figs13 (3 of 5), fig5c, fig5d, multifield, figs12, fig6, fig6f, figs14, figs2, fig7, figs15.
  - **fig6:** familiar ON is 10 of 45 sessions under every seed (10 to 11), which is one session beyond the "within one session" allowance. The within-turn null is now conservative (false-positive rate 0.035, cell 91).
- **fig4-glm-deviance, partially reproduced:** I agree; it remains a judgment, since the criterion's partial clause does not cover this case. One nuance: the measured values given are reading (a), and the held-out OFF value of 0.128 is within tolerance only under the claim's seed. Under the other four seeds it is 0.114 to 0.121 (cell 55). Reading (b), in-sample 0.202 and 0.145, holds without depending on the seed and would be the better measured value. The outcome is a criterion gap, so `assumed: true` would fit.
- **fig4di, partially reproduced, assumed (trials from the fourth on):** the assumption is stated and reasonable; the trial counts 1031/288 match the legend's 1029/281. The record now says plainly that the decrease disappears once the last two trials are also left out (no correlation significant, cell 64). I agree.
- **figs8, now reproduced, assumed (per frame of forward locomotion):** the assumption is stated and the outcome is acceptable, but it is weak.
  - The paper's two values point to different units: familiar p = 3e-11 implies about 4×10⁵ samples, novel p = 0.78 about 200.
  - Per trial, both r are well outside tolerance (0.154 and −0.148). Per trial over all frames they are −0.082 and −0.261 (cell 67).
  - Within cell 67, the code comment still calls per-trial "the main, as the claim's legend plots one point per trial". That contradicts the adopted reading, and the Figure S8C legend says no such thing.
- **fig4no, partially reproduced, assumed (per position bin):** the assumption is stated and reasonable, and matches my round-1 outcome. The margin is very thin: 9.73 against 10.0 head-scan trials per bin in the central arm and the delay zone (cell 70).
- **figs1, now not reproduced on one session, assumed (peak-to-trough amplitude):** I agree only as a one-session result, and the assumption is misplaced.
  - The adopted switch time (the animal at the field's peak) is not one of the criterion's two readings.
  - Under the criterion's reading (a), the trial start, neither test is significant (p = 0.32 and 0.88), which would be reproduced.
  - Under reading (b), entry into the field, OFF gives p = 0.00023, and with trough depth p = 0.031 (cell 104).
  - So the outcome depends on the switch-time reading more than on the amplitude definition, and the record should flag that as the assumption.
  - Also unflagged: the 1,382 pairs reuse the same ~140 neighbours across switches from 32 units, so the pairs are not independent and the p values are inflated. Every change is at most about 1% of the amplitude, and only 1 of the 45 sessions was tested.
- **figs14:** the OFF fraction (0.436 against 0.2) depends on reducing the shuffle threshold to a mean over the field's bins. This is stated as a deviation but not flagged `assumed`. It does not change the partial outcome.

### 2. Sentences the outputs do not support

- **Cell 42:** "below the expected 0.54 to 0.77 for orders 1 and 3". Order 2 (0.510) is also below 0.54.
- **Summary, cell 107:** "under it the Familiar against Novel test … gives p = 0.058, and no other outcome would differ". The trial-averaged variant reran only the cell-50 and cell-52 summaries plus multifield (cell 52). The GLM, fig6, figs12, figs14, figs13, figs5 and fig4di were not rerun, so this cannot be claimed for them.
- **Cell 105 and the figs1 notes:** "The changes are about 1% of the amplitude in every reading" / "Every change is about 1%". At the code's switch time the OFF change is 0.03% (relative 0.0003). The supported wording is "at most about 1%".
- **Cell 71 and the fig4no notes:** "bin 50 … at the end of the choice arms". Cell 70 prints the bin's segment as return_side; it is the first bin past the 111 cm cut. This is consistent with the paper's "between green and red sections", but it is not inside the choice arm.
- **Cell 21:** "In 52 session and environment units (fields per unit 79 to 711)". Cell 20 prints 53 units; 52 have slopes. Trivial.
- **Cell 8:** "The x and y of the novel figure-8 maze carry no scale (the file says so)". No output shows this.

Everything else in the Results, the Summary, the README (including the timings: 1,353 s of pipeline runs and 473 s of streaming) and the record's notes matches the printed outputs.

The record states my round-1 reasons faithfully, near-verbatim, with my problem numbers attached.

### 3. Round-1 points

**Resolved:**
- **Problem 1 (figs8):** all readings are now run; the remaining doubt is covered in section 1.
- **Problem 2 (fig6):** the null is now within-turn, and the lag-1 variant and false-positive rates are shown.
- **Problem 3 (figs12):** three selections, including the code's, are shown; no change of outcome.
- **Problem 4 (GLM):** the gap in the partial clause is stated.
- **Problem 6 (fig4di):** the trailing zeros are shown and stated.
- **Problem 7 (fig1h):** now uses per-lag averages.
- **Problem 8 (cell 5 mislabel):** fixed.
- **Problem 9 (data version):** unchanged and still reasonable.
- **Requested outputs 1–7:** all added.

**Remaining, and bearing on a conclusion:**
1. **Upstream counts are still low under every variant**: 2,794–2,825 putative fields against 3,184 ± 318; familiar switching 1,884–1,933 against 2,310 ± 231. The cause is not found. This drives switch-step-size-filter, fig2d and multifield.
2. **fig2d hinges on two things**: the familiar OFF fraction is 0.0014 short, and the tie rule (647 fields tied). With ties broken toward the larger K, all four fractions are within tolerance, which would make it partially reproduced. The smaller-K rule is cited to the code, which is not under `paper/`, so I cannot verify it. The same applies to the new figs12 code_mismatch finding (windows swapped).
3. **figs1**: the switch-time reading, non-independent pairs and one session, as in section 1.
4. **figs8**: the per-frame reading is fragile, and the cell-67 comment contradicts it.
5. **fig4-glm-deviance**: held-out OFF is within tolerance under one seed only.

### 4. Critical findings

No finding in the record is rated `critical`.

One part of finding 1 (rated `major`) would be critical if taken alone. In the cited version, `is_familiar_maze` is False for 28 of the 30 familiar trials of e16_3m1_210201 (cell 7). That is a wrong label that nothing in the file reveals. The pinned version corrects it, so the `major` rating is right for the finding as a whole, which also covers the missing cell-type and light-responsive labels. Only one session was checked, so how far the mis-flag extends in the cited version is unknown.
