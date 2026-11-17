I've revised the attempt for round 1 and re-run the entry twice with `python tools/entry.py all entries/watson-2016`. Both runs passed (about 19 minutes each) and gave identical numbers, and `check` reports 0 errors. Every conclusion and record note now matches the new outputs.

**Outcomes.** Totals went from 18 reproduced / 21 partially reproduced / 14 not reproduced to 27 / 10 / 16, with none blocked. All 53 outcomes now match the ones the verifier gave.
- **How outcomes are judged.** In round 1 a claim counted as reproduced only if it held on both datasets; the claims file has no such rule. Outcomes are now judged on CRCNS:fcx-1, which holds all 27 sessions and the lab's own labels, intervals and detections. DANDI results are given beside them in each section. This moved 10 claims to reproduced, including `fig4-updown-within-packets`, and `sleep-homogenizes-rates` follows from the three claims it rests on.
- **`fig2c-acg-peaks` → partially reproduced.** I now take a histogram bin's lag to be its centre, so the nonREM peak is at 9.5 ms, outside 8 ± 0.8. This is recorded as an assumption, with the other two bin readings shown.
- **`fig4cd-packet-rate-lfp-correlations` and `fig4e-within-up-sextiles` → not reproduced.** A part now "holds" only when it meets the bound the paper reports for it, not just p < 0.05. Only 3 of 6 and 1 of 3 parts do. Also recorded as an assumption, with the lenient result given in the notes.

**Fixes and added outputs**
- **Burst index (problem 1).** The verifier was right: the old code also dropped every interval between spikes that crossed a second boundary. Intervals are now counted from spike times, which the verifier's synthetic test case confirms. The CRCNS medians fell (reading c is now 4.6 / 11.5 / 6.5% for WAKE / nonREM / REM); both burst outcomes stay the same.
- **Short time bins (problem 2).** Each grid second now goes to the bin that holds its centre, so short bins are no longer empty. The REM part of `figs5-within-wake-rem` also uses exact spike times; its outcome is unchanged.
- **Microarousals (problem 4).** A per-session table shows where the 2130 deposited MAs lie: 434 in SLEEP, 26 in WAKE, and 1670 in no scored SLEEP or WAKE. No subset gives the paper's 790; the finding is updated.
- **Regression to the mean (problem 5).** Added sextile tests with cells ranked on WAKE without the tested windows, and reverse slopes for the rate-rate claims. `fig3e` still holds under the held-out ranking; the notes now say where a slope below 1 is mostly regression to the mean.
- **Smaller points (problem 7).**
  - `fig3e` is also run with one point per cell, where the fourth sextile misses (p = 0.077).
  - The sigma band is now 9–25 Hz, which uses the same frequency bins as before, so no number changed.
  - A coarse version of the S4B map is shown.
  - The 5 dropped movement triplets come from sessions with no top-sextile cell.
  - EMG is shown as a variant for the movement claim (R = 0.55, p = 0.015, n = 19). The claim is still judged on motion, so it stays not reproduced.
- **What the verifier could not check.** Every DANDI LFP starts at time 0; the code now adds that start time to the LFP times and detections. A new clock check shows delta power is higher in nonREM than WAKE, and the difference disappears when the states are shifted by 30 minutes. DANDI's only electrical signal is the 1250 Hz LFP, so EMG can't be derived there.
- **Records.** The five claims-file readings the verifier flagged (problem 8) are now questions for a reader in the new `questions/watson-2016.yaml`; no claim was changed. Round 1 is recorded under `verifications`: the verifier disagreed on 13 claims, and each entry has its reason and my response.

**Not done**
- I kept the 200 ms window used for power within UP states (problem 6) as a stated assumption. The verifier found `fig1e-up-state-dynamics` partially reproduced either way.
- I kept the chi-square test on paired rates, because it is the paper's own test.
- The movement claim is not tested on DANDI, which has no motion or EMG signal.
- Deleting the leftover `__pycache__` and an empty `.claude` folder in the entry directory was refused by the permission system. Git ignores `__pycache__`, and git doesn't track empty folders, so neither will be committed.

Nothing was committed or pushed.
