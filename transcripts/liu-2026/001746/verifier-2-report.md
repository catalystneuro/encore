**Verifier report, round 2: attempt 001746-liu-2026-01 (Liu et al. 2026, DANDI:001746 v0.260825.0222)**

The claims file has 33 claims. The attempt record has 33 outcomes: 24 tested here or blocked here, and 9 blocked as `other`. Cell numbers below are notebook indices in this round's notebook.

## 1. Outcomes and assumptions

| Claim | Record | I agree? | Comment |
|---|---|---|---|
| patchseq-cell-table-link | reproduced | yes | 462/462 rows found, cell IDs 462/462, subjects 461/462. Half-width 96.7%, amplitude 97.5% and rate 98.9% within 10% (cells 13–14). The outcome rests on reading row 235 as the row for s172. That choice is stated and reasonable, but it is not flagged `assumed: true`. |
| morph-table-link | reproduced | yes | 166/166 rows found; clusters agree 163/165 (cell 80). |
| patchseq-sample | partially_reproduced | yes | 10 subjects, not 12 (cell 18). |
| patchseq-mapping | partially_reproduced | yes | 30 inhibitory against 34 ± 3.4 (cell 21). |
| fig2a-subclass-counts | partially_reproduced | yes | L5 IT FEZF2 is 125 against 143 ± 14.3 (cell 24). |
| ven-map-et-ct | reproduced | yes | 14 and 15 (cell 27). |
| fig6f-ven-subtype-mapping | partially_reproduced | yes | 12 VEN-L against 10 ± 1 (cell 30). |
| fig2d-l23it-small-tau | reproduced | yes | q39 = 0.034 and q_F20 = 0.023 (cell 37). Within one device the difference is not significant (p = 0.47 and 0.13, cell 34). This is reported and does not enter the criterion. |
| fig2f-l23it-narrow-ap | partially_reproduced | yes | Its median ranks 2nd (2.08 against 1.92 ms for IT RORB), while reading (a) is significant (cell 40). |
| supp11-rm-itrorb-l6pc | partially_reproduced | yes | IT RORB has q39 = 0.087; L6 PC has q39 = 0.006 (cell 43). |
| supp11-l5it-threshold-latency | reproduced | yes | Reading (a): q39 = 0.005 and 0.0008 (cell 46). |
| supp11-ven-broad-ap | partially_reproduced | yes, but fragile | VEN 3.03 ms against 2.98 ms for L5 IT FEZF2. A 0.05 ms margin that changed sign with the threshold fix (cell 49). |
| supp11-l5et-deep-sag | blocked (methods_underspecified) | yes | The readings disagree, also at −200 pA only (cell 52). |
| ven-firing-rate-variability | not_reproduced | yes | Cell 55. |
| l5et-vs-l5it-sag-rm-rate | partially_reproduced | yes, with a caveat | All three hold under sag ratio; two hold under sag value (cell 58). "The outcome that holds under both readings" is not a rule in the criterion. The criterion's "sag readings as in supp11-l5et-deep-sag" could also be read as inheriting that claim's "blocked when they disagree" rule. The outcome rests on this choice, which is not flagged `assumed: true`. |
| fig3e-phase-peak-index | partially_reproduced | **no**; I'd keep blocked (methods_underspecified) | See remaining point R1. The outcome also rests on the unflagged 5% prominence guard. At 0.02 the median-AP reading no longer gives VENs the lowest median (0.200 against 0.173 for L5 IT FEZF2), and on the first AP Dunn separates no group (L5 ET 0.0545). Under the criterion that would not be partially reproduced (cell 61). |
| fig3d-saddle-phase-plane | partially_reproduced | no | It takes fig3e's outcome. |
| fig4ac-ven-broader-smaller-ap | blocked (data_missing) | yes | Cell 67. |
| fig4i-peak-index-ais-distance-real | not_reproduced | **no**; blocked, inherited from fig3e | It uses the same automatic index (R1). The hand-read indices give a negative slope, p = 0.018 (cell 70). |
| ext9cd-ven-subtypes-ap | blocked (data_missing) | yes | Cell 73. |
| supp8-ven-subtypes-similar-features | blocked (data_missing) | yes | Cell 74. |
| supp9-venl-more-distinct-from-ct | reproduced | yes | 6 against 0 over 39 features, 1 against 0 over 20 (cell 77). |
| morph-more-distinct-than-ephys | reproduced | yes | 445 against 120 tests; fraction 0.376 against 0.286. Every random 40-feature set is above physiology too (cell 83). |
| fig7c-tau-rna-distance | not_reproduced | yes | r = 0.105, p = 0.40 (cell 86). |
| 9 claims with data elsewhere | blocked (other) | yes | |

