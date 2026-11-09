I've revised the attempt for round 1. The entry was re-run with `python tools/entry.py all`; it passes in 414 s with 0 check errors, and the conclusions match the new outputs.

**Outcome changes (all three are claims where the verifier disagreed):**
- **fig3c-speed-within-trial-lower and fig3d-speed-iti-lower:** partially_reproduced → not_reproduced. The criterion only defines "reproduced when p < 0.05", and the signed-rank p-values are 0.063 and 0.079. My earlier partial outcome had borrowed a rule from other claims' criteria, so I withdrew it.
- **fig4supp-ks-every-mouse:** reproduced → partially_reproduced, marked `assumed: true`. Where the 5th–95th percentile cut is computed is a method detail, so the "reproduced under any reading" rule doesn't apply. I adopted reading (a), per session, because the Methods put the cut in the MATLAB pre-processing of each recording. Under it 11 of 13 mice reach p < 0.001. The notes now also give the verifier's point that DOI medians are lower in 5 of the 13 mice. A `methods_unavailable` finding asks the authors which reading they used.

Tally now: 23 reproduced, 3 partially reproduced, 2 not reproduced, 9 blocked (data_missing).

**Fixes and added output:**
- **Signed-rank test:** when a zero difference is present it now uses the normal approximation, as R does. No tested pair has a zero, so no number changed.
- **Fitted-clock speed variant:** speed is now scaled by the fitted rate, not by 80. fig3c gives p = 0.75 and fig3d p = 0.054 under it.
- **Fitted-clock quality check:** it now also requires the implied video to cover the trials and end at most 2 minutes after the last one. This excludes 2204 DOI (71 frames/s, ending 311 s late). 30 of 44 sessions pass; fig5f's good-fit result is unchanged (p = 0.0001).
- **Every file listed (Figure 2):** all 44 files' groups are now printed. `acquisition`, `analysis` and `stimulus` are empty in every file, and nothing names a port, poke, reward, lick, beam or drink apart from the trial table's `repoke` column. Figure 2 stays blocked.
- **Which clock the HTR series uses:** the nose moves most within 1 s of frame t × 80 in all 22 DOI sessions, against 8 of 22 when the HTRs are placed by the fitted trial clock. So the HTR times are on the video's 80 frames/s clock. This doesn't settle which clock the trial table is on.
- **Sniff descriptions:** each file's description and its count of rows dropped for a missing exhalation are now printed. One session the code keeps, 2200 saline, lost 7,933 of 14,626 rows; this is added to a finding.
- **Interpolated nose frames:** the fraction is higher on DOI in 11 of 22 mice, so it is not biased by condition.
- The README, the notebook summary and the round-1 `verifications` entry in the record are updated, with the verifier's reasons and my responses for all 36 claims.

**Not done, and why:**
- **The clock disagreement (problem 1):** no outcome changed. The claims file fixes the code's clock, which the verifier also says decides the outcomes; the fitted-clock reversals stay in the notes and findings.
- **10 cm corners (problem 5):** kept, because the corner sizes come from the claims file. I added no reader question: the outcome holds on the other two measures either way.
- **R parity:** not checked, since no R environment is available here.

Nothing was committed or pushed.
