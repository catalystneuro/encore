**Verifier report, round 1: Jarzebowski & Bendor (2026) on DANDI:000713 0.240702.1725**

The claims file has 31 claims: 14 model claims (data elsewhere) and 17 with_inputs claims, including ccf-layer-link. The notebook blocks none. The archive API confirms that version 0.240702.1725 exists and has 4293 assets, which matches cell 5. No claim in the paper states a chance level for a selection.

The notebook says it adopts O9(b) wherever the two session readings disagree (cell 38). I agree with that choice, because O9(b) is the only reading that gives the paper's cell counts.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| model-positive-error-short-latency | partially_reproduced | At 60 nS, p1 = 1.0, latency 3.7–3.8 ms, and doublets appear from 90 nS. The criterion's "no spike after the basket peak" fails in 2 of 5 seeds (1.2% of spikes after 8.5 ms), and the notebook checks it only at 60 nS. |
| model-negative-error-delayed-release | reproduced | Under reading (a), the median latency is 17.1–17.9 ms in all 5 seeds and every spiking run fires exactly once (single = 1.0). |
| fig2a-weak-sensory-silenced | not_reproduced | For L4 below 12 nS the expected count is 0.89–0.99 against a threshold of 0.1, in all seeds. I ran the module with noise switched off: L4 = 10 nS still gives a release spike at 18.7 ms, so the failure is deterministic in this model. |
| fig2b-breakthrough-doublet-threshold | reproduced | With prediction, the count is 1.0 at 150 nS and there is no doublet within 0–150 nS (threshold 260–345 nS when the range is extended). Without prediction the threshold is 110–120 nS under (a) and 90 nS under (b). Holds in all seeds. |
| fig2c-robust-to-input-delay | reproduced | The count at ±5 ms differs from the count at 0 ms by 0.13–0.31, below the 0.5 limit, in all seeds. |
| fig2d-latency-grows-as-sensation-weakens | partially_reproduced | Spearman rho is between −0.989 and −0.999. The no-jump test uses the author's own threshold of half the latency range. The largest single step is 2.8–6.3 ms of a 16 ms range, at the switch from release spikes to breakthrough spikes (around 35–40 nS). |
| fig3a-low-gain-suppresses-errors | reproduced | At the strong-L4 values, p2 is 0 at Low gain and 1.0 at High gain, and Low-gain omission runs are 100% silent, in all seeds. |
| fig3b-gain-lowers-burst-threshold | reproduced | Under reading (b), the burst threshold falls from 515–565 to 215–230 to 110–115 nS in all seeds. Omission spike probability is 0, then 0–0.075, then about 0.94. The strict rise from Low to Mid fails in 2 seeds because both are 0, but pooled over the 5 seeds it is 0/400 against 12/400. |
| fig3c-gain-keeps-release-delay | not_reproduced | Low gain gives no release spike in 400 runs, so its latency cannot be measured. The Mid latency (22–35 ms, from 1–4 spiking runs per seed) exceeds the High latency (17.4–18.2 ms) by more than 5 ms in 4 of 5 seeds. |
| fig4a-basket-reduction-lowers-burst-threshold | reproduced | Thresholds rise with basket scaling (55, 65, 75–90, 95–105 nS) in all seeds. |
| fig4b-chc-reduction-shortens-latency | reproduced | Latency rho is above 0 at every L4 tested (15–17 values), and the breakthrough-threshold rho is 0.96–0.99. This rests on the stated, reasonable threshold definition; the plain reading gives 5 nS at every ChC level. |
| fig4cd-l5it-shortens-release-and-doublets | reproduced | Rho is about −1, and the first doublet appears at 22–24 nS. |
| fig4d-strong-prediction-lowers-burst-threshold | reproduced | Rho is between −0.88 and −0.94. See problem 8 for how much of this comes from L5 IT alone. |
| fig4ef-compensation-restores-latency | reproduced | At L5 IT 20 nS, ChC of 52.5–95 nS and E_ChC of −65 to −75 mV each bring latency back within 1 ms, in all seeds. At 24 nS, raising ChC does not restore it. |
| ccf-layer-link | reproduced | 7996 of 7997 units with coordinates fall in a VISp layer voxel. 351 units in 7 sessions have no coordinates and are counted. |
| cell-counts | reproduced | Under O9(b), all 16 combinations of O1–O3 put the four counts within tolerance (for example 247/76 L2/3 and 997/100 L5). Under O9(a), none do. |
| fig5c-fsb-highest-on-first-repetition | partially_reproduced | Under O9(b), every reading gives both intercepts negative with p < 1e-7, but none is within tolerance (the closest misses by 0.0024). Under O9(a), one reading is within tolerance. |
| fig5c-l5-fsb-keeps-declining | reproduced | Under O9(b), O4 a, linear: slope −0.00099 (p = 0.008) with O8 a, and −0.00095 (p = 0.012) with O8 b. Both are within −0.0009 ± 0.0002. |
| fig5c-l23-fsb-stable | reproduced | The L2/3 slope has p ≥ 0.39 under every reading. |
| fig5d-firing-rate-dips-then-stable | reproduced | The criterion is met under all four combinations of O9 and O8. The median modulation index at repetition 2 is −0.39 (L2/3) and −0.21 (L5), and every later repetition is above it. |
| figs1-post-omission-bursting | reproduced | The L5 intercept is positive with p < 0.05 in 6 of 6 readings, under both O9 readings. |
| figs1-novel-image-bursting | reproduced | The L5 intercept is positive with p < 0.005 in 6 of 6 readings, under both O9 readings. |
| figs1-novel-firing-rate-unchanged | not_reproduced | Under O9(b), L5 gives −0.043, p = 0.0095. Under O9(a), p = 0.059 from a fit that did not converge. |
| fig6b-omission-firing-below-spontaneous | partially_reproduced | Using spontaneous block 3 or both blocks with O5 a, both layers are negative with p < 1e-8 but outside tolerance (L2/3 −0.22 to −0.25, L5 −0.23 to −0.25). With block 1, the reading the notebook adopts, L2/3 is not significant (p = 0.75 or 0.87). |
| fig6c-omission-bursting-below-spontaneous | partially_reproduced | With block 3 or both blocks, O5 a, the difference measure gives −0.0053 to −0.0071 (p of 0.02–0.03), outside the −0.004 to −0.001 tolerance. With block 1 the sign reverses (+0.007 to +0.008, p < 0.03). |
| figs2-l23-l5-activity-correlated | reproduced | Positive with p < 0.001 under both test readings, both conditions, both populations, and both O9 readings. |
| figs2-l5-bursting-not-predicted-by-rate | not_reproduced | 13 of 16 cases (O9 b) have p < 0.05. The L5 rate residual predicts L5 FSB with t from 14 to 41 in every case. |
| fig7a-running-raises-first-repetition-bursting | reproduced | Under O9(b), O4 a, difference measure, both windows: L2/3 0.053–0.059 and L5 0.047–0.058, all p < 0.01 and all within tolerance. |
| fig7b-running-raises-first-repetition-rate | partially_reproduced | Both layers are positive with p < 1e-5. L2/3 (0.18–0.21) is within tolerance; L5 (0.17–0.20) is above the 0.05–0.16 range. |
| fig7c-running-leaves-omission-bursting | reproduced | Under O9(b), 0 of 8 cases have p < 0.05. No cell selection matches the paper's 47/35 and 658/94 counts; per the criterion, the counts do not decide this claim. |
| fig7d-running-lowers-omission-rate | not_reproduced | No reading has both layers negative and significant. Selection (a) gives positive values (+0.14 to +0.27); selection (b) gives L2/3 negative but L5 not significant (p of 0.12–0.88). |

