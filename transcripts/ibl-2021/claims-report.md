I wrote `claims/000045/10.7554-elife.63711.yaml`. The quote checker reports 38 claims, 38 quotes, 26 statistical values and 0 problems. Nothing is committed.

**Text read**
- The eLife version of record (PMC8137147, from Europe PMC): main text, figure and figure-supplement legends, Methods, the Appendix 1 table, and the reviews with the authors' responses.
- The only supplementary file is eLife's transparent reporting form, which holds no results.
- The Methods send the reader to "Protocol 2" (figshare doi:10.6084/m9.figshare.11634729.v3) for the psychometric fitting and the full training criteria. That protocol is not in `paper/` and I did not read it; the code settles the fitting.
- Code: `int-brain-lab/paper-behavior` at commit `edc4531…`, the commit the paper archives. It has one script per figure panel and reads from the IBL DataJoint database.

**Claims**
- All 38 claims have a quote and none needed an `inferred` note.
- 16 claims record statistics (26 values) and 37 have criteria.
- `fig3f-positive-control` is marked `with_labels`, because the lab-to-time-zone mapping comes from the code. All other claims use `dataset`.
- The opening comment defines the shared selections, the psychometric fit, the lab test and the lab classifier, so each criterion can refer to them by name.

**Details the paper leaves open, and the readings named**
- **When a mouse became proficient:** the code reads a training-status label from the IBL database. Readings: use the dataset's own label if it has one; otherwise recompute it from the trials with the 1a criteria, or with the 1b criteria from when they were introduced. The paper says only "September 2019" for that date.
- **Counting days to proficiency:** the code counts up to and including the proficiency day in one branch and up to the day before in the other.
- **Figure 2 interquartile ranges, the absolute bias and threshold during training, and performance at days 15 and 40:** the code does not compute these numbers. Readings cover whether values are median-filtered, what "thereafter" spans, whether means pool all sessions or average lab means, and per-day versus binned values.
- **Threshold 14.3 ± 3.8 (n = 7 laboratories):** spread over mice, or over the seven lab means.
- **Basic-task choice consistency:** the legend says the Figure 3 sessions; the code uses the proficiency day and the two days after it.
- **First three full-task sessions:** the legend says the first three; the code uses days 1 to 3, or −1 to 3 in the classifier script. The code also applies a Holm-Sidak correction the legend does not mention.
- **Trial duration p = 0.004:** with or without the code's FDR correction.
- **The choice model (GLM):** the Methods say three sessions per mouse, while the code uses a window of training days from 2 before to 3 after the first full-task session. The Methods include 50% contrast and the code drops it. For accuracy, the legend counts a prediction as accurate when the actual choice gets more than 50% probability; the code averages the predicted probability. The 5-fold cross-validation has no seed.
- **Random Forest prediction of slow learners (53%, 7%):** there is no code for it and the Methods do not describe it. Readings cover the features and what "accuracy" means; the claim is blocked as `methods_underspecified` if the readings disagree.
- **Win-stay/lose-switch, updating by contrast, and session-end criteria:** these follow the code. If the dataset has no session end status, the session-end claim recomputes it from the legend's three criteria.

**Gaps and inconsistencies in the paper**
- Protocol 2 is missing, as above.
- t(125) = 4.817 gives p ≈ 4×10⁻⁶ (two-sided), which is above the printed "p<10⁻⁶". The criterion uses the t value as the reference.
- Several "similar across labs" findings report no test (Figures 4f–i and 5). Their criteria take the tests the code runs.
- The dataset's archive description cites the bioRxiv preprint of this paper.
