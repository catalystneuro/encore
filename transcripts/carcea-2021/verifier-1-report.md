**A. Outcomes** (all 19 claims in `10.1038-s41586-021-03814-7.yaml`; no separate attempt record was among my materials)

| Claim | Outcome | Reason |
|---|---|---|
| label-link | reproduced | Cell 15: in V116 03122018, 7 of 7 "Mom agressing" intervals coincide with "Shepherding" and 2 of 2 "Mom retrieval" with "Self gen retrieval". Pooled "Virgin in rest" ≤40 s is 366/499 = 73.3%, inside 63.5–77.6. This passes on V111 (343 of the 499 intervals); V116 and V118 give 9.9% and 0% (problem 6). |
| ed7a-nest-entry-fraction | partially_reproduced | Cell 17: 42/194 = 21.6% activated, Fisher p = 1.9e-14. That is outside both tolerances (23.9–29.2 and 23.6–28.8). 37 of the 42 are in V116. Without the 40 s cap, as in the authors' code, it is 2/194 (cell 18). |
| ed7a-shepherding-fraction | not_reproduced | Cell 20: 3/194 = 1.5%, Fisher p = 0.12 (≥ 0.05). Only the code's equal-duration baseline variant gives p < 0.05 (9/194, 4.6%), and that fraction is still far below 9.3–11.9%. |
| ed7a-dam-retrieval-fraction | partially_reproduced | Cell 22: 13/132 = 9.8%, p = 9e-05, below both tolerance ranges. Nine of the 13 come from one V111 session with a single retrieval episode. With sessions of ≥2 episodes it is 4/101, p = 0.061, which would be not reproduced. |
| fig2j-shepherded-entry | not_reproduced | Cell 24: 128 units, median shepherded − voluntary = 3.9, Wilcoxon p = 0.182. The 5 s and 30 s windows give p = 0.37 and 0.17. Two sessions go in opposite directions (V110 p = 5e-9 one way, V116 03102018 p = 0.007 the other). |
| fig1j-shepherding-rate | partially_reproduced | Cell 26: mean 0.65/h (s.e.m. 0.17, n = 10 sessions), t-test against 0.2 gives p = 0.029, so the t-test part holds. The mean is far outside 3.5 ± 0.9. Per mouse, p = 0.19. |
| ed8a-dam-retrieval-rate | not_reproduced | Cell 28: mean 0.21/h, outside both 0.45–0.55 and 0.31–0.66. Two of the 10 sessions have no "Mom retrieval" events. |
| ot-pvn-units | blocked (data_missing) | The asset list (30 files) has no optical-tagging recordings. The units table has only `spike_times` and `unit_name` (cell 3). The `unit_name` values are never printed (see C). |
| fig2f-virgin-chasing | blocked (metadata_insufficient) | "Virgin Agressing" exists (1 to 15 per session in V110, V111 and V116; cell 7), but nothing defines it. Taking it to mean virgin→dam chases, a test could run, but only on the 3 shepherding-activated units, not the paper's 6. |
| ed6-dam-vs-pup | blocked (data_missing) | There are no 5-min interaction periods and no audio. All acquisition series are 16-channel 30 kHz voltage, too slow for ultrasonic calls. |
| fig1cd-retrieval-onset | blocked (data_missing) | No retrieval-test data for the co-housed cohorts in the asset list. |
| fig2a-dreadd | blocked (data_missing) | No DREADD cohort files. |
| fig3fg-observational-learning | blocked (data_missing) | No observation-cohort retrieval scores. |
| fig3ij-observation-units | blocked (data_missing) | Every ecephys file is a multi-hour home-cage recording; none is an observation session. |
| fig4c-ac-photometry | blocked (data_missing) | No auditory cortex photometry during co-housing and no pup-call times. The ophys events are only "Pup out" and "retrieval". |
| fig4f-pvn-ac-correlation | blocked (data_missing) | No simultaneous units and photometry. |
| fig4i-projection-photometry | blocked (metadata_insufficient) | Partly testable. Responses to the dam's retrievals can be computed for all six ROV animals from their obs files. ROV40 and ROV41 have retrieval-test files with retrievals, so they are probable learners. ROV43/44/45/49 have no test files, so the 3-vs-3 split cannot be formed. Fibre location is "unknown". |
| fig4jk-oxytocin-in-ac | blocked (data_missing) | No infusion or optogenetic cohort files. |
| ed9-colliculus | blocked (data_missing) | No tracing data or stimulation cohort. |

Tally: 1 reproduced, 3 partially_reproduced, 3 not_reproduced, 12 blocked.

**B. Problems**

