**Verifier report, round 2: Drieu, Todorova & Zugaro 2018 (doi:10.1126/science.aat2952) on CRCNS hc-18**

The claims file has 35 claims and the attempt record has 35 outcomes: 13 reproduced, 13 partially reproduced, 9 not reproduced, none blocked. I agree with 32. I disagree with 3: figs7, figs8 and figs10.

### 1. Outcomes and assumptions

**Outcomes I disagree with**

- **figs7-control-cell-count: partially reproduced in the record; I find not reproduced.**
  - The criterion's partial clause is "Active effects hold at 0.001 only".
  - In the normalized-score effect, Active is not highest: Passive 2 has median 0.659 and Active 0.643.
  - Passive 1 against Passive 2 slopes gives P = 0.0049, where the claim needs P > 0.05.
  - Neither the reproduced rule nor the partial rule covers this (controls cell 9).
- **figs8-control-firing-rate: partially reproduced in the record; I find not reproduced.**
  - Under rate reading (a), the score Kruskal-Wallis gives P = 0.0048, which is not below 0.001, and Passive 2 is highest.
  - The rates still differ (P = 0.02).
  - Under reading (b), the slope comparison Active against Passive 2 gives P = 0.0075.
  - So the Active effects do not hold at 0.001 under either reading (cell 12).
- **figs10-control-lap-variability: partially reproduced in the record; I find not reproduced under the assumed reading.**
  - The assumed reading (a), each lap decoded with its own firing curves, is stated and reasonable.
  - Under it, Passive 2 (1.207) is above Active (1.193) on normalized scores, so that Active effect fails. By the letter of the criterion this is not reproduced.
  - Reading (b) passes every part, except that only the Kruskal-Wallis is printed for scores, with no Active against Passive 2 post hoc test (cell 15).
  - Neither reading gives "partial".

**Outcomes I agree with, with caveats**

- **figs2b-place-cell-count (partial, assumed field reading c).**
  - The assumption is stated.
  - It is reasonable: it follows the claims file's rule of using the Methods where they speak (4.5 cm kernel) and the code where they are silent (field size and spike limits).
  - It was adopted after round 1, and under the claims file's readings (a) and (b), and the code's own settings, the claim is not reproduced.
- **fig1c-field-size-similar (not reproduced).** Agree.
- **fig1d, fig1e, figs2d (partial, assumed).**
  - Each rests on 1 of 8 readings (fields b, cells in both, linear correlogram); this is now stated.
  - They were not rerun under the field reading (c) adopted for figs2b.
- **fig2b-theta-power-reduced (reproduced, assumed per-window reading).**
  - This follows the claims file's reading (b): P = 2.1e-4, and the post hoc tests pass.
  - The test treats about 3000 windows as independent. With one value per rat, P = 0.044 to 0.17.
  - The per-window test was run only for LFP reading a with moving samples.
- **fig3g-theta-self-consistency and fig4g-theta-replay-correlation-active (not reproduced).** Agree.
  - Neither sequence reading reproduces, so fig3g's `assumed: true` is unnecessary.
  - Every condition, Active included, comes out below the 5% chance level (3.8–4.1%). This fits the discrete surrogate test: `np.mean(sur >= rho)` over spike-order shuffles of single theta cycles with few spikes. With 3 cells and one spike each, there are only 6 orderings, so p cannot fall below 1/6.
  - This may be how the paper's test works too, but the paper's tie handling is not shown.
- **All other outcomes:** agree, with these notes.
  - figs4de has little power (12 and 20 cells).
  - figs4b's oscillation half rests on spectral modes within 0.001 of 1 cycle⁻¹, and its denominators use field reading (a), not the adopted (c).
  - fig3e and fig4d rest on the claims file's region bounds, as stated.

**Places where the claims file misreads the paper (reported, not corrected)**

- fig2cd and figs4b: the Methods say spectrograms, not one spectrum (my round-1 problem 7; still open).
- fig2b-theta-power-reduced: the statement includes "power reduced at both the fundamental and the first harmonic", but the criterion only reports the harmonic. The harmonic is not reduced (P = 0.58–0.77).
- figs7, figs8, figs10: the criteria do not say what happens when one part fails outright. They give a partial outcome only for "Active effects hold at 0.001 only".

