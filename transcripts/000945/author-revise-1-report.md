I've revised the attempt after round 1. The entry re-ran cleanly with `tools/entry.py all` (0 check errors, notebook passes in 92 s), and every conclusion now matches the new numbers.

**Outcome changes (all five agree with the verifier)**
- **fig3-cell-type-sorting**: partially reproduced → blocked (data_missing). Both outcomes the criterion allows require the clusters to separate on waveform features, and the files hold no waveforms. The match on unit counts is also no better than chance: a simple binomial model expects 3.84 matching recordings, and 2 were found. The other claims depend on fig3 but stay tested, because they use the dataset's own cell-type labels, which the claims header allows. I recorded this as a deviation, since the protocol would normally block every claim that depends on a blocked one.
- **fig4h-awake-latency-wider**: not reproduced → blocked (methods_underspecified). Two readings of the claims file (D1/D2, which bin the latency may start in) give different results, and the claims header blocks a claim in that case. I had been overriding that rule; I now follow it.
- **fig6ef-rsu-ispta-rise-then-fall**: partially reproduced → blocked (methods_underspecified). The two window readings (W1/W2) disagree when the repeat recordings are left out.
- **fig7c-rsu-delayed-dc**: not reproduced → blocked (data_missing). The paper's own 30% duty-cycle recordings are missing. The stand-ins borrowed from other sessions now decide no outcome.
- **fig7d-fsu-delayed-dc**: reproduced → partially reproduced. The sham part cannot be tested, and no claim with an untested sham part is judged reproduced any more.

The other 17 outcomes are unchanged, including delayed-anesthesia-factor, which stays reproduced on an assumption.

**Added or corrected**
- **Recording dates.** The notebook now prints the dandiset description and every file's start time. Three of the ten `_2` repeat files start *before* their unsuffixed pair, so the suffix does not mark the later recording. I added a third repeat reading, Rep3, which keeps the earliest recording of each pair.
- **delayed-anesthesia-factor.** Rep3 gives the same outcome as leaving the `_2` files out (FSU p = 0.0012 to 0.0015). Dropping the recording filed under two rats doesn't change it either. The assumption is restated as one recording per rat and condition.
- **Duty-cycle claims.** A new reading, C0, runs the tests with no 30% group at all. It shows that fig7a, fig7a-60 and fig7b fail on parts that don't need the 30% group, and that fig7d's parts (1) and (2) hold without it. The recording dates of the duty-cycle files and of the borrowed 30% files are printed.
- **Smaller points.**
  - fig4-rsu: notes that the awake half already fails (mean below 100%).
  - Two-rat confound: discussed for the anesthetized claims.
  - Latency rule: notes that it flags 86% of FSU.
  - fig5f: notes that part (3) only holds without direction.
  - Partial thresholds: notes where they cannot be met even if the sham parts held.
  - Time-locked responses: a caveat that most 200 us recordings show none.
- **Helper fix.** `tfus.py` now decodes start times that are stored as arrays; the unlabelled anesthetized files store them that way.
- **Record.** New findings: the `_2` suffix contradicts the dandiset description; the duplicated recording's start times are 6.5 hours apart; and a question for the paper's authors about the latency start bin. The 30% duty-cycle question became a data_missing finding. The round is recorded under `verifications` (17 claims agreed, 5 disagreed and were changed).
- **README.** Updated to match.

**Not done**
- I added no reader questions, because the verifier reported no misreading of the paper by the claims file.
- Three things can't be checked from the files, and the notebook says so: whether the 500 trials are trials 6 to 505, whether the labels are the paper's k-means output, and which rat the doubly filed recording belongs to.
- Nothing is committed, as instructed.
