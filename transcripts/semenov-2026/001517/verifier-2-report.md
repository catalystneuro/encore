**Verifier report, round 2: Semenov et al. 2026 on DANDI:001517 (0.261006.1856)**

The claims file has 31 claims. The attempt record has 31 outcomes: 5 reproduced, 3 partially_reproduced, 8 not_reproduced and 15 blocked (data_missing).

### 1. Outcomes and assumptions

I agree with all 31 outcomes.

- **Reproduced:** fig1-pole-dimming, fig2b-di8-climbs-to-570, fig2b-di8-bleaching (fragile), fig2b-di8-decline-within-set and fig7b-charging-during-pulse.
- **Partially reproduced:** fig3-dye-sensitivity, fig4b-cathodic-asymmetry and fig5b-conductivity-calibration.
- **Not reproduced:** fig2a-fluovolt-saturation, fig2a-fluovolt-stable, fig3-fluovolt-nonlinear, fig4a-fluovolt-limits, fig4a-fluovolt-cathodic-decline, fig4b-di8-limits, fig4b-first-10-pulses and fig4c-equator-follows-cosine.
- **Blocked:** the 15 blocked outcomes match my reading of the session descriptions in round 1.

Every tested outcome except fig5b carries `assumed: true`. Each states the assumptions it uses: the volts mapping, background distance, automatic outline, dark frames, field direction, cell selection, and, where IMPC is used, the pixel size and tau. fig5b correctly states none. All are stated and reasonable, with these qualifications:

- **Volts to V/cm in order.** This is reasonable but rests on one step. The 25→50 V ratio (FluoVolt 3.05, Di-8-ANEPPS 2.90; cell 10) discriminates between the two readings. The later Di-8-ANEPPS steps (1.49, 1.35, 1.23) are at or below both scales. fig7b's "reproduced" depends entirely on this mapping (cell 78: no reading passes with the field proportional to the volts). The record says so.
- **Pixel 0.267 µm.** The adopted value is the right default. The paper's 8 µm is "assumed … in CHO cells [20]" for Eq. (2) (Methods 2.3, text lines 265–270), not a measurement of these cells. So the 8-µm variant is weakly motivated, and fig3 stays partially reproduced.
- **Far background.** This is the reasonable reading of the claims file's "cell-free region". But several outcomes change at 14–20 px or with the near band (section 3).

### 2. Statements the printed numbers do not support

**Result conclusions**

- **Cell 47 (and the fig3-fluovolt-nonlinear notes).** "The cause is an asymmetry between the poles, not a bend … the cathodic fit pulled down by the negative 43 V/cm cathodic values of the bleaching."
  - Cell 45 shows the anodic Di-8-ANEPPS smooth also departs from its own line (0.58 to 0.80 over 150–500 mV), so there is a bend.
  - No output removes the 43 V/cm points, so the attribution to bleaching is untested.
  - The outcome is unaffected.
- **Cell 52 (and the fig4a-limits notes).** "in the 14 to 20 pixel band … measured IMP is already below the calculated at 150 V/cm". Cell 51 prints only `none_at_43_150 False` for that band, with no direction and no field strength.
- **Cell 75.** "The equation's own curve is far below the paper's figure for 10-fold". This is wrong in direction and size: Eq. (2) gives a smaller reduction (1.33% against 2%), so its curve lies about 0.7 point above.
- **Cell 21.** "the anodic pole does not grow beyond 570 V/cm (−72.2 to −61.9%)". It does grow, by 2.4 points at 780 V/cm (−69.8 → −72.2). That is within the criterion's tolerance, but the wording is not accurate.

**Summary, cell 81**

- "with the poles dimming before the regions nearer the equator". This is overstated. Under the adopted far background, 16 of 24 equatorial arcs fall below IMPC (cell 70). The 270° cathodic-side arc is low already at 570 V/cm (ratio 0.52).
- "responses decline within the electroporating sets". This leaves out the record's own caveat: at 780 V/cm the decline cannot be told from bleaching (cell 36: net −3.3% against −2.6% at 570).

**Header, cell 0**

- "four sets, two used: FluoVolt c2 at 300 V and Di-8-ANEPPS c7 at 300 and 350 V" lists three used sets. Cell 3 and the Summary say three.

**Attempt record**

- The pixel-size deviation (fig3, fig4a, fig4b, fig4c) and the pixel finding both say "radii … 7.7 to 14.6 um by cell". No printed range matches. Cell 5 gives 7.80–14.92 (equal-area) and 7.84–15.06 (perimeter); cell 11 says 7.8 to 15.1.
- fig3 notes: "Pearson as low as 0.01". Cell 41 prints 0.005 and −0.02 (trivial).

**Entry README**

- "The notebook shows each claim under a sweep of the background distance, the pixel size that gives the paper's 8-um radius, and a field proportional to the volts." Only fig3, fig4a, fig4b, fig4c and fig7b get the pixel or volts variants, and fig5b has no sweep.
- The table lists fig2b-di8-bleaching and fig7b as plain "Reproduced". The record qualifies them as fragile (38/56 subsets) and as resting on the volts mapping.

Every other sentence I checked matches the outputs, including the subset counts, p-values, sweep ranges, the bleaching-control figures and the fig7b ratios.

**My round-1 reasons in the record.** The `verifications` block gives them faithfully and in my words, with problem references added where relevant. One small difference: it records my 39/56 bleaching subset count alongside the notebook's computed 38/56, which is fine.

### 3. Round-1 points

**Resolved**

- **Problem 2 (pixel).** The NWB dump shows no ImagingPlane, Device or pixel size. The 8-µm variant now runs for fig3-fluovolt-nonlinear and for fig4a, fig4b and fig4c.
- **Problem 4 (bleaching control).** Added and disclosed.
- **Problem 6 (subsets).** Now given for bleaching (38/56) and fig4c (0/56).
- **Problem 7 (equal-area radius).** Now run; same results.
- **Problem 8 (per-pole background).** Local variants added.
- **C: outline overlays.** Added. They led to re-tracing three used sets.
- **C: dump.** The NWB dump settles the pixel-size question.
- **C: bleaching control.** Same as problem 4.
- **C: 8-µm variant.** Same as problem 2.
- **Problem 5 (multiple tests).** Referred to a reader and disclosed. It does not change the outcome as written.

**Disclosed but still bearing on a conclusion**

1. **Volts mapping (problem 1).** fig7b's "reproduced" stands only on the in-order matching. The fig3 slopes also fail under proportional volts. The only evidence that tells the two readings apart is the noisy first step (Di-8-ANEPPS per-cell ratios range from 1.38 to 4.04). Only the authors can settle it.
2. **Background distance (problem 3).** The 14–20 px band passes fig2a-fluovolt-saturation, both fig3 slopes and fig4b-first-10-pulses. The near band passes fig4b-first-10-pulses and fig4b-cathodic-asymmetry. These not_reproduced and partially_reproduced outcomes hold only under the adopted far band.
3. **Di-8-ANEPPS outlines (new, from the overlays, cell 11).** The c7, c10, c12, c13 and c14 outlines are wavy and cut inside the membrane, and this is not corrected. It may bias the Di-8-ANEPPS magnitudes and the equatorial arcs (fig4b-di8-limits, fig4b-first-10-pulses, fig4c-equator-follows-cosine).
4. **Pixel size.** fig3-dye-sensitivity would be reproduced with a 0.192-µm pixel. The data cannot settle this.
5. **Which five Di-8-ANEPPS cells.** Still unknowable. fig2b-di8-bleaching passes in 38 of 56 subsets, fig7b in 43 and fig4b-first-10-pulses in 5.
