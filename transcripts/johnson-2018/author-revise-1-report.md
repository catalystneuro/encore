Round 1 of verification is answered. Of 21 claims, 5 are now reproduced, 7 not reproduced and 9 blocked; before this round it was 5, 16 and 0. The entry re-ran clean with `python tools/entry.py all` (47 minutes, check 0 errors), and two full runs gave identical numbers. Nothing is committed.

**What changed in the outcomes**
- **Time axis (verifier's B1), now the main reading.** I added a per-electrode test comparing the 900 ms and 1150 ms delay trials, with a 200-permutation null. In all three segments the two groups differ where the trial table puts the first delay-dependent event, and not where the deposited code's windows put it. The clearest case: in the postcue segment the ERPs differ from −0.25 to 0.75 s (p down to 0.005), around the response screen at −0.3 s; at 1.0 to 2.0 s, where the code puts it, p is 0.29 to 0.94. Every window is now placed 1.5 s earlier than the code places it. The code's windows still run as a variant for ERP, power, PLV and both PSI measures.
- **Nine claims changed from not reproduced to blocked (`methods_underspecified`):** crossspectral-equal-strength and the 8 PAC claims. I added a calibration with one signal's trials shuffled, which removes any real coupling (B3). Under it the code's PSI form still passes 57% of units, the same rate as on the real data (56%), against the 2.5% its threshold implies. The Methods' PSI selects at most 3 units per system, too few for the models. The protocol's chance-level rule therefore blocks these claims. The results on the code's selection stay in the notebook as an unjudged variant.
- **Kept, with the disagreement recorded:**
  - behavior-no-difficulty-difference stays reproduced (assumed); the verifier gave partial. I searched for where the `summary_file.csv` response times come from. Means over correct trials explain 9 of 30 values (s6, s8 and s9 only); medians, all or kept trials, other subjects' rows, blocks of 40 trials and trial type explain none of the rest. I kept the outcome because the file's condition means and SDs are the paper's.
  - psi-theta-shift stays not reproduced (assumed); the verifier gave partial. It is now judged on the claims file's sliding windows (B4), placed by the trial table, where neither network shifts. The verifier's partial pattern appears only in the code's windows.
- **erp-no-condition-difference** stays not reproduced, now marked assumed. The deposited `erp_compute.m`, now quoted in the notebook, subtracts the trial-mean baseline (B5). A per-trial baseline leaves 0 significant electrodes, so the outcome depends on that choice.

**What I added or corrected**
- Cross-spectral PSI with sliding windows for crossspectral-shift, phase-directing-counts and theta-peak-bands.
- Calibration tables for every PSI form.
- Script excerpts streamed from `analysis_scripts.tar.gz`.
- The response-time source search.
- Updated conclusions, summary and README.
- Revised findings: the time-axis finding now reports the jitter evidence, and the PSI code finding the calibration.
- The `verifications` block, one entry per claim with the verifier's reason and my response.

**Not done**
- PAC on all units without selection (verifier section C). It tests a different population from the claims', and it would push the notebook past its 60-minute limit (it already takes 47).
- PSI resolved by frequency with a 2 Hz bandwidth (B6). The verifier marked it as not affecting a conclusion, and it is recorded as a deviation.
- No new reader questions: the report found no place where the claims file misreads the paper.
