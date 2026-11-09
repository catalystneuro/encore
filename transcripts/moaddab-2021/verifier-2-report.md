**Round-2 verification: Moaddab & McDannald 2021 (doi:10.1016/j.cub.2021.02.055) on CRCNS rrf-1**

**1. Outcomes and assumptions**

The claims file has 30 claims and the attempt record gives an outcome for each: 24 reproduced, 5 partially reproduced, 1 not reproduced, 0 blocked. I agree with all 30 outcomes. Four of them need a comment:

- **kmeans-elbow (reproduced).** I agree with the outcome, but the record gives a weaker basis than it needs. It rests the outcome on the code's single run and the code's `mean(sumd)` measure. That measure is a sum at k = 2, and its drop from 2 to 3 (4848) is larger than its drop from 1 to 2 (1216). With the Methods' measure, the same runs are not monotone (cell 20). The claims file's criterion accepts the result under z-a or z-b. With scikit-learn, z-b meets it in 4 of 4 combinations, so the outcome holds on the claims file's own terms. The deviation also says "the Figure 1E axis (0 to 9000) fits only the code's measure." No printed output shows that, and I could not check it.
- **fig6f-k6-ppe-then-valence (changed from reproduced to partially reproduced).** I agree. The change comes from the 20-draw majority rule (omission CI excludes zero in 18 of 20 draws; cell 85), and the partial condition holds (cell 100). The majority rule is the author's convention, not the claims file's, so the record should say so. The rule is applied to all judged CIs alike, and it is the stricter choice here.
- **fig6a-k1-shock (not reproduced).** I agree under the claims file's window of 0 to 8 s. The claims file's second reader confirmed the gray boxes from the rendered page, so the claims file reads the figure as drawn. The mismatch with Table S4 is correctly recorded as a paper inconsistency.
- **fig3d-inhibitory-clusters (reproduced).** I agree, but it holds on an 11-of-20 majority for the k8 uncertainty − safety CI.

Every outcome marked `assumed: true` states its assumption: the code's normalization, the code's clusters, and for fig6 the claims file's window. The code lines are now printed in cell 7, so I find these assumptions reasonable.

**2. Statements the printed outputs do not support**

- **Cell 49:** "R2 0.479, 0.209 and 0.210". Cells 47 and 48 print 0.483, 0.214 and 0.210.
- **Cell 27:** "differ between clusters … under both readings of the inter-spike intervals". In the variant, skewness has p = 0.0511 (cell 26), which is not significant.
- **Cell 86:** "Two of them change a count against the single draws … and the k8 uncertainty - safety CI (fig3d) includes zero … in 11 of 20". The single draw for k8 already includes zero ([−0.002, 0.131], cell 38), so k8 changes nothing. Only k6 changes a count.
- **Cell 108 (Summary):** "Every count, F value and correlation of the paper that depends only on the data and the code was recovered". Several were not:
  - Table 1 cue F for k4: 8.09 against 7.93.
  - Table 1 outcome F: k4 47.5 against 46.62, k7 94.8 against 95.16, k1 1.21 against 1.23 (cell 79).
  - Regressor × cluster: 2.40 against 2.15.
  - Table S3 for k3 and k5.
  
  "Most" would be accurate, as the README says.
- **Cell 33:** "for k1 the degrees of freedom are those of Table 1, F(110, 3520)". Table 1 prints no df. The df are the claims file's inference from the printed partial eta squared.
- **Record, fig5a-tuning-anova deviation:** "the weighted version gives F = 21.87". No output prints this.
- **Record, fig4ghi notes:** "their late cue and delay R2 are outside the tolerance". This is incomplete: under z-b the onset R² (0.1215 against 0.14 ± 0.014) is outside too (cell 50).
- **Record, fig6g notes:** "the means are larger than Table S4's". Cell 103 prints only how many means are within tolerance, not their direction.
- **README:** "gives the paper's eight clusters exactly". What the outputs show is that the sizes match and the pattern map agrees (cell 23). With no label file, membership cannot be confirmed.

Everything else checks against the outputs. That covers the other conclusions in cells 10–107, the Summary table and the README counts table: 3 / 17 / 2 / (4, 3, 1) adds up to 24 / 5 / 1. The attempt record restates my round-1 reasons faithfully in its own wording, including the B-references.

**3. Round-1 points**

Resolved:
- **2 (normalization):** cell 7 prints the code's z-score lines.
- **3 (Table S3):** no unit is dropped to fit the outcome; the 362-unit pooled ANOVA was run, giving 28.72 and 4.34 against the paper's 28.57 and 4.13.
- **4 (bootstrap):** nested standard errors and 20 draws were added.
- **5 (elbow):** the code's measure is printed and the MATLAB-stream variants were added.
- **6 (k-means readings):** the full table of readings was run.
- **7 (k5 tuning bins):** the code's line 3499 is printed.
- **1, in part:** the claims file does not misread the figure. The gray boxes are 0 to 8 s, confirmed by the second reader's check and by the code's trace axis.

Still open and bearing on a conclusion:
- **Figure 6 window (point 1).** The record asks a reader and the authors which interval the paper analysed. The answer decides fig6a (0 to 8 s: not reproduced; 0 to 4 s: reproduced). It also decides the k5 omission mean in fig6de.
- **CIs at the zero boundary.** fig6b and fig6f depend on draws where the CI lands just past zero (5–20% and 10–20% agreement), and on the majority convention, which the claims file does not set.
- **k4 in fig4abc part (2) (point 8).** This is with a reader. Even with k4 excluded, k7 still fails, so the outcome would probably stay partial.
- **kmeans-elbow basis.** The record should cite the claims-file reading that passes (z-b with scikit-learn, 4 of 4) and not rest the outcome on the code's `mean(sumd)`.
