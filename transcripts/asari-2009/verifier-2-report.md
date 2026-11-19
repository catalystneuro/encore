**Verifier report, round 2: Asari & Zador (2009), CRCNS ac-1**

The claims file has 21 claims and the attempt record has 21 outcomes: 7 reproduced, 7 partially reproduced, 4 not reproduced and 3 blocked. "Cell N" means `reproduce_asari_2009.ipynb`; "STRF cell N" means `strf_wehr.ipynb`. I found no new place where the claims file misreads the paper. I checked Table 1 again: the row sums in fig8a's criterion match it.

One correction to my own round 1: my outcome table left out figs1-silence-probe, which I covered only in problem 5. The record draws its figs1 entry from that problem, which is fair.

### 1. Outcomes

| claim | agree? | notes |
|---|---|---|
| methods-recording-counts: partial | yes | |
| a1-mgb-firing-rates: partial | yes | |
| fig2-example-reliability: reproduced | yes | |
| fig2-example-long-context: reproduced | yes | |
| fig3a-proportion-significant: partial | yes | |
| fig3a-significance-decay: partial, assumed | yes | Assumption (sizes ≥ 0) is stated and reasonable. |
| fig3b-fractional-power-decay: not reproduced | yes, but see below | |
| timescale-longer-than-membrane: reproduced | yes | |
| fig4-predictability-upper-bound: partial | yes, but see below | |
| fig4-strf-performance-low: not reproduced, assumed | yes | The 16-cell choice is forced by Eq. 52 and is stated. It is reasonable. |
| fig5 / fig6: blocked | yes | |
| fig8a-proportion-by-property: partial, assumed | yes, fragile | See below. |
| fig8b-decay-by-property: partial | yes, with a gap | See below. |
| fig8a-significance-fits: not reproduced | yes | |
| fig8c-relative-effects: not reproduced, assumed | yes | See below. |
| fig8-natural-synthetic-probes-alike: reproduced, assumed | yes | The assumption is the claims file's own test. It is stated in the deviations, though not labelled "Assumption." |
| fig9-mgb-fast-decay: reproduced | yes | |
| fig9-example-first-bin: reproduced | yes | |
| fig7-example-frequency-context: blocked | yes | |
| figs1-silence-probe: reproduced | yes | It rests on the criterion's own wording (a first crossing), and the record says so. |

**fig3b against fig4 consistency.** Neither criterion defines a partial outcome, and the two are graded differently:
- fig4: 1 + α₁ is within tolerance in 10 of 14 fits, τ is not, and the outcome is partial.
- fig3b: α₁ is within tolerance in all 4 silence-counted readings (cell 29), τ is not, and the outcome is not reproduced.

I accepted this split in round 1 without asking for a reason. Either the two should be aligned, or the record should say why "about half" counts for fig4 while α₁ ≈ 0.46 does not count for fig3b.

**fig8a assumption (each natural sound tested against its own noise).** It is stated, and Table 1's legend supports it. Two things weigh against it, and the record should set them beside it:
- Only the pooled grouping gives Table 1's exact 137 higher-order probes; the pairing gives 131 (cell 38).
- Under pooling, the order AM > FM > higher-order fails by 0.640 against 0.642, which is 16/25 against 88/137.

The partial outcome does hold under all three readings that do not pool, so I accept it.

**fig8b gap.** Its criterion uses "the probes of fig8a-proportion-by-property". But its higher-order group is the pooled one, not the pairing adopted for fig8a. The partial rule (higher-order τ < 0.3 s) was never run under the adopted grouping.

**fig8c assumption (the bias correction).** It is reasonable. I checked `power_resampled` (asari.py:1043) by hand: it takes the weighted mean of x_a·x_b over draws of different original trials, which is unbiased. I could not run it, because numpy is not installed here. The outcome does not hinge on the correction anyway: the point estimates (0.67 and 0.58) and the probe-resampling intervals fail on their own.

### 2. Statements the printed numbers do not support

