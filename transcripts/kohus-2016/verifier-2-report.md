## Round 2 verification: Kohus et al. 2016 on CRCNS hc-7

I agree with all 44 outcomes. Two places in the record and notebook text cite fig11 numbers that the printed outputs contradict, and one of them is the author's response to my round-1 point 11.

**1. Outcomes and assumptions**

The claims file has 44 claims and the attempt record has 44 outcomes: 10 reproduced, 4 partially reproduced, 12 not reproduced and 18 blocked. I agree with every one.

- **Changed since round 1:**
  - **Onset claims.** fig6-cckbc-async-onset, cckdti-async-onset, fig10-cck-cck-heterogeneity and fig10-cck-cck-async are now not_reproduced. Under both onset rules and both scalings the CCK+BC EPI median is 1.0 to 3.5, and 9 of 9 CCK+ pairs are asynchronous (cells 52, 58).
  - **async-charge-epi-vs-160** is now not_reproduced. After the 10th AP, CCK+BC gives p 0.0934 under both readings (cell 55).
  - **decay-epi-vs-160** stays partially_reproduced. Under reading a, both tests hold with EPI longer (p 0.00025, 0.0121), and 1 of 4 medians is within tolerance. That matches the criterion's partial.
  - **Blocked (data_missing):** fig8-cck-pairs-uipsc, fig8-cckbc-vs-cckdti-pairs, decay-pc-vs-interneuron, and fig10bd-be-async-charge for its 320 Hz parts.
- **fig11-model-prediction (reproduced):** this holds only for the three types that can be tested. PV+BC to PV+BC has no RIP or EPI data, which is stated as a deviation. I accept it with that caveat.
- **Assumptions:** 21 outcomes carry `assumed: true`, all on IN to PC pairs. Each states the high-KCl assumption as a deviation, and the check in cells 13 and 14 makes it reasonable.
  - Leaving fig4c and the two cckdti claims unmarked is correct, because the paper has no CsCl CCK+DTI group.
  - One sign against a clean assumption is shown but not discussed: in CCK+BC to PC pairs, latency rises with holding current (rho 0.58, p 0.048, cell 13). CsCl lengthens latency, so a CsCl admixture would push toward the fig4b latency differences.

**2. Sentences the outputs do not support**

- **Cell 63 and the fig11c-parameter-differences notes:** "tau_f (p 0.0339, 0.0001)". Cell 62 prints `tau_f: 0.026` under weighting a. The outcome does not change.
- **Cell 63 and the fig11-model-prediction notes:** "AAC to PC (953.2 pA²)". Cell 62 prints 953.1.
- **Record, response to fig11-model-prediction (round-1 problem 11):** "In the re-run the TM dep test error for CCK+BC under weighting a is finite (3765.7 pA2) ... so the infinite value could not be reproduced here." Cell 62 prints `CCK+BC to PC  inf` under weighting a, so the statement is false for this notebook.
  - Together with the two figures above, this suggests the fig11 text was written from a different run than the one saved.
- **Cell 63:** "Under reading a the AAC to PC test error is lowest for the TM depressing model". This is true, but it leaves out that under reading a the lowest error for PV+BC to PC is UDR dep+fac (317.9). That still counts as UDR under the criterion.
- **Minor wording:**
  - Cell 46 and the fig9 transmission-probability notes say "0.1 to 0.9 at 320 Hz" (M2 b). Over the judged 3rd to 10th APs the range is 0.1 to 0.6.
  - Cell 40 says "1 or 2 fits per reading reach the bound", but the free-plateau fit under M4 a has 0. Its own parenthesis says so.
- Every other sentence in the Result conclusions, the Summary (cell 64), the README and the record's notes and findings matches the printed outputs.
- **My reasons in the record:** they state my round-1 reasons in my own words, including the problems I attached to each claim.

**3. Round-1 points**

Resolved:
- **Point 1:** `train = times[:10]`, and the window, fits and duration now start at the 10th AP.
- **Points 2, 3 and 5.**
- **Points 6 and 7.**
- **Point 9:** the two templates at a fit bound are dropped.
- **Point 10.**
- **All the section C requests:** the per-sweep fig4c table, the `_EPA` T01S01 column check, the fig10 charges and durations, the facilitation maxima, the pipette table and the list of fig8 pairs.
- **Point 12 (claims-file issues):** passed to a reader.

Still open, bearing on a conclusion:
- **Point 4, pipette solution:** an assumption that cannot be tested from these files. It is properly marked. The CCK+BC latency correlation above is the one sign in the data that cuts against it.
- **Point 11 and fig11 run-to-run variation:** the record's response is contradicted by the output. The differing p value and test error mean the fits vary between runs. fig11-model-cck-facilitation rests on a BIC margin of 2 (−1389 against −1387, reading b), so it may not survive a re-run. Repeating the fits with a few seeds would settle this.
- **Claims-file issue, made sharper by the fix:** with the trains cut at the 10th AP, onset rule (b) flags the 1st AP of the 160 Hz train in nearly every pair of every type (for example 11 of 12 PV+BC to PV+BC). Summation of synchronous IPSCs at 160 Hz alone would do that. So the rule cannot separate asynchronous release from summation, and the authors' `AR` marks match the paper where the rules do not. The not_reproduced outcomes of the four onset claims are correct under the claims file, but they do not test the paper's procedure.
- **Claims-file reading of fig4c:** counting any success in any sweep gives 3 of 7 silent. Counting only the first sweep gives 7 of 7. The question has been passed to a reader.
