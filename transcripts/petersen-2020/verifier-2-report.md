**Verifier report, round 2: Petersen & Buzsáki (2020), attempt petersen-2020-02**

**1. Outcomes**

The claims file has 46 claims and the attempt record has 46 outcomes, one per claim: 17 reproduced, 19 partially reproduced, 8 not reproduced, 2 blocked. Twenty outcomes are marked `assumed: true`.

In round 1 my table left out suppl2d-interneuron-oscillation-slows, as the record says. I agree with its partially_reproduced. Interneuron frequency falls (P = 6.4e-13) and pyramidal cells oscillate faster before cooling (10.42 against 8.93 Hz). The decrease is 5.8 to 8.7%, outside 12.6 to 15.4% (cell 111).

I agree with every other stated outcome, with two caveats:
- **fig4d-precession-slope-decrease (partial, assumed).** The partial rule is met only by cooling against pre, P = 0.016, at 2 cycles and 5 cm. That result depends on the 8 to 10% of fields at the slope bound. Without them, the P values are 0.090 and 0.20 (signed 0.077 and 0.080), and with 3 cycles the magnitude test against pre gives 0.149 (cell 83). The outcome holds under the criterion, but it is weak.
- **fig5cg-compression (blocked, methods_underspecified).** I agree the claim cannot be decided from these fits. I do not agree with the stated reason (see section 2).

The assumptions:
- **Field map** (fields found on the map over all trials, states pooled): stated in all 20 assumed outcomes, reasonable, and the record asks the authors about it.
- **Slope range of ±2 cycles** (fig4d, suppl3e): stated and reasonable. suppl3e has the same outcome under 1 cycle.
- **Phase lag as the largest peak within π** (fig5i): stated. It is a claims-file reading, but it is the one that favours this claim of absence. Lag reading (b) gives P = 2.7e-8. With pair reading (b) and without MS13-171130, reading (a) also fails (P = 0.040, cell 129).
- **fig5cg** lists the field-map assumption in its deviations but has no `assumed` flag. This does not matter while it is blocked.

**2. Sentences the printed numbers do not support**

- **Cell 5, Summary ("What was found"), and the record's tracking-rate metadata_error.** They say every behaviour description gives 40 Hz. Cell 4 prints the rates the descriptions give as `['120', '30', '40']`, so the descriptions differ between sessions and may match the timestamps. As stated, the finding is not supported.
- **Summary, "values from -1751 C to 1354 C".** These values are not printed anywhere; cell 4 prints only counts of samples outside 5 to 45 C. The same applies to some values in the findings: 8.68 to 8.27 Hz, 7.53 to 8.13 Hz, and 25683 s / 28409 s.
- **Cell 60 and the suppl2 notes, "no P is below 1e-6".** Cell 59 prints 6.24e-07 (3 cm bins, Figure 5 rule fields, peak rate). The outcome does not change.
- **Cell 77, "P above 1e-9 in two states".** All three are above 1e-9; cooling is 1.1e-9 (cell 76).
- **Cell 93, "MS10 never does".** With normalised spectral power, MS10 has P = 7.2e-6 at R = −0.123 (cell 92). That also means the "4 of 5" for spectral power includes one negative R.
- **Cell 26, "over 50 sessions … under each of the three state readings".** The 12 and 10 min readings have 49 sessions (cell 25).
- **suppl1g notes, "P = 2.2e-4 to 0.043".** The per-session interpolated P values run from 9.9e-7 to 0.043 (cell 145).
- **fig4d: cell 84, the notes and the README** leave out the result without bound fields printed in cell 83 (no comparison significant). The README's "flattens during cooling against pre but not post" holds only at 2 cycles. At 3 cycles the significant comparison is the signed slope against post (P = 0.037), and pre gives 0.149 (cell 83).
- **fig5cg: cell 134, the notes, the README and the finding** say the surface "does not describe the density". The numbers do not show this. In both readings, as b grows without limit the oscillation term becomes constant and the surface becomes the envelope alone. The envelope alone fits with a per-session median R2 of 0.41 to 0.68 (cell 133). So converged fits with R2 of −0.10 to −5.1 are stuck short of the best fit; they do not show what the best surface fit would give. The outputs show that the fit failed.
- **README, "phase lags do not change".** This holds only under lag reading (a) (cell 129).
- **README, "The place field features of Figure 3 … are not reproduced".** fig3d is partially reproduced (cell 77) and fig3hi is reproduced (cell 115).
- **fig5h notes, "Both cooling comparisons hold under every reading".** Under lag reading (b) with pair reading (a), post and cooling medians are both 16 ms, with rank-sum P = 0.85 (cell 127). The tests are significant, but a longer cooling lag is not shown there.

Everything else I checked in the conclusions, the Summary, the README and the notes matches the outputs. The README totals match the attempt record.

The record states my round-1 reasons in my own words, close to verbatim, and correctly says my round-1 table had 45 rows. One small misfiling: my problem 12, which was about the fig5d session readings, is filed under fig5-speed-control-cooling instead of fig5d.

**3. Round-1 points**

Resolved:
- Problem 6: peak spacing is now printed, 107.2 and 103.5 ms.
- Problem 7: no in-trial sample below 15 C; the lowest trial temperature is 17.1 C.
- Problem 8: results without MS13-171130 are shown for fig2i, fig6c, fig6h and fig5i.
- Problem 9: medians and a one-sided test are added.
- Problem 10: interpolated latency and spike counts are added.
- Problems 11, 12 and 13.
- Problem 4: now stated in the notes.

Partly resolved:
- **Problem 1.** The slope range is now ±2 cycles, stated as an assumption, with the fraction at the bound printed. The fig4d result still depends on the fields at the bound.
- **Problem 2.** Fit errors, convergence counts, start values and a plot are now printed. The change to "blocked" brings in the overstated reason above.
- **Problem 5.** Information is now computed with equal trials per state. Equal trials do not mean equal data: speed falls within sessions (cell 54), so later trials hold more time and spikes, and the remaining pre-to-post fall (−0.030 bits per spike, P = 0.016) could still be a sampling effect.

Unchanged: problem 3. Under the criterion, partial is correct.

What remains that bears on a conclusion, and the output that would settle it:
- **fig4d.** Either state the bound-field dependence in the conclusion, or treat the outcome as unsettled until the authors give the slope range.
- **fig5cg.** A bounded or multi-start fit, for example with b held near the summed period of 104 to 109 ms, or started from the envelope solution. That would show whether the surface fits the density. Until then, the reason for "blocked" should say the fit failed.
- **fig3f.** Skaggs information with an equal number of spikes or equal occupancy time per state, or a shuffle-corrected version.
- **fig5h** (pre against post P = 0.034 at equal medians) **and fig5j/fig5k** (pooled-cycle rank-sum P = 1.6e-25 and 4.9e-7, against per-session P = 1.0 and 0.80). These tests count pairs or cycles that share cells and sessions as independent. A per-session or session-stratified test would show whether these outcomes reflect cooling or the sample size. The criteria fix the tests used, so the stated outcomes stand.
