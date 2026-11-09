**Round-3 verifier report: Semenov et al. 2025 (DANDI:001274 and related dandisets)**

The claims file has 26 claims and the attempt record has 26 outcomes. Only one outcome has a `proposed` change: fig3c-sustained-firing-2s, at record line 228. Line 452 also uses the word "proposed", but it describes my round-1 suggestion for fig1-max-rate-ceiling, not a proposal by the author.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig3c-sustained-firing-2s | reproduced, marked assumed | **Yes**, provided it is marked `assumed: true` | — | See below. |

**Part (iii), cell 59.**
- **The numbers come from the data.** They are computed on c7's own bleaching-corrected trace at 83 V/cm (`corr[ptop.path]["whole"]`). The output matches the record: residual SD 0.94%; mirrored trace 6 (a) and 7 (b); Gaussian mean 7.8 / 5.1, with 0.91 / 0.99 of draws reaching the observed count; shuffled 8.4 / 4.6; 1.12 / 0.73 false APs per 250 ms, which is the Gaussian mean / 7 for the 1.75-s window.
- **The noise level is checked independently.** The 0.94% residual SD agrees with the trace's pre-stimulus SD (0.89%) and with that of the fast recordings (0.83%).
- **The test does not just assume white noise.** The mirrored-trace estimate keeps the trace's own temporal structure. It gives as many detections as were found or more under both readings, and so do the other two estimates.
- **The detector is unchanged.** The test uses the same `T.detect_aps` as everywhere else, with reading (a)'s 5% prominence and reading (b)'s 5% rise in 5 ms.
- **Reading (b) leans further towards no APs.** The trace has 1 upward event against about 5 to 7 from noise.
- **The analysis was not tuned to reach the result.** I asked for this test in round 2, and its design is fixed in advance and stated in the cell. The 31-ms median window is about four AP durations, and the result does not depend on it, since three different estimators agree.
- **The plateau condition holds.** Mean dF over 0.25–2 s is 6.7%, above 5% (cell 57).

**Parts (i) and (ii), cell 57.** These hold with a wide margin over the measured noise rate:
- (i): 8, 10 and 10 APs in the last 250 ms at 52, 61 and 72 V/cm, against about 1.1 (a) and 0.7 (b) expected from noise.
- (ii): the AP count rises 0 → 17 → 73 → 89 under (a), and 0 → 19 → 75 → 90 under (b).

**On the criterion as written.** Taken literally, "no APs after 250 ms" fails, because the detectors find 5 (a) and 1 (b) peaks. The proposal reads (iii) instead as "no more detections than the trace's noise gives". That is a reinterpretation, so the outcome must carry `assumed: true`, as the author asks. I accept it for two reasons:
- The claims file's detection readings are stand-ins, since the Methods give no detection rule.
- On a plateau above the 5% detection level, any trace with this noise yields detections at about this rate. So the literal test could not pass for any recording, whatever the neuron did.

**A flaw in the claims file, reported and not corrected.** The fig3c criterion gives no allowance for false detections on a depolarized plateau. Criteria that use the readings on a plateau have the same gap, as fig1-max-rate-ceiling showed. This is a flaw in how the criterion is put into practice. It is not a misreading of the paper: the paper's "the block had already developed before the end of the 250-ms ramp-up period" is rendered faithfully.

**Caveats to keep in the record.**
- The test rests on one neuron, c7, because only c7 has an AP-free reference trace.
- The other three neurons reach no block (c5, c6, c8, cell 57). That is consistent with the paper only if they were not driven to block; it does not count against the claim under the criterion as written.
