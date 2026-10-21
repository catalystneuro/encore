**Verifier report: Girardeau et al. 2017 (nn.4637) on DANDI 000061 @ 0.250624.0426, round 1**

The claims file has 32 claims. My outcomes: 6 reproduced, 1 partially reproduced, 3 not reproduced, 22 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| unit-counts | not_reproduced | Cell 26: 40 sessions against 61, and 4,702 units against 7,390. Only rat 1 is within tolerance; the totals fail, so the criterion gives "not reproduced". The cause is an incomplete deposit (7 of 40 files have no units table), not a contradiction of the paper. |
| rats-learn-puff-location | blocked (too_large) | No position or puff location in the data, only gzip video frames: about 227 h of streaming plus tracking (cell 11). DANDI asset metadata lists no SpatialSeries/Position in any of the 40 assets. |
| each-rat-learns-puff-location | blocked (too_large) | Same data gap. |
| dz-speed-slower-post-run | blocked (too_large) | Same data gap. |
| puff-location-no-speed-bias | blocked (too_large) | Same; it also needs the puff location on the track. |
| habituation-over-days | reproduced | Cell 29: pooled Spearman ρ = 0.38, 0.33, 0.40 with p = 0.015, 0.046, 0.011 for the three lap counts. 4 of 4 rats have ρ > 0 under every lap count. Laps use O1 reading (c) only, which the criterion allows, recorded as a deviation. |
| bla-pyr-sleep-firing-increase | reproduced | Cell 32: 152 identified excitatory BLA cells (one rat, 5 sessions). REM median 0.39 (p = 7e-15) and NREM median 0.18 (p = 7e-12); the REM median is above the NREM median. |
| bla-int-sleep-firing | not_reproduced | Cell 34, n = 36: the REM/wake ratio is significant (median +0.029, p = 0.020), so the absence fails. The NREM/wake ratio is not significant (median −0.035, p = 0.26). Neither part holds. |
| hpc-bla-reactivation-post-sleep | blocked (metadata_insufficient) | No putative cell types. The identified excitatory hippocampal units reach at most 4 per file, below the minimum of 6 (cell 5). Confirmed. |
| reactivation-all-cell-pairs | reproduced | Cell 37: EV > REV in 13 of 15 sessions, two-sided Wilcoxon p = 0.00031. |
| reactivation-decay | blocked (metadata_insufficient) | Pyramidal pairs. The all-cell periods (cell 38: means 2.49, 1.27, 0.52%) are descriptive only. |
| no-rem-reactivation | blocked (metadata_insufficient) | Pyramidal pairs. The all-cell variant has p = 0.43. |
| piriform-weaker-reactivation | blocked (metadata_insufficient) | Pyramidal pairs. Piriform spike trains are not even loaded (`KEEP_LABELS`). |
| cen-no-reactivation | reproduced | Cell 42: NREM p = 0.30 (9 sessions) and REM p = 0.25 (8 sessions); neither reaches p < 0.05. This is a claim of absence tested with about half the paper's n (19). |
| intra-structure-reactivation | blocked (metadata_insufficient) | Pyramidal tests are missing. However, the BLA all-pairs NREM test already fails (p = 0.14, cell 44), so the claim can at best be partially reproduced. |
| bla-ripple-up-subgroup | blocked (metadata_insufficient) | The denominators are putative cell types. Descriptive (identified) results: inhibitory 22.2% (paper 25.8 ± 2.58), excitatory 5.9% (paper 11.1). |
| bla-ripple-down-subgroup | blocked (metadata_insufficient) | Same. Identified inhibitory down 47% (paper 14.7%), excitatory down 15% (paper 8.3%); far from the paper, descriptive only. |
| ripple-modulated-cells-larger-reactivation | not_reproduced | Cell 48, all-cell test judged alone as the criterion directs: rank-sum p = 0.27 (reading a) and 0.30 (reading b), 12 sessions; modulated larger in 7 of 12. |
| run-correlated-pair-fractions | blocked (metadata_insufficient) | Needs hippocampus–BLA pyramidal pairs. |
| reactivation-involves-ripple-up-cells | blocked (metadata_insufficient) | Same. |
| pair-group-ev | blocked (metadata_insufficient) | Same. |
| contributing-up-cells-gain-increase | blocked (metadata_insufficient) | Same. |
| ev-independent-of-firing-rate | blocked (metadata_insufficient) | Same. |
| reactivation-peaks-at-ripples | partially_reproduced | Cell 51, all-cell test alone: post > pre in 11 of 15, one-tailed p = 0.0042. The criterion gives "partially" when the pyramidal test cannot be run. |
| airpuff-trajectory-ripple-reactivation | blocked (metadata_insufficient) | Pyramidal cells. |
| safe-trajectory-no-ripple-reactivation | blocked (metadata_insufficient) | Pyramidal cells. |
| aversive-direction-stronger | blocked (metadata_insufficient) | Pyramidal cells. |
| direction-all-cell-pairs | reproduced | Cell 52, 14 sessions: air puff p = 0.010 and safe p = 0.0043 (both < 0.05); air puff > safe p = 0.48 (≥ 0.05). |
| bla-rate-same-across-directions | blocked (other) | O7 reading (b) needs position. Every reading that can be run gives p < 0.05 on the all-cell test (0.022 and 0.0048, cell 54), which is the "not reproduced" direction. |
| ripple-rate-unchanged | reproduced | Cell 56: 23 sessions, two-sided p = 0.26 (paper n = 41). |
| contributing-pairs-run-sleep-coupling | blocked (metadata_insufficient) | Pyramidal pairs; it would also need pre-run and post-run correlations. |
| contributing-quartiles-run-sleep-coupling | blocked (metadata_insufficient) | Same. |

