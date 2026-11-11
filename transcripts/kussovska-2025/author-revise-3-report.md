One outcome changed: **fig6e-load-modulation-in** went from reproduced to partially reproduced. The verifier agreed with that proposal in round 3, so I set the outcome and removed `proposed`. No proposals remain, and no other outcome changed.

**Why fig6e changed.** On the main ACG fit, the interneuron concept cells come out at 3 of 16 = 18.75% (p = 0.042). That is just below the tolerance of 19.28 to 23.56%. The criterion is met only under two of the four fits that differ at rounding level: start point x (1 + 1e-9) and ACG x (1 + 1e-12). Under those it gives 20.00%. Interneurons and their concept cells are load-modulated under every fit, and pyramidal neurons are not.

**Re-run.** I ran `python tools/entry.py all entries/kussovska-2025` twice; both passed with 0 check errors. The main fit kept 317 neurons both times (102 PY, 215 IN), as in the run the verifier reviewed. The two runs' outputs agree line by line except for timings.

**Text that was out of date.** The verifier found that the fig6e text described a different run, which had kept 316 neurons. The same was true of the text for most other claims that depend on the ACG fit, so I corrected their numbers to this run's output too:
- **fig6e:** the measured values are now 13.95, 18.75, 5.88 and 0.0, and the notes and cells 78, 81 and 131 match this run.
- **Other fit-dependent claims:** I corrected their conclusion cells and record notes to the printed values, plus the "215 IN" in 17 deviation entries and two findings.
- **fig1e:** preSMA is 20.40% (51 of 250); the outcome is unchanged.
- **Three readings changed result without changing an outcome:**
  - fig4c now also passes at the main 2-bin spacing.
  - ext5bd and ext2 no longer hold under the Methods' 1 s windows.
  - fig5kl's reading (a) count of IN concept cells (16) is just above tolerance. Its outcome rests on reading (b), which is unchanged.

**Summary, README and record.** The notebook summary and the README now show fig6e as partially reproduced. Round 3 is recorded under `verifications` with the one claim the verifier reviewed: it agreed, would give partially reproduced, its reason is in its own words, and my response says what changed. Nothing is committed.
