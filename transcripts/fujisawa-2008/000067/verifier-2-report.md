**Round 2 verifier report: Fujisawa et al. 2008 (doi:10.1038/nn.2134) on DANDI 000067 @ 0.250624.0419**

I still could not get the full text. Europe PMC returned HTTP 500, BioC returned "Too Many Requests" and PMC returned a reCAPTCHA page. Only the abstract is saved, as `paper/abstract.txt` (PMID 18516033). So I cannot check anything that depends on the Methods or supplement wording, such as whether fig4 is really "methods underspecified".

The claims file has 16 claims, and the attempt record has 16 outcomes: 6 partially reproduced, 7 not reproduced and 3 blocked.

## 1. Agreement with each stated outcome

| Claim | Record | Agree? |
|---|---|---|
| channel-region-link | partially_reproduced | Yes (cell 16) |
| rats-and-units | not_reproduced | Yes, under the criterion. The fixed eight sessions are what make the unit count fail; see 3. |
| task-performance | blocked (data_missing) | Yes |
| fig2c-active-fraction | not_reproduced | Yes (cell 25) |
| fig2-field-size | partially_reproduced | Yes (cell 28) |
| fig2b-trajectory-selective | partially_reproduced | Yes (cell 31) |
| traj-diverge | partially_reproduced | **No.** It should stay blocked (data_missing). See 3. |
| odor-nosepoke | partially_reproduced | Yes (cell 37) |
| fig3-connection-rates | partially_reproduced | Yes, as the criterion is written. The inhibitory match it rests on is the artefact the notebook itself demonstrates (cell 41). |
| fig3-cell-classes | not_reproduced | Yes |
| fig3f-distance | not_reproduced | Yes, under the fixed 8-point Spearman test |
| fig4-position-dependence | blocked (methods_underspecified) | Yes. Cell 51 shows the criterion's test flags 30% and 75% of constant-efficacy pairs, so "not reproduced" would be unfounded. Whether the paper's null and thinning step are only in the supplement I cannot check. |
| fig6-facilitation-depression | not_reproduced | Yes |
| fig7-supralinear | not_reproduced | Yes under the criterion, but it remains uninformative. See 3. |
| fig3-trajectory-by-class | not_reproduced | Yes |
| ee188-example-session | blocked (data_missing) | Yes |

## 2. Sentences the printed outputs do not support

- **Cell 35, the record's traj-diverge notes and the README row "Trajectories diverge at position 0.3: Partially reproduced".**
  - The x1 divergence point of 0.49 does not measure the paper's 0.3. The notes themselves say "The sides differ mainly along the y coordinate, which is not in the dandiset."
  - Cell 34 shows x1 falling roughly linearly to its minimum near 0.5 on both sides. The x1 difference therefore appears where the path turns back in x, not where it separates laterally.
  - The first half of the claim ("overlap in the central arm") fails by x1 in 5 of 9 sessions (11 to 14 of 15 bins). One session (GG.149) diverges at 0.06.
  - The criterion's rule "partially reproduced when above 0.33" means any x1 result above 0.33 counts as partial support, whatever the paths do in y.
- **Cell 59 and the record's fig7 notes: "Neither measure finds supralinear summation."**
  - On the same 40 satellites the variant gives a median two-spike response of 0.0015. Under the criterion's measure, one partner gives 0.0145 and two give 0.0197 (cell 57).
  - Two coincident excitatory inputs producing about a tenth of one input's effect is implausible. The likely cause is that `pfc.linear_gain` subtracts post-unit spikes in flanks 10 to 30 ms from the event, and those flank rates rise around synchronous events.
  - The synthetic check in cell 58 uses stationary Poisson trains, so it does not cover that case. The variant's result on real data is therefore not evidence either way.
- **Attempt record, task-performance response: "bounds performance at 77.0% or more".**
  - Cell 22 gives 77.0% only if every error trial produced a lap that x1 detects.
  - Counting the 147 unlisted nose-poke bouts as errors instead gives 335/482 = 69.5%.
  - The notes say "a bound, not a test", which is fine. "Or more" is not supported.
- **Attempt record, channel-region-link: "Channels 1 to 64 carry no hippocampal theta in any rat".** Cell 9 shows a lower theta ratio (0.16 to 0.27 against 0.37 to 0.54), not an absence of theta.
- **Summary (cell 65), minor wording:**
  - "the rank band rarely reaches 0.01": it reaches 0.01 in 102 of 285 pairs (cell 50).
  - "Eight of the paper's sessions are used": the paper does not list its sessions.
  - "Only correct trials are listed" appears twice.

Every other "**Result:" sentence (cells 17 to 62), the rest of the Summary, the README and the other notes match the printed numbers.

The record's verification entries state my round-1 reasons correctly and in my own terms, including the problem numbers.

## 3. Status of my round-1 points

**Resolved:**
- **B1:** 34 of the 74 inhibitory connections are mirrored troughs. The synthetic check gives 21 of 30. Rates and classes without them are shown, and the fragility is stated.
- **B3:** The test is now calibrated (cell 51) and the outcome changed to blocked.
- **B4:** Shank order is consistent: 47.7% of units have their second-largest shank next to the largest, against 25% at random.
- **B5:** The markdown about the empty rank band is corrected.
- **B6:** `field_size` now returns NaN for an all-zero map; no side was affected.
- **B7:** `lin_t0` is read from `starting_time` and is 0 in every file.
- **B10:** McNemar tests are added for fig2b and odor-nosepoke.
- **B11:** The decoder now z-scores with the training trials only.
- **B12:** The count leaving out each block's first unit is 416.
- **B9:** Bounds on unlisted laps and poke bouts are added (wording issue above).
- **B8:** x1 is now compared between sides, but this produced the new disagreement below.

**Remaining issues that bear on a conclusion:**
1. **traj-diverge:** x1 cannot locate a lateral divergence, so the outcome should stay blocked (data_missing).
2. **fig7 (B2, partly resolved):** The new linear-prediction variant looks biased by its local baseline on real data. Settling it needs two outputs:
   - the mean flank rate around two-partner events against one-partner events;
   - the two-partner response with a global baseline.

   Until then, fig7 is not evidence against the claim.
3. **fig3-connection-rates:** "Partially reproduced" rests on an inhibitory rate that includes artefacts. Without them, none of the three rates is within tolerance (cell 41).
4. **rats-and-units:** The block-order rule matches the waveform placement perfectly in both other EE sessions (cell 19). Including EE.088 by that rule gives 631 units, within tolerance. The unit-count failure is therefore a result of the fixed session set, and the rat count fails only because data are absent. The README row should not be read as the dandiset contradicting 633.
5. **Full text:** Still unavailable to me, so I cannot check the Methods-based parts. That covers fig4's "methods underspecified" reason, the definitions behind fig6 and fig7, and whether the published jitter test excludes mirrored troughs.
