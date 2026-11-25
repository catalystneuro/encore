I've finished the round-2 revision. No outcome changed. For fig5-recording-day-effects I kept the verified "not reproduced" and proposed "partially reproduced" for a third round.

**Re-run.** `python tools/entry.py all entries/peterson-2021` passed its checks with 0 errors, but the run is marked FAIL because it took 63.5 minutes against the 60-minute limit. Every cell ran without error. That is inside the 80 minutes the verifier's re-run and the PR checks allow, but over the target for my own run. The time goes to the 3904 regression models (2109 s, limited by the 4 CPUs). I did not cut any analysis to get under 60 minutes, and no `.clean-run.json` stamp was written. All earlier numbers came out the same. `entry.py check` passes, and the record validates against the schema.

**fig5-recording-day-effects.** I ran the electrode set the verifier asked for, which removes only the electrodes bad in every file. It gives 21 of 24 agreeing pairs with band means and 20 with band medians, so it would be partially reproduced. The main set gives 18 and each file's own flags give 20. I then counted removed electrodes, surface and depth separately, against the paper's 4.9 ± 4.9 surface electrodes per subject:

| Electrode set | Surface electrodes removed per subject | fig5 pairs agreeing (band mean) |
|---|---|---|
| Main: bad in any file removed | 12.6 ± 8.4 | 18 |
| Each file's own flags | 4.2 ± 2.1 | 20 |
| Only bad in every file removed | 1.2 ± 0.4 | 21 |

The verifier's figure of 3.0 for the last set included S03's 16 depth electrodes, which have no position. Each file's flags match the paper's count best, and both alternatives to the main set give partially reproduced. The proposal's reason and the analysis behind it are in a new notebook cell. The notebook now also compares the paper's Table 2 per-day intervals with this attempt's day medians, as the criterion asks: 41 of 55 subject-days fall inside in LFB and 42 of 55 in HFB.

**Other points from the report:**
- **Electrode variants for the region claims.** Every region claim is now shown under three variants: each file's flags, removing only the electrodes bad in every file, and the main set without electrodes holding 50 ms runs of zeros. No outcome changes. One thing to note: under "bad in every file only", fig4 would have all four parts hold and so be reproduced. That set removes far fewer electrodes than the paper reports, and each file's flags give 3 of 4, so I proposed nothing for fig4.
- **Runs of zeros in S09 and S10.** Leaving those electrodes out does not explain the open results:
  - S09 still has no HFB increase (−0.029 dB).
  - S10's HFB day effect stays at p = 0.054.
  - S09's onset and pseudo-onset power still do not differ (p = 0.84 and 0.87), so its alignment is still not established.
- **Sentences the numbers did not support.** I corrected all four:
  - the fig2-reach-shape row of the Summary;
  - the fig4 row of the Summary;
  - the "move both arms most" phrase in the fig2 contralateral-wrist conclusion (cell 38);
  - the run time in cell 0, the README and `entry.yaml`, now about an hour.
- **Round-1 record.** The verifier's problem 2 (the 86400 s timestamp mismatch) was missing from the stated reasons; I added it under fig2-event-counts.
- **Round 2 under `verifications`.** All 25 claims are recorded: 24 agree, and fig5 is recorded as not agreeing, with no outcome since the verifier left it undecided. There is no `findings` list because no finding is rated critical.
- **Findings.** I updated the text of four existing findings (good-electrode flags, the zeros, the checks that passed, and the question to the authors). Their order is unchanged and none was added.

**Code changes.** In the helper (`ajile.py`), the spectral pass now builds the extra electrode variants and records which electrodes hold runs of zeros. Regression jobs run largest first, and all variant fits run in one pool; neither change alters any number. I also added retries for the Figshare downloads, because a Figshare timeout stopped the first run attempt.

**Not done.** The regression claims were not refit with each file's flags; the verifier agreed with the regression's electrode set. No question was added to `questions/peterson-2021.yaml`, because the report names no place where the claims file misreads the paper. Nothing was committed.
