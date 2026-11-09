**Verifier report, round 1: Ramachandran et al. 2025 on DANDI:000945 (0.250213.2212)**

The claims file has 22 claims. The notebook treats 3 as blocked and tests 19.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig3-cell-type-sorting | blocked (data_missing) | The files hold no waveforms, so the k-means features and the cluster separation the criterion requires cannot be computed (cell 16). Using the deposited labels, 2 of 59 recordings fall within the count tolerances (BH508_4500_200_2 at 28/30/58 and BH527_30_200 at 28/34/62). This is weak evidence, since recording totals run from 31 to 127 units. |
| fig4-rsu-time-locked-both-states | blocked (data_missing) | There is no sham (checked on the archive). The awake half already fails the criterion's "above 100%" condition: the awake 1500 Hz RSU mean is 98.1–98.7% under every reading (cell 18). So the best this claim could reach is partially_reproduced. |
| fig4hi-fsu-delayed-latency | not_reproduced | No reading gives p < 0.001; p runs from 0.018 to 0.85. The anesthetized mean is 0.38–0.52 s against an expected 0.24 ± 0.08 under every reading (cell 20). |
| fig4h-awake-latency-wider | blocked (methods_underspecified) | Awake SD > anesthetized SD under D1 but not under D2 (cell 22), and the claims header blocks a claim when its readings disagree. Every SD is about 0.37–0.41 s, with no contrast like the paper's 0.14 vs 0.08. |
| fig5a-rsu-time-locked-prf-awake | not_reproduced | Part (1) holds. Parts (3) and (4) fail under every reading, and (2) fails in 3 of 4 (cell 24). The 3000 Hz mean is the highest and differs from 1500 and 4500 Hz. Even if the sham parts held, the partial threshold could not be met. |
| fig5c-rsu-time-locked-prf-anesth | not_reproduced | Parts (1) and (7) hold; (2), (3) and (4) fail under W1 and W2 (cell 26). Only two labelled rats are available. |
| rsu-time-locked-anesthesia-factor | not_reproduced | p for the anesthesia effect is 0.011–0.018, but the effect goes the wrong way: anesthetized 102.6–102.9% vs awake 100.1–100.4% (cell 29). |
| fig5bd-fsu-time-locked-no-prf | not_reproduced | The Kruskal-Wallis is significant in both states (awake p ≈ 1.8e-12; anesthetized p = 5.5e-4 and 7.8e-4), with 2 to 6 significant post hoc pairs (cell 31). |
| fig5e-rsu-delayed-prf-awake | not_reproduced | Part (1) holds. Part (2) fails under both its readings, R1 and R2: 30 Hz has about the same mean as 1500 Hz and is above 3000 Hz (cell 33). |
| fig5f-fsu-delayed-prf-awake | not_reproduced | Part (2) fails (30 Hz has the highest mean, not 4500 Hz) and (4) fails. Only (1) and (3) hold, so the partial threshold cannot be reached even with the sham part (cell 35). |
| fig5gh-delayed-prf-anesth | not_reproduced | The Kruskal-Wallis is not significant for RSU or FSU under either window (p = 0.12–0.18, cell 37). |
| delayed-anesthesia-factor | reproduced (on the Rep2 assumption) | Under Rep2, RSU p ≈ 5e-9 and FSU p = 0.0013–0.0015, with anesthetized below awake for both types. That holds under A1/A2 and W1/W2 (cell 39). Under Rep1 the FSU p is about 0.04, which would make it partial. Rep2 is better supported than the notebook argues (problem 1). |
| fig6ad-time-adjacent-batch | blocked (data_missing) | Checked on the archive: 75 assets, two kinds of session description, no sham and no two-PRF series. All 10 subject folders are first-batch rats or duplicate folders. |
| fig6ef-rsu-ispta-rise-then-fall | blocked (methods_underspecified) | The delayed window fails under every reading: 30 Hz (106.6) is above 300 Hz (101.2). The time-locked window holds under W2 but fails under W1 Rep2 by 0.1% (98.2 vs 98.1), so the window readings disagree (cell 42). At best it is partial. |
| fig6fh-fsu-ispta | not_reproduced | Spearman rho is −0.4 (Rep1) and −0.3 (Rep2) against a required 1. The time-locked part inherits fig5bd's failure (cell 44). |
| fig5a-1500-highest-time-locked-mean | not_reproduced | 3000 Hz has the highest mean under every reading, and 1500 vs 3000 Hz has corrected p ≤ 0.004 (cell 46). |
| fig7a-rsu-time-locked-dc | not_reproduced | Parts (2) and (4) fail under every reading: the 6% mean (176–181%) is above 60% (147%) and above 30% (cell 50). Part (2) does not involve the substituted 30% condition. |
| fig7a-60-highest-time-locked-mean | not_reproduced | 6% has the highest mean under every reading (cell 52). |
| fig7b-fsu-time-locked-dc | not_reproduced | Kruskal-Wallis p ≤ 3.5e-12 and all 3 pairs are significant, including 6% vs 60%, which does not use the 30% substitute (cell 54). |
| fig7c-rsu-delayed-dc | blocked (data_missing) | The paper's own 30% DC recordings are not in the dandiset. The substitute 30% condition decides the outcome: C1 is not reproduced (KW p = 0.21) and C2 is partial. Part (4), 6% vs 60%, fails under every reading (corrected p = 0.071) (cell 56). |
| fig7d-fsu-delayed-dc | partially_reproduced | Parts (1) and (2) hold under every reading (6% vs 60% corrected p = 0.015). Part (3), the sham comparison, cannot be tested. The effect is tiny: 98.2% vs 99.6%, both below baseline (cell 58). |
| sham-no-auditory-response | blocked (methods_underspecified; also data_missing) | The criterion blocks this claim, and the archive holds no sham recording. |