### B. Problems

1. **[affects a conclusion]** Cells 43–73 compute every downstream claim only on the O1 aa / O2 a / O3 a cells. Under O9(b), all 16 combinations of O1–O3 match the paper's counts equally well (cell 42), and the O1 "ab" and "bb" readings add about 20 L2/3 and 50 L5 cells. fig5c-fsb-highest misses tolerance by only 0.0024, so it could change outcome under another combination, and fig6b and fig7b might too. These readings were not run.
2. **[affects a conclusion]** Cells 58–61 adopt block 1 (10 s, 40 windows, median 0 stationary windows) as the spontaneous period "immediately following the task". But cell 5 prints that block 1 starts between 17.95 and 3276.62 s after the last active presentation, and this is never investigated. The paper's Results say "spontaneous activity outside the stimulus blocks", which allows block 3. The block choice flips the sign in fig6c and the L2/3 result in fig6b.
3. **[affects a conclusion]** The figs1-novel-firing-rate-unchanged outcome depends on O9. The O9(a) L5 fit did not converge (cell 57, p = 0.059). Other non-converged fits are reported without a refit or a second optimizer: cell 45 (all, O8 a, O4 a, sqrt, k−2, L5), cells 53, 59, 61, 63, 65 and 71.
4. **[affects a conclusion]** In fig2d (cell 21), the jump threshold of half the latency range is the author's own and is lenient. A threshold of a quarter of the range (about 4 ms) would fail 3 of 5 seeds (steps of 5.25, 6.28 and 6.06 ms).
5. **[does not affect a conclusion]** fig7a and fig7b (cells 67–69) drop cells that lack Repetition-1 presentations in one running state (67 L2/3 and 232 L5 cells under O9 b). The paper's degrees of freedom, t(265) and t(1074), imply that all 266 and 1075 cells were kept. Under D7, 80% of active presentations are classed as running (584,067 running against 112,277 stationary), and this was never compared with the paper's n.
6. **[does not affect a conclusion]** In fig7d selection (a), 272 of 1407 L5 cells have no omission spikes in one state, so their modulation index is ±1. This explains why the sign differs between selections; the claim fails under both.
7. **[does not affect a conclusion]** In `m_positive` (cell 11), late spikes are checked only at 60 nS. `late_all` is computed and never used.
8. **[does not affect a conclusion]** fig4d (cell 35) passes mainly because L5 IT at 24 nS or more produces doublets with no L4 input (threshold 0). From 12 to 20 nS the threshold is 310–360 nS and is non-monotone at 16 nS in 2 seeds. It is lower at 20 nS than at 12 nS in all 5 seeds.
9. **[does not affect a conclusion]** In fig3b and fig3c (cells 25 and 27), the per-seed strict tests rest on very few spiking runs: Mid-gain omission spiking is 0–6 of 80 runs per seed.
10. **[does not affect a conclusion]** In the clock check (cell 7), 10 sessions have AUC below 0.8 at 30–100 ms, and one (20201203T231053) is at 0.55. All are kept, with no sensitivity check.
11. **[does not affect a conclusion]** The `opto_tagged` function never reports how many units it removes. The count match under O9(b) comes from which sessions are kept, not from the filter, and O3 changes counts by at most 1 cell.
12. **[does not affect a conclusion]** Possible claims-file misreadings, reported and not corrected:
    - O5 assumes a single spontaneous block after the task, but the dataset has two (10 s and 289 s).
    - fig7a and fig7b do not address that the paper's n equals the full cell-counts n.
    - fig2a reads "weaker" as L4 conductance below L5 IT conductance, although the two have different time constants. This does not change the outcome: the minimum count over 0–150 nS is 0.15.