### 2. Text against the printed outputs

**Statements the numbers do not support**

- **Travel/sleep cell 44**, "both below 0.05 but not 0.04", and **record fig2f** notes, "neither below 0.04": the KS test of Active against Passive 2 gives P = 0.027, which is below 0.04 (cell 43). The outcome does not change.
- **Decoding cell 32** and **record figs9**, "the median 500-ms error equals Active's in each rat": in rat 292, Passive 2 is 0.387 against Active 0.479 (cell 31).
- **Controls cell 19** and **record figs9**, "median errors rise (pooled after restriction 0.487, 0.627 and 0.525 m": these numbers are means ± s.e.m. (cell 18).
- **Controls cell 7**, "Reading (a), with 100 shuffles, gives the same as the decoding notebook":
  - The proportions are 7.79/12.51/10.59% against 7.34/12.04/9.86%.
  - Which values fall within tolerance changes: Active moves inside and Passive 2 moves outside.
- **Controls Summary, cell 29**:
  - "not in normalized scores, where Passive 2 is as high as Active": under lap reading (b), Active is highest (0.659 against 0.632; cell 15).
  - "Pairwise bias correlations find no self-consistency … above chance": under reading (b), Active has 804/15000 = 5.4% significant pairs, and Passive 1's mean correlation is above 0 at signed-rank P < 0.005 (cell 22).
- **Record figs7** notes, "The effect holds in part": see section 1.
- **Decoding Summary, cell 58**, "replay after Active is … forward-biased": this holds on all events, but not on ripple-restricted events (P = 0.096 and 0.081; cell 56).

**Statements no printed output shows**

- Record findings: LED loss "almost all during sleep"; rat 272's LFP saturating in "about 1% of sleep samples"; the ClusterIsolation.m counter bug.
- README: "47 GB".

**Checked and supported**

- Every other "Result:" conclusion in all three notebooks.
- The README's outcome table: 13 / 13 / 9, matching the record.
- The remaining record notes.

**My round-1 reasons in the record:** the `reason` fields reproduce my round-1 text almost word for word, without the cell references. That is acceptable.

### 3. Round-1 points

**Resolved**

- 1, field-entry bug: fixed, with an assert added, and rerun.
- 2, fig4f: fixed.
- 3, other readings: field reading (b) for theta in full; replay on a fifth of events.
- 4, blocked claims: all run.
- 6, theta frequency: 8-s spectra added.
- 10, figs9: a cross-validated error is added.
- 12, V-test: now two-tailed.
- 8, rat 272: the reversed channels are left out.

**Remaining, bearing on a conclusion**

- **Point 5, place-cell definition (partly resolved).** Reading (c) is used only for figs2b and fig1c. Remapping, precession, figs4b, decoding and replay still use reading (a): 207/203/228 cells, with very large fields. The remapping bootstrap, which decides whether fig1d is partial or reproduced, has not been run under (c).
- **Point 7, burst frequency.** The claims file's spectrum reading remains, so the oscillation half of figs4b rests on modes at 1.000 ± 0.001. The spectrogram variant would make fig2cd partial under phase reading (b) only.
- **Point 8, theta polarity (extended).** In rats 292 and 314, spikes fall at −5 to −51° on every channel. The record notes a polarity common to all of a rat's channels is not corrected. If the signal is inverted, the trough-centred phase windows used for the quadrant scores (windows 2–5) and the theta-sequence windows are shifted by about π in 2 of 5 rats. This bears on fig3b, figs5b, fig3f and the controls.
- **Point 9, remapping.** Disclosed, but fig1d, fig1e and figs2d are still partial on 1 of 8 readings.
- **Point 14, pseudo-replication.** This now decides fig2b-theta-power-reduced.
- **New: control outcomes.** figs7, figs8 and figs10 are mislabelled as partial (section 1).
- **New: bias-correlation test.** The significance test's resolution limits fig3g and fig4g.
