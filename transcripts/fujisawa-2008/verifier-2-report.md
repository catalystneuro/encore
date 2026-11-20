**Verification report: Fujisawa et al. 2008, round 2**

All counts come from the claims file and the attempt record: 33 claims and 33 outcomes. The record has 5 reproduced, 12 partially reproduced, 15 not reproduced and 1 blocked (data_missing). Cell numbers below refer to the re-executed notebook, which has more cells than in round 1.

### 1. Outcomes

I agree with all 33 stated outcomes, with three qualifications.

- **fig2c-active-fraction (partially reproduced): I withdraw my round-1 disagreement.** Neither this criterion nor population-vector-width's defines a partial outcome. In round 1 I gave population-vector-width partial for one value in tolerance, so the same rule makes fig2c partial. Under R-a, layer 5 is 20.3% (in tolerance), layer 2/3 is 12.6% (out), and the fraction is constant over the maze (cell 59).
- **rats-and-units (partially reproduced): I agree under the adopted unit list, but the outcome rests on an assumption the record does not mark.** With every NWB mPFC unit the total is 1,373, outside 633 ± 63.3, and no rat has 222 units. That gives not reproduced by the criterion (cell 11). The lab's lists were also chosen because their total matches 633, so the total check is partly circular. This outcome should carry `assumed: true`.
- **fig6-facilitation-depression (not reproduced): I agree, but it rests on a deviation not marked as an assumption.** The claims file says "depression is first above later". The attempt reads this by the tail of the permutation distribution, and that deviation is stated. The literal sign reading was run only with the presynaptic jitter, never with the shared jitter (cell 106). With the presynaptic jitter and the sign reading, depression is above 5% in (b,x,i) at p = 0.044 and in (b,x,ii) at p = 0.013, but facilitation is not.

Assumptions (`assumed: true`) are set on population-vector-width, traj-diverge, central-arm-selectivity, fig4-position-dependence, fig5a, fig4-pair-156-136, fig5b and thinning-preserves-dependence.
- Each is stated in the deviations and is reasonable:
  - population-vector-width: the normalisation of each neuron's rate.
  - traj-diverge: M = 10,000 permutations.
  - central-arm-selectivity: the unit list.
  - fig4-position-dependence, fig5a, fig4-pair-156-136, fig5b and thinning-preserves-dependence: M = 5,000 surrogates, shown to be needed because 17 of 23 tests cannot reject with 1,000 (cell 89).
- traj-diverge is marked assumed in the record, but neither the README nor the Summary table (cell 114) marks it.

### 2. Statements the outputs do not support

- **Cell 12 and the rats-and-units notes:** "so the outcome does not depend on the unit list". Cell 11 shows that under the NWB list the outcome becomes not reproduced.
- **Summary (cell 114):** "only the central-arm outcome would change with it". rats-and-units would change too.
- **Cell 21 and the side-arm notes:** "33.8% (409/1,211)" and "Fisher p = 1.2e-09". Cell 20 prints 33.7% (408/1211) and p = 1.09e-09. The value 1.21e-10 belongs to reading (b).
- **Cell 24 and the central-arm notes:** "15.2%". Cell 23 prints 15.3%.
- **fig6 notes:** "Facilitation is within tolerance in two combinations". Cell 106 shows three: (a,y,i) 10.4%, (b,y,i) 9.9% and (b,y,ii) 11.1%.
- **fig2-field-size notes:** "P-a (c)(i)(x), the first listed reading … that matches". P-a (b)(i)(x) comes earlier in the list and also matches (cell 62).
- **population-vector-width notes:** the measured layer 2/3 value is 0.282 (reading a). The "misses by 0.001" in the notes and in cell 66 refers to reading (b), 0.268 (cell 65).
- **Finding (metadata_insufficient):** "spike times are identical to the lab's for all 627 cells". Cell 3 shows 105 of 117 identical for EE188, 615 in total. The 12 extra cells have no lab spikes to compare against (cell 5).
- **Findings with no printed output behind them** (not contradicted, but not shown):
  - NWB units have cell_type 'not classified' and lab_cell_number −1 in 11 of 13 sessions.
  - DANDI uses EE188's 105-cell list.
  - Cells 32 and 72 are coded as interneurons and appear as presynaptic in `pairs_all`.
- **Cell 54:** "two of 20 P-b tests" fall below 0.05. One of the two (EE.210, p = 0.022) is a shank-against-class test, not a P-b test.

Every other "**Result:**" sentence, the Summary, the README and the attempt record's notes match the printed outputs.

Verification entries: all 33 restate my round-1 outcomes, and their reasons are mine, nearly word for word; the fig6 reason merges B3 and B4 faithfully. The traj-diverge reason keeps my own typo "see B8", which should read B6; the response cites B6 correctly.

### 3. Round-1 points

**Resolved:**
- **B1 (unit list):** compared with spikeph and the NWB units; there is no `Cells` variable; the NWB variant was run. What follows from it for rats-and-units still bears (below).
- **B2 (peak positions):** peaks are now taken from both P-a and P-b, and every session fails under both.
- **B3 and B4 (first/later spike test):** now uses the shared jitter and labels each pair by the tail of its permutation distribution.
- **B6 (head direction):** the LED axis follows the direction of movement (resultant length 0.98). The early angles are far from the wrap, and the re-centred angles give 0.03. So the 0.02 onset is real: it is the turn out of the start box (cell 74).
- **B7:** the troughs were inspected; this does not affect a conclusion.
- **B8:** the one-cell jitter variant was run and finds more connections, not fewer.
- **B9:** fixed; values unchanged.
- **B10:** now reported in the conclusion and the findings.
- **B11:** EE049, FF103, GG097 and GG149 are now named as sessions where the clock check is weak.
- **Section C:** every output I asked for is now printed.

**Remaining, bearing on a conclusion:**
1. **rats-and-units** depends on the unit list. It needs `assumed: true`, and the "does not depend on the unit list" sentences need correcting.
2. **population-vector-width (B5):** the outcome is decided by the normalisation. Peak normalisation gives partial; z-scoring gives reproduced. This is stated and flagged as an assumption, so it remains only as a question for the authors.
3. **fig6-facilitation-depression:**
   - The claims file's literal criterion (raw sign) with the shared jitter is not shown, so the outcome under the criterion as written is unknown.
   - The observed difference lies above the permutation median in only 43% of tests (cell 106). The tail labelling is therefore lopsided overall, so part of the facilitation excess may come from the test itself. This does not change the not-reproduced outcome.
   - As I reported in round 1, the claims file's "first above later" for fig6 and fig6b repeats a misreading of the Figure 6c legend.