I tested the helpers on synthetic inputs and they behave correctly: `_counts` (burst spikes are counted only within the same window), `fsb` (modes a and b), `mod_index`, `run_state`, and `alpha` (peaks at tau). The model's units and parameters match the Methods.

### C. What I could not check, and what output would have let me

- **Block-1 timing.** I could not tell why block 1 can start up to 3276 s after the task. A per-session table of block order and start times for block 0, block 1 and block 3 would settle this.
- **Optotagging.** A table of tagged units per session for each O3 reading and each genotype would show whether the filter does anything.
- **Downstream claims under other selections.** I could not see fig5c, fig6b or fig7b under the other 15 O1–O3 combinations. Their intercept tables would show whether any outcome changes.
- **Repetition ordinals.** I could not confirm that `flashes_since_change` does not count omitted flashes, which matters for O8. Printing one block with an omission in it, showing `flashes_since_change`, `omitted` and the assigned repetition, would confirm it.
- **Running state and cell counts.** I could not compare the notebook's running classification with the paper's n. Per-session running and stationary fractions, plus the number of cells with both states, would allow that.
- **Model fidelity.** The paper's code is not public, so I cannot tell whether the fig2a and fig3c failures come from differences in the implementation. The noise implementation is one example: the module draws independent noise for each compartment, which matches the Methods' separate n_soma and n_ais terms, but I could not confirm it against the code. Noise-free voltage traces of the soma and AIS at L4 = 10 nS with prediction would show which conductances fail to silence the release spike.
- **Figures S1 and S2.** Their legends are not in the text, so the tests used for the figs1 and figs2 claims could not be checked against the paper.
