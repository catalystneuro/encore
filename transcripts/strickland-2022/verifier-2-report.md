# Round 2 verifier report: Strickland and McDannald (2022), attempt strickland-2022-01

## 1. Outcomes

The claims file has 30 claims, and the attempt record has 30 outcomes: 23 reproduced, 6 partially reproduced, 1 not reproduced, 0 blocked. **I agree with all 30.** In round 1 I disagreed on four of them. All four are now settled:

- **fig2c-pc1-contribution (reproduced):** I now agree. The claims file's standard for a k-means result is the median over 20 seeds. On that measure the nine largest clusters hold 481 units, within 505 ± 50.5. Single seeds range from 360 to 590, and 13 of 20 are within tolerance (cell 35). The L1 part matches Source Data to 0.0003 (cell 34).
- **fig4b-phasic-network and fig4b-tonic-network (partially reproduced):** These are now judged with Pearson r, as the criterion says. Every profile part holds and the network part fails: within −0.329 against 0.008 for phasic, −0.250 against 0.000 for tonic (cell 72). Under the criterion that is partial.
- **fig5e-no-anatomical-bias (reproduced, assumed):** I accept this. My round-1 "partial" was my own call, not one of the criterion's levels. The claims file's own check log keeps reading p-b "for Fig. 5e only". Under p-b the largest differential is 4.48, which equals Source Data. The record now states the assumption and that p-b passes by construction. It also reports p-a: 9.82, with a permutation p of 0.001 (cell 93).

**Assumptions flagged `assumed: true`:**
- **fig2f (r squared):** stated and reasonable. The Methods write "(R2)" and the Source Data column is headed R2. With r, k1 and k3 are the two highest means, so the claim would not even be partial (cell 45).
- **fig5e (p-b):** stated and reasonable, for the reason above.

**One assumption that is not flagged:** cue-outcome-membership-independent is judged on L1. Under L2 the median goodness-of-fit p values are 0.048 (phasic) and 0.011 (tonic), and only 4 of 20 seeds pass (cell 96). Its criterion only says "reported under L1 and L2", so choosing L1 to decide is a judgment that would flip the outcome. That judgment is reasonable and the notes state it, but it should carry `assumed: true`.

## 2. Sentences the printed outputs do not support

- **Cell 61, and the attempt record's fig3d-supranetwork-lesion notes:** both say PC2's "probability peak [is] in the first cue second". Cell 58 prints `PC2 |prob| peak s` = 2, the index into cue seconds 1 to 10 plus one, so the peak is in the second cue second. The criterion only needs the first half, so the outcome stands.
- **Cell 73:** "k6 is the only cluster inhibited to surprising shock". Cell 72 shows a negative uncertainty-shock mean for k3 (−0.14), k4 (−0.31), k5 (−0.18) and k9 (−0.24) as well.
- **Cell 73:** the tonic network fails "because k3 and k6 change firing in the opposite direction to their fellow clusters". This is incomplete for the tonic network. The r matrix in cell 72 shows k9 anticorrelated with k7 (−0.60) and k8 (−0.79) and positively correlated with k6 (0.67), so k6 and k9 together oppose k7 and k8. The record's own wording, "k6 is anticorrelated with k7 and k8", is accurate.
- **Cell 88:** "L2 gives 47.80 and 30.92%, out of tolerance". Only PC1 is out of tolerance. 30.92 lies inside 33.4 ± 3.34 (30.06 to 36.74).

Every other "Result" sentence (cells 14 to 97), the Summary (cell 99), the README table and text, and the record's notes and findings agree with the printed outputs. I checked counts, p values, the seed medians, the 4-of-20 count, the 9-of-10 animals and the latency counts.

**Round-1 reasons in the record:** the verification entries give my round-1 reasons in my words. Each claim's problem points have been folded into its reason. The only omission is minor: the Source Data latency R² values (0.508 and 0.394) are left out of the fig2d reason, though they appear in the notes.

## 3. Round-1 points

**Resolved:**
- **Point 1 (fig4b r against r²):** on the attempt's side, the outcomes now follow the criterion.
- **Point 4 (L2 resting on one seed):** fig2c-pc1-contribution and cue-outcome now use all 20 seeds. Elsewhere L2 is only a variant.
- **Point 5 (latency markdown):** corrected. Cell 11 also shows that no script computes the latency.
- **Point 6:** v-b now runs on s-c, giving 0.263 against 0.266 (cell 59).
- **Point 7 (Fig. 4f k7/k8 labels):** explained as swapped labels. The rows labelled k7 hold 111 k7 values and 60 k8 values (cell 78).
- **Point 8:** `z.ms500` is now recomputed from the spike times, largest difference 9.5e-13 (cell 5).
- **Round-1 section C:** script passages are now printed (cell 11). They cover subject mapping, region remap, regression terms, PE/shock column order, lesion shuffles, the outcome hub r², and empty trials set to 1. L2 now runs per seed. s-c stability is shown: standard deviation 0.0001, and the subnetwork lesion's weight is above the supranetwork's in 0 of 10 runs (cell 60).

**Still open, bearing on a conclusion:**
- **fig4b-phasic/tonic:** the claims file allows r and r² for fig2e but only r here. With r² both claims would be reproduced. This is a claims-file inconsistency, now referred to a reader.
- **fig5e:** the threshold comes from the same quantity it tests, so p-b cannot fail. The reproduced outcome adds nothing beyond the Source Data link, and the Results' reading (p-a) fails. This is a claims-file design flaw.
- **fig2f:** Source Data matches the 42-column r², not the Methods' danger-only measure. This is a paper inconsistency; the outcome is partial under the criterion.
- **fig3c/3d:** the criteria compare unit-norm weights. With loadings, fig3c would pass (0.709 against 0.680). This is a claims-file weakness, referred to a reader.
- **fig2d:** how the paper computed its latencies is still unknown; the record lists it as a finding.
- **cue-outcome-membership-independent:** the L1 judgment should be flagged `assumed: true` (section 1).
- **Shuffle function:** it is not in the data set. The lesion matrices still match the Source Data percentages to within 0.04 points.
