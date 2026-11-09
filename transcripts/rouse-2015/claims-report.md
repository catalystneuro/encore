I wrote `claims/000941/10.1152-jn.00686.2015.yaml`. It parses and the quote checker accepts all 25 quotes. The checker raised one flag, which I could not clear (point 4 below). Nothing is committed.

**Text read.** The version of record of the paper (J Neurophysiol 114:3268–3282), taken from the supplied PDF. It is complete: Methods, Results, all figure legends and Tables 1 and 2. The paper has no supplement and links no code, so no code was read. The dataset's title is "FALCON Benchmark M1-A: primary motor cortex recordings…". Whether it actually holds this paper's kinematic data (markers or joint angles) is for the author to find out.

**Claims.**
- 25 claims, all findings; there are no link claims.
- All 25 have a quote and a criterion; none needed an `inferred` note.
- 3 have statistics: the Kruskal-Wallis test on movement time, and the Bonferroni-corrected ANOVA F-tests behind Fig. 4 and Fig. 5.
- 6 have expected values: the Table 2 trial counts, the median movement times and sample counts, the 28 trials in Fig. 2, the Qm values in Fig. 6A, and the Fig. 7 mean effect sizes at the 30% and 90% points.
- Every claim uses the dataset alone; nothing comes from outside data.

**Details the paper leaves open, with the readings named:**
- **Sum-of-squares type** for an unbalanced design with empty cells: type I (location first), type II, or type III (Matlab's default).
- **Where the 153, 143 and 185 tested time points lie** around movement onset and contact, which also sets the maximum error term: split equally before onset and after contact, with the maximum taken from onset to contact only as a variant.
- **Movement-onset threshold:** baseline mean plus 5 SD, or 5 SD alone.
- **The 30% and 90% points:** nearest sample, or interpolated.
- **Discriminant analysis:** class priors (empirical or uniform), stratified folds or not, and how the confidence interval is formed after averaging (pooled counts, or the mean accuracy).
- **Which trials are counted:** analyzed or all successful trials, for the Table 2 medians and for the 28 trials in Fig. 2.
- **Elbow flexion:** the Results say object effects dominate in all three monkeys; the Discussion says location and object are similar in monkeys X and Y. Both readings are listed, and the Discussion's agrees with Fig. 6A.
- **Fig. 10's monkey is not named:** monkey L, or each monkey.
- **Words with no number behind them** ("nearly 100%", "little or no object effect", "almost all the variance"): read with the protocol's default 10% tolerance, so at least 90% correct, Qm of at least 0.9, and an effect size of at least 0.9.
- **Shapes with no stated measure** (bell-shaped, monophasic, pause, "comparable", "early", spread of the finger markers): the measures in the criteria are my readings and are marked as open.

**Missing or uncertain in the paper:**
1. There are no numbers for the classification accuracies (Fig. 8), the trajectories (Figs. 9 and 10) or the effect-size curves (Fig. 5), so those claims are judged by the criteria alone.
2. The plots of the elbow-point trajectory are described but not shown.
3. The text gives 798 successful trials for monkey X and Table 2 gives 788. The table is used, with 798 named as a second reading.
4. The extracted text garbles the "<" and ">" signs. I took each one's direction from its sentence. The Kruskal-Wallis bound is printed as "P �10�3"; I read it as P < 0.001, and this is the one value the checker flagged. I could not open the PDF page to confirm it, because no PDF renderer is installed here.
