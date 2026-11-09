No outcome changed: all 28 stay as verified (14 reproduced, 3 partially reproduced, 11 blocked), and nothing is proposed. The entry ran three times with `tools/entry.py all`. All passed, and the last two runs gave identical numbers.

**Added to the notebook:**
- **Table S1 check (the open point).** A new cell downloads the supplement from the publisher, parses Table S1 and compares it with the transcription in `merkel.py`. All 60 rows parse and agree on every column, including the experiment group. A test copy with two values changed is caught. `pypdf` is now in the requirements and the lock file is updated. The record's `inputs` now says where the check is shown.
- **Mi and dMi in the EMG files.** A new cell compares their curves across the whisk cycle with positive and negative velocity. In 7A, 8A and 9A, the correlation with positive velocity is −0.026 to 0.002 for Mi and −0.570 to −0.534 for dMi. That is close to the medians in every group of afferent files, so neither series is the intrinsic protractor EMG. The units are N·m and N·m/s.
- **Viscoelastic fit stability.** This run gave slightly different fig4c numbers from round 2, with the same code, data and locked packages:
  - mean r 0.656 against 0.657;
  - difference −0.030 against −0.029;
  - confidence interval −0.061 to −0.006;
  - 10 of 25 higher against 9;
  - 6 fits at a bound against 7.

  I did not find the cause. A new cell refits with three other sets of random starts. The mean difference is −0.037, −0.040 and −0.017, all inside the criterion's 0.1, but single recordings can change by up to 0.555 in r. The notes and conclusion now give the new numbers and say this.

**Corrected text:**
- **fig5e-phase-span notes.** Removed the claim that 11 of 15 "fits" the paper's slight excess of retraction. They now say that agreement with Figure 7G is not established, and that the 20- and 60-bin variants use the outlier-free frames.
- **EMG files.** "Whisker video series" is now "tracked whisker series" in the fig7d-cut-emg and figs4-intrinsic-protractor notes and in the data_missing finding. The metadata finding now gives the units and size of Mi and dMi.
- **Summary cell.** "Closely" is replaced by a sentence naming the three values that differ: the non-preferred rate is 16% above the paper's, curvature noise 28% above, and direction selectivity 65% against the 80% the criterion asks.
- **Data check cell.** The velocity label now says the values are per millisecond.
- **Round-1 record.** The held-out statement is limited to the five pairs that are printed, and it notes that the full model's held-out r was not computed. The round-1 `reviewed` text now says its cell numbers refer to the round-1 notebook.

Round 2 is recorded under `verifications` for all 28 claims, with the verifier's reasons and my responses. `entry.py check` reports 0 errors.

**Not done:** I left the README unchanged because none of the corrected statements appear in it. The PDF is saved at `paper/mmc1.pdf`, a folder git ignores. The Table S1 cell downloads the PDF from `ars.els-cdn.com` on every run, so CI needs access to that host.
