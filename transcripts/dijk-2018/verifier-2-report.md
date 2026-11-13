**Verifier report, round 2: van Dijk & Fenton 2018 on CRCNS hc-17**

The claims file has 44 claims. The attempt record gives 44 outcomes: 23 reproduced, 3 partially reproduced, 14 not reproduced and 4 blocked (data missing). I ran nothing from the notebook. I read the new pooled-error LSD code (`H.mixed_lsd`), which compares level means using the mixed model's own covariance; it is a sound way to do Fisher's LSD after a mixed model.

### 1. Outcomes and assumptions

**I agree with all 44 outcomes.** Two changed since round 1:
- **fig3b-avoidance-learning** is now not reproduced, which was my round-1 position. It also fails with WT15's first 10 min (p = 0.067) and with WT15 left out (p = 0.17) (cell 57).
- **fig4d-room-ipos-near-active-zone** went from partially reproduced to reproduced. I agree. With the pooled error that the criterion's Fisher's LSD implies, conflict is above pretraining (p = 0.028) and above training (p = 0.012) near the conflict zone (cell 126). The result is fragile:
  - With 16-px locations, the room plus arena normalizer and the paper's df, conflict against pretraining is p = 0.055.
  - Paired t tests over mice fail (p 0.060 to 0.20).

**Assumptions:** 18 outcomes are flagged `assumed: true`. Each one names its open reading (M2/M5, M6, M10, M11, the class reading, or the speed session reading), and each choice is reasonable and argued. Two outcomes are `assumed: false`: standardized-rates-no-difference and network-consistency-overall. Both readings now agree for each, so I accept that. No unflagged outcome rests on a reading that changes it.

One deviation is not true. fig6-inset-rate-changes says "Reading (a) is shown beside it", but cell 109 runs only M11 (b) (`MAN_ADOPT`).

**Claims-file readings to report, not correct:**
- **Information content (Tables S1/S2):** the claims file takes the "bits/s" label literally, but the values match bits per spike (cells 31, 37). The record now raises this as a paper inconsistency.
- **Mean ISI (Table S1):** the 5.77 ms in the table cannot be a mean interspike interval; the files give seconds (3858 ms, cell 31).

### 2. Text against outputs

These sentences are not supported by the printed numbers:
- **Cell 84, and the pc-int-pair-classes notes:** "All readings give 152 pairs". Cell 83 shows that readings (a)(ii) and (b)(ii) give 103 pairs. The quoted ranges (positive 67–71, independent 60–73) leave those readings out. The record's own deviation says that "reading (ii) covers 103 pairs", which contradicts the note.
- **Cell 106, and the fig6b notes:** "Conflict near the conflict zone is the highest cell (0.019) … LSD p 0.075 to 0.63". This holds only for the raw minima. With smoothed minima, pretraining near the training zone (0.0189) is above conflict near the conflict zone (0.018), and one LSD p is 0.82 (cell 105). The outcome is unaffected.
- **Cell 127, and the fig4d notes:** "above training p 0.008 to 0.012". These are the residual-df values; with the paper's df they run 0.012 to 0.017.
- **Cell 89, and the negative-pairs notes:** "Only the shuffle classes of reading (b)(i) give no difference". The (ii) class readings are not tested in cell 86, so "only" covers four of the six class readings.
- **Cell 38:** this conclusion omits that room-frame field counts on unsmoothed maps also differ (Kruskal-Wallis p = 0.030, cell 37). This is minor and does not change the outcome.
- **Summary (cell 144):**
  - "log shocks (5 to 33)": WT15Ini2_1 logs 1 shock (cells 9, 60). The record's finding correctly says 1 to 33.
  - "leave 115 place cell values per manipulation against the paper's 120": 115 is the total over the three manipulations (cell 35).
- **README:**
  - "Correlations near shock zones and before avoidances (Figures 5E, 6) | Not reproduced, except the absence before errors and the rate change insets". fig5e1-inset-rate-change-near-zone is not reproduced (cell 100). correlation-not-speed, which is reproduced, is not listed as an exception.
  - The place cell-interneuron row ("Mostly reproduced; pair class counts and negative pairs not") omits that pc-int-fraction-increased is partially reproduced.
  - "about seven minutes, about two of which are streaming": cell 143 prints 592 s in total and cell 1 prints 88 s for loading.

Every other Result sentence, the rest of the Summary, and the record's notes and findings match the outputs.

**My round-1 reasons:** the attempt record gives them as the 44 `reason` fields, verbatim from my round-1 table. The `fig4d-room-ipos-near-active-zone` entry correctly keeps my round-1 outcome, partially reproduced.

### 3. Round-1 points

**Resolved:**
- **B2:** the field part of fig3d now runs under M11 (b) with every mask (cell 49).
- **B3:** fig4d now uses a pooled-error LSD.
- **B4:** variants now drop the shock-logging recordings and test WT15's first 10 min and the data without WT15.
- **B5:** a 100-ms entrance rule matches the Tracker's count (median ratio 1.00).
- **B6:** the paper's df are applied where results are borderline (fig4b, fig4d).
- **B7:** both information units are printed with their tolerances.
- **B9:** every environment claim is also run without the two sessions that fail the clock check.
- **B10:** the paper's 4.5 cm is the right distance whatever the grid, so I accept the response.
- **B12:** the fragile acceleration test is now stated.

**Partly resolved:**
- **B1:** fields are now found on smoothed maps (the authors' RmSm maps in the environment experiment), so few cells have no field. Fig1 single-field share for CA (35–55%) and removed-DG field count (at most 2.09) still miss tolerance under every reading. Those two not-reproduced outcomes rest on the field definition, as the record states.

**Not addressed, no bearing on a conclusion:**
- **B8:** the pair classes still do not match the paper's counts; the record says so.
- **B11:** raw-distance minima still give about 1,000 approach events per session; both readings are shown.
- **fig1-field-number-scaling post hoc tests:** these still use paired and unpaired t tests rather than a pooled-error LSD (the same issue as B3). This cannot change the outcome, because removed DG is already outside tolerance.

**What remains that bears on a conclusion:**
- **fig1-single-field-proportion and fig1-field-number-scaling** rest on the field definition, which the paper does not give.
- **fig4d-room-ipos-near-active-zone** is reproduced only narrowly; see section 1.
- **Several M11-dependent outcomes** pass only under reading (b): fig3d whole-cell, fig5d2, figs2bc at 20 ms, and fig5d3 with relocation highest.
- **fig6-inset-rate-changes** has not been run under M11 reading (a), despite the deviation text.
- **correlation-not-speed** (acceleration p = 0.05004) and **fig4d-room-maps-uncorrelated** (r = 0.16, p < 0.001 at 16 px) remain fragile.
