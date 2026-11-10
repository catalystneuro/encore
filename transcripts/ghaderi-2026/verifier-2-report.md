**Verifier report, round 2: Ghaderi et al. 2026 on DANDI:001530 (0.260605.0601)**

The claims file has 30 claims and the attempt record has 30 outcomes: 14 reproduced, 9 partially reproduced, 3 not reproduced and 4 blocked. The README table matches the record.

### 1. Outcomes

I agree with 26 of the 30 outcomes. Four need comment.

- **fig5c-cluster-removal (blocked): I do not agree.** Under the criterion, blocked applies only when the two SVM readings disagree.
  - The Methods' reading is not reproduced (decoding_clusters_whisker cell 7).
  - The code's reading was run 3 times with different seeds, plus once with the code's quiet rule. It is not reproduced in 3 of those 5 runs (cell 7):
    - seed sets 1 and 2: cluster 25 is not significant (p_FDR 0.075 to 0.234);
    - the mean of the three sets: three other pairs are significant, where the criterion allows two.
  - Even the code's quiet-rule run, counted as partial, has cluster 11 significant in wS2.
  - Only seed set 0 gives partial. The record treats set 0 as the main run without saying so or marking it as an assumption.
  - The evidence supports not reproduced. At least, the choice of set 0 should be marked `assumed`.
- **fig5d-null-space-decoding (blocked: not runnable): I still do not agree.** The inputs are in the dataset; only the subspace optimisation would need re-implementing. My disagreement is recorded.
- **figs18-later-lick-coding (not reproduced): I agree under the claims file, but the claims file misreads the paper.** Supplementary Fig. 18, which the reader did not read, is in `paper/supp1.pdf`. Its legend defines the effect: "The projection amplitude in the lick coding direction was largest for ALM, followed by wM2, wS2 and wS1 (in rank order), with A1 having the smallest and not significant difference."
  - That is the plain lick minus no-lick difference. In cell 89 the notebook shows it but does not judge it: ALM 0.46, wM2 0.35, wS2 0.18, wS1 0.11, A1 smallest. That is the paper's order.
  - The criterion's two readings, Cohen's d and the Kruskal–Wallis H, are not the paper's measure. Under the paper's own measure this claim would be reproduced. I report this; I do not correct it.
- **fig2-other-trial-types (not reproduced): I agree under the criterion.** The two thresholds are the reader's, and the Supp. Fig. 3 legend says only that effects on the other trial types "were less prominent". The data fit those words: the largest change is 19.0 points, against 33 to 52 on Go-tone Whisker trials. The outcome depends entirely on thresholds the paper does not give. I report this.

Notes on outcomes I agree with:
- **fig8a-wm2-lick-divergence (partial).** The criterion tests Nogo-tone lick against Nogo-tone no-lick trials. My text extraction of the Supp. Fig. 17 legend is incomplete. It appears to give the wM2 Nogo-tone result as "Nogo-tone Lick vs No tone no lick trials", a pair cell 82 never computes. This is a possible misreading for the reader to check.
- **fig4-29-clusters (not reproduced).** Low confidence. The four seeds put the BIC minimum at k = 36, 40, 42 and 42 (cell 13), and one seed alone would give partial. More initialisations can only lower the BIC at each k, and probably most at large k. So the minimum is more likely to stay at or above 38 than to fall to 29.
- **fig7d-context-decoding-after-whisker (blocked).** Correct by the criterion's rule. But it rests on a reduced Methods run (1 run, 2 of 10 baseline bins), and that run's wM2 and ALM onsets are one bin apart.
- **fig8b-lick-coding-direction (reproduced).** Holds under the criterion. ALM's Go-tone comparison comes after a non-significant Kruskal–Wallis test (p 0.155); the record says so.

**Assumptions.** No outcome in the record carries `assumed: true`. Four outcomes rest on choices that should be flagged:
- **fig3d:** partial is the author's judgement, since the criterion has no case for this result. It is stated in the notes; it is reasonable.
- **fig5c:** seed set 0 taken as the main run. It is not stated; I do not think it is reasonable (see above).
- **fig7d:** a 1-run, 2-baseline-bin grid search stands in for the criterion's Methods reading. It is stated; it is weak, given the run time printed (see section 2).
- **fig4:** 20 GMM initialisations stand in for 1,000. It is stated; it is acceptable.

### 2. Sentences the printed numbers do not support