- **Cell 42 and the fig8b notes:** "only AM is within tolerance." Cell 41 prints `tau_within False` for AM in all four readings. τ = 0.097 (or 0.090 with per-probe centering), which is outside 0.11 ± 0.011, i.e. 0.099 to 0.121. No time constant is within tolerance. The outcome does not change.
- **STRF cell 7 and the fig4-strf notes:** "The gain comes from the 6 cells of 2003." STRF cell 6 shows the 2002 cells gaining as well, from 0.093 to 0.118, with 7 of 10 improving (p = 0.12). The gain is larger and only significant in the 2003 set; it does not come from it alone. "With the 2002 cells alone the claim of absence would hold" is correct as a test result.
- **Cell 65 (Summary):** "it holds Asari's current-clamp and MGB recordings with the sample sizes of the paper." The data set holds 145 and 14 cells against 194 and 16, and 133 cells meet the criterion against 123 (cell 8). Only the analysed natural-sound and MGB samples (305/39 and 93/14) match. The record's own data_missing finding says this correctly.
- **Cell 65, the fig8a deviation, and the methods_unavailable finding:** the groups "reproduce the paper's totals for amplitude, frequency and higher-order (95, 110, 137)."
  - The amplitude and frequency totals match only by counting 25 + 25 probes from the natural-sound variant files (5 cells), which Table 1 has no row for.
  - Meanwhile, Table 1's 25 + 25 MHT probes (in 20–21 cells) are absent, TORC has 42/44 against 39/40, and natural sounds 20/21 against 23/25 (cell 8).
  - 137 holds only under the pooled grouping, not the adopted one (131).
  - The totals should not be offered as evidence that the grouping is right.

Every other sentence I checked matches the printed output: the Result cells 9 to 63, STRF cell 7, the Summary table rows, the README (run times 37 and 21 minutes against "about 40" and "about 20") and the record's notes and findings.

The record's `verifications` entry states my round-1 reasons faithfully and in my terms. Its values (p = 0.003, 0.143, 4.97 → 6.76 and 0.98 → 2.77, 1.41 mV², and so on) match my report, and the `agrees` flags match my round-1 outcomes.

### 3. Round-1 points

**Resolved:**
1. fig8c bootstrap bias: a corrected estimator is used, its intervals contain all five point estimates, and the biased reading is set aside.
2. Per-probe centering: it is now a variant that decides nothing, and CxtDep.m lines 346–347 are printed.
4. Colored-noise grouping: the alternatives were run.
5. figs1: the 100-ms bins and the peak are printed, and the outcome is tied to the first-crossing wording.
7. Experiment 3: a table is printed; it has no sequences, no sounds back to back, and a smallest gap of 0.54 s.
8. Nothing was needed.
9. `_runs`: CxtDep.m line 313 (last index minus first ≥ 50) gives 51 points, so the helper follows the code.
10. Fits at the 100-s bound are flagged and not used.
11. The frame shift is applied and the band range is stated. A centred 10-ms frame still reaches about 3 ms past its bin, which is negligible against A1 latency.
12. Both noise-floor windows are printed.

All section C requests were met: the per-file table, the experiment-3 table, the CxtDep.m lines, the tie share and midranks (187 of 305 either way), the figs1 bins, the per-set Wilcoxon tests, and the corrected fig8c intervals.

**Mostly resolved:**
- **Point 3:** the per-file table locates the AM/FM shortfall in the files. 27 MHT files hold 14 MHT probes against 178 tests in Table 1, and the parser drops no notes line.
- **Point 6:** the per-set tests, per-cell table and LN cell count were added.

**Remaining points that bear on a conclusion:**
- The fig3b and fig4 outcomes are graded inconsistently (section 1).
- fig8b's partial rule, and fig8c's higher-order interval, were not run under the higher-order grouping adopted for fig8a.
- The fig8a partial outcome rests on an assumption that the exact 137 count weighs against. The record should state this, together with the 0.002 margin by which the order fails under pooling.
- Cell 42 and the fig8b notes wrongly say AM's τ is within tolerance.
- Three overstatements need correcting: "the gain comes from the 6 cells of 2003", "with the sample sizes of the paper", and "reproduce the paper's totals (95, 110, 137)". They appear in STRF cell 7, cell 65, the fig8a deviation and the methods_unavailable finding.
