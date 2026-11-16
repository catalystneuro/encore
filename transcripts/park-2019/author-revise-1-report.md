I went through every point in the round-1 report, changed two outcomes, and re-ran the entry. `python tools/entry.py all entries/park-2019` passes: the notebook ran in 427 s with no errors, and the checks report 0 errors. Round 1 is recorded under `verifications` in `attempts/park-2019-02.yaml`, with the verifier's reasons in its own words and my reply under `response`.

**Outcome changes**
- **fig1c-directionality: partially reproduced → reproduced (rests on an assumption).** The verifier was right that the Tukey test ignored the repeated-measures error term that the paper's F(3, 342) implies. I added `hd20.tukey_rm`, a Tukey test that uses that error term; for two conditions it gives the same p as a paired t-test. With it, room against stable2 is p = 0.0019, so every required pair is at p < 0.01. The old between-groups test (p = 0.055) is kept as a variant. The choice is recorded as an assumption and as a `methods_unavailable` finding asking the authors which error term they used.
- **fig4c-arena-registration-short-lived: partially reproduced → not reproduced.** The verifier gave not reproduced and I agree. The "after" window side now runs at every interval, and the notebook checks each part of the criterion under all four readings of window side and normalisation. In none of them is the arena frame below the other three at 20 to 50 s. It drops below them only from 50 or 60 s, after the room frame has already dropped.

**Added or corrected (outcomes unchanged)**
- **fig1c-speed:** the new Tukey test is now the main one. Reading (a) gives the claimed pattern with either test.
- **fig1c-firing-rate:** the ANOVA without the 40 AP/s R523 unit gives p = 0.275, so the result does not depend on that unit.
- **cell-counts:**
  - Reading (b) now applies the Rayleigh test to the tuning curve's vector, as the Methods describe; 110 of 115 units still pass.
  - The notebook now says reading (b) is circular, since the deposited units were already selected as head-direction cells.
  - Both R523 units are named R523 in all their files, so the unit Table S1 counts under another rat cannot be identified.
- **fig2c:** I added distance to the zone's nearest point and angular distance. None of the 24 readings comes within tolerance, so the outcome no longer rests on how distance is measured, and I removed `assumed`.
- **no-angular-velocity-tuning:** a test against time-shifted spike trains, and the same test with head direction removed, still find more significant cells than chance. The excess does not come from the anti-conservative p-values the verifier flagged.
- **fig4 and fig1d:** added a KLD variant with curves rescaled to spike counts. fig4's one passing reading still passes (instability p = 0.052).
- **fig3:** every session's units share the same first timestamp. Session 1017R035 holds a single unit and forms no pair, so no pair was offset.
- **figs2:** per-ensemble values are now printed at 45° bins; two of the six labels rest on differences of 0.02 to 0.03.
- **fig5:** the notebook prints the sample sizes implied by the paper's z values (681, 679, 10,671 and 1,072). No pooling of the ensembles matches them.
- **fig5c:** minima are now matched by bin centre only; the one pooled match still holds. Chance rates are printed: 0.20 rows expected to hit both minima, 6.6 to hit one.
- **Data check:** it now reads the two `.xls` file lists, which match the tracker files exactly. This needed `python-calamine`, so `requirements.in` and the lock file changed.
- **Handover:** the fig1d conclusion cell is split into two cells that start "**Result:", so the next handover strips both.
- **Record text:** I corrected the figs2 note on undefined Idir. The code drops an interval when any cell's value is undefined; it does not sum over the others.
- **Reader question:** added to `questions/park-2019.yaml`, asking whether the Figure 1D legend's order is garbled. The claim is still tested as written.

**Not done, and why**
- The decoder still returns the start of the winning bin, because that is what the paper's code does; it is noted as a deviation.
- I did not commit or push, as instructed.
