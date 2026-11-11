**Verifier report, round 1: Kussovska et al. 2025 on DANDI:000469 (0.231213.2047)**

The claims file has 45 claims; all appear below. I queried the archive: the pinned version is valid, with 41 assets including 21 Sternberg `ses-2` files. It holds every input the three dPCA claims need (spike times and trial tables), and the notebook streamed those in 14 s.

### A. Outcomes

| claim id | outcome | reason |
|---|---|---|
| units-by-region | reproduced | 902 units from 21 patients; AMY 259, HPC 190, dACC 171, preSMA 250, vmPFC 32, all exact (cell 16). |
| behavior-accuracy | reproduced | 88.73% ± 1.25 (s.e.m.), exact (cell 18). |
| fig1c-accuracy-load1-vs-load3 | reproduced | Load 1 median 94.4% against 86.7% at load 3. Rank-sum raw p = 0.009, Bonferroni p = 0.027, which equals the paper (cell 20). |
| behavior-rt | reproduced | (a) 1.120 s (s.d. 0.252); (c) 1.097 s. Both are inside 0.78–1.34 (cell 22). |
| rt-in-vs-out-memory | reproduced | In-memory probes faster; p = 0.001–0.002 under all four readings (cell 24). |
| rt-correct-vs-incorrect | reproduced | Correct trials faster in 20 of 21 participants; p = 0.001 under both readings (cell 26). |
| fig1e-load-modulated-neurons | reproduced | Matched trials, shared permutation: preSMA 20.4%, vmPFC 18.75%, dACC 10.53%. All within tolerance, p = 0.000 / 0.009 / 0.025 (cell 28). |
| fig1f-rt-modulation-not-significant | not_reproduced | With each trial's own RT (the main reading), preSMA, AMY and dACC have BH p < 0.05 under every trial reading (cell 30). The paper's numbers (AMY 5.79%, preSMA 8.00%, vmPFC 6.25%, none significant) come out exactly only under the code's bug, which uses subject 1's RT vector for every neuron. |
| concept-cells-count | reproduced | Code reading gives 57–60 cells over seeds, with AMY 70.7% and HPC 19.0%. The Methods reading gives 49–54. Per participant 4.14 ± 3.66 (cell 32). |
| fig2ab-single-cells-not-persistent | reproduced | 50 of 58 cells are not persistent under (a), 48 of 58 under (b) (cell 34). |
| fig2c-population-persistence | reproduced | Load 1: preferred trace above nonpreferred in 100% of bins, all bins significant (cell 36). |
| ext1bc-persistence-by-load | reproduced | Significant bins: 1.00 at load 1, 1.00 at load 2, 0.60 at load 3 (cell 38). |
| fig2d-cross-temporal-localized | reproduced | 17 encoding or early-maintenance training bins generalize. The largest fraction of maintenance test bins reached from a maintenance training bin is 0.14–0.18 (cell 40). See problem 6. |
| ext1de-cross-temporal-load23 | reproduced | Off-diagonal kept pairs: load 1 217/280, load 2 6–10, load 3 0, under every rule and label (cell 42). |
| fig2e-maintenance-decoding-amy-mtl | reproduced | Methods reading: AMY 35.63%, MTL 33.61%. Code reading: 34.33% and 32.89%. All p = 0.001 (cell 44). |
| ext1f-maintenance-decoding-load2 | partially_reproduced | Both groups are significant and MTL is in tolerance (26.67 / 29.56%). AMY is above tolerance under both readings: 26.43 / 27.89% against 21.2–25.9 (cell 46). |
| fig2f-bin-width-decoding | partially_reproduced | All widths are significant and accuracy rises with width. But no reading has all four accuracies in tolerance: code 250 ms gives 30.0% (36–44); rank reading 250 ms gives 50.0% and 500 ms gives 66.67% (cell 48). |
| fig2f-bin-width-pairwise | not_reproduced | 1000 vs 500 ms is not significant under any reading (BH 0.08–0.48). Under the code trial reading, 500 vs 250 ms is significant (cell 51). The criterion's partial condition is not met either. |
| ext1g-bin-width-load2 | reproduced | Load 2 range is 16 points (code) or 4 points (rank), both below 20, and load 2 is below load 1 at every width (cell 53). |
| fig3abc-trajectory-complexity | blocked (too_large), contested | Nothing was computed. The data are present; the block rests on run time only (problem 1). |
| fig3d-encoding-vs-maintenance-separability | blocked (too_large), contested | Same as above. |
| fig3h-early-vs-late-maintenance | blocked (too_large), contested | Same as above. |
| fig4c-encoding-bursts-vs-poisson | reproduced | Only under methods groups / height rule / real threshold (d1 and d2). There, All902 has BH p = 0.0054 and LowACG 0.038 / 0.048, and the other four groups are not significant (cells 67–68). The LowACG result is marginal. |
| fig4d-maintenance-bursts-vs-poisson | reproduced (weak) | Under the 2.8 s window, the five named groups exceed the null and concept cells do not, in 8 of 12 readings (cell 70). With each trial's own maintenance length (cell 71), ShortDecay fails (BH p = 0.114). See problem 3. |
| fig4-acg-group-differences | partially_reproduced | With the prominence rule, low ACG exceeds high ACG in both epochs (p = 0.0005). Short τdecay never exceeds long in encoding (p = 0.086–0.20). With the height rule the low/high direction reverses (cell 73). |
| fig4f-all-cells-epochs | partially_reproduced | Encoding to M1, M2 and M3 rises with q < 0.05 under the prominence rule. Encoding to probe is not significant under any reading (q = 0.61–0.71; medians 6.0 vs 5.5) (cell 75). |
| fig4hj-group-epochs | partially_reproduced | Under `*/prominence/M-code`, long τdecay rises at M1, M2 and M3, and low ACG, short τdecay and concept cells have 0 significant pairs. High ACG never rises to the probe (cell 78). |
| ext2-bursts-loads23 | reproduced | `methods/prominence/M-code` holds for all three groups at loads 1, 2 and 3 (cell 80). |
| acg-fit-yield | reproduced | 317 (all spikes) and 298 (trial spikes); tolerance 264.6–323.4 (cell 57). |
| fig5c-cell-type-clusters | reproduced | Reading (b) gives PY 100 and IN 198, both in tolerance. Reading (a) has PY 102, outside 82.8–101.2 (cell 59). |
| fig5dfh-cluster-features | reproduced | IN is higher on all three features, BY p ≤ 8e-5 under both readings (cell 61). |
| fig5gh-burst-index-cv2 | reproduced | Reading (b) types with the plain ISI CV of session spikes, medians: burst index 0.947 / 0.622 and CV 1.593 / 1.322, all in tolerance; p = 5e-3 and 1e-4 (cell 63). Holt's CV2 (1.18 / 0.93) never matches; the paper's "CV2" is a plain CV. |
| supp4-rodent-validation | reproduced | On the code's shipped features (data elsewhere): 333 of 343 correct, 1 PY and 9 IN misassigned (cell 65). |
| fig5kl-concept-cell-types | reproduced | Reading (b): PY 11, IN 14. Burst index 0.949 > 0.390 and Holt CV2 1.217 > 0.991. Reading (a) gives 16 IN concept cells, out of tolerance (cell 82). |
| fig6ab-celltype-bursts-vs-null | partially_reproduced | No reading meets all four parts. With the Poisson null and prominence rule, IN encoding is also elevated (q = 0.02–0.03). With the height rule, PY encoding fails (q = 0.06–0.11). With the label-shuffle null, IN maintenance fails (q = 0.063) (cell 84). |
| fig6cd-celltype-epochs | not_reproduced | IN encoding to probe has q = 0.73–0.80 under every reading. PY is stable at all loads only under M-code. The criterion's partial condition (load 1 only) does not apply (cells 86–87). |
| ext5bd-in-load-dependence | reproduced (weak) | The measure rises from load 1 to 3 (3.67 → 6.33) only under `prominence/M-code`, 2 of 8 readings (cell 89). |
| fig6e-load-modulation-in | partially_reproduced | IN 13.95% with p = 0.001 in tolerance; PY groups p ≥ 0.157. IN concept is 18.75% or 25.0% (tolerance 19.3–23.6). Under the (b) types it is 14.29% with p = 0.15 (cell 91). |
| fig6f-rt-modulation-in-concept | not_reproduced | With own RT, IN concept is 12.5% (p = 0.19), while all IN and PY are significant (cell 93). Only the code's subject-1 RT variant gives IN concept 31.25% with p = 0.001. |
| fig6gh-in-concept-cv2 | not_reproduced | IN preferred, maintenance vs encoding: p = 0.86 (load 1) and 0.13 (all loads) (cell 95). |
| ext5gh-py-decay-preferred | not_reproduced | PY preferred vs nonpreferred: p = 0.13–0.73 in every epoch and load set (cell 97). |
| fig6i-py-bin-width-decoding | not_reproduced | 750 and 1000 ms have BH p = 0.072 and 0.060; 250 ms gives 33.3%, outside 24.0–29.3 (cell 99). |
| fig6j-in-bin-width-decoding | partially_reproduced | Every width is significant (BH p = 0.002). Two of four accuracies are out of tolerance under each reading (code: 46.67 and 53.33 at 750 ms) (cell 101). |
| fig6kl-cross-temporal-by-type | reproduced | PY has 0 significant pairs; IN has 162–230 kept off-diagonal pairs (cell 103). |
| ext5ij-load2-decoding-by-type | reproduced | IN has BH p ≤ 0.013 at all widths; PY has none below 0.49 (cell 105). |

