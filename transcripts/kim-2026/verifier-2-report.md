**Round 2 verifier report: 001868-kim-2026-01 (doi:10.1126/sciadv.aef0343)**

The claims file has 43 claims. The attempt record has 43 outcomes, one per claim: 16 reproduced, 4 partially reproduced, 4 not reproduced and 19 blocked. Cell indices below are positions in the notebook's cell list, starting at 0. They are not the round-1 numbers.

## 1. Outcomes

**Agree, no assumption involved:**
- fig2a-threshold-decrease: early 5.39 uA, late 3.88 uA, p = 5.32e-06.
- figs1e-response-times-decrease
- figs5c-wheel-onset-decrease
- fig4-unit-counts, not reproduced: 2 of 6 counts are within tolerance.
- figs3b-modulation-increase-all
- figs3d-modulation-stable-at-threshold: reading (a) gives p = 0.16.
- fig4g-modulated-count-mouse1
- both fig4ij claims
- fig5d-pulse-locking-stable-across-currents, not reproduced: 0.792, and 0.774 to 0.793 under three other seeds, all below 0.80.
- fig5fg-pl-modulation-increase: time to maximum now falls at 6 uA, p = 0.041.
- figs4de-npl-no-change: smallest p is 0.0824.
- figs5-restricted-window-consistent, under the "keep" reading.
- fig6c-kl-divergence and fig6d-npl-hit-miss-divergence, not reproduced.
- fig6f-population-coupling and figs9a-coupling-700ms
- all 19 blocked claims. For figs2de-control-stable, density still cannot be formed.

**Partially reproduced, where the criterion has no partial clause** (figs3c, fig5e, figs4b, fig5h):
- I agree with all four. In each, a distinct part of the claim holds and another fails:
  - figs3c: the 5 uA fall holds; 4 uA is also significant (p = 0.0465).
  - fig5e: the effect holds (p = 7.7e-10); the NPL fraction is 0.553 against an upper bound of 0.548.
  - figs4b: latency rises at every current; the velocity at 4 uA is 0.161 to 0.169 m/s, below 0.18.
  - fig5h: 6 uA holds; 5 uA gives p = 0.0613 at the fixed seed, and 0.0197 to 0.0485 under the other seeds.
- I am withdrawing my round-1 "not reproduced" for figs3c. In round 1 I gave fig5e a partial on the same grounds, so this makes my judgments consistent.
- The record is not consistent, though. It moves fig4-unit-counts to not_reproduced because "the criterion … has no partial clause", yet uses partial for these four. The fig4 outcome stands on substance (4 of 6 counts outside), but the stated reason should change.

**Outcomes resting on an assumption (`assumed: true`):**
- **fig2a-steepest-decline-early:** the assumption is stated and reasonable. It is the claims file's own reading of the figure. The MLE reversal is disclosed.
- **figs7-control-no-change:** the assumption is stated. I agree with the outcome, but with a caveat that bears on it.
  - The baseline is the 700 ms before each 200 ms burst. The helper's docstring says bursts are 300 ms apart, so for bursts 2 and 3 that baseline contains the previous burst.
  - This is a claim of absence, and a baseline that contains stimulation lowers the test's power. Control z medians are 0.32 to 1.88, against 2.6 to 5 in the trained mice (cells 87, 28).
  - The record does not say that the baseline contains stimulation.
  - PL time to maximum moves the opposite way to the paper's: r = +0.25 here (5 to 55 ms), against −0.39.
- **figs9-coupling-window-and-control:** the assumption is stated, but its justification is weak.
  - The outcome depends on choosing trial segments (s1) over burst segments (s2). Under s2 the early test gives p = 0.00428.
  - "Whose n match the paper's more closely" holds only in ratio. In absolute numbers s2 is closer:
    - s1: 47/93 and 33/242
    - s2: 41/18 and 28/46
    - paper: 49/64 and 25/128
  - The criterion's "the full train" does favour s1.

