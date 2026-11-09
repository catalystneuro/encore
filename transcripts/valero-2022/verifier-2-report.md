# Verifier report, round 2: Valero et al. 2022 (doi:10.1126/science.abm1891) on DANDI 000568 v0.230705.1633

The claims file has 22 claims and the attempt record has 22 outcomes: 5 reproduced, 5 partially reproduced, 6 not reproduced and 6 blocked. I agree with 21 of them; I disagree with fig3g. The paper text (PMC author manuscript, PMC9632609) is saved as `paper/PMC9632609_bioc.json` and `paper/PMC9632609.txt`. Cell indices below are those of the current notebook. I read the new `find_fields` in `valero.py` but could not run it, because numpy is not installed here.

## 1. Outcomes

| Claim | Record | My view |
|---|---|---|
| cohort-counts | partially_reproduced | Agree (cell 17). |
| fig1c-pulse-protocol | partially_reproduced | Agree (cell 20). |
| fig1e-responsive-fraction | reproduced | Agree (cell 23): reading (b), 66/91 = 72.5%. |
| fig1i-swr-decrease | reproduced | Agree (cell 27). |
| figs10-swr-gain-vs-baseline-rate | partially_reproduced | Agree (cell 30). |
| fig2b-theta-trough-gain | not_reproduced | Agree (cell 33). |
| figs11-place-cell-fraction | partially_reproduced | Agree (cell 37): p = 0.20; 84.2% is outside 73 ± 7.3 and 70.6% is within 71 ± 7.1. |
| fig2e-infield-gain | reproduced | Agree (cell 40). |
| figs12-gain-rate-correlations | not_reproduced | Agree (cell 43). |
| fig3a-place-cells-more-excitable | not_reproduced | Agree (cell 46), p = 0.19. This outcome flipped with the new place-cell calls, so it is fragile. |
| fig3c-unmasked-fields | not_reproduced | Agree under the criterion (cell 49). In practice it is undecided: reading (a) has n = 9 and its interval runs 40.0 to 97.2%. |
| fig3e-ghost-fields | partially_reproduced | Agree (cell 53). |
| fig3f-light-stability | not_reproduced | Agree (cell 56). |
| fig3g-spatial-information | reproduced | **Disagree: partially_reproduced.** Part 2 rests on p = 0.039 (cell 59) with dark-window control maps. Against time-matched control the increase is negative in both groups and does not differ (p = 0.3). The paper says "Random intervals (20 ms) between the light pulses served as control epochs" (`paper/PMC9632609.txt`, Results paragraph 2), which the time-matched variant follows most closely. The response says "the criterion fixed the control maps before the analysis", but the criterion fixed "time when no uLED is on", and the revision already replaced that. So the main control maps are not the pre-registered ones either, and the selection bias still favours part 2. |
| fig4c-swr-cofiring-place-pairs | reproduced | Agree under the criterion (cell 62). It is weak: p = 0.032, carried by sess9 alone, and the participation variant gives p = 0.056. The coefficient for place/non-place pairs (0.062) equals that for place pairs (0.060), so the contrast the claim describes is absent. |
| fig4d-light-unmasked-cofiring | not_reproduced | Agree (cell 65). |
| fig1j, fig1km, figs9, fig3h, fig4ef, fig4gh | blocked | Agree. The figs9 proxy (cell 68) is shown, and the reason it stays blocked is sound. |

## 2. Statements the numbers do not support, or overstate

- **Cell 54, and the fig3e notes in the record:** "For 70 control fields of light-responsive place cells" / "For 70 place fields", and "14 light fields" / "14 unmasked fields". Cell 53 prints "n = 70 field directions" (fig2e has 80 fields), and the 14 are field directions from 7 cells.
- **Record, figs10 notes:** "is negatively correlated with the baseline rate … in every subject (-0.37 to -0.71) and every session." The sign is negative in every session, but 3 sessions are not significant (cell 30: fCamk1 sess13 p = 0.12, fCamk3 sess13 p = 0.29, fCamk5 sess14 p = 0.81). Cell 31 words this correctly ("negative").
  - **Cells 31 and 30, and the record:** "Without the three sessions whose ripples fail the clock check". Only two of the three are in the analysis (fCamk5 sess10 has under 50 first-epoch ripples). n drops by 111 = 70 + 41.
