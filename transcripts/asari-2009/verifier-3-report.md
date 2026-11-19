**Verifier report, round 3: Asari & Zador (2009), CRCNS ac-1**

The claims file has 21 claims and the attempt record has 21 outcomes. Only one outcome has a `proposed` entry: fig3b-fractional-power-decay, from not reproduced to partially reproduced. "Cell N" refers to `reproduce_asari_2009.ipynb`.

| claim | proposed outcome | agree? | my outcome if different | reason |
|---|---|---|---|---|
| fig3b-fractional-power-decay | partially_reproduced | yes | — | See below. |

**The numbers come from the data.** Cell 29 fits one exponential with constant 0 to Q(t) of Eq. 20 under the 8 readings, each with each trial's mean removed.
- With silence counted, α₁ is 0.457 to 0.464. That is within 0.49 ± 0.049 in 4 of 4 readings, and 4 of 8 in all.
- τ₁ is 1.94 to 2.01 s with silence counted and 1.50 to 1.58 s without. That is within 1.04 ± 0.104 s in 0 of 8.

Cell 37 builds its side-by-side table from the same `r3` frame and from cell 35's `tab4`, and it does not refit anything. I recounted cell 35's table by hand:
- 14 fits stay inside the bounds.
- 1 + α₁ is within 0.459 to 0.561 in 10 of them (the 0.455, 0.426, 0.424 and 0.453 fits fall outside).
- τ₁ ranges from 1.60 to 2.83 s.
- The ratios printed (1.86 to 1.93 times 1.04 s, and 1.54 to 2.72) are right.

The proposal's reason and cell 38 match these printed outputs.

**The choice was not made to reach the result.**
- The decisive figures are from the silence-counted readings. That is the reading that gives the 305 probes the criterion names.
- It was already the record's main reading and its `measured` value (0.458 and 1.975) in rounds 1 and 2, before any change was proposed.
- No reading, centering or fit range is new. The only addition is the side-by-side cell, which recomputes nothing.
- Cell 30's "Result" still says not reproduced, so the verified outcome is kept apart from the proposal, as asked.

**The criterion is applied as written.** "Reproduced when both are within tolerance under one reading" fails in 0 of 8, and the proposal does not claim reproduced. The criterion defines no partial outcome, and neither does fig4-predictability-upper-bound's. In both claims, the size is within tolerance and the time constant is about twice the paper's, outside tolerance in every fit.

For fig3b, the size part is if anything stronger than for fig4:
- fig3b: α₁ is within tolerance in every silence-counted reading.
- fig4: the main reading's 1 + α₁ (0.426) is itself outside tolerance.

Grading fig4 partial and fig3b not reproduced was the inconsistency I raised in round 2, and this proposal resolves it in the direction the numbers support.

**One caveat for the record, which does not change my outcome.** The quote this claim rests on is "a long decay constant of about one second". That is the part that fails as a value: 1.94 to 2.01 s. What holds is the size, and the qualitative point that the decay lasts on the order of seconds, far beyond the 71-ms noise autocorrelation. The partial outcome should be read that way, and the notes already say "its time constant is about twice the paper's."

**Claims file.** I found no new place where the claims file misreads the paper.