The paper states no chance level for any selection.

### B. Problems

1. **[affects a conclusion] Repeat recordings are justified on weaker grounds than are available, and their dates are never checked (cells 7 and 13).** The dandiset description says repeats were "taken a few months after the original ones … at 12 months", and the paper describes no such repeats. That supports Rep2 (leaving repeats out) more firmly than the Methods 2.3 sentence the notebook cites. But the notebook never prints which date belongs to which identifier: `inv.start` is computed but never displayed. So it is unverified that the `_2` files are the later recordings. delayed-anesthesia-factor is reproduced or partial depending on this.
2. **[affects a conclusion] The 30% DC condition is a substitute (cells 47–48).** The paper's DC series, recorded at 10 months, had its own 30% recordings, and none are in the dandiset. C1 and C2 both borrow PRF-series recordings from other sessions; C2 also adds rats with no 6% or 60% data. The notebook adopts C1 by its own choice, where the honest outcome for 30%-dependent parts is data_missing. This decides fig7c.
3. **[affects a conclusion] The notebook overrides the claims file's rule for disagreeing readings (cell 13).** It says that where readings disagree, the best-supported one is adopted (W2, Rep2, C1). The claims header says such a claim is blocked as methods_underspecified. This matters for fig6ef (W1 vs W2) and fig4h (D1 vs D2).
4. **[affects a conclusion] Sham parts are dropped beyond what the claims file provides (cell 13).** The header only covers a missing *anesthetized* sham. Dropping the awake-sham parts goes further, and a criterion with an untested part should not reach "reproduced". I scored fig7d as partial for this reason, not reproduced.
5. **[does not affect a conclusion] fig4-rsu is blocked without noting that its awake half is already decided (cell 18).** The awake RSU mean is below 100% under every reading, so the claim cannot be reproduced whatever a sham would show. The notebook does not say this.
6. **[does not affect a conclusion] The fig3 count match is weak (cell 16).** One of the two matching recordings, BH508_4500_200_2, is a 12-month repeat that Rep2 would drop. No base rate is given for a match among 59 recordings. That the labels are the paper's k-means output (K0) is assumed and supported only by baseline firing rates (cell 9).
7. **[does not affect a conclusion] Anesthetized cell-type tests rest on two rats (cells 26, 29, 37).** The 30 Hz anesthetized group is one rat's 32 units, so PRF effects are confounded with rat. In the two-rat ANOVA variant the anesthesia effect disappears (p = 0.43). The notebook shows this but does not discuss it.
8. **[does not affect a conclusion] One recording filed under two rats is assigned to BH498 arbitrarily (cell 5).** BH498_30_200 and BH508_30_200_2 share 18,860 spike times. Which rat it belongs to is not established.
9. **[does not affect a conclusion] Latency detection flags most FSU and looks noise-driven (cell 20).** Under S1, 86% of FSU count as responders, and latencies spread over 0.07–1.39 s in both states. That follows from the claims file's readings, not a coding error. The helper `tfus.latency` behaves correctly on synthetic PSTHs I built: the D1/D2 boundary, L1/L2 timing and the three-bin rule all check out. `group_test` and `pair` correctly orient pairs and apply Bonferroni over all pairs, and `_counts` uses half-open windows.
10. **[does not affect a conclusion] Part (3) of fig5f is tested without direction (cell 35).** This matches the criterion's word "differs", but the 30 Hz FSU mean is the *highest*, opposite to the paper's pattern.
11. **[does not affect a conclusion] Most recordings show no time-locked response at all (cell 11).** Only 10 of 64 recordings show a population rise in the 67 ms window, and the awake 1500 Hz, 200 µs recordings show none. That limits every time-locked claim. It is consistent with the outcomes above but is never raised as a caveat.

### C. What I could not check

- **Recording dates per identifier.** I could not confirm that the `_2` files are the 12-month repeats (problem 1). Paths suggest BH498's awake files (5–6 March 2024) fall within a week of its anesthetized ones (10 March 2024), but I could not map paths to identifiers, so I could not judge whether a one-rat proxy for fig6ad exists. Printing `inv[["path", "identifier", "start"]]` would have settled both.
- **Recording dates of the 6%/60% DC files against the borrowed 30% files.** These were needed to judge C1; the same printout would show them.
- **Whether the 500 trials per file are trials 6–505 (reading T1).** The archive's description only says each recording has 500 trials.
- **Whether `celltype_label` is the paper's k-means output, and the cluster separation.** Both need waveforms, which the archive does not hold.
- **fig3 counts under Rep2, and the number of recordings expected to match by chance.** A row for each in cell 16 would have shown both.