### B. Problems

1. **[affects a conclusion]** Cell 53, bla-rate-same-across-directions: the notebook says the criterion "needs both the pyramidal-cell test and the all-cell test". That misreads it: "not reproduced when **either** test has p < 0.05 under every reading". The all-cell test is significant under both session readings. Only O7 reading (b), which needs position, keeps this claim from being "not reproduced". The blocking reason should say so.
2. **[affects a conclusion]** Cells 42, 56 and 34 (absence claims judged on p ≥ 0.05) run on much smaller samples than the paper: central nuclei 9 and 8 sessions against 19; ripple rate 23 sessions against 41; interneurons 36 against 175, all from one rat. The "reproduced" outcomes for cen-no-reactivation and ripple-rate-unchanged are weak evidence of absence. The notebook gives no power or effect-size context.
3. **[affects a conclusion]** `lap_intervals` / `laps` (O1 reading c): each lap runs from the reward at one end to the reward at the other, so it includes the reward-consumption time on the starting platform. M8 laps (position inside a 150-cm window) exclude it. The air puff and safe templates (cell 51/52) therefore include awake platform activity. This is allowed as the O1(c) deviation but is not flagged in the analysis cells. Rat08-20130708's safe template is a single lap of 463 bins (23 s).
4. **[does not affect a conclusion]** Cell 46: the identified-interneuron fractions (22% up, 47% down) differ strongly from the paper's (25.8% and 14.7%). Nothing checks whether the "inhibitory" label equals the paper's monosynaptic interneurons, beyond firing rate. The bla-pyr and bla-int outcomes rest on that unverified mapping (cell 6 says so).
5. **[does not affect a conclusion]** Cell 11: the notebook reports raw voltage in 16 files (`acquisition/ElectricalSeries` only). DANDI asset metadata lists ElectricalSeries for 24 different files: all Rat10 and Rat11 files plus Rat08 0715–0722, and none of the 16 files the notebook names. It also omits ProcessingModule for files the notebook reads states from. One of the two is wrong; probably the metadata, but the loader only looks at a single path.
6. **[does not affect a conclusion]** Cell 26: Rat08–Rat11 are mapped to the paper's rats 1–4 by assumption. The unit totals do not depend on that mapping.
7. **[does not affect a conclusion]** `hpcbla`: M3's rule "spikes after the end of the last run epoch dropped" is not implemented. It cannot change the sleep bins.
8. Helpers checked on synthetic inputs, all correct:
   - `ev_rev` equals squared partial correlations (EV 16.19 = 16.19; REV 3.69 = 3.69).
   - `pair_correlations` equals `np.corrcoef`.
   - The Poisson tails for O2 readings (a) and (b) are right, and a synthetic upmodulated unit is detected while a flat one is not.
   - `peri_centres` gives the 12 window bins of ±0.22 s; `peri_ripple_mean` peaks at the 0 s bin.
   - `in_intervals`, `subtract` and `binned` behave correctly.
   - No training/test leakage is possible: no decoder decides a claim (the cell 17 decoder is leave-one-out and only a clock check).

### C. What I could not check

- **Whether any file holds position or a processed behaviour module.** The loader opens only `processing/behavior/states`. Printing the full HDF5 group tree of one file per rat would settle the four behaviour claims and O7 reading (b).
- **Whether the inhibitory label tracks the paper's interneurons beyond firing rate.** Printing which identified units have monosynaptic partners, or their spike widths, would show it.
- **Cell 51's per-rat line for Rat11 is truncated in the output.** The full output, and per-session lists of excluded units (`hpc_used`/`bla_used` against the totals), would let the R inputs be audited.
- **Whether a BLA-only pyramidal test could be formed.** The criteria ask for putative types, but listing the per-session counts of identified excitatory BLA units against the M4 minimum would show whether a BLA-only variant of the intra-structure pyramidal test could be run as a variant.
