# Round 2 verifier report: Semenov et al. (2026) on DANDI:001518

I agree with all 30 outcomes. Three statements in the record or notebook are wrong (cells 26, 38, and the verification entry). One remaining point affects how the fig3-dye-sensitivity conclusion is worded, though not its outcome.

## 1. Outcomes and assumptions

The claims file has 30 claims and the attempt record has 30 outcomes, one per claim:
- 15 blocked as data_missing.
- 12 not reproduced, 7 of them marked `assumed`.
- 2 partially reproduced, 1 of them `assumed`.
- 1 reproduced, marked `assumed`.

| Claim(s) | Record | Agree | Note |
|---|---|---|---|
| fig3-dye-sensitivity | not_reproduced, assumed | yes | In round 1 I called this blocked because the factor was fitted to the slopes. The factor now comes from the electrode geometry, so the test is no longer circular. The outcome still depends entirely on the factor (see 3). |
| fig3-fluovolt-nonlinear | not_reproduced, assumed | yes | It fails under both factors, with and without the offset, and at every factor in the sweep (cells 28, 75). |
| fig2a-fluovolt-saturation, fig4a-fluovolt-limits, fig4a-fluovolt-cathodic-decline, fig4b-di8-limits, fig4b-first-10-pulses | not_reproduced | yes | These do not depend on the factor. No set's mean comes near the paper's values (cells 18, 33, 43, 57). |
| fig2a-fluovolt-stable | not_reproduced, assumed | yes | 2 of 16 baseline tests are significant (cell 36). That is close to the rate expected by chance, but the criterion counts any significant test. |
| fig2b-di8-climbs-to-570 | partially_reproduced, assumed | yes | Every testable step rises. There is no 43 V/cm set. It fails for the centre cell. |
| fig2b-di8-decline-within-set | reproduced, assumed (factor and pole) | yes, by the criterion | The criterion only asks for a direction. Cell 51 shows the decline is not specific to strong fields, and the record says so. |
| fig4b-cathodic-asymmetry, fig4c-equator-follows-cosine, fig1-pole-dimming, fig7b-charging-during-pulse | not_reproduced, assumed | yes | Each fails at every factor where it can be tested (cell 75). "Assumed" here only concerns which sets exist. |
| fig5b-conductivity-calibration | partially_reproduced | yes | Cell 72. |
| The 15 blocked claims | blocked, data_missing | yes | — |

The 9 `assumed` outcomes each state the volts-to-V/cm factor of 5.6 V/cm per V through the deviation they share with fig3-dye-sensitivity. fig2b-di8-decline-within-set also states the cathodic-pole reading, citing Results 3.1 and 3.4. Both assumptions are reasonable. The factor lies within the 4.64 to 7.19 range of the two-dimensional rod model (cell 15). I checked `rod_field_per_volt` against the line-charge solution and it is correct. The files' 1.00 mm spacing would put the factor at 8 to 17.5, above the sweep's range.

I found no place where the claims file misreads the paper. I checked the Fig. 3 range of 43 to 360 V/cm with a fit over −150 to +150 mV, and the 560 and 760 V/cm of Fig. 7B.

## 2. Statements the outputs do not support

- **Cell 38, repeated in the record's fig2a-fluovolt-stable notes.** The text says: "The other 14 baseline changes lie between -1.70% and +0.64%." Cell 37 prints −3.043 (1400 V/cm cathodic, p = 0.060), −2.403 (780 V/cm anodic) and −2.240 (1400 V/cm anodic). The range is −3.04 to +0.64%. The p range of 0.055 to 0.93 is correct.
- **Cell 26, repeated in the record's fig3-dye-sensitivity notes.** The text says: "The slope varies as one over the factor. The paper's slopes would need 1.31 (FluoVolt) and 1.46 (Di-8-ANEPPS) V/cm per volt." The sweep in cell 75 contradicts this:
  - The FluoVolt slope is 26.7 at a factor of 1.5 and 24.0 at 1.72. Both are within 26 ± 2.6.
  - The Di-8-ANEPPS slope is 9.0 at 2.0, within 9.1 ± 0.91.
  - The slope does not scale as one over the factor, because which sets fall at or below 360 V/cm changes with the factor. The 1.31 and 1.46 come from the one-over-factor extrapolation in cell 24.
- **Attempt record, verification entry.** The text says the verifier "agreed with 19 of 30". The record's own results list has `agrees: true` for 21 claims and `false` for 9, which matches my round-1 table.
- **README.** "It takes about 17 minutes" does not appear in any output. Cell 3 prints only the 11.2-minute load.

Everything else checks out against the printed outputs: every other "**Result:**" sentence, the summary, the README table and its claim counts (four claims, 15 claims), and the record's notes and findings.

The record states my round-1 reasons in my own words and accurately, apart from the 19-of-30 count.

## 3. Round-1 points

**Resolved:**
- **B1** (factor circular and not geometric): the adopted factor is now `top` (5.6 V/cm per V).
- **B2** (Di-8-ANEPPS claims blocked): they are now tested.
- **B3**: outcomes that do not depend on the factor are no longer marked assumed. A trace check was added: pole dF on rings around the trace, an overlay image, and an edge-following trace.
- **B4**: a variant with the offset removed was added, and the outcome is unchanged.
- **B5**: the count expected by chance is now stated.
- **B6**: a drift control was added, and the conclusion now says most of the decline is drift.
- **B7**: a camera-offset background reading was added.
- **B9**: the conclusion now says the per-cell mean-pole ratios carry no information.
- **B10**: the header table now matches the summary.
- **From section C**: the factor sweep, the pole values at all 19 sets, the trace check and the low-field drift control were all added.
- **B8**: kept as before. All three cell readings are shown, and it changes no verdict.

**Remaining, bearing on a conclusion:**
- **fig3-dye-sensitivity.** "No factor from 1.5 to 8 meets the criterion" holds only at the grid points run. Between 1.72 and 2.0 the FluoVolt slope leaves its tolerance while the Di-8-ANEPPS slope enters it, so a factor in that interval meeting both was not tested. Under `bottom` (1.72) both correlation coefficients are already within tolerance. Cell 15 also shows the paper's own calibration implies 1.5 to 1.6 V/cm per V. The outcome at the adopted factor stands. The text should say the result is not reproduced at the factors run, give the factors that would match the paper's slopes as about 1.5 to 2, and drop the 1.31 and 1.46.

**Does not change an outcome:**
- **fig7b-charging-during-pulse.** All ratios are normalised to the 25 V set, where both poles share a −3.9% bleaching offset (cell 15). That offset makes the anodic value at 25 V too large and the cathodic one too small. The record calls the anodic reading the "closest", but it is the one the offset affects most. The mean-of-poles reading, in which the offset cancels, gives ratios of 0.55 to 0.85, meaning measured values above the linear line. The claim fails under every reading either way.
