**A. Outcomes by claim** (44 claims in the claims file: 14 `data: dataset`, 30 `data: elsewhere`)

| Claim | Outcome | Reason |
|---|---|---|
| fig1b-th-loss | partially_reproduced | Cell 43, per-cohort normalisation: DLS and DMS do not differ (Dunn p = 0.38) and VS is less depleted than both (p < 0.001). But the losses are 64.3% and 56.8%, outside 50 ± 5. With all-controls normalisation DMS is 52.4% but DLS is 60.5% and DMS vs VS gives p = 0.052. |
| figs1d-snc-cells | reproduced | Cell 45: control median 316, parkinsonian 187 cells/mm², Mann-Whitney p = 0.00026 (n = 9 and 20). It stays below 0.002 whichever group the 3 unlinked mice are put in. |
| fig1c-rotarod | reproduced | Cell 47, Dunn: control vs parkinsonian baseline p = 1e-15, baseline vs PPX p = 1.8e-5 (longer latency on PPX), baseline vs saline p = 0.83. The Wilcoxon variant gives saline p = 0.074. |
| figs1ef-ppx-locomotion | blocked (data_missing) | The Zenodo file list (cell 6) has no PPX open-field file. The DANDI files have no position or velocity data (processing holds only ecephys/LFP). I agree. |
| figs1-instrumental-learning | partially_reproduced | Cell 49, blocked phase: success is lower in parkinsonian mice in sessions 1, 3 and 4, and latency is slower in sessions 3 to 6, as required. Random phase: session 1 success differs, p_bonf = 0.003, where the criterion requires no difference. |
| fig1fg-baseline-similar | reproduced | Cell 13, reading (a): group F(1,178) = 0.0071, p = 0.93 (paper F = 0.0031, p = 0.955), and every per-delay p = 1. Reading (b) also gives p ≥ 0.05. |
| fig1fg-delay-discounting | reproduced | Cell 15, reading (a): delay F(3,178) = 38.15 (paper 38.53), p = 4e-19. Control goes from 91.7% to 32.1% and parkinsonian from 85.7% to 32.9%. Reading (b) gives p = 0.11, but it is not a usable sample (problem 5). |
| fig1f-ctrl-ppx-no-change | reproduced | Cell 17: the PPX effect p ≥ 0.10 and every per-delay p ≥ 0.21 under all four readings. |
| fig1g-park-ppx-fewer-large | reproduced | Cell 18, baseline all with PPX four: F(1,116) = 91.5 (paper 95.5). Pooled Bonferroni p is < 0.0001 at 0, 3 and 6 s and 0.022 at 9 s. The "first" reading is partial (6 s and 9 s not significant). |
| fig1ijk-ppx-a-k-auc | partially_reproduced | Cell 21, ON four: A is lower (Dunn p = 2e-6) and AUC is lower (p = 3e-8). K is higher but not significant (Dunn p = 0.19; ON first gives p = 1). The Friedman omnibus for K (p = 0.032) matches the paper's 0.03, so the paper may have reported the omnibus p. |
| figs2abc-sex-similar | blocked (data_missing) | Accepted, but not verified: the notebook does not show that KeyResourceTable_ICD.xlsx or the README were searched for sex (part C). |
| figs2de-omissions-low | reproduced | Cell 25: in parkinsonian mice only the 6 s centre-omission comparison is significant (p < 0.0001). No side-omission or control comparison is. Mean rates are 1.6% to 9.4%. |
| figs2gh-ppx-latency | partially_reproduced | Cell 27: reward size modulates latency at baseline (p = 0.023) and not on PPX (p = 0.71 for four sessions, 0.19 for the first). The PPX effect on small-reward latency fails: p = 0.093 (four) and 0.15 (first). |
| figs2ijk-ppx-washout | partially_reproduced | Cell 23: A returns to baseline under both tests. No single test gives both K and AUC persisting. Dunn's gives K p = 0.020 but AUC p = 0.078; the repeated-measures ANOVA gives AUC p = 0.039 but K p = 0.063. |
| fig2bc-a77636-locomotion | reproduced | Cell 57 (only the −20 to 0 min baseline exists in the files): controls p = 0.065; parkinsonian mice faster, p = 0.016. Using only the 10 parkinsonian mice on the README list gives p = 0.020 (my recomputation from the printed table). |
| fig2d-ctrl-a77636-no-change | reproduced | Cell 29: the A77636 effect p ≥ 0.31 and every per-delay p ≥ 0.71 under all readings. |
| fig2e-park-a77636-fewer-large | reproduced | Cell 30, baseline all with ON four: F(1,60) = 45.06 (paper 45.68). Per delay: 0 s p = 0.56, 3 s p = 0.0049, 6 s p = 0.0003, 9 s p = 0.0003, close to the paper's printed values. |
| fig2fgh-a77636-k-auc | reproduced | Cell 31, ON four: A Friedman p = 0.31, K Dunn p = 0.0053 (higher), AUC Dunn p = 0.0008 (lower). All three match the paper. |
| figs3-a77636-washout-latency | partially_reproduced | Cell 32: K and AUC do not differ between OFF and ON and stay on the ON side of baseline. No omission comparison is significant. Baseline reward-size effect p = 0.0003. But the reward-size effect on A77636 is p = 0.032, where the criterion requires p ≥ 0.05 (paper p = 0.07). |
| fig3a-a-correlates-dms | not_reproduced | Cell 51: A vs DMS TH gives r = 0.32, p = 0.13 with n = 24 (paper r = 0.51 with n = 28; tolerance 0.46 to 0.56). Only the ON-four reading was run (problem 1). |
| fig3b-k-no-correlation | reproduced | Cell 52: all six p ≥ 0.055. |
| figs4-a77636-no-correlation | reproduced | Cell 53: all six p ≥ 0.235; the smallest is K vs VS, r = −0.31, which matches the paper. |
| figs6-dreadd-validation | reproduced | Cell 55: oIPSC Wilcoxon p = 0.031 (lower after CNO); firing at 300 pA p = 0.016 (higher); input-output F(1,32) = 17.64, p = 0.0002, the same F as the paper. |
| fig5cf-cno-locomotion | partially_reproduced | Cell 58: hM3Dq mice are faster (p = 0.001) and hM4Di mice are faster (p = 0.004). mCherry mice did not speed up, but they were significantly slower (p = 0.016, 11 of 12 slower), so the criterion's p ≥ 0.05 fails. This rests on an unchecked injection time (problem 2). |
| fig5g-mcherry-no-change | reproduced | Cell 34: CNO effect p = 0.34 and every per-delay p = 1, under both baseline readings (n = 14). |
| fig5hi-dreadd-fewer-large | partially_reproduced | Cell 35, baseline all: hM3Dq fully holds (main effect p = 9e-8; 3, 6 and 9 s all p < 0.05). hM4Di main effect p = 0.0009 but only 3 s is significant (6 s p = 0.38, 9 s p = 0.62). The criterion's partial clause applies. |
| fig5jl-dreadd-params | not_reproduced | Cell 36: hM4Di K is not higher (Wilcoxon p = 0.20; sign test 0.77). Every other component holds. The criterion's partial clause needs the K and AUC results to hold, so by its wording this is not reproduced, though narrowly. |
| fig6b-ctrl-ppx-stable | reproduced | Cell 39: baseline vs first p = 0.46, baseline vs fourth p = 0.75, first vs fourth p = 1. |
| fig6c-park-ppx-progressive | reproduced | Cell 40: first vs fourth p = 0.024 (fewer delayed/large choices in the fourth); baseline vs first and vs fourth p < 0.001. This uses comparisons pooled over delays; no single delay is significant. |
| fig6de-a77636-persistent | reproduced | Cell 41: in parkinsonian mice baseline vs first p = 0.0004, vs fourth p < 0.0001, first vs fourth p = 1. In controls every p ≥ 0.31. |
| fig4bc, fig4de-ctrl-immediate-suppression, fig4de-ctrl-no-change-4-5h, fig4f, fig4g, fig4-insets, fig4hk, figs5abcd, figs5ef, fig6f, fig6g, figs8, fig6h, fig6i (14 claims) | blocked (data_missing) | I checked the archive API. 54 of 56 assets hold only SpikeEventSeries (unsorted threshold crossings) plus raw data and LFP. Two have Units, holding only spike_times and unit_name: E0 day 4 (parkinsonian, 4th session) and P4 day 1 (control). No asset has stimulus or optogenetics data, including the K4 "optoSession" file, and none has an injection mark. The draft version has the same 56 assets. Nothing can be tested: two sessions from different groups, with no MSN class, no optical label and no injection time, cannot form any claim's unit pool. |