## 2. Sentences the printed outputs do not support

1. **Cell 26 and the fig4-unit-counts notes:** "a dip in the 0.45 to 0.50 ms bin (22 units) between 59 and 44, so the distribution is bimodal about 0.45 ms."
   - At 30 kHz, the 0.45–0.50 ms bin holds one possible trough-to-peak value; the bins either side hold two each.
   - Per value, the counts are 29.5, 22 and 22, so the dip comes from the binning.
   - The histogram also alternates in the same way elsewhere: 128, 61, 150. This is reported, not judged.
2. **Attempt record finding (Fig. 6D question):** "the early NPL onset is about 105 ms." Cell 70 gives 75 ms with 10 ms bins and 87.5 ms with 5 ms bins.
3. **Cell 53, the figs4b notes and the stim_channel finding:** "The mapping is supported by the outputs … the fraction of modulated responses falls" with distance.
   - This holds pooled from 60 to 120 um outward, but the 0–60 um bin is the lowest (0.315).
   - Per mouse it reverses in Mouse 5 (0.31 near, 0.48 far) and Mouse 6 (0.08 near, 0.88 far), cell 52.
   - Mouse 5 is in the fit, and under the electrode-table mapping its pattern looks local (0.68 near, 0.56 far).
4. **Statements in the record and the blocked notes that no notebook cell prints:**
   - the per-session planar ROI counts (385, 172, …)
   - the "separate segmentation" description
   - "reference_images is empty" (also cited in the fig3b response)
   - `voxel_mask`
   - "136 planes"
   - "200 ms bursts 0.5 s apart"
5. **figs5c notes:** "No onset is found in 568 of 4772 hit trials." Cell 18 shows that these 568 trials have no wheel trace at all.
6. **Format:** the figs7 and figs9-coupling outcomes have no `notebook`/`output` fields.

Everything else checks against the outputs: all other "**Result:**" cells, the Summary, the README table (8 + 9 + 2 = 19 blocked) and the rest of the notes.

The verification block gives my round-1 reasons accurately, in close paraphrase, with the problems folded in where they belong. Its `agrees` flags match my round-1 judgments.

## 3. Round-1 points

**Resolved:**
- **1, psignifit:** now run at the default grid with the scaled x50; the late median is 0.10 uA inside its bound.
- **2, PL call:** now follows the paper's code; 62.3% of responses are PL and the PL/NPL n match the paper's. No uniform synthetic response is called PL. Only 7 PL calls peak in the last two bins.
- **3, cell type:** both variants are now run.
- **5, control counts:** run.
- **6, controls:** now run.
- **7, `accepted` flag:** every unit is accepted.
- **10, channel days:** both counting rules drop the same channels.
- The other checks I listed as missing in round 1 have been run.

**Partly resolved:**
- **4, the figs4b mapping:** the code's mapping is far better pooled, but it fails in Mouse 5, which is in the fit, and in Mouse 6.

**Remaining that bears on a conclusion:**
- **figs4b:** the per-mouse mapping check above. Whether the 4 uA velocity misses its range may depend on Mouse 5's distances.
- **figs7:** the control baseline contains the previous burst, so a no-change result is easier to get. Time to maximum also runs opposite to the paper's.
- **figs9 control half:** the outcome depends on s1 against s2, and the n-match reason given for s1 is weak.
- **fig6d (round-1 point 9):** still unexplained. With 5 ms bins the late PL clusters flip sign almost every bin, at the pulse period. This points to a pulse-timing effect, not a hit-miss difference. The outcome holds anyway, because large one-sign PL clusters remain (405–505 ms and 645–685 ms).

**Remaining that does not bear on a conclusion:**
- fig6c reading k2: the week-4 PL KL median is 0.859, against 0.008 to 0.066 in the other weeks. It is unexplained; both readings fail on PL either way.
- The planar `reference_images` check is not shown in the notebook.
