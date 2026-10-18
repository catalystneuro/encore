**1. Outcomes**

The claims file has 19 claims. The attempt record gives 6 reproduced, 6 partially reproduced, 4 not reproduced and 3 blocked.

- **18 outcomes:** I agree with these, the same as in round 1. For fig7j-iti-timebin-mouse and fig7f-iti-knn-locust, "reproduced" holds on the criterion only, and the record and notebook now say so.
- **figs7e-ibi-chance:** the record has blocked (methods_underspecified); my round-1 outcome was not_reproduced. I now accept blocked.
  - With the Methods' k = 50, the procedure's own null averages 10.8% (cell 57), so the 3.8% cannot count as meeting the criterion. The paper's 34.8% cannot come from the procedure its Methods describe.
  - My not_reproduced rested on k = 20, which the criterion does not specify.
  - Every working variant gives 35% to 98% (k = 20, 10, 5), well above 34.8%. If a working method were ever fixed, the outcome would be not_reproduced.

**2. Statements the printed outputs do not support**

- **Whole-window z-score and fig2f.** Three statements say the ON/OFF anticorrelation appears when traces are z-scored over each trial window:
  - README: "With traces z-scored within each trial window … they appear as the paper reports".
  - Summary (cell 79), first bullet: "The mouse ON/OFF anticorrelation (fig2f, fig7d) and the contrast enhancement (fig6e) appear with that z-scoring".
  - The record's first metadata_insufficient finding: "the paper's ON/OFF anticorrelation … appear[s] … with that normalisation".

  Cell 34 prints r_zscored median +0.068, 12 of 28 below 0, p = 0.33, and the odor medians are mixed. Only fig7d from 5 s on (cell 47) and fig6e (cell 44) show the effect with that z-score.
- **Window drift.** Summary (cell 79), third bullet: frame counting "drifts by up to about 2 s over a 57-s trial at the sessions' 13.7 to 17.8 Hz". Using the frame rates in cell 4, 912 frames last 66.4 s at 13.73 Hz and 51.2 s at 17.83 Hz, so the drift is 6 to 9 s at the extremes. About 1.8 s holds only for sub-141 ses-8 (cell 25).
- **README: "The ON-OFF angles exceed 90 degrees only because of the centring".** In the locust, subtracting the pre-odor baseline without centring gives a mean of 91.9, with 9 of 11 odors above 90 (cell 65). For the mouse the statement holds (uncentred 71.8, 2 of 28 above 90, cell 29).
- **Null mean, fig7h.** Cell 51 and the record's fig7h notes give "null mean 17.1%" for sub-148 ses-3. Cell 50 prints 0.167.
- **Block-relabelling null, fig7j.** Cell 55, the fig7j notes and the response to round 1 say that under the 24 relabellings of whole blocks, accuracy "stays at 68.2% to 88.5% … close to the observed values". Renaming whole classes does not change a k-NN classifier's accuracy except through vote ties (cell 53 code), so this null repeats the observed accuracy by construction. It is not evidence. The pseudo-trials carry the argument.
- **Pseudo-trials as high as the ITIs.** Cell 55, the fig7j notes and the Summary say pseudo-trials are classified "as high as" or "as well as" the ITIs. In 4 of 7 sessions the pseudo-trial maximum is below the ITI minimum (cells 53 and 54; for example sub-141 ses-1, 0.899 against 0.911). "Nearly as high" fits the outputs.
- **Pseudo-trial timing.** The Summary calls them "pseudo-trials 15 min after a block". They lie within the 15 min after each block (cell 54 code comment).
- **Synthetic check, fig7d.** Cell 48 and the fig7d notes say the synthetic whole-window z-score "gives the same negative values". The synthetic values are −0.90 and −0.93 (cell 35); the data give −0.34 to −0.48 (cell 47). The sign is the same, the size is not.

All other numbers in the Result cells, the Summary, the README and the record notes match the outputs. This includes the 44.7° and the locust "solitary block structure", both of which I checked against the published version's text (Fig 2G legend and Table 1).

My round-1 reasons are stated in my own words and are correct. 18 of 19 agreements is right. Some reasons fold in later problem numbers (14 into mouse-sessions, 11 into fig7d), but they do not distort them.

**3. Round-1 points**

- **Resolved:**
  - 1: figs7e is no longer counted as met; k = 10 and k = 5 added.
  - 2: centring controls and synthetic check added.
  - 3: pseudo-trial control added and the block confound stated. A locust control cannot be built from the Figshare files.
  - 4: pre-onset z-score added.
  - 5 to 14: all addressed (three-session variant, k ≤ class size, self-angle variant, no extrapolation in cell 18, frame-counted variants, Table 1 findings).
- **Partly resolved, round-1 item C:** I could now read the v2 preprint text (bioRxiv API JATS, saved in `paper/`). It confirms 121.8, 106.7, 34.8, n = 286 and the 11-odor list. Its Fig 4B text gives no ON-ON value. Table S1 is an image and remains unchecked.
- **Remaining, bearing on a conclusion's interpretation; none changes an outcome:**
  - The fig2f z-score overstatement in the README, the Summary and the record's finding.
  - The wrong drift magnitude in the Summary.
  - The block-relabelling null presented as evidence in fig7j.
  - The README's "only because of the centring", which the locust baseline variant contradicts.