**Assumptions.** No outcome in the record carries `assumed: true`. The two choices labelled "Assumption" are the 19 features taken from the xlsx and the genes ranked by dispersion. For both, the variants give the same outcome, so leaving them unflagged is correct. Three outcomes do rest on unflagged choices:
- the row-235 reading (link claim);
- the "holds under both readings" rule (l5et-vs-l5it);
- `PROMINENCE_FRAC = 0.05` and the shoulder rule (fig3e, fig3d and fig4i).

The deviations call the last one "standard choices made against noise", but it decides the outcome.

**Claims file.**
- fig3e's criterion turns the Methods' "lowest derivative value" into "where d2V/dt2 is lowest before the global maximum". Taken literally, d2V/dt2 falls towards 0 at the dV/dt maximum, so a monophasic AP scores about 0, the most saddle-like value.
- Its "Psd the largest maximum after it" does not require Psd > Pais. That allows negative indices, down to −0.897 (cell 64), which are read as most saddle-like.
- fig7c's rule ("more than five mapped Patch-seq neurons") contradicts its own cluster list, which includes clusters 1 and 4 with 4 and 5 cells (cell 86).

## 2. Sentences the outputs do not support

- **Attempt record, fig3e notes and response; cell 63.** "Leaving out the APs whose AIS phase is not resolved (at most 3% of a group's APs)" and "such APs are at most 3% of a group's". The 3% is the mean over all APs of the sweep. For the first-AP reading, the unresolved case covers 5 of 30 L2/3 IT HPCAL1 cells, 3 of 18 L5 ET and 3 of 29 VEN (cell 61; `phase_idx_first_x` keeps 25, 15 and 26 cells).
- **Attempt record, fig3e deviations.** "leaving such APs out does not change the outcome". The outcome is unchanged, but the first-AP Dunn result changes: VENs are separated from 3 groups instead of 1 (cell 61).
- **Cell 68 and the attempt record's fig4ac notes.** The untyped files "are described as Patch-seq experiments in every file". Cell 10 prints only that `experiment_description` has one distinct value, not what that value is.
- **Cell 0 and the README.** "takes about seven minutes": the printed run time is 8.4 min (cell 89). "the first 5 GB of the GEO archive" is not printed; only the 3.43 GB member is (cell 86).
- **Formatting.** Stray `**` at the end of the result paragraphs in cells 19, 22, 25, 28, 31 and 81.

Every other sentence I checked in the "Result" paragraphs, the Summary, the README and the record's notes matches the printed numbers.

**My round-1 reasons in the record.** They are in my words and are faithful. Problems 5 and 7–10 are folded into the reasons of the claims they concern.

## 3. Round-1 points

**Resolved:**
- 1, the 'none' branch: an AP with no AIS peak or shoulder now scores 0.81 on the synthetic test.
- 2: the 39-feature FDR is now exact.
- 3: n175 is left out of the L5/6 CT group.
- 4: fig4i was run.
- 5: the device-by-typed-status table settles the question of recordings without RNA.
- 6: fig7c is tested.
- 7: the 57-feature choice is stated, with random 40-feature sets as a variant.
- 8: the sag variant at −200 pA only was added.
- 9: tau per-cell fit counts and a median-over-sweeps variant were added.
- 10: the table inconsistencies are stated.
- The HDF5 search for annotations was done.

**Remaining, bearing on a conclusion:**

- **R1 (fig3e, fig3d, fig4i).** Problem 1 persists in the shoulder branch of `aic.phase_index`, which handles 195 of 237 first APs (cell 61). The branch takes the lowest interior local minimum of d2V/dt2 anywhere before the dV/dt maximum. With noise, such minima occur just before the peak, where Pais ≈ Psd, so the index comes out near 0. I tested a synthetic monophasic AP (no AIS phase) at 50 kHz, without noise and with Gaussian noise of 0.02, 0.05 and 0.1 mV:
  - without noise it scores 0.81;
  - with noise it scores median 0.70, 0.010 and 0.008;
  - the synthetic shoulder AP falls from 0.21 to 0.011 at 0.05 mV.

  Slower rises are hit more: at 0.03 mV and 50 kHz, a slow monophasic AP scores below 0.1 in 96% of trials and a fast one in 3%. At 25 kHz the effect is much smaller. So an AP with no AIS phase, if broad and slow-rising like a VEN's, can get the most saddle-like index without any saddle. This fits the sampling-rate sensitivity (cell 34: 0.088 → 0.168 on decimation) and the loose agreement with the hand-read values (Spearman 0.39 and 0.20, cell 62). The automatic index cannot support either the partial result for fig3e or the not-reproduced result for fig4i.

- **R2 (fig3e).** The outcome depends on the prominence guard (above) and is not flagged as an assumption.

- **R3 (l5et-vs-l5it).** The rule for disagreeing sag readings is an unflagged assumption; the alternative reading is blocked.

- **R4 (fig2d, fig2f; interpretation only).** Device and recording era are confounded with group. Within either device, the short tau and narrow APs of L2/3 IT HPCAL1 are not significant (cell 34). The record reports this, and it does not change the criterion outcomes.
