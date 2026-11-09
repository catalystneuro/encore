**Verifier report, round 2: Silkuniene et al. 2025 on DANDI:001276 (0.250701.1609)**

The claims file has 23 claims, and the attempt record has 23 outcomes:

- 7 reproduced
- 4 partially reproduced
- 2 not reproduced
- 10 blocked: 8 as "other" and 2 as data_missing

Four outcomes are marked `assumed: true`: fig7be, fig7-sharpest, fig7-offtarget and fig4b-40-fold.

### 1. Outcomes and assumptions

| Claim | Agree? | Comment |
|---|---|---|
| fig7be-center-linear-with-bursts (partial, assumed) | Yes | The assumption is stated. The CT26 p is 0.0013 without well P1_20240627_B1 and 0.00098 with it, under reading (a) (cell 21), so the outcome turns on that one well. Leaving it out is reasonable, but the stated reason is weak (see section 2, cell 12). |
| fig7b-ct26-saturation (partial) | Yes | Saturation is now ruled out: at most 5.4e-4 of the pixels in any diagonal ROI are at full scale, and none at the center (cell 15). |
| fig7cf-fwhm-with-bursts (reproduced) | Yes | Both parts hold in 2 of the 12 readings (cell 27). The pass is fragile, and the record now says so. |
| fig7-sharpest-peak-one-burst (reproduced, assumed) | Yes | The 0.5 mm spacing assumption is stated and reasonable. At 1 mm spacing the outcome would be partial (cell 30). |
| fig7-offtarget-40-50-fold (not reproduced, assumed) | Yes | The median background is stated as an assumption and is reasonable. With one footprint per well, 62.5% of the 64 combinations put a 6 mm reading in range (cell 33), so the data do not settle this claim. |
| fig7-cho-replicates-ct26 | Yes | |
| fig4b-40-fold-at-02mhz (not reproduced, assumed) | Yes | The assumption is stated and reasonable. With one footprint per well, 42.3% of the 1024 combinations put a reading in range (cell 39). The mean-of-ratios reading is unstable: it gives -11.90 with the lower-right footprint and 140.53 with the lower-left one. |
| fig3a-cancan-center-enhanced (partial) | No, I keep not_reproduced | The control is the half of the claim that makes it a contrast, and it fails: the control's center is its brightest point (2275 against 1837 to 2085 a.u., cell 42). The CANCAN half is tested on only 2 of 4 rates. The record states my disagreement correctly. Without the protocol in front of me I cannot rule out "holds only in part". |
| fig3bc-lorentzian-profile, fig3bc-offtarget-deviation, fig4b-center-no-rate-effect, fig4b-near-electrode-rate-decline, fig4c-fwhm-decreases-with-rate | Yes | |
| fig4c-log-dependence (blocked, other) | Blocked: yes. The "other" category: not supported | The record itself says that whether DANDI:001047 holds 1 kHz and 10 kHz "was not established", and that its description names only 1 Hz and 0.2 MHz. Unless that is shown, this is data_missing. |
| fig5 ×3, fig6 ×3 (blocked, other) | Yes | Dandisets 001284 and 001277 describe these series. I could not check the protocol's definition of "other". |
| fig5c-irreversible-center (blocked, other) | No | The criterion asks only that Hoechst inside the footprint be "above background". It does not require post-exposure images. Cell 66 shows Hoechst in every footprint at 20 to 60 times the camera offset and 0.74 to 0.99 of the monolayer, and the YP part holds. The only block the claims file supports is the undefined reference level, an open item, which makes this methods_underspecified. The alternative is reproduced, with the camera offset as an assumed reference. The author's point that the paper's Hoechst check was made after exposure (Methods 2.4, Results 3.2) is a fair reading of the paper. It suggests the claims file's criterion omits the timing, and it should be reported that way. It should not be decided by adding a requirement to the test. |
| fig2-heating-below-44c, fig1e-field-simulation (data_missing) | Yes | |