**reproduce_ghaderi_2026.ipynb**
- Cell 48: "The code's whisker-only quiet rule gives the same pattern." Cell 46 shows that under this rule (i) fails for ALM, type 1 against type 3 (p 0.0547). The record states this correctly.
- Cell 91, the Summary: "two sessions have trials without video". Cell 7 shows that all 35 sessions have at least one such trial, 343 in all. Two sessions have many (243 and 29).
- Cell 91: "optogenetic sessions … are those of the paper". Cell 13 shows ALM inactivation in 7 mice, where the paper gives 8.
- Cell 77, minor: "the code's FDR … gives the same bins for … wS2". The pre-stimulus negative bin at 0.96 s drops out (cell 76).

**decoding_delay.ipynb**
- Cell 0: "about 25 ms per bin and subset … grid search about ten times more". Cell 5 prints 99 ms against 93 ms for the warm-up. The full runs work out to about 6 ms against about 300 ms per fit.
- Cell 8, minor: the Methods' A1 accuracy is given as "53.0"; cell 6 prints 53.05, and the record gives 53.1.

**decoding_clusters_whisker.ipynb**
- Cell 8: "about 77 min per run". Cell 6 prints "about 39 min per run".
- Cell 11: "about 57 min per run". Cell 10 prints "about 30 min per run".
- Cell 8: "with the code's quiet rule (one other pair)" gives partial. Cell 7 shows that under that rule cluster 11 is also significant in wS2, which the claim says should not happen.

**Attempt record**
- fig4 `measured: 44`. Cell 13 gives 40 (best of 20), as the record's own notes say.
- fig5b deviations: "about 54 min … and 45 h". decoding_delay cell 5 prints 28 min and 23.8 h.
- fig5c deviation and response, "77 min", and fig7d deviation and response, "57 min": as above.
- fig5c notes: the code's quiet-rule run is called partial; this is the cluster 11 in wS2 point above.
- fig2-other notes: "(4.4 to 12.6 points)" is given for a group that includes the Go-tone No-Whisker changes in the Auditory window. Those run from 8.2 to 19.0 points (cell 37).
- The data_missing finding and the fig8b response, "BehavioralEvents hold only Valve_OpeningTime". No notebook output shows what BehavioralEvents contains.
- Inputs: "the notebooks print the lines they rely on". Only the nwb_findQuietTrial.m and PSTHBehavior.m lines are printed (cell 24). The Data_Clustering.ipynb choices are asserted in comments only.

**README**
- "decoding_delay.ipynb … About 30 minutes". Its cell 13 prints 16.8 min.

**My round-1 reasons.** The verifications section states my round-1 reasons accurately and in my own words. The omissions are minor:
- units-recorded: "probe sessions and mice match";
- fig4b: "partial is the floor either way".

### 3. Round-1 points

**Resolved**
- **Point 3 (no-video trials in the quiet rule).** The code lines are printed and a per-session NaN table is shown (cell 24).
- **Point 7 (20 or 21 delay bins).** Explained.
- **Point 9 (Methods reading on the cue bins).** Run (decoding_delay cell 10).
- **Point 11 (fig8b and figs18 blocked).** Both are now tested.
- **Point 2 (code's quiet rule in decoding).** Done for fig5b and fig5c; not for fig7d, where it bears on no conclusion.
- **Point 4 for fig5b.** The spread over seed sets is now shown.
- **Point 6, in part.** The GMM now uses reg_covar 0 and four seeds.
- **Point 5.** Now moot: the Methods reading already fails on clusters 11 and 25.
- **Point 1** stays a claims-file matter, recorded as a finding.

**Remaining, bearing on a conclusion**
1. **fig5c:** the outcome should be not reproduced, or the choice of seed set 0 marked (section 1). The Methods reading is still a single run with p_FDR 0.085. The full run is printed at about 39 min, so it was feasible.
2. **fig7d:** the blocked outcome rests on a cut-down Methods run whose onsets are one bin apart. The full run is printed at about 30 min, so "for time" does not hold.
3. **figs18:** the claims file misreads the effect size; under the Supplementary Fig. 18 legend the notebook's own numbers reproduce the claim.
4. **fig2-other-trial-types and fig8a:** the claims file's criteria go beyond, or possibly misread, Supplementary Figs. 3 and 17.
5. **fig4:** the minimum still depends on initialisation (20 against 1,000), and the code-matching choices are not printed from Data_Clustering.ipynb.
6. **fig5d:** still blocked although the data are in the dataset.
7. **Record fixes:** stale numbers (`measured: 44`, the run times) and the missing `assumed` flags.
