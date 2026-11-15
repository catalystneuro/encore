I worked through the round-1 report. All 25 outcomes stay as they were and the verifier agreed with every one. The only change to an outcome's fields is on fig3-example-vs-neuron: it is still blocked, but the reason code moves from `other` to `data_missing`, as the verifier gave it, because session 144 is not in the dandiset. I re-ran the entry with `python tools/entry.py all entries/chandravadia-2020`: it passed with 0 errors, and every number in the conclusions is the same as before.

**Fixes and added output**
- **Problem 1, units-table:** the isolation-distance column's description was a typed-in string. `nomem.load_session` now reads every units column's description from the files, and the notebook prints them. IsolationDist is described as "IsolDist" in all 87 files.
- **Problem 2, spike-time unit:** "seconds" was also typed in. The notebook now reads the spike_times attributes from the files. The column gives no unit, only the description "the spike times for each unit"; the events timestamps say "seconds". The text now says the NWB standard defines spike times in seconds.
- **Problems 3 and 4, docstrings:** `nomem.auc` now explains how its (0,0) test differs from calcROC_AUC.m and why the AUC comes out the same. `nomem.zroc_slope` now gives the sixth ROC point as it is after the 0/1 adjustment.
- **Problem 4, sessions left out of the slope test:** leaving out the 5 sessions with no defined z-ROC slope is now stated as an assumption (`assumed: true`), and two variants were added:
  - With the slope MATLAB's `regress` would return for them (0 for four sessions, −0.415 for one), all 87 sessions give a mean of 0.732, p = 5.4e-10. A new helper, `zroc_slope_regress`, computes this.
  - With those five set to 1, the mean is 0.794, p = 5.4e-09. The claim stays reproduced.
- **Problem 6, fig5f-site-proportions:** the conclusion and notes now say the Fisher tests have little power with only 77 TWH units.
- **Problem 7, new-old-label-coding:** the notebook now also prints the strict count: with the labels reversed, both tests hold in 78 of 87 sessions. The text gives that first and names the 50% threshold (86 of 87) as a choice of this attempt.
- **Electrode impedance:** it is stored as float64 and its only value is NaN.
- **Faraut et al. 2018 Table 1:** now printed in full, one row per session. Session 98 is listed under H48, variant 2.
- **Selected units:** a new cell lists, for each session, the units selected as visually or memory selective, with their p-values, under both the Methods' tests and the code's choices.
- **Record:** I added the round under `verifications`, with the verifier's reasons and my response for each claim.

**Not changed, and why**
- **Problem 5** (memory-selective and dual-cell counts match the code, not the Methods): this is context only. The conclusions and the existing code_mismatch finding already give that explanation.
- **Problem 8** (data findings missing from the narrative): the narrative already states all three, in the data-check text and the label-coding and ISI conclusions. I said so in the responses and did not duplicate them.
- **The 4 sessions "dropped" from `info`:** none are dropped. The cell's output says "Files: 87", and the verifier had cut that output short themselves.
- **helper.dynamic_split:** I did not fetch it for checking. The verifier said reading (a) alone decides fig5d.
- **No questions file:** the verifier reported no place where the claims file misreads the paper, so I did not create `questions/chandravadia-2020.yaml`.

Nothing was committed or pushed.
