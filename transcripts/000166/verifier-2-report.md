**Verifier report, round 2: 000166-senzai-2019-01 (doi:10.1016/j.neuron.2018.12.009)**

Counts come from the claims file and the attempt record. There are 47 claims and 47 outcomes: 9 reproduced, 9 partially reproduced, 23 not reproduced and 6 blocked. 29 outcomes carry `assumed: true`. In round 1, 7 claims were tested; now 41 are.

### 1. Outcomes and assumptions

I agree with all 47 outcomes. Three need a remark.

- **figs7-strongest-3-6hz-coupling, partially_reproduced.** In round 1 I said not_reproduced. I now accept partial. Under the adopted distant-site reading (b), 3–6 Hz is first (0.073), which is half of the claim. 30–60 Hz is fifth under that reading and never second under any reading, including the IC reading that has now been run (cell 45). The record states the disagreement.
- **fig2b-six-coherence-clusters, reproduced (assumed).** This follows the letter of the criterion, but the passing reading cannot fail:
  - Six clusters are imposed (reading b).
  - Each mouse's boundaries are tested against the across-mouse median, which gives p 0.74 to 1 by construction.
  - Left free, the clustering converges to 8–20 clusters (6–10 from 16 starts), and 3 of 5 boundaries differ from the IC boundaries (cell 48).
  - The boundaries also range across mice by up to 34 sites (680 µm; boundary 1 runs from −46.5 to −12.5, cell 48). That is wider than the 220–620 µm the attempt calls inconsistent for fig1g.
  
  The record's notes admit the comparison can hardly fail, but neither the notes nor the README give the ranges. The README shows a plain "Reproduced (assumed)". This is a flaw in the claims-file criterion: reading (b) for the cluster number together with reading (b) for the boundaries cannot fail. I am reporting it, not correcting it.
- **fig8cd-down-active-suppressed, partially_reproduced.** I accept partial. The per-cell condition fails for 3 of 20 cells. The mean rebound (6.97 against 5.66 Hz) comes mostly from three cells the dataset labels "down state" (YMV05 units 40 and 71 at 18.8 and 31.6 Hz, YMV08 unit 60 at 14.3 Hz); most of the others do not rebound (cell 114). The notes should say so.

The assumptions are all stated in the deviations and are reasonable:
- depth aligned on the MUA peak c;
- FastICA in place of runica, on waking only;
- layer 4 site at the peak of the third IC;
- layer 6 site 15 sites below c;
- LFP 10 sites from the unit for figs7;
- k-medians on the full profile for the eight clusters;
- the spread rule for volume-conducted ICs;
- site 0 as the most superficial.

The depth direction (site 0 at the top) is still not checked directly. The laminar results are consistent with it: deep units couple to faster gamma, the superficial clusters are the most bursty, and the slowest cluster is the most superficial.

There is one assumption problem that runs across claims. The deepest-site component is a high-variance IC that peaks at site 63 in 15 of 18 mice and is spread over depth (cell 36: YMV01 0.592, YMV12 0.712). It is counted as volume-conducted in ica-volume-conduction-fraction reading (a), but it is also "IC 6" in fig2c, fig2d, the IC layers of fig3c and the features of fig5b. It plausibly inflates fig2c IC 6 (rho 0.94) and drives fig2d's "deep larger" result (median 0.30).

### 2. Statements against printed outputs

Nearly every number in the conclusions, Summary, README and record notes matches the outputs. These do not:

- **Cell 121, and the fig3d-slow-oscillation-gamma-coupling notes:** "the deep sites couple to amplitudes above 100 Hz." This is not shown. `mi_deep` is by construction the largest index above 100 Hz, and `f_deep` is computed but never printed (cell 120).
- **Cell 61 and the slow-gamma-superficial-wake notes:** these omit the output in cell 60 that waking 30–60 Hz power in cluster 1, minus the site mean, has a median of −7.06. That runs against the claim's "dominates in superficial layers". The claims-file criterion tests only the state order, which leaves this part of the claim untested.
- **Cell 97:** "0.402, 0.269 and 0.364, still outside for E-E and I-E." This implies E-I is inside, but 0.402 is below the 0.404 lower bound, so all three are outside.
- **fig2b-clusters-same-across-states notes and cell 52:** "differ by at most 3 sites." Boundary 1 differs by 3.2 (−23.4 against −20.2, cell 51).
- **figs2c notes:** "the signed-rank tests reject zero in the positive direction." For the 10 s windows at the deepest site, p = 0.01 (cell 63), which is not below the criterion's 0.01.
- **Cell 118 and the fig8eh notes:** "strongest for the cells the dataset labels down state." This holds mostly but not strictly: YMV10 unit 36, which is not labelled, has a non-REM ratio of 0.74, below the labelled YMV15 unit 33 at 0.77 (cell 117).
- **Labels:** the Summary (cell 126) shows fig2d without "(assumed)", and the README row for "3-6 Hz power largest in layer 4…" shows "Reproduced" without "(assumed)". The record has `assumed: true` for both.

The record's `verifications` block gives my round-1 reasons faithfully, close to my own words, including points B1, B3, B4, B5, B7, B8 and B9 and the section C requests.

### 3. Round-1 points

**Resolved:**
- **B1:** the blocks that were inherited from fig1g have been removed and all 33 claims are run.
- **B2:** column order is checked (the best-correlated site is adjacent for 50–63 of 64 sites). `max_channel` is shown to be the electrode-table id: it matches the id of the unit's peak column for 1157 of 1255 units.
- **B3:** CSD maps are shown, the mice where the rule lands near the probe edge are listed, and the message is fixed. fig1g stays blocked, which I agree with.
- **B4:** the genotype contradiction is flagged.
- **B5:** the IC reading is run.
- **B8:** the edge is now 8 s and the cap 600 s in total.
- **B9:** the I-E reading is stated.
- **Section C:** groups are listed per file (`stimulus/*` holds nothing), and the counts without units 0–1 sites apart and per state are printed.

B6 and B7 needed no action.

**Remaining that bears on a conclusion:**
1. fig2b-six-coherence-clusters is reproduced only under a reading that cannot fail. The 620–680 µm boundary spread should be reported, and the README entry needs the caveat. This is a claims-file problem.
2. The probe-edge deep IC is used both as volume-conducted and as main IC 6. This affects fig2c, fig2d, ica-volume-conduction-fraction and, plausibly, fig5b.
3. The fig3d-slow-oscillation-gamma-coupling statement about deep coupling above 100 Hz is unsupported until `f_deep` is printed.
4. The slow-gamma-superficial-wake conclusion should report the −7.06 output against superficial dominance.
5. The fig8cd notes should say that the mean rebound comes from the few labelled "down state" cells.
