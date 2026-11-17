**Verifier report, round 3: Ghaderi et al. 2026 on DANDI:001530 (0.260605.0601)**

The claims file has 30 claims and the attempt record has 30 outcomes: 14 reproduced, 9 partially reproduced, 3 not reproduced and 4 blocked. Only one outcome has a proposed change: fig5c-cluster-removal. The cells cited are in `decoding_clusters_whisker.ipynb` unless marked "main", which means `reproduce_ghaderi_2026.ipynb`.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig5c-cluster-removal | not reproduced (from blocked: methods_underspecified) | Yes | — | The numbers come from the data, and both readings give not reproduced. The dependency on fig4b does not touch the parts this claim uses. Details below. |

**fig5c-cluster-removal, in detail**

**1. The numbers come from the data (cells 6 and 7).** The proposal's figures match cell 7:
- **Methods' grid search:**
  - Cluster 25: 1.31 and 1.91 points, p_FDR 0.085 in both wM2 and ALM, so not significant.
  - Cluster 11 is significant in wS1 (0.20 points, p_FDR 0.030; cell 6).
  - Either result alone fails the criterion's "clusters 11 and 25 behave as stated". Outcome: not reproduced.
- **Code's decoder, seed sets 1 and 2:** cluster 25 p_FDR is 0.075 and 0.194 (set 1), and 0.152 and 0.234 (set 2). Outcome: not reproduced.
- **Code's decoder, mean of the three sets:** the four decreases are within tolerance and significant. But three other pairs are significant (cluster 2 in wM2; cluster 13 in wM2 and ALM), and the criterion allows at most two. Outcome: not reproduced.
- **Code's decoder, code's quiet rule:** cluster 11 is significant in wS2, which the statement excludes. Outcome: not reproduced.
- **Code's decoder, seed set 0:** the only run that gives partial, with one other pair significant (cluster 24 in A1, 0.49 points).

**2. The choices were not made to reach the result.**
- The sign of the decrease is turned, as the deviations state, and only positive decreases count as significant. Both match the criterion's wording.
- All seed sets of the code's decoder use the same construction (seeds 10000·r + 5000 + i). The quiet-rule run shares set 0's seeds.
- Averaging over the sets is a fair way to reduce Monte-Carlo noise, and sets 1 and 2 also fail on their own. The outcome does not depend on that average.
- Set 0 is now described as the first run, not a chosen main run (cell 8). That answers my round-2 objection.

**3. The criterion is applied as written.**
- The fig5b rule says that when the two SVM readings disagree, the claim is methods_underspecified. Here they do not disagree: the Methods reading is not reproduced, and the code reading is not reproduced in 4 of its 5 runs, including the least noisy one.
- Confidence is moderate. The Methods reading is still one run, covers only clusters 11 and 25, and its cluster 25 p_FDR is 0.085.
- More runs cannot easily move it to partial. Cluster 25 would have to become significant and cluster 11 would have to lose significance in wS1, both at once.
- Testing the other 27 clusters could only add failures.

**4. The dependency on fig4b-named-clusters.**
- I could not read the rule itself, because `docs/protocol.md` is not among my materials. My judgement is that the dependency does not apply here.
- The fig5c criterion uses fig4b only for its cluster labels ("Cluster labels as fig4b-named-clusters"). Those labels come from cluster-label-link, which is reproduced: all 10,294 labelled neurons link with matching area, CCF label and layer (main, cell 56).
- fig4b is blocked only because the two readings of "mostly" disagree on cluster 1 (30.5% A1). The parts on clusters 11 and 25 hold under both readings (main, cell 59):
  - their shares in wM2 and ALM are 90.4% and 83.1%;
  - Hit against Nogo CR over the late delay is 11.54 against −0.79 Hz and 3.56 against −0.29 Hz.
- If the protocol's rule is meant to apply mechanically, without that judgement, the outcome would stay blocked.

**Minor record fixes, which do not affect the outcome**
- **Run time:** cell 8 and the proposal's notes give "about 74 min per run" for the full Methods grid search, but cell 6 of this run prints "about 77 min per run".
- **Mislabelled row:** in cell 7, the Methods row "mean of sets" is a copy of set 0, since only one Methods run was made. Calling it a mean overstates what was run.