### 2. Text the printed numbers do not support

- **Cell 40:** "with the upper-left footprint the ratio at 6 mm is 35.75 and 38.41 … so single footprints put it in range". The value 35.75 is outside 36 to 44; only 38.41 and 40.38 are in range (cell 39).
- **Cell 12, and the fig7be response in the record:** the left-out wells' "smallest corner contrast (0.013 to 0.045) is below the median of the wells used (0.333), so the placement is less certain". Cell 9 shows wells that are used with smaller minimum contrasts: P1_20240827_B3 at 0.000, P1_20240702_A2 at 0.004, P1_20240813_B2 at 0.027, P2_20240821_B2 at 0.036 and P1_20240918_B3 at 0.044. The contrast does not separate the left-out wells from the used ones.
- **Cell 68 (Summary):** "with them added … the CT26 slope … reaches p < 0.001". This is true only under reading (a), at 0.00098. Under reading (b) p is 0.059 (cell 21). Only one of the three added wells is CT26.
- **Cell 68:** "for most groups are more than the paper's n" and "The well counts exceed the paper's". In cell 3, CT26 has 2 wells at 1 Hz CANCAN against the paper's 3, and 4 controls against 5. CT26 at 1, 4 and 6 bursts has 3 wells, inside the paper's 3 to 5.
- **Cell 0 table, cell 68, README row "Figures 4C (log fit), 5 and 6 … Blocked: in other dandisets":** "a rate series is in DANDI:001047" does not establish that the 1 kHz and 10 kHz wells are there. The record says this was not established.
- **README:** "Three outcomes rest on choices the paper leaves open: which wells … and which electrode footprint". Four outcomes are marked assumed. The ROI spacing behind fig7-sharpest is missing from this sentence, though the README table marks that row "(assumption)".
- **README:** "It takes about 25 minutes". The notebook prints no total run time; cells 1 and 7 together account for about 20 minutes. This is minor.

All other "Result:" sentences, the rest of the Summary and the record's notes match the outputs. I checked every figure the notes quote against cells 21 to 66.

The verifications block states my round-1 reasons faithfully and in my own terms.

### 3. Round-1 points

**Resolved:**

- Point 1, background: the single-footprint and per-well-combination variants are shown, and the median is declared an assumption.
- Point 2, well exclusion: the variant with the left-out wells is shown, and fig7be is marked as resting on it.
- Point 4, pixel size: now read from the OME-XML, along with exposure.
- Point 5, fig5b YP half: computed. R² is 0.979 for the Lorentzian against 0.975 for the Gaussian.
- Point 6, fig7cf fragility: stated.
- Point 7, sides geometry: the variant with ROIs inside the side midpoints is shown.
- Point 8, degrees of freedom: p with two fewer degrees of freedom is printed.
- Point 9, center bias: documented in the helper, not corrected.
- Point 10, well provenance: stated as a deviation.
- Section C, saturation, Hoechst in the footprint and excluded wells: all now computed.
- Section C, square fits: I have now viewed the figures in cells 10 and 11. In the wells used, the squares sit on the footprints. One corner of P1_20240827_B3 lies off the imaged area, which the median background absorbs. In the variant placement of P1_20240627_B1, the square sits on faint footprint rims with the YP spot near its center.

**Remaining, bearing on a conclusion:**

1. fig5c: the outcome should be methods_underspecified, or reproduced under an assumed reference, not blocked as "other". The post-exposure question should be raised as a gap in the claims file.
2. fig3a: I keep not_reproduced.
3. fig4c-log-dependence: "other" rests on an unestablished claim about DANDI:001047.
4. fig7be: the outcome turns on one well, and the stated reason for leaving it out, its corner contrast, does not hold (cell 9). The assumption should be kept with a correct justification, or stated as open.
5. The text corrections listed in section 2, in cells 40, 12 and 68 and in the README.
