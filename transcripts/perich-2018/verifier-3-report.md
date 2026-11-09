**Verifier report, round 3: Perich, Gallego & Miller 2018 on DANDI:000688 (0.250122.1735)**

The claims file has 28 claims and the attempt record has 28 outcomes. Only one outcome has a `proposed` field: fig3b-pmd-higher-dimensional (record line 59).

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig3b-pmd-higher-dimensional | partially_reproduced (from reproduced) | Yes | — | See below. |

**The numbers come from the data.**
- Cell 16 gives the median dimensionalities for all 21 sessions. With rule (b), noise of the trial average, window (a) and the standard-deviation kernel, M1 is 7.0 and PMd is 10.0, and PMd > M1 in 21 of 21 sessions. In the 19-session set the medians are 7.0 and 11.0, with PMd > M1 in 19 of 19.
- Cell 17 gives the per-session values. PMd exceeds M1 in every session; the closest is M 2014-03-03, at 9 against 8.
- Over all 2002 possible sets of 16 sessions (cell 17), the medians range from 7.0 to 7.5 (M1) and 10.0 to 11.0 (PMd). None falls within tolerance, and PMd > M1 in every session in all 2002 sets.
- By monkey, C gives 7 and 10 and M gives 7 and 11. Cell 33 prints the same deciding numbers.
- The record's reason matches these outputs.
- The helper's kernel readings are correct (`perich.py:83`, `perich.py:236-238`):
  - SD reading: σ = 100 ms.
  - FWHM reading: σ = 100/2.3548 ms.

**The criterion is applied as written** (claims file lines 274–277):
- Under the SD reading, no combination of window and threshold rule meets "reproduced":
  - Window (a), rule (b): medians out of tolerance, PMd > M1 in every session, so partially reproduced.
  - Window (b), rule (b): PMd > M1 in only 20 of 21.
  - Rule (a): PMd > M1 in 19 of 21 and 18 of 21.
- So partially reproduced is the best outcome the SD reading allows. The result is also less fragile than the verified one: it does not depend on which 16 sessions are the paper's.

**The choice of kernel was not made to reach the result.**
- Cell 33 shows that one kernel reading now applies to every claim:
  - Under SD, figs4c meets the criterion in 4 of 4 readings, figs4d holds, fig6c is significant under window (a), and fig3b is partial.
  - Under FWHM, fig3b is reproduced and no fig6c reading is significant (p 0.18–0.38), so fig6c would be not reproduced.
- Either single reading costs one claim a step, so SD is not the uniformly favourable choice. It is also the reading under which every other recorded outcome stands, and it resolves the round-2 point that the record took the favourable kernel for each claim separately.
- The reasons for SD hold:
  - The paper says only "a non-causal Gaussian kernel of width 100 ms" (paper txt line 748).
  - Gallego et al. 2020 says "a Gaussian kernel (s.d.: 50 ms)" (checked in `paper/10.1038-s41593-019-0555-4.txt`).
- Cell 34 overstates the Gallego support slightly. It calls the 2020 rates "the same square-root, binned rates", but that paper used 30 ms bins of multiunit threshold crossings, not 50 ms bins of sorted units. This does not change the reason, which is about how the group states kernel width.

**Points left open**
1. The claims file header (lines 85–87) says a claim is blocked as methods_underspecified when the readings of an open detail disagree. Under that rule fig3b would be blocked: FWHM gives reproduced and SD gives partial.
   - The record follows the protocol's author step 1.6 (adopt the best-supported reading as an assumption) and says so in cell 34 and in the deviations. `docs/protocol.md` is not among my materials, so I could not check that step.
   - The conflict between the header rule and the criteria's "under one reading" is internal to the claims file, not a misreading of the paper. So is the expectation that O4 would not change an outcome; the paper's wording is ambiguous, so this is a wrong expectation, not a misreading.
2. If the change is accepted, the record's other fields for fig3b need updating to the SD reading:
   - `measured` is still 9 and 13.
   - The notes and the cell 19 conclusion are still written around the FWHM reading.
3. The outcome is still an assumed one: it rests on the noise scale (√(2K)) chosen in rounds 1 and 2, which is unchanged.
