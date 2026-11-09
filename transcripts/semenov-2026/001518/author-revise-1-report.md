I've finished the round-1 revision. The entry re-ran cleanly with `python tools/entry.py all entries/001518-semenov-2026`: 0 check errors, notebook passed in 962 s. The outputs are identical to the run I checked every conclusion against. Nothing is committed.

**Main change: the volts-to-V/cm factor.** The verifier was right that the old choice (1.72 V/cm per volt) was circular: it had been fitted to the dye slopes that fig3-dye-sensitivity tests. I now assume 5.6 V/cm per volt (250 V = 1400 V/cm). A two-dimensional model of the paper's electrodes (0.5-mm rods, 1.6 mm apart) gives 4.64 to 7.19, and this model is now in the helper. The old factor stays as a variant. A new section runs every criterion over factors from 1.5 to 8.

**Outcome changes**
- **Eight Di-8-ANEPPS claims were blocked and are now tested:**
  - fig2b-di8-climbs-to-570 is partially reproduced.
  - fig2b-di8-decline-within-set is reproduced, reading the cathodic pole and citing Results 3.1 and 3.4.
  - fig1-pole-dimming, fig4b-di8-limits, fig4b-first-10-pulses, fig4b-cathodic-asymmetry, fig4c-equator-follows-cosine and fig7b-charging-during-pulse are not reproduced.
- **fig3-dye-sensitivity** goes from partially reproduced to not reproduced (assumed). The verifier would block it as metadata_insufficient, and I recorded that disagreement. My reason: with the factor now taken from the geometry the test is no longer circular, and no factor from 1.5 to 8 gives both slopes. The paper's slopes would need 1.31 to 1.46 V/cm per volt.
- **Five claims no longer rest on the factor:** fig2a-fluovolt-saturation, fig4a-fluovolt-limits, fig4a-fluovolt-cathodic-decline, fig4b-di8-limits and fig4b-first-10-pulses fail at every factor, so they are no longer marked assumed.
- **Unchanged:** the other outcomes. The 15 claims whose experiments are not in the dandiset stay blocked as data_missing.

**Added**
- **Trace check.** The overlay showed a real fault: the automated trace is pulled inwards in some cells, and in c7 two touching cells are traced as one object. I added an edge-following trace as a variant and ran every criterion under it. At the adopted factor it changes no result. Neither moving the trace nor following the edge brings the mean pole dF near the paper's values. Single cells do reach the paper's values, so the shortfall is in the means.
- **Background with the camera offset only**, as a variant between no subtraction and the cell-free median.
- **Pole dF at all 19 sets** printed as numbers.
- **Drift control for fig2b-di8-decline-within-set.** The cathodic pole also declines within sets below 780 V/cm (9 of 11 sets). Most of the decline is a drift shared by both poles at every field strength, and the conclusion now says so.
- **Bleaching offset for fig3-fluovolt-nonlinear.** I kept the offset in the main reading, citing Results 3.2, where the paper reports bleaching in its own Di-8-ANEPPS dF. Removing it is shown as a variant, and the claim still fails under either.
- **fig2a-fluovolt-stable:** the count expected by chance (1.9 of 38) and the share of negative changes (32 of 38).
- **fig7b-charging-during-pulse:** a note that the per-cell mean-pole ratios carry no information.
- **Record and docs:** the header table now shows the revised outcomes. The record has the round-1 verification for all 30 claims (19 agree with the outcomes as first recorded, 11 do not), each with the verifier's reason and my response. The README, entry description and findings are updated.

**Not done:** I added no questions file, because the verifier reported no place where the claims file misreads the paper.
