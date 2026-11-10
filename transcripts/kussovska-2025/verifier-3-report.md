## Verifier report, round 3: Kussovska et al. 2025 on DANDI:000469 (0.231213.2047)

The claims file has 45 claims and the attempt record has 45 outcomes: 31 reproduced, 7 partially reproduced and 7 not reproduced. Only one outcome carries a `proposed` change: fig6e-load-modulation-in, from reproduced to partially reproduced.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig6e-load-modulation-in | partially_reproduced | Yes | — | See below. |

### What the re-executed notebook prints

**The main fit no longer meets the criterion.** In this run the main ACG fit keeps 317 neurons (cell 76). Its reading (a) types are 102 PY and 215 IN, with 16 IN concept cells (cell 77). With matched trials and the shared permutation (cell 129):
- IN: 13.95%, p = 0.001. This is within the tolerance of 12.92 to 15.80%.
- IN concept cells: 3 of 16 = 18.75%, p = 0.042. This is just below the tolerance of 19.28 to 23.56%.
- PY: 5.88%, p = 0.43. PY concept cells: 0%, p = 1.0. Neither is significant.

The other trial and permutation readings do not meet it either:
- Matched trials with the within-participant permutation: IN concept 18.75%.
- All trials: IN concept 25.00%, above the tolerance.
- Reading (b) types with matched trials: 14.29%, p = 0.15.
- Reading (b) types with all trials: IN concept 21.43% (p = 0.032) is within tolerance, but IN is 17.68%, above it.

**Two rounding-level fits do meet it.** In the stability table (cell 130), the "start x (1 + 1e-9)" and "ACG x (1 + 1e-12)" fits give 15 IN concept cells. Under them IN concept is 20.00% (p 0.032 to 0.040) and IN is 14.02 to 14.15%, so the criterion is met. The main fit and "start x (1 − 1e-9)" give 16 cells and 18.75% under every tie rule.

### Why I agree with partially reproduced

The criterion says "reproduced when, under one reading, the IN and IN concept percentages are within tolerance with p < 0.05, and the PY groups have p ≥ 0.05". The readings it names are the fig1e GLM, permutation and trial readings, plus the reading (a) and (b) cell types. Perturbing the fit by 1e-9 is not one of those readings; it is numerical instability.

Applied as written to this run's main fit, no named reading passes. Every part holds except the IN concept percentage, which misses the tolerance by one neuron in the denominator. Under fits that differ from the main one only at the level of rounding, it passes in full.

So the effect is there:
- IN and IN concept cells are load-modulated (p < 0.05) under every fit.
- PY groups are not modulated (p ≥ 0.05) under every fit.

But the tested percentage holds only in part. "Reproduced" overstates that, and "not reproduced" would ignore that every other part holds and that it passes under equally valid fits. The variants were run as a stability check that I asked for in round 2, not chosen to reach a result. My own round-2 report already said partially reproduced would describe the evidence better.

### The record and notebook text no longer match this run

These do not change the outcome, but the record should be corrected:
- **The record's `measured` values (14.02, 20.0) and notes, and the cell 131 text**, describe the main fit as giving 3 of 15 = 20.00%, p = 0.038. In this run the main fit gives 3 of 16 = 18.75%, p = 0.042 (cells 129 and 130). The 14.02 and 20.0 come from the "start x (1 + 1e-9)" variant.
- **Which fits pass:** cell 131 says the main fit and "start x (1 + 1e-9)" pass. Cell 130 prints that "start x (1 + 1e-9)" and "ACG x (1 + 1e-12)" pass, and the main fit does not. The proposed reason itself ("two of four fits") is consistent with what is printed.
- **Reading (b) with all trials:** cell 131 says PY 10.00%, p = 0.041. Cell 129 prints PY 9.00%, p = 0.075.
- **Upstream counts:** cell 78 says 316 neurons are well fit, and cell 81 says 214 IN; cells 76 and 80 print 317 and 215.

The main fit came out the same as in round 1 (317 neurons), so this text appears to come from the round-2 run, not this re-execution.

I found nothing in the claims file's fig6e criterion that misreads the paper.
