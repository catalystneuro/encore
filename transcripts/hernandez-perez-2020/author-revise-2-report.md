No outcome changed, and I proposed no outcome changes. The entry re-ran cleanly (`python tools/entry.py all` gives 0 errors, notebook passes in 158 s), and `tools/entry.py check` passes.

The verifier agreed with 23 of the 24 outcomes. The one disagreement is fig5c-rise-decay-gradient: the record says partially reproduced and the verifier reads it as not reproduced. I kept the round-1 outcome and recorded the disagreement again; their report calls my reasoning defensible. The natural-log question for that claim is still waiting for a reader in `questions/hernandez-perez-2020.yaml`.

**Corrected text (the three overstatements the verifier found):**
- **fig7-residual-delay** (cell 64, the record's notes, the Summary): with half of the asymmetry delay removed, the residual is within tolerance (6.99 to 12.23) only under the `counts` readings (7.86 to 9.20). Two of the four readings without the amplitude restriction (6.80 and 6.81) fall below it. The Summary sentence about the half-delay variant now says this.
- **Hilbert-frequency sentence** (the Summary and the Figure 8 question for the authors): it no longer says the absolute delay falls "as the paper finds". It now says the median slope is negative under every reading, but the test finds the fall in only one of the four `counts` readings (p = 0.094 under the main reading) and in all four without the amplitude restriction.
- **fig8-correlation-strength** (cell 73 and the record's notes): added the r² centred combination the verifier pointed to (counts, O3 c, O7 b: T+ = 20, p = 0.0625, absolute median r² 0.005).

**Checks loosened to match the criteria:** the checks in cells 60 and 72 required T+ = 21, which is stricter than the criteria. Cell 60 now requires a positive median over rats, and cell 72 requires the absolute delay's median to be the larger. The counts did not change: 2 of 8 for fig7-asymmetry-delay (both from readings without the amplitude restriction, as before) and 0 of 64 for fig8-correlation-strength.

**Recorded:** a round-2 entry under `verifications` in `attempts/hernandez-perez-2020-01.yaml`, giving the verifier's reasons in its own words and my responses.

**Not done:**
- The report's open questions, the unit reading of the integer files and the Figure 8 period definition, are already disclosed in the record. Only the paper's authors can settle them, so I made no change for them.
- The verifier listed figures as the one round-1 request still unmet but did not ask for anything new this round, so I added none.
- As instructed, nothing is committed.
