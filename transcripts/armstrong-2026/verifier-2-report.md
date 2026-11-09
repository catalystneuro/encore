**Round 2 verification: Armstrong & Vlasov (2026) on DANDI:001341 (0.260414.1316)**

**1. Outcomes and assumptions**

The claims file has 33 claims and the attempt record has 33 outcomes with matching ids: 5 not_reproduced, 1 partially_reproduced, 15 blocked (metadata_insufficient) and 12 blocked (data_missing).

| Claim | Record | Agree? |
|---|---|---|
| table-s1-recordings | not_reproduced | Yes. Both unit counts and both OL counts miss (cell 24). The outcome does not depend on the 1000-row assumption, which is stated, so `assumed` is not needed. |
| fig1n-epoch-rates | not_reproduced (blocked in round 1) | Yes, I agree with the change. The criterion needs all four values. The epoch 1 rate is 6.65 to 7.80 Hz at every lag from −20 to 60 s, 7.18 to 7.26 Hz over the CL rows and 7.09 Hz over the whole recording (cell 27). No clock could bring that to 2 Hz, and 4 missing units cannot either. |
| figs1-running-speed | not_reproduced | Yes (cell 30). |
| fig2a-success-rate | not_reproduced | Yes. The rate is 0.609 to 0.694 under all 8 readings (cell 33). |
| fig2b-lateral-spread | not_reproduced | Yes. With the NaN fix every trial now has a value. Under (b) the t = 0 SD is 0.84, outside 0.55 ± 0.055; under (a) the SD does not widen (0.00 → 2.78 → 0.76) (cell 36). |
| fig4-ddm-fit | partially_reproduced, `assumed: true` | Yes, with low confidence. NDT is out of tolerance under all three early-RT handlings. GDDM BIC is below DDM BIC with all RTs kept and with the 0.1 s cutoff, but in 0 of 4 fits with the mixture (cell 41). The assumption is stated in the deviations and is reasonable. The record should say plainly that the GDDM condition, and with it the partial outcome, fails under the mixture handling. The notebook says this ("only when the early RTs are not absorbed by the mixture", cell 43); the record's notes drop it. |
| 15 blocked, metadata_insufficient | blocked | Yes. The speed clock for 503 has a residual SD of 0.56 s and 489 has no clock, against windows of 5 to 180 ms. |
| 12 blocked, data_missing | blocked | Yes. |

**2. Sentences the printed outputs do not support**

- **Cell 28 (Result):** "At the stored onsets it is 7.27 to 7.48 Hz." Cell 27 prints (a) 7.32 and 7.27, (b) 7.48 and 7.15. The range is 7.15 to 7.48 Hz.
- **Cell 43 (Result) and the record's fig4-ddm-fit notes:** "the fitted mixture weight is at its limit in every fit (0.100; 0.158 to 0.243 with a limit of 0.3)". The limit-0.3 fits are at 0.161, 0.158, 0.237 and 0.243 (cell 42), all below the limit. The weight is at its limit only in the limit-0.1 fits, and one GDDM fit there is at 0.099.
- **Cell 43:** "NDT fixed at 0.12 s gives a BIC 4.4 above the best ... disfavoured but not excluded." The profile fits have equal parameter counts, so 4.4 is a deviance difference. That puts 0.12 s just outside a 95% profile-likelihood interval (p ≈ 0.04). "Not excluded" is a stretch; "narrowly excluded" fits the numbers better.
- **Cell 43:** the GDDM leak is "near the +10 edge with the cutoff". The cutoff fits are at 6.04, 6.10, 9.88 and 9.99, so only two of four are near the edge.
- **Cell 17:** "the largest bin of the ramp window is no higher than the largest bins elsewhere in −1 to 2 s." For 503 OL_R, the ramp-window maximum of 10.78 Hz is the maximum of the whole −1 to 2 s range (cell 15). The sentence holds for 489, the claims' animal.
- **Cell 22:** "0.865 (0 to 0.5 s) and 0.912 (0.5 to 1.8 s) against shuffled 95th percentiles of 0.535 and 0.552." Cell 21 prints 0.552 for 0 to 0.5 s and 0.535 for 0.5 to 1.8 s, so the two values are swapped.
- **Cell 22:** "the onset lags of windows 1 to 3 (11.78, 14.15, 12.07 s) lie near it (13.24, 14.19, 15.23 s)." Window 3 is 3.2 s from the line, about 6 residual SDs. Windows 0 and 4 to 6 (5.58, 52.54, 19.92, 21.91 against 12.33, 16.26, 17.22, 18.13) are left out without comment.
- **Cell 22, README and record findings:** "In 489 ... finds nothing beyond chance" and "no alignment can be found". Windows 0 to 6 of 489 give best lags that rise almost steadily: 4.36, 6.81, 7.50, 7.37, 9.57, 10.93, 12.23 s (cell 18). The first two speed-lag windows (5.50 and 5.85 s, cell 19) agree with them. Independent random maxima over −20 to 60 s would rarely form such a sequence. The per-window z test misses this pattern. The blocked outcomes do not change, because any such clock would be as coarse as the one for 503.
- **Record, verification entry:** "the header now notes that the SI says TTL signals were used for synchronisation." The claims file I was given has no such note; it contains neither "TTL" nor "LabVIEW".