### B. Problems

1. **[affects a conclusion]** Cells 54–55: the block on fig3abc, fig3d and fig3h is about compute time, not data. The estimate is 127 min of serial dPCA fits, while the notebook took 19.2 min. The splits are independent, and `wm.pmap` (4 workers) is already used elsewhere; that alone would bring this to about 35 min. fig3abc needs only a handful of fits, and could have been decided on a reduced number of splits.

2. **[affects a conclusion]** Cells 59 and 67 onward: everything downstream uses `TY = TYPES["a"]`. That reading's PY count (102) is outside tolerance, and it yields 16 IN concept cells against the paper's 14. Reading (b) matches fig5c and fig5kl, but was carried into only one GLM configuration (cell 91). Claims never run with the (b) types: fig6ab, fig6cd, ext5bd, fig6f, fig6gh, ext5gh, fig6i, fig6j, fig6kl, ext5ij, and the PY/IN burst groups. The cell type is an open detail that can change these outcomes, e.g. IN concept 3/14 = 21.4% in fig6e.

3. **[affects a conclusion]** `wm.group_bursts`, cells 67, 70 and 84: with the 2.8 s maintenance window, real spikes stop at the probe (2.5–2.8 s), so each trial has a silent tail. The surrogates spread spikes uniformly over the full 2.8 s and fill that tail. I tested this on synthetic homogeneous Poisson data (spikes on [0, 2.5] in a 2.8 s stride): real 54 bursts against a null of about 41. Without the gap: real 40 against about 44. So "maintenance exceeds the Poisson null" (fig4d; fig6ab maintenance) can arise from the windowing alone, and encoding (no gap) cannot show it. The criterion's own-duration reading was run only for `code/prominence/real` (cell 71), and there fig4d fails.