1. [affects a conclusion] `pvn.shuffle_test` / `pvn.modulation`: on the real episodes, an episode with no spikes in either window is dropped; in the shuffles it counts as 0, as in the authors' code. This inflates significance for sparse units with few short episodes. On synthetic Poisson units with no response (4 episodes of 3 s, 10 s baseline, 0.05 Hz), 17% come out "activated" and 43% "suppressed" after BH. At 0.3 Hz and above it is about 0–4%. V116 medians are 0.23–0.37 Hz (min 0.006), and the shepherding and retrieval tables have values at ±100 and high suppressed counts (V116 03092018: 10/21). The positive results are biased upward, so the not-reproduced outcomes stand, but the suppressed counts are unreliable.
2. [affects a conclusion] Cell 22: 9 of the 13 dam-retrieval activations come from one episode in V111 03032018. V111 units have 86% of spikes coincident with another unit within 0.1 ms (cell 5), so these 9 are probably not independent neurons. The Fisher test treats them as independent.
3. [affects a conclusion] Cells 5 and 17–24: V111's 31 units are probably the same clusters on three days (log spike-count correlation 0.93–0.97). They are counted as 93 units in all fractions and in the fig2j Wilcoxon test. V110 and V111 also have 7–9% of inter-spike intervals under 2 ms and 79–90% coincident spikes. The notebook flags this but keeps them in the headline numbers.
4. [affects a conclusion] Cell 9: the shared-clock test fails in every session (best rank 17/121), and the analysis proceeds anyway. In V116 03102018 the spikes and events run to 13.46 h against 4.46 h of raw voltage, so their clock relation to the raw series is unknown. That session has 17/26 nest-entry activations.
5. [affects a conclusion] Cell 26 / `session_length_s`: the rate denominators assume each session was annotated over its whole length. Annotation coverage is never checked. If only part of each session was scored, both fig1j and ed8a rates are underestimated. The paper's 3.5/h (Extended Data Fig. 3b) also comes from a pups-present vs pups-removed comparison in 4 dyads, a different window from these 12-h recordings.
6. [affects a conclusion] Cell 15: "Virgin in rest" means different things across mice. The median dwell is 5–52 s in V110 and V111 but 800–2500 s in V116, where it lies inside "Virgin in nest" 13/13 times. label-link passes only on the pooled count. Nest-entry results are split the same way: 37/70 in V116 against 4/124 in V110 and V111.
7. [affects a conclusion] Cells 17–18: the nest-entry fraction depends almost entirely on the 40 s cap (42 with it, 2 without). The cap follows the Methods, so the outcome stands, but it is fragile.
8. [does not affect a conclusion] `fisher_vs_zero`: as in the paper, it compares against zero activated units, so any k ≥ 5 of about 100–200 is "significant". The paper's chance level is zero; the notebook's uncorrected positive rate (cell 18, 28.4%) is compared with "about 5%". By my simulation, the pipeline's real false-positive level after BH is about 0–2% for nest entry, but higher in the sparse case of problem 1.
9. [does not affect a conclusion] `shuffle_test` takes the p-value one-sided in the observed direction and then applies BH. This is effectively a two-sided test at 2q, as in the code.
10. [does not affect a conclusion] `_counts` counts both window edges, so a spike exactly at the episode start falls in both the 10 s baseline and the episode. I checked this on a synthetic train.
11. [does not affect a conclusion] `bh` matches statsmodels `fdr_bh` on 200 random inputs that include NaNs. `triggered_change` is defined but never used.

**C. Not checked, and the output that would have allowed it**

- Whether `unit_name` encodes OT-PVN identity or channel. Printing the unique `unit_name` values per session would settle this for ot-pvn-units.
- Annotation coverage. Printing, per session, the first and last annotation of any label and the largest gap between annotations would test the rate denominators (fig1j, ed8a).
- fig4i partial test. Per-animal mean retrieval-triggered photometry change in the obs files (`triggered_change`), and the retrieval-event times in the ROV40/ROV41 test files, would show which animals learned and give a partial learner-group test.
- fig2f. The modulation of the 3 shepherding-activated units during "Virgin Agressing" episodes, plus the per-session onset-time overlap between "Virgin Agressing" and "Mom agressing", would let me judge what the label means.
- Overlap between baseline windows and earlier episodes. A count of capped nest-entry baselines that overlap a preceding "Virgin in rest" or "Mom agressing" interval would show whether the baselines are contaminated.
- Whether the empty-episode exclusion drives the result. The number of real episodes dropped per unit, or the activated counts with empty episodes set to 0 in the real value too, would show this.
- Unit independence. Pairwise spike-train correlation, or coincidence per pair, among the 9 V111 03032018 retrieval-activated units would show whether they are separate neurons.
- Draft vs pinned version: only one file's content was compared (cell 13). I did not re-run anything and read no NWB content myself.