The rest of the checked sentences match the outputs. That covers the remaining Result cells, the Summary (cell 45), the README, the outcome notes and deviations, and the findings, including 0.92 to 0.95, 12.9 to 19.75 s, 11.86 s plus 1.37 ms per s, 62 and 63 negative rows, 256 of 305, 1.7% and 31.8%, and 94 trials.

On the round-1 reasons: the `reason` fields state my round-1 reasons faithfully. Problem 3 is repeated on every metadata_insufficient claim, and the section C note about the epoch 1 rate is added to fig1n. There is a cosmetic fault: the fig1jk-all-units and fig5b `response` fields repeat "Kept blocked." with the boilerplate pasted after it.

**3. Status of round-1 points**

Resolved:
- **Problem 1 (NDT and early RTs):** early RTs are now counted, three handlings are fitted, and cutoff, mixture and profile checks are added.
- **Problem 2 (GDDM leak at its bound):** the leak is reported for each handling. With all RTs kept, a leak at the edge can only make the GDDM BIC lower, so the BIC comparison stands.
- **Problem 3 (clock-drift model and null):** the speed clock for 503 and the onset-lag null are added.
- **Problem 4 (running fraction):** reported by row type.
- **Problem 5 (NaN counts):** fixed, and the counts are printed.
- **Problem 6 (decoder leakage):** z-scoring now uses training-fold statistics only.
- **Problem 7 (1000-row assumption):** stated, and the 1611-row count is given.
- **Section C items:** the recursive file listing, early-RT refits, per-time non-NaN counts, the epoch 1 rate at every lag, and the speed-clock PSTH with a null are all done.

Not resolved:
- **Point 8 (header note on TTL sync):** the record says the claims-file header was updated, but the file I have has no such note.

Remaining points that bear on a conclusion:
- **fig4-ddm-fit:**
  - The partial outcome depends on how early RTs are handled: it holds with all RTs kept and with the cutoff, and fails with the mixture. The record's notes should say so.
  - The mixture weight sits at its 0.1 cap and rises to 0.16 to 0.24 when the cap is 0.3. That is well above the 4 to 5% of RTs below 0.1 s, which suggests the plain DDM misfits the RT shape more broadly. This adds to the low confidence.
  - The two misstatements above (mixture weight at its limit, 0.12 s "not excluded") should be corrected.
- **fig1n-epoch-rates:** the stored-onset range in cell 28 should read 7.15 to 7.48 Hz. The outcome does not change.
- **No effect on outcomes:**
  - The 489 lag trend contradicts "no alignment can be found" and the wording should be softened.
  - The 503 speed clock was fitted to running speed, and running differs by trial type (1.7% of OL_L rows against 31.8% of OL_R). So the "turn-specific responses" and the 0.865 to 0.912 decoding on that clock may partly reflect running, and the 0.655 decoding before the onset may too. The README and findings should not present them as neural turn responses without that caveat.
