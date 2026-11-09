**Verifier report, round 2: 000140-churchland-2010-01**

**1. Outcomes** (20 claims in the claims file, 20 outcomes in the attempt record)

| Claim | Record | Agree? | Assumption |
|---|---|---|---|
| fig4d-mean-correlation-j-array | not_reproduced | Yes | – |
| fig4abc-mean-correlation-other-datasets | blocked: data_missing | Yes | – |
| fig4-broad-near-zero | not_reproduced | Yes | O1a: stated and reasonable. The O1b passes rest on 3–5 units. |
| fig4e-correlation-time-course | reproduced | Yes, on the criterion only | O1a: stated and reasonable. Cell 16 shows the pass is mostly shared trial noise. With disjoint trials the fig4 units have r at −200 ms of only 0.02–0.145, and 4 of 12 readings pass. The record says this. |
| suppfig1-population-averages-lose-tuning | reproduced | Yes, on the criterion only | – |
| fig6d-perimovement-best-j-array | partially_reproduced | Yes | O1a: stated and reasonable. Under O1a both T-matrix readings give reproduced or partial in every setting, so O1a alone carries the outcome. |
| fig6abc-perimovement-best-other-datasets | blocked: data_missing | Yes | – |
| fig6-perimovement-best-each-dimensionality | not_reproduced | Yes | – |
| fig6-maze-endpoint-speed-space-poor | not_reproduced | Yes | O1a: stated and reasonable |
| fig6-dimensionality-trend | not_reproduced | Yes | O1a: stated and reasonable |
| fig6e-summary-rank | blocked: data_missing | Yes | – |
| prep-dimensionality-7-to-10 | not_reproduced | Yes | – |
| fig7a-shuffled-space-poor | reproduced | Yes (weak) | – |
| fig7b-window-start-slide | not_reproduced | Yes, but the assumption is not marked | Under the adopted O1a reading the ratio is undefined (cell 53), so the outcome rests only on the O1b readings (7–8 units). Everywhere else O1b is the non-adopted reading. The record should carry `assumed: true` and say that the outcome rests on O1b. |
| ap-location-no-effect-j-array | reproduced | Yes | Array identity as AP location: stated, reasonable, and valid under both mappings. |
| ap-location-no-effect-other-datasets | blocked: data_missing | Yes | – |
| fig7c-anterior-posterior-performance | blocked: other | Yes | – |
| prep-activity-more-anterior | blocked: metadata_insufficient | Yes | – |
| fig7d-pd-consistency | not_reproduced | Yes | – |
| fig8-linear-dynamics-simulation | reproduced | Yes | – |

On the claims file: I found nothing new where it misreads the paper. The paper confirms the 10 vs 5 spikes/s inclusion rule, the 97%/94% values and the 25-condition PD draws.

**2. Text against the printed outputs**

Everything else I checked matches the printed numbers. That covers every value in the fig4d, fig4-broad, fig6d, fig6-each, fig6-maze, fig6-trend, prep-dim, fig7a, fig7b, AP, fig7c, prep-anterior, fig7d and fig8 conclusions, the README, and the findings. The following are not supported:

- **Cell 25 and the fig4e record note:** "Under O1b … partially reproduced in 10 of 12 readings." Cell 24 shows 11 of 12 marked partial. The 12th (O3a, O4a, sd, ii; r at onset 0.091, drop starting at +90 ms) is neither a pass nor a partial.
- **Cell 72 (Summary):** "the SD reading keeps 7 or 8 units with clearer tuning, and on them the peri-movement space built from all recorded units performs best with positive performance, as in the paper."
  - Cell 30 shows it is best in 5 of 6 O1b settings. Under O3b/O4b the kinematic space is higher (0.134 against 0.129).
  - Cell 32 shows no O1b gap is significant (p 0.47–0.98).
  - "Clearer tuning" is not shown for these units; no reliability is printed for them.
- **fig7d record deviation:** "raw and z-scored axes … agree on the segment-directions comparison in 23 of 24 readings." Cell 67 has 12 raw/z pairs, and they agree in 11 of 12. The figure 23 of 24 is the number of rows where the peri-movement space loses.
- **Cell 28 and the suppfig1 record note:** "the strongest trace being on top at −150 ms … comes mostly from noise shared within the same trials." This is an inference, not something shown. The disjoint halves also use about half the trials (cell 16), so the extra noise could hide a real effect. "Suggests" would be accurate.
- **Record, fig6d `reason`:** it includes my round-1 problem 6, which I marked as not affecting a conclusion. Otherwise the record states my round-1 reasons faithfully. Problem references and cell numbers were dropped, and agrees/outcome are recorded correctly, including `agrees: false` for fig4-broad, fig6d, fig7c and prep-anterior.

**3. Round-1 points**

- **Resolved:**
  - **Problem 1 (no noise control):** cell 16 now has a condition-shuffled null and a disjoint-trial reference, and the conclusions cite them.
  - **Problem 2 (the range rule admits noise):** shown in cells 16–17 (82–96 units pass with shuffled labels) and filed as a finding.
  - **Problem 3 (no uncertainty):** fig6d and fig6-maze now print SEs and paired tests. The fig7b ratio is now undefined when the denominator is ≤ 0. fig7c is blocked.
  - **Problem 4 (array mapping):** cells 57, 61 and 64 show both mappings, and prep-anterior is blocked.
  - **Problem 5 (subset of readings):** fig7a, fig7b and fig7d now run all six O3/O4 settings and both O1 readings.
  - **Problem 6 (T-matrix units):** the included-units reading is added.
  - **Problem 7 (unused hold):** `hold` is removed from `simulate_rotation`.
- **Remaining, bearing on a conclusion:**
  - fig7b: the outcome rests on O1b alone and is not marked `assumed` (section 1).
- **Remaining, not bearing on an outcome:**
  - The wording errors in section 2: fig4e 10 vs 11, the Summary's "performs best", and fig7d 23/24.
  - The O1b "upper limit" (0.123 in cell 30) is below the peri-movement best (0.209), so it bounds nothing. That affects only fig7c's O1b normalisation, and fig7c is blocked anyway.
  - fig7c is still run on O3a/O4a only. This is stated, and the claim is blocked anyway.