4. **[does not affect a conclusion]** `wm.epoch_burst_counts` with the Methods M-reading: M3 counts include the 0.2–0.5 s empty tail, so M3 bursts are deflated. This produces the spurious M3 decreases under the height rule (cells 75, 77, 86). The rate per second was printed only for All902. Outcomes were decided on M-code readings, where this does not arise.

5. **[affects a conclusion]** `wm.fit_acg`, cell 57: the scipy fit agrees with the shipped MATLAB values for only 48% of R2, 7% of τrise and 11% of τdecay (within 1%). The fitted yield is 317 against 294, and τrise is a clustering feature, so the cell types differ (feeds problem 2). This is not stated as a limitation.

6. **[does not affect a conclusion]** `ct_analysis`, cells 40 and 42: the Methods cluster rule is degenerate. No shuffled map had any BH-significant pair (`null95_extent` = 0), so every real cluster is kept. The one-sided and two-sided tests are also identical, because of the `acc > 0.2` filter.

7. **[does not affect a conclusion]** Chance level: the paper states 20%. The notebook's LOOCV label-shuffled nulls average 9–17% for the pseudo-population and about 18% within participant (cells 44, 48, 99, 101). All p values are taken against this lower empirical null, which is never compared with the paper's 20%. This matters only for borderline cases such as PY at 250 ms (33%), which is not significant after BH anyway.

8. **[does not affect a conclusion]** Cell 32 onward: the downstream concept set is a single draw (code reading, seed 0). Counts range 57–60 over seeds, and the Methods reading (49–54 cells) is not carried downstream.

9. **[does not affect a conclusion]** Cell 49: at 1000 ms, accuracy on random six-per-image trial draws ranges 56.7–86.7%. The fig2f tolerances (±10%) are narrower than this trial-selection spread, so in-tolerance or out-of-tolerance results there carry little weight.

10. **[does not affect a conclusion]** Cell 7: one subject-9 trial has 0 s maintenance and 0 s fixation. It is kept in every analysis (fixation statistics, maintenance windows) and never excluded or checked.

11. **[does not affect a conclusion]** Different claims pass under different readings. fig4c passes only with the height rule, under which low ACG has fewer bursts than high ACG (contradicting fig4-acg-group-differences). The prominence-based claims pass with the opposite rule. Each criterion allows "one reading", but no single burst reading supports Fig. 4 as a whole.

12. **[does not affect a conclusion]** `cv2_cell` and `decay_cell`, cells 95 and 97: both build ISIs and ACGs from trial-concatenated spikes, which adds artificial cross-trial intervals. The ext5gh τdecay fits are made on ACGs of 25–34 spikes per cell, so that reading (taken from the claims file) is close to uninformative.

### C. Not checked, and what would have allowed it

- I could not check the code repository, so I cannot confirm three implementation choices said to follow it:
  - z-scoring window counts with fixation rate statistics in `zcounts` and `psth_z`;
  - drawing surrogate spike times on [0, TRIAL_WIN];
  - the 3 s window used for maintenance burst counts.
- **Would decide whether problem 3 is a code artefact or this notebook's:** the code's own surrogate output, or a run on Poisson-shuffled real data (a real-vs-null comparison on data with no true bursts).
- **Would settle problem 2:** fig6ab–ext5ij rerun with `TYPES["b"]`, plus the burst groups built from the (b) features.
- **fig4d and fig6ab maintenance:** the own-maintenance-duration burst variant under every reading, and M3 rates per second for every group.
- **Blocked dPCA claims:** at least the fig3abc fits, and H and Dunn tests on a parallel or reduced set of splits.
- **Problem 7:** decoding p values against the 20% binomial chance alongside the empirical-null p.
- **Problem 6:** the observed largest cluster extent, and the per-map significant-pair counts of the shuffled cross-temporal maps.
