I wrote the claims file at `claims/001845/10.1523-jneurosci.0143-26.2026.yaml`: 35 claims, all with quotes. Nothing is committed.

The quote checker passes every quote and the schema. It flags two p-values as not found, but both are in the text: "p = 1.410 × 10−10" (Fig. 3E) and "p = 0.2407586" (Fig. 7B). It misses the first because of the trailing zero and the second because it has 7 significant digits. I left the checker and the recorded values as they are.

**Text read.** The version of record (open access, PMC13277500, served by Europe PMC): main text, Materials and Methods, and the legends of Figs. 1 to 8. There was no PDF, so I saw no figures.

**Code.** The repository the paper links, JadhavLab/Social_CoOp_Behavior (commit e2d560d), holds only a README. There is no analysis code, so no method detail is settled by code.

**Counts.**
- 35 claims, all findings, no link claims.
- 35 have quotes, none are marked inferred.
- 31 have statistics (80 values in total).
- 35 have criteria.
- 8 have expected values.

**Details the paper leaves open, and the readings named:**
- **ANOVA type.** The legends say "Two-way RM ANOVA", but every reported df fits an ordinary two-way ANOVA (genotype × session) on one value per unit and session. The readings are that ordinary ANOVA (A) and a mixed-design repeated-measures ANOVA with pair or rat as subject (B). Absence claims are judged on A, with B shown as a variant.
- **Number of 50% sessions.** The df show 33 sessions in Figs. 3E, 4C and 5E. The readings are the first 33 and the first 35.
- **Rate units** (match and transition rates, Fig. 1): per minute, or count per session.
- **Performance equation (Eq. 1)** is garbled. The text says the maximum is 100%, so I read it as 200 × matches / transitions. The scale factor changes no test.
- **Fig. 1G regression:** what a data point is (pair-session, rat-session, or session). The legend's n = 35 doesn't fit its p-values.
- **Fig. 1H permutation:** which rat is shifted, how far, and which sessions count as early and late.
- **Fig. 1J classifier:** the moment the partner's location is read (three readings), and whether sessions are pooled per rat or scored per session.
- **Fig. 2B:** which transparent sessions are compared with the opaque ones.
- **Sample entropy (Fig. 3D):** m = 2 or m = 3, with r = 0.2 SD.
- **Optimal triplets (Fig. 3).** The Methods list 8 of the 12 triplets without a repeated well. The readings are any triplet visiting all three wells, or only the literal 1-2-3 and 1-3-2.
- **Jaccard similarity (Fig. S2):** which sets are compared and how a pair is summarised. Its test is in the supplement.
- **Arrival, departure and dwell time (Fig. 4):** the Methods don't define them. The readings are poke times, or the 40-pixel zone around a well.
- **Cross-correlation (Fig. 4):** well centres, the downsampling method, what counts as an arrival, the shuffle, and the lag range searched for the peak.
- **State-space model b0 (Fig. 5):** read as 0, following Smith et al. 2004.
- **Leading difference (Fig. 5E):** absolute or signed.
- **Trial definition and data points for the Fig. 7C correlation.**
- **Gaze GLMMs (Fig. 7G, H):** how the session blocks are cut and how gaze durations are normalised.
- **Fig. 8 GLMM:** the subject's own-history covariates, the scaling of Δt, and the reference level for per-genotype betas.
- **Fig. 8B:** whether the partner's previous trial is looked for within the session or across sessions.
- **MARL model (Fig. 6):** learning rate, discount factor, steps per episode, number of runs and the state encoding are not given, and there is no code.

**Contradictions in the paper, noted in the claims:**
- The Results say Fmr1 dwell times are longer, but the legend's tests are not significant (p = 0.25 and 0.063).
- The Results say Fmr1 rats did not adjust to partner behaviour at 50%, but the legend gives Fmr1 β = 0.13 with p < 0.01 there.
- For the visual-cue genotype effect, the Methods give p = 0.981 and the legend gives p = 0.391.

**Missing from the paper.** The supplement is not in the text: Figs. S1 to S3 (mixed pairs, Jaccard similarity, leadership history) and Tables S1 and S2 (the gaze GLMMs). The three claims on Figs. S1 to S3 rest on the Results sentences alone, and their tests are unknown. Following the precedent of claims/001887, I wrote claims anyway because the main findings rest on Figs. 1 to 8, which are complete. The Methods also never define arrival lag, departure lag or dwell time, though the Fig. 4 legend refers to them.

**Data.** The dataset's description covers the cooperative task: event timestamps, well-visit intervals and positions, for 5 pairs per genotype group. Whether it also holds the opaque-barrier sessions, the mixed pairs, the visual-cue and virtual-agent tasks, or the DeepLabCut keypoints the gaze claims need is for the author to find. The MARL claim is a simulation and uses none of the dataset; I marked it `with_inputs`.
