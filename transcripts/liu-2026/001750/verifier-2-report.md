**Verifier report, round 2: Liu et al. 2026, DANDI:001750 v0.260825.0222**

The claims file holds 34 claims, and the attempt record has 34 outcomes: 28 blocked, 3 reproduced, 2 partially reproduced and 1 not reproduced. No outcome carries `assumed: true`.

### 1. Outcomes

| Claim | Record | Agree? | Comment |
|---|---|---|---|
| na-cell-table-link | partially_reproduced | Yes | 35/35 files and cell IDs match. At most 2 of 35 cells are within 10% under the readings (cell 7). |
| fig4d-sodium-current-lower | blocked (methods_underspecified) | Yes | Only a1b1c1 (p = 0.045) and a1b1c2 (p = 0.025) are significant; the other readings give 0.077 to 0.29 (cell 14). |
| model-na-ratio | blocked (methods_underspecified) | Yes, now | In round 1 I gave partially_reproduced. The record cites the protocol rule that a claim whose parent is blocked is itself blocked (Author, step 1.5). The claim lists fig4d under `depends_on`. I cannot read docs/protocol.md to confirm the rule. If it holds, blocked is correct. It is also the sounder outcome, because every in-tolerance ratio comes from an a1 reading. |
| na-patch-capacitance | blocked (data_missing) | Yes | Cell 21 prints all 52 entries per file. None names a capacitance, resistance, seal or compensation, and neither does the metadata of any of the 35 assets. |
| fig8a-metabolite-gradient | not_reproduced | Yes | 175 and 84; log2 190 and 95 (cell 23). The 23 missing metabolites cannot close the gap of 30 or more for AIC vs V1. |
| fig8de-glycolytic-bias | partially_reproduced | Yes | The criterion defines no partial outcome, so the protocol's definition (an effect that holds only in part) is a fair basis. The outcome is partial with either glutamate entry: 2 of 3 parts hold with L-Glutamic acid, 1 of 3 with the other entry (cell 26). |
| fig4j-eepsp-amplitude | reproduced | Yes | Two-way ANOVA p = 0.0065 and repeated-measures p = 0.0068. The re-organized block gives p = 0.0033 (cells 28–29). |
| ven-subtypes-similar-physiology | reproduced | Yes | Tested on the authors' per-cell tables, a deviation the record states. p = 0.55 and 0.27, BH q = 0.55 and 0.54, ANOVA p = 0.958 (cells 32–33). The BH argument is correct: an adjusted q is never below its raw p. |
| fig3e-phase-peak-index | reproduced | Yes, with caveat | The VEN median is lowest and every Bonferroni p is ≤ 0.001 (cell 36). The sheet has 29 VENs against the 22 of Fig. 2d–f, a 32% excess, so the cell set is clearly not the paper's. The record says this. |
| fig3c-ais-distance-length | blocked (metadata_insufficient) | Yes | The sheet has no slice or animal column (cell 39). |
| Other 24 `elsewhere` claims | blocked | Yes | Cell 41 now gives a reason for each claim, and the reasons match the record. ven-firing-rate-variability is now blocked as methods_underspecified, which is what its criterion says. |

### 2. Sentences the printed numbers do not support

- **Record, fig4d notes:** "The readings that subtract no baseline find the effect". Only 2 of the 4 a1 readings do. a1b2c1 gives p = 0.27 and a1b2c2 gives p = 0.18 (cell 14).
- **Record, fig4d notes:** "In 6 of the 14 VENs and 4 of the 21 PCs the maximum under the readings is a brief transient". The widths were computed only under a2b1c1 (cell 11). The same generalisation appears in the Summary (cell 42): "Those readings take one sample … in 10 of 35 cells … that sample is a brief transient".
- **Cell 18:** "so in the paper's values too the difference rests mostly on one session". In session AS the table's medians are 17.5 against 29.1 pA, a ratio of 0.60, in the same direction as HS. That gap is only non-significant at n = 7 and 10 (p = 0.11, cell 14). The difference in the paper's values does not rest on one session; only its significance does.
- **Record, methods_unavailable finding:** "a peak after 0.5 to 1 ms smoothing matches the table closely". At 0.5 ms only 19 of 35 cells are within 10% (cell 9).
- **Summary (cell 42):** "The code table's values match a peak taken after smoothing". The best fit, at a width chosen to fit the table, gives 26 of 35. That is below the link criterion's own 28 (cells 9 and 13).
- **Cell 41, and record ven-firing-rate-variability notes:** "0.33 GB in about 3 minutes". Cell 1 prints 256 s (about 4.3 min), and the README says about four minutes. The "over two hours" conclusion still holds.
- **Record, na-cell-table-link notes:** a stray fragment, "a2b1c1 agrees best. A Under a2b1c1…".
- **Record, na-patch-capacitance notes, and cell 22:** "capacitive transients that could give an estimate are removed". This is inferred from the Methods; no printed output shows it.
- **README:** "24 claims on other data (other dandisets, GEO, NeuroMorpho, models)". The list leaves out fig4j-eepsp-latency, which has no data source, and ven-firing-rate-variability, which is blocked on method. This is minor.

All other figures checked out against the printed outputs, including:
- 17 of 24 and 13 of 24 baseline-subtracted variants (cell 16);
- 11 maxima (6 VEN, 5 PC) and 10 transients (6 VEN, 4 PC), with median ratios 1.94 and 1.28 (cell 11);
- the ratios 0.68 to 0.99 and 0.79 to 0.99 (cell 19);
- the Games-Howell and ANOVA values;
- the counts per claim.

**Round-1 reasons in the record:** they are stated faithfully and in my own words, including the claims-file gap on filtering and the strict reading of fig8de.

### 3. Round-1 points

**Resolved:**
- **Problem 1 (noise and non-Na⁺ maxima):** documented. Cells 11–12 and the figure show the biphasic transients, about 0.1 ms wide, and the claims-file gap is put to a reader.
- **Problems 3, 4, 6, 7, 8 and 9:** all resolved.
- **Problem 2 (a1 holding offset):** stated in the fig4d and model-na-ratio conclusions.
- **Problem 5 (session dependence):** now discussed, but see the new point below.
- **Not-checked items:** all four are now addressed (capacitance fields, traces and I–V curves, noise by type, per-claim reasons).

**Remaining points that bear on a conclusion:**
1. **Transients and sessions (fig4d interpretation; the outcome stays blocked).** 9 of the 10 transient maxima are in session AS, including 5 of its 7 VENs; the only HS one is HS1c18 (cell 11). Under a2b1c1, the AS reversal (VEN 40.7 against PC 36.2 pA) therefore coincides with the transients. The record presents it as a session effect, and in the paper's values, as a difference that rests on one session. It should instead say that the AS result under the readings is mostly the artefact.
2. **Wrong count for the a1 readings (fig4d).** As quoted above, the record says the no-baseline readings find the effect, but only 2 of 4 do.
3. **Filter description (non-deciding variants).** The "4-pole Bessel at 2.9/5/10 kHz" is run with `sosfiltfilt` (nacurrent.py:200–203). Running it forward and backward makes it effectively 8-pole, about −6 dB at the stated cut-off. So it is not equivalent to an amplifier's 2.9 kHz Bessel. These variants decide nothing, but the record cites them in the methods_unavailable finding.
4. **model-na-ratio outcome.** My agreement depends on the protocol's rule for claims that depend on a blocked claim, which I could not read.