- **Cell 24:** "none of the 364 tests passes, so false positives do not inflate these fractions." The sham tests were run on PreStim only (cell 23), so they cover reading (a). The outcome rests on reading (b), which has no sham test.
- **Cell 57:** "Leaving the laps without stimulation out of the control maps changes little (p = 0.059 and 0.39)". Also the record's fig3f response that this variant was added. The variant cannot differ: dark windows exist only next to deposited pulses, so unstimulated laps already contribute no control time. The control medians are identical (0.714 and 0.527, cell 56).
- **README row:** "Ripple cofiring tracks spatial overlap for place cell pairs only | Reproduced". Cell 62 contradicts "only": place/non-place pairs give rho 0.062 against 0.060 for place pairs.
- **README row:** "Spatial information, control against light | Reproduced" and the Summary row for fig3g: see my disagreement above.
- I checked every other sentence of the Result cells, the Summary, the README and the record's notes against the printed outputs, and they are supported.
- **My round-1 reasons:** the record states them faithfully, close to my own words. It adds the relevant problem numbers (fig1e: 5; fig2b: 4; figs11: 1 and 2; fig3c: 3; fig3f: 10 and 7; fig3g: 7; figs9: 11). It drops the round-1 cell numbers, which would be stale now anyway.

## 3. Round-1 points

**Resolved:**
- **1 (missing pulses).** The device lists 12 uLEDs, the files hold 6 series, and deposited pulses come at 5.76 and 7.50 per s. Control time is now restricted to the dark windows.
- **2 (field rule).** `find_fields` now has the sub-field and dip rules; changing the rule alone moves 1 cell.
- **4 (theta).** The LFP rate and start are now read from the file and checked, the ripple-power check is repeated inside the Maze epoch, control-window spikes have a circular mean of 128 and 130°, and the theta-band light artifact is small.
- **5 (chance level).** N_BOOT is now 500, and 0 of 364 sham tests pass.
- **6 (fig2e ratio).** Now stated in the notes.
- **8 (fig4d).** Moot, since the outcome is now not_reproduced.
- **9 (figs10 unlabelled first epoch).** The variant restricted to labelled sessions gives -0.450.
- **10 (fig3f halves).** Resolved by construction, as above.
- **11 (figs9).** The proxy and the units columns are now printed.
- **12 (paper's counts).** Now recorded as a finding.
- **Section C items.** All answered except the Methods.

**Remaining, bearing on a conclusion:**
1. **fig3g (problem 7).** The outcome should be partially_reproduced, as argued above.
2. **No chance level for reading-(a) light fields.** This affects fig3c reading (a), and the unmasked groups in fig3e to fig3g. Reading-(a) light maps use only the uLEDs each cell responds to, so they have less time than the all-uLED light maps (12.1% and 10.7% of lap time, cell 35). Yet the thinned null (15.8%, cell 49) is matched to the all-uLED time of reading (b). All 7 unmasked cells have light fields in both directions (14 field directions, cell 51), against 70 directions for 48 place cells. Noise fields from sparse maps may explain part of the 77.8%.
3. **Problem 3 (two sessions, one mouse).** The record now states it, with intervals. Still, fig3a and fig4c changed outcome with the place-cell calls alone, and fig4c rests on sess9.
4. **Minor: the dark-window premise.** It assumes every offset is at least 20 ms. In PreStim, 3 to 4% of deposited end-to-start offsets are under 10 ms or negative (cell 11), so the stated protocol does not hold exactly.
5. **Methods.** The supplement is still unavailable, so the response test, field rule and control rule remain unchecked against the paper.
