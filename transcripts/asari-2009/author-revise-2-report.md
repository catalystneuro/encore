No outcomes changed and none are proposed for change. The verifier agreed with all 21 outcomes in round 2. I re-ran the entry twice with `python tools/entry.py all entries/asari-2009`; the second run executed the final text. Checks reported 0 errors and both notebooks passed. Every number that was already in the record came out the same.

**Added in reply to the report**
- **fig2-example-long-context (point A):** the notebook now prints the reliability of each probe of 20051222-ha1-001-002. Probe 4 is the 0.737 probe, so it is most likely the paper's Figure 2 example, and it fails the strict 2 to 4 s test by a run that starts 30 ms before 4 s. The outcome stays reproduced under the criterion as written. The notes, Result cell, README and summary now say the passing probe is not from the paper's example cell. The gap in the claims file is a new question for a reader in `questions/asari-2009.yaml`.
- **fig8c (point C):** the trial-resampling reading now runs, computed in the pass with its own random generator so the existing numbers stay the same.
  - Its amplitude and frequency intervals lie above 1.
  - The higher-order upper bound is 1.003 to 1.078, so no reading meets the rule for reproduced.
  - Its resampled areas are biased upwards (natural sounds 1.69 s against a measured 0.752 s), because a trial drawn twice adds noise to Eq. 17.
  - The point estimates do not change, so the rule for partial is still not met. The outcome stays not reproduced.
- **fig7:** the notebook now prints a checksum of each DMR's modulation parameters. Each of the 5 recordings with frequency variants has a single checksum, so the record's sentence about shared modulation parameters is now backed by printed output.
- **fig4-strf (point B):** the STRF notebook now prints the results without cell 20020602-mw-001. Without that cell:
  - LN beats STRF by 0.025 on average.
  - Mean validation performance reaches 0.222 (STRF) and 0.253 (LN), above 0.22.
  - The longer window still helps significantly (p = 0.011 and 0.0075).

  The notes now say the two statements rest on that cell. The outcome is the same.

**Corrected**
- **README runtimes:** now 29 and 22 minutes, from this run. They were 25 and 22; the verifier's earlier run took 18.2 and 10.0.
- **fig4-predictability notes:** the mean over the first 100 ms is 0.50 only with silence counted; it is 0.57 without.
- **a1-mgb-firing-rates notes (point D):** they now say that with the code's own MGB detector the partial rule rests on a margin of 0.03 to 0.07 Hz, and holds by a wide margin only at half that detector's threshold.
- **Round 2 under `verifications`:** recorded for all 21 claims, with the verifier's reasons and my responses.

**Not done**
- The fig8 choice of main reading is post hoc. I made no change, because the verifier noted that all three readings give the same outcomes, and the existing findings already cover the split by probe type.
- Nothing is committed, as instructed.