**B. Problems**

1. [affects a conclusion] `corr_block` (cells 51–53) correlates TH only with A and K from the ON-four reading. The claims file lists both ON readings for the fig1ijk dependency, but "first" was not run, so fig3a's not_reproduced rests on one reading. The join keeps 24 of the paper's 28 mice, and the dropped IDs are never listed, so an ID mismatch cannot be ruled out.
2. [affects a conclusion] `of_table` (cell 58) assumes injection at 20 min for every CNO file. 12 files have no tracking gap near 20 min (H and J cohorts, including 5 of 12 mCherry mice), and 2 more have gaps at 17.7 and 18.5 min. The significant mCherry decrease that fails fig5cf depends on these windows. Separately, H0 and H0.4 have identical rows (same date, length and values), so one recording is probably counted twice; without it hM4Di still gives p = 0.008.
3. [affects a conclusion] `friedman_block` (cell 21) runs only the pairs (ON four, OFF all) and (ON first, OFF first). Friedman ranks, and so the Dunn baseline-vs-ON p, depend on which OFF sessions enter. The other two pairs were not run, and fig1ijk's K result and figs2ijk could change.
4. [affects a conclusion] `icd.rm_oneway` makes its Bonferroni comparisons with separate paired t tests. The pooled-error comparison Prism offers was not run as a variant. figs2ijk reading (b) has K p = 0.063, close enough that the choice could change the result.
5. [does not affect a conclusion] `stable_window`, reading (b) in cell 13: 35 of 47 mice have no stable run. The rest are 3 controls and 9 parkinsonian mice whose curves barely fall (control 95% to 82%). The reading selects mice that discount little, not the paper's cohort.
6. [does not affect a conclusion] Cell 57 counts all 16 non-control open-field mice as parkinsonian, including 6 that are in neither README list. Restricting to the 10 listed mice still gives p = 0.020.
7. [does not affect a conclusion] Cell 47 uses 40 controls where the paper has 31, and applies Dunn's correction over 3 chosen pairs. Neither is commented on, and the conclusions survive correction over all 10 pairs.
8. [does not affect a conclusion] Cell 43 has 45 parkinsonian mice where the paper has 44. Cohorts 3 and 4 have a single control each for the per-cohort normalisation.
9. [does not affect a conclusion] Cell 9 counts the 2020 control cohort's 0/6/12/18 s blocks as 0/3/6/9 s. This is stated, and the close F match in fig1fg suggests the paper did the same.
10. [does not affect a conclusion, as far as the outputs show] `icd.condition_of` labels files tagged ppx, a77636 or cno as "on" whatever archive they sit in. The DREADD archive shares 233 byte-identical files with PPX and 75 with A77636. It has no OFF sessions and about 4 ON sessions per mouse, which suggests only baseline files are shared, but this is never printed.
11. On the claims file: I found no clear misreading. One paper inconsistency: the oIPSC p < 0.01 cannot come from a two-sided exact signed-rank test on 6 cells, whose minimum p is 0.031.

**C. What I could not check, and the output that would have let me**

- Log parsing (event names; "cen tri" taken as the side-cue onset) against the linked code: an annotated event sequence for one session, with its derived counts and latencies.
- The 24-mouse join for the correlations: the parkinsonian PPX and A77636 IDs that have no TH match, and the reverse.
- Whether mice or drug-tagged files are shared across the PPX, A77636 and DREADD archives: mouse-ID overlaps, and the condition tag of each shared file.
- The figs2abc block: the sheets and columns of KeyResourceTable_ICD.xlsx and the README lines searched for sex.
- The injection time in CNO files with no gap: velocity around 15–25 min for those files.
- The instrumental-learning columns used (13/14 and 5/8): their header cells.
- The stable reading: per mouse, the number of baseline sessions before the first drug session, and its per-block CVs.
- The DANDI Units tables: the `unit_name` values of the two files. I limited myself to API metadata and did not stream the files.
