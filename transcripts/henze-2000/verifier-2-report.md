**Round-2 verification: Henze et al. (2000) on CRCNS hc-1, attempt henze-2000-01**

**1. Outcomes and assumptions** (21 claims in the claims file, 21 outcomes in the attempt record)

| Claim | Record | I agree? | Comment |
|---|---|---|---|
| sample-cells | not_reproduced | yes | Cell 21. |
| fig1c-start-end-timing | not_reproduced | yes | Cell 26: the start lead is never in tolerance, under any of the four site rules (S1 to S4). |
| ap-duration-match | reproduced | yes | Cell 29: 1, 6, 1 and 2 readings pass under S3, S1, S2 and S4. Under S3 the extracellular duration SD is 0.59 against the paper's 0.19, but the criterion tests means only. |
| duration-correlation | reproduced, assumed | yes, with a reservation | The assumption (rule S3) is stated. It is reasonable in that it agrees with the paper's own label of D53. The reservation is that the result rests on D12821, a cell S3 adds. Its intracellular duration is 5.70 ms against the paper's 1.28 ± 0.18 (cell 29). From cell 29's per-cell durations (all spikes, both starts by dV/dt, end at threshold) I get R = 0.742, which matches cell 32. Without D12821 it drops to R = 0.02, and without D12821 and D8131 to 0.46. The reproducing readings share D12821's intracellular duration, so they are probably driven the same way, but cell 32 does not print the per-cell values that would show it. The record should say this. |
| neg-peak-precedes-intra-peak | reproduced | yes | Cell 35. |
| fig1c-derivative-mismatch | reproduced | yes | Cell 38. |
| notch-and-ahp-landmarks | not_reproduced | yes | Cell 42. |
| fig2-interneuron-narrow | blocked (metadata_insufficient) | yes | |
| fig3b-latency-vs-amplitude | reproduced | yes | Cell 45: holds under all four rules. |
| fig3a-example-pair | not_reproduced, assumed | yes | The pair identification is stated and reasonable. Cell 45 shows the 0.975 ms latency of D11222 is not a window-edge artefact. |
| fig3c-backprop-velocity | not_reproduced | yes | Cell 52: 0 of 96 readings in tolerance. |
| fig4bc-burst-attenuation | partially_reproduced, assumed | yes, but fragile | The selection assumption is stated. See remaining point (a). |
| fig4d-amplitude-correlation | reproduced | yes (changed from round 1) | With the corrected threshold, D15121 gives R = 0.408 and 0.374 with P < 0.0001 (cell 61). The per-spike threshold now passes the synthetic check (cell 15: −59.6 against a −60 mV rest). |
| fig5-theta-smaller-spikes, theta-higher-rates, fig6-amplitude-vs-distance, tetrode-cell-count-estimate, fig8-neighbouring-shanks | blocked (data_missing) | yes | |
| silent-cells-inference | blocked (data_missing) | yes on the outcome | I gave blocked_by other. The author's reason (a claim that depends on a blocked claim is blocked for the same reason) is acceptable. I cannot check the protocol step cited. |
| fig7-vertical-spread | not_reproduced | yes | Cell 64: 4 of 10 cells. |
| propagation-velocity-range | blocked (data_missing) | yes (changed from round 1) | The claims file's criterion itself says the counts point to reading (b). Reading (a) is reported in the notes. |

**2. Text against the printed outputs**

- **Summary, cell 71:** "The spreadsheet IntraExtra.xls covers 18 of the 39 cells, none of the 19 earliest tetrode cells". Not supported. D15121 is not in the spreadsheet and is later than the listed D14521 and D14921 (cells 9 and 17). It should read "19 of the 21 tetrode cells".
- **Attempt record, duration-correlation notes:** "S1 (8 cells) and S4 (9 cells) give positive R with P < 0.03 under 4 readings each, R 0.76 to 0.95". Cell 32 prints only the R range over all readings (S1 0.274 to 0.945, S4 0.091 to 0.945). The 0.76 lower bound is not printed. Cell 33's "R up to 0.945" is supported.
- **Attempt record, finding 1:** "Six of the paper's 21 findings cannot be tested for this reason." Seven outcomes in the record are blocked_by data_missing.
- **Cell 68 and the propagation-velocity-range notes:** "their finite velocities are 0.18 to 0.54 m/s". This is the fit pairing only. The farthest-site pairing gives up to 0.60 m/s (D18712, cell 67).
- **Cell 41 (method text):** still says the slope change is "a local maximum of the second derivative". The code in cell 42 and conclusion cell 43 use the first local maximum or minimum. The text is stale, the conclusion is correct.

Every other Result sentence (cells 22, 27, 30, 33, 36, 40, 43, 47, 50, 53, 59, 62, 65, 68), the rest of the Summary, the README and the other notes match the outputs.

My round-1 reasons appear in the verification block in my own words for all 21 claims. The added sentences are attributed correctly ("The verifier asked…", "The verifier gives other").

**3. Round-1 points**

Resolved:
- **1, site rule.** Four rules are run and the main rule is stated. Residual: see (b).
- **2, per-spike threshold.** Fixed and checked on synthetic APs.
- **3, negative-peak window.** Widened to −2 ms with a synthetic check. No tetrode cell's latency changes, and D11222's trough stays at −0.97 ms.
- **5, extracellular gain.** Compared with Fig. 6A and recorded as a finding.
- **6, slope change.** Fixed in code (the cell 41 text above is stale).
- **7, reading v_c.** The conclusion now says it is unstable.
- **8, file descriptions.** D6811 uses 3 channels, D13521's rate is checked, and D13921 is shown per file.
- **9, site-order smoothness.** Now computed.
- **10, header table.** Now says blocked.

What remains and bears on a conclusion:
- **(a) Point 4, fig4bc partly resolved.** Cell 58 now prints step durations but the selection ignores them. They range from 0.1 to 500 ms, against the 350 ms steps of Fig. 4A. The 6 of 11 majority under the criterion's selection includes D8131, whose median step is 0.1 ms. Without it the count is 5 of 10, not a majority. Taking only those 11 cells with steps of at least 100 ms leaves 6 cells. Full set and amplitude parts then each hold in 3 of 6 (reading (a), extracellular amplitude baseline to negative peak). That is not a majority, so the outcome would fall from partial to not reproduced.
- **(b) duration-correlation rests on D12821** (5.70 ms intracellular duration, see section 1). Of the readings whose per-cell durations cell 29 prints, the correlation disappears without it (R 0.742 to 0.02). The outcome needs that dependence stated, or a check without D12821 and D8131 under the reproducing readings.

Minor, does not change an outcome: cell 60 defines intracellular amplitude reading (b) as peak minus the mean of −3 to −1.5 ms. The claims file defines it as the 2 ms before the start, and the record does not list this as a deviation.
