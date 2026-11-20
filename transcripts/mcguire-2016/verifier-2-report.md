**Verifier report, round 2: McGuire et al. 2016 (doi:10.1371/journal.pbio.1002549) on CRCNS ssc-4**

The claims file holds 37 claims and the attempt record has 37 outcomes, one per claim: 25 reproduced, 10 partially reproduced, 2 not reproduced, 0 blocked. Ten of them are marked `assumed: true`: fig6e, fig6fg, fig7-fff, fig7-sss, s4, fig7de, fig8d-slow-positive, s5, fig9b-slow-chance and fig9d. I again found no place where the claims file misreads the paper.

### 1. Outcomes and assumptions

I agree with all 37 stated outcomes.

**Outcomes that changed since round 1, all marked assumed:**

- **Main unit set.** The attempt now uses the deposited modulated set (`TemporalPval < 0.05`) as the main set. This is stated, and it is reasonable: the descriptor names that set as the paper's units, and no recomputation reproduces it.
- **fig6e and fig6fg: now reproduced.** On the deposited set the four classes equal the deposited labels unit for unit, and all six laminar values are within tolerance (cells 56 and 60). I agree.
- **fig7de: now reproduced. I withdraw my round-1 disagreement.** The criterion asks only for three negative means and two non-significant paired tests, and the deposited set meets both (cell 80). In round 1 I asked for a test of suppression, which the criterion does not require. The effect is tiny (−0.27 to −0.52 Hz, p ≥ 0.45 against 0), and the notes say so.
- **fig8d-slow-positive: now reproduced.** This passes on reading (a) only, and only just: L5a p = 0.049 with n = 7 (cell 89). It fails under reading (b) and on the recomputed set. The record states this. I agree.
- **fig7-fff: now reproduced.** The criterion defines the units as Fast RS units that pass the impulse t test, but the attempt uses all 62 Fast RS units. This is stated and reasonable: the paper's n = 61 is close to 62, and every t-test reading selects 29 to 37 units. Every one of those t-test selections fails, so the outcome rests entirely on this assumption (cell 71).
- **fig7-sss and s4.** Both use the same 62 units. For s4, every selection gives FMS lower with p ≥ 0.06, so its assumption does not bear on its outcome.
- **s5: now partially reproduced.** I agree. On the deposited set the 25-ms baseline fails on the right-choice ANOVA (p = 0.016). The 10-ms baseline fails only on the left-choice correlation with the speed of pulses 2 and 3 (r = −0.96, p = 0.04, n = 4). That fit uses the impulse speeds now taken from S1 Fig; the earlier Table 1 ramp gives p = 0.05 (cell 98). See section 3.
- **fig9b-slow-chance and fig9d: now partially reproduced.** I agree. The slow decoder scores 33.9% but is above chance by test (a), p = 0.027. The fig9d Fast/Medium single-bin value is 38.2%, 0.5 points under the tolerance band.

**Outcomes that did not change:** I agree with these as stated. fig9e, still reproduced, now rests on test (a) alone (p = 0.060); the binomial test gives p = 0 (decoders cell 17).

### 2. Text against printed outputs

Nearly every sentence matches the printed numbers. These do not:

- **Decoders cell 21 and the fig9f notes.** They give "72.7% and 75.8% with C by cross-validation" and "65.2% and 76.1%". The cell 20 printout gives 72.8%, 75.8%, 65.3% and 76.2%, so these look like values left over from an earlier run.
- **Decoders cell 21.** It says the unweighted fits "fall to 50 to 54%". The printout includes 56.0% (Slow, draws ii). The attempt record says "50 to 56%", which matches the printout.
- **latency-by-layer `measured`** (15, 19, 15, 17, 21). These are the one-sided centred medians, the reading under which the ordering fails (cell 47, row 1). The partial outcome rests on the two-sided reading (rows 8 and 9).
- **Cell 96 and the fig8d-fast-medium notes.** They say "28 to 32 ms", but 30 ms is not significant: the printout lists [28, 29, 31, 32, 91] (cell 95).
- **fig9d notes.** "The first run ... gave 39.4%" refers to the earlier run; the current notebook does not print a recomputed-set single-bin decoder.
- **baseline-rates.** The criterion says "over all trials", but the main table uses completed trials (cell 34). The notes mention the all-trials value (11.49 Hz), but the deviations list leaves it out. The outcome is the same either way.

The Summary sections (cell 106, decoders cell 25) and the README match the outputs. The README's "three claims use the paper's supporting data" is correct: fig2d, fig3 and s6.

The `verifications` entry restates my round-1 reasons and points B1 to B11 accurately and in my own terms. It records my fig7de disagreement correctly (`agrees: false`, not_reproduced).

### 3. Round-1 points

**Resolved:**
- B1: the attempt switched to the deposited set, kept the recomputed set as a variant, and ran the bin-shuffle null (cell 37).
- B3: the guard is now pulse 1 > 1 Hz.
- B4: forward, trailing and unsmoothed latencies were added, and ties are fixed; no reading puts all five layers within tolerance.
- B5: balanced training is stated, and accuracy is now shown against the number of units.
- B6: the notes now say that test (a) is not a null distribution.
- B7: impulse speeds now come from S1 Fig.
- B8: session counts are added.
- B9: S1 Table is added, and the 33 extra units are located by layer.
- B10 and B11.
- Every item in my "could not check" list was run.

**Remaining points that bear on a conclusion:**

1. **fig7-fff-adaptation (B2).** This is reproduced only if all 62 Fast RS units are taken as the paper's 61. No t-test selection meets the criterion. The assumption is stated and plausible but cannot be checked against the data.
2. **Unit-set dependence (B1).** Seven outcomes change between the deposited and the recomputed set: fig6e, fig6fg, fig7de, fig8d-slow-positive, s5, fig9b-slow-chance and fig9d. All are marked assumed, but how the deposited p-values were computed is still unknown (the record lists it as a question for the authors). fig8d-slow-positive also hangs on L5a p = 0.049.
3. **s5 impulse speeds (new, from B7).** The 0.2-mm span rule gives the M impulse 123.7 mm/s in FMS but 103.3 in SMF, and the first F impulse 135 against 151 for the later ones (cell 98). This suggests the spans are not capturing comparable parts of each impulse. Under the 10-ms baseline, whether that reading meets the criterion turns on this extraction (p = 0.04 here, 0.05 with the ramp). Under the 25-ms baseline it fails anyway on the deposited set, so the outcome could go from partial to reproduced only through the 10-ms baseline.
4. **fig9e (B6, carried over).** "Abolished" is met only by test (a) at p = 0.060, which is not a null distribution; the binomial test gives p = 0 and the 32% reading is not met. The criterion allows this, so the outcome stands, but it is weakly supported.
5. **fig9d.** The miss is 0.5 points (38.2 against 38.7). The partial outcome is correct but sits at the edge of the band, and the previous run on the recomputed set gave 39.4%, inside it.
