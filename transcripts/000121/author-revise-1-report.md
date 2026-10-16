I re-ran the entry with `python tools/entry.py all`: the check passes with 0 errors and the notebook runs in 342 s. All the conclusions, the summary, the README and the attempt record now match the new outputs. The round-1 review is recorded under `verifications`, with the verifier's reasons in its own words and my reply under `response`. Nothing is committed.

**Outcome changes**
- **pca-variance**, partially reproduced → not reproduced. The verifier disagreed, and it is right on the criterion's wording: the partial case needs all of R's values within tolerance, and R's PC1 is 72.8% against a lower bound of 72.9%.
- **plane-timecourse**, reproduced → partially reproduced. The verifier had agreed with "reproduced", so round 2 should look at this change. The new outputs show that R's D is already below 0.9 in 6 of the 10 bins before target onset, so R's divergence time cannot be told apart from baseline noise. When the converged state comes only from trials whose delay window starts after the bin, R diverges at 10 ms, outside tolerance. J's times hold under both checks (pre-onset SD 0.03; 70 and 250 ms in the variant). The conclusion now also says that "starts at the center" is not borne out.

**Added or corrected**
- **Spikes between trials (B3):** 99.93 to 99.95% of PMd spikes fall inside trials in every session, so the day mean already equals the rate over trial time and stays as the main choice. This is now part of the data check.
- **Reaction time (B1):** I added a variant that only looks for movement onset after the go cue (J 342 ms, R 340 ms, just inside the bound), and printed the share of onsets before the go cue. The conclusion says R's mean matches only because those trials are kept; its median (361 ms) and trimmed mean (362 ms) do not. The outcome stays partial, since the claim fails on other parts.
- **onoff-predicts-kinematics (B2):** I added deviations from session × condition means. The result barely changes (R on-axis r = 0.020, p = 0.023), so it stays reproduced.
- **speed-axis-within-distance:** I added counts per task and session (R 1, 4, 10, 7 of 12; J 1 and 3) and noted that the pooled counts depend on combining sessions.
- **distance-error-and-plane-projection:** I added a paired test and recorded as a deviation that the plane is fit on all trials, including the test folds.
- **r-trial-counts:** I added a reading that also counts failed trials without a go cue; it gives 0 of 4 within 10%.
- **Smaller fixes:**
  - The per-session p values now print correctly.
  - The meaningless ring-task correlation is removed.
  - The notebook prints the smallest p that 1000 shuffles can give.
  - The conclusion for relative-deviation-decreases says the test discriminates little.

**Not done**
- The 912 R 3-rings trials and the paper's held-out SVM trials still cannot be identified from the files.
- Whether the horizontal/vertical swap comes from the paper or the conversion is still open, because the raw `.mat` files return 403.
- I left the tuned-SVM variant tuning on the same trials it reports; the notebook already says so.
- I made no SVM fix for the plane leak; it is recorded as a deviation, and it works against the claim, which still passes.
