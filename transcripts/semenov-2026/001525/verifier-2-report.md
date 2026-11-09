**Verifier report, round 2: Semenov et al. 2026 on DANDI:001525 (0.261006.1856)**

The claims file has 27 claims and the attempt record has 27 outcomes. Two are reproduced, three partially reproduced and 22 blocked (data_missing).

## 1. Outcomes

| Claim | Record | I agree? | Assumption stated and reasonable? |
|---|---|---|---|
| fig7a-test-pulse-cosine-up-to-1000 | reproduced (assumed) | Yes, under the criterion | Stated: the trace, rank mapping, single-pulse benchmark and main reading. All are reasonable, but see the trace point below. |
| fig7b-test-pulse-unchanged-to-760 | reproduced (assumed) | Yes | Stated, the same assumptions. The "~80%" holds only at the anodic pole (79.7%); cathodic is 57.5% (p 0.21, d −0.78) and the mean is 71.9%. The record says so. |
| fig7b-test-pulse-reduced-1200-1400 | partially_reproduced (assumed) | Yes, under the criterion as written | Stated. It rests on the cathodic and mean-of-poles readings; see the claims-file point below. |
| fig7c-full-reseal-mild-residual-strong | partially_reproduced (assumed) | Yes | Stated. Normalizing by the group control is a reasonable choice, and the per-cell variant is shown. |
| fig5b-conductivity-calibration | partially_reproduced | Yes | No assumption. `f_factor` matches Eq. (2) in the paper's text layer (paper .txt lines 225–239). I still could not render the PDF page itself. |
| 22 blocked claims | blocked: data_missing | Yes | — |

**The trace, which bears on fig7a and fig7b-reduced.** The analysis now traces the membrane at the intensity peak within 8 px inside the cell's outer edge. This rule came in after round 1, and it changes two outcomes (fig7a and fig7b-reduced). The overlays in cell 6 do support the change on their own: the old trace lies 11.7 and 8.9 px inside the edge in c5 and c9, against 2.5–4.8 px for the new one.

However:
- The 8 px window is a free parameter, and no variant tests a different width.
- 19 of the 22 variants use the new trace, so "holds in 19 of 22" is not 19 independent confirmations. The outcome turns on the trace choice: all 3 variants with the old trace fail (cells 14 and 22).
- In the cell 6 overlay, the c5 trace has a visible inward notch near the top of the cell. I cannot tell whether it falls within a pole arc.
- c5 has a large effect on the results. Dropping it moves the fig7a hindrance to "anodic;mean" and makes fig7b-unchanged fail (cell 18, row 15).

**Where the claims file misreads the paper (reported, not corrected).**
- **fig7b-reduced.** Results 3.7 ¶6 says the paper's cathodic dF at 1400 V/cm was negative and was left out. So the paper's "~50%" cannot be a cathodic or a mean-of-poles value; only the anodic reading can carry 70/50. The criterion still allows cathodic and mean readings, and the partial outcome comes only from them.
  - Under the anodic reading alone: the values are within tolerance (68.7 / 48.0) but p is 0.086 and 0.011 (cell 21). The claim would then be not_reproduced.
  - This bears on a conclusion.
- **fig7c pole-difference part.** The paper's statement "no difference between the poles was detected by the test pulse" refers to Fig. 7C, which leaves out the negative cathodic point at 1400 V/cm. The criterion tests 1400 V/cm anyway. Without 1400 V/cm the part holds under the main reading: paired p is between 0.12 and 0.82 at 360–1200 V/cm (cell 25). The outcome does not change.

## 2. Sentences the printed outputs do not support

- **Attempt record finding** (clock): "best split at image 39 to 41 in 54 of 73 files". Cell 5 prints "within 39 to 41 in 56".
- **Attempt record finding** (dark frames): "Keeping or dropping them shifts the test-pulse dF by about 1.3 percentage points". Cell 7 gives 1.33 only without background subtraction. Under the main, background-subtracted reading the profile-mean shift is 2.17 (−2.09 vs −4.26), and the amplitude shift is 0.0–0.3.
- **Cell 9:** bleaching "accounts for the offset in sign and size". **Cell 15** likewise calls the offset "dye bleaching" as an established cause. Cell 8 does not support the size match:
  - over all files, −5.16% predicted against −3.67% measured;
  - at the control, −6.96% predicted against −3.58%;
  - at 760 V/cm, −4.68% against −1.81%;
  - r = 0.18 over files.
  
  The sign does match the paper's bleaching description (Results 3.2: −5% cathodic, +5% anodic). This does not affect any conclusion.
- **Attempt record, fig7b-reduced notes:** "The cathodic values fall well below the paper's." At 1400 V/cm the paper's own cathodic value is negative (Results 3.7 ¶6), so −11.3% is in line with it. The sentence is supported only at 1200 V/cm.
- **Attempt record, fig7b-unchanged notes:** "The paired test … finds no difference under the main reading (smallest p 0.098)". This is true for the cathodic and anodic poles. For the mean-of-poles reading, the paired test gives p 0.018 at 760 V/cm and 0.016 at 1000 V/cm (cell 12), and the sentence leaves that out.
- **README, fig7c row:** "Partially reproduced … (the during-pulse part is not testable)". This leaves out that the testable "no pole difference at the test pulse" part fails (paired p 0.0002 at 1400 V/cm, cell 25). The Summary (cell 31) does say so.

Every other number in the Result cells (15, 19, 23, 27, 30), the Summary (31), the README and the record's notes matches the printed outputs.

The record's `verifications` section states my round-1 reasons in my own words, accurately. That includes the caveats I did not count against a conclusion and the things I could not check.

## 3. Round-1 points

**Resolved:**
- **B1:** fig7c is now tested and reported as partially_reproduced.
- **B3:** the metadata strengths and the electrode gap are discussed (cells 2 and 9).
- **B4:** the single-pulse control is now stated in the notebook.
- **B5:** unchanged; the readings are carried through.
- **B6:** a variant with the field direction from the control files only (−73.9°) gives the same outcomes.
- **B8:** reading (a) is now shown per variant.
- **C, overlays:** added. c5's cathodic control dF is now +11.8%.
- **C, recording order:** the single pulse is recorded first in every cell (cell 4).
- **B2, the offset:** mostly resolved. The baseline trend is now shown and its sign matches the paper's description of bleaching. The size match is overstated (see section 2).
- **B7, the amendment:** explained in the record. I still have not seen questions/001525.yaml, but the criterion text I have makes the unpaired test decisive.

**Open, and bearing on a conclusion:**
1. **The trace.** Two outcomes (fig7a reproduced, fig7b-reduced partial) depend on the post-round-1 edge trace and its untested 8 px window. All old-trace variants fail. A window-width variant, and a check that the c5 notch is clear of the pole arcs, would settle this.
2. **fig7b-reduced pole reading.** The partial outcome rests on cathodic and mean readings that the paper's own negative cathodic 1400 V/cm value excludes. Under the anodic reading alone the claim is not_reproduced. This is a claims-file issue, reported for the reader.
3. **Eq. (2) (minor).** The page-3 PDF rendering is still unconfirmed by me. The text layer matches the code.
