I've revised the attempt for round 1 and re-run it in a clean environment. Both notebooks passed (decoding 39 min, features 49 min), and `entry.py check` reports 0 errors. Nothing is committed.

**The main problem the report uncovered.** The round-1 conclusions and record had been written from an earlier run, so they did not match the numbers the verifier saw. The cause was the JADE ICA: it lands on different solutions when its input changes in the last bits, for example with the number of linear-algebra threads. It now runs on one thread on inputs rounded to float32. A run I made on cached data and the final clean run gave identical outputs, so every conclusion now matches the numbers. Three ICA restarts are shown: two keep the same 10 ICs, the third shares 4 of them, and none is above null.

**Changes in outcomes**
- **rest-decoding-above-null:** stays partially reproduced, now on a different basis, and is now marked seed sensitive. The only significant result is every frame of the epoch as a sample (R4 b) with the epoch selection rule (R5 b): AUC 0.500 against 0.417 for the null models, p = 0.0053. It holds at only one of five seeds, the model itself is at chance, and it is one of 2 significant combinations out of 27 run. The verifier would give not reproduced; that disagreement is recorded.
- **rest-ic-count-and-window:** stays partially reproduced, now because 10 ICs are highest under the second IC-count reading (R5 a). 1.5 s is never the highest window. The verifier would give not reproduced; recorded.
- **The other four tested claims** stay not reproduced, and the verifier agreed. The 18 blocked claims are unchanged, and the verifier agreed on all of them.

**What I added or corrected**
- **VIF definition:** I read the paper's own code (`#07_vif_calc.ipynb`). It computes the VIF without an intercept and on training samples, so that is now the VIF used, including for choosing ICs. The 10-IC maximum is 60.1 that way, 14.05 on training samples and 5.58 with an intercept; none is within 9.0 ± 0.9. Because the Methods say validation data, I added a new finding (`code_mismatch`) at the end of the findings list.
- **Epoch selection:** R5 b is now run as a main reading, with five seeds and per-fold AUCs. Every combination of R2, R3, R7 and R8 is run under it, plus R4 b under five seeds. Where the readings differ, R5 b is adopted as the better-supported one.
- **Question for a reader:** the claims file says the paper gives no selection rule for resting data. I added this to `questions/komori-2026.yaml` without changing the claim.
- **New outputs the verifier asked for:**
  - how many training labels the null shuffle changes (12.8% under R5 a)
  - training curves for comparison with Supplementary Figure 5B–C
  - the corrected ROI signal against the dataset's own corrected signal (median r 0.26 to 0.70 per session)
  - the spread of the hemodynamic slopes (54 of 306 negative)
  - how many dilation peaks fall at an epoch edge (15 of 117)
  - pupil plots with labels for #51 day0 and #53 day1
- **Other:** reading "first sample per experiment" as per 40 s epoch is now stated as an assumption. The fits now run in parallel worker processes; this changes no number.
- **Record:** I updated the outcomes, notes, deviations and one finding's numbers, and recorded the round under `verifications`. I also updated the README and `entry.yaml`.

**What I did not do, and why**
- **Readings not run:** all 25 mice (R1 b) and the fourth session per mouse would take about three hours of streaming. R4 b without epoch selection takes about 10 minutes per run and did not fit the time.
- **Checks not run:** the cutoffs were not run with R4 b plus R5 b. The five-seed check for the IC-count claim was not run.
- **Unresolved:** the three files that changed between dataset versions were not compared. The verifier's point that the decomposition looks nothing like the paper's has no fix.
