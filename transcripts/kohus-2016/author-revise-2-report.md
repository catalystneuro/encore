Round 2 is handled and no outcome changes: 10 reproduced, 4 partially reproduced, 12 not reproduced, 18 blocked. Nothing needed a `proposed` change. The last run of `python tools/entry.py all entries/crcns-hc-7-kohus-2016` reported 0 errors and the notebook passed (1378 s). I checked the new text against that run's outputs.

**Outcomes**
- **The fig11 fits vary between runs, as the verifier suspected.** A new notebook cell repeats all 32 fits with three more seeds and also keeps the best fit over all 16 starting points.
  - One seed hits a worse optimum for PV+BC to PV+BC.
  - Another (seed 3) hits a worse TM depressing plus facilitating optimum for CCK+BC to PC under weighting b (BIC -1341). There UDR with facilitation has the lowest BIC.
  - Taking the best fit over all 16 starting points gives every fig11 and Table 4 conclusion of the saved run, so all five fig11 outcomes stand.
  - fig11-model-cck-facilitation rests on a BIC margin of 1.8 (-1389.1 against -1387.3). The notebook and the notes say so.
- **The verifier was right about the infinite value.** The CCK+BC TM depressing test error under weighting a is infinite in this run (seed 11), and 3765.7 with the other seeds. My round-1 response saying it was finite came from an earlier run, and the round-2 response corrects it.

**Pipette solution check**
- Cell 14 now discusses the CCK+BC to PC latency correlation with holding current (rho 0.58, p 0.048).
- I added a sensitivity test. Using only the 6 CCK+BC to PC pairs at or below the median holding current, the rise and latency tests give p 0.26 and 0.14, against 0.021 and 0.0084 with all 12 pairs.
- So the reproduced fig4b-in-pc-kruskal-wallis depends on the pairs where a CsCl admixture would lengthen latency. With only 6 pairs the tests also lose power, so this doesn't show the difference is absent.
- This is now in the fig4b notes, in the pipette deviation on all 16 assumed outcomes, and in the summary. I kept the outcome: the verifier found the assumption reasonable, and the test cannot tell CsCl pairs apart.

**Text corrections**
- fig11c tau_f p is 0.026, not 0.0339.
- AAC to PC test error is 953.1, not 953.2.
- Under weighting a, the lowest PV+BC to PC test error is UDR with facilitation (317.9).
- fig9 raw-trace transmission probability at 320 Hz is 0.1 to 0.6 over the 3rd to 10th APs.
- fig13 now says "up to 2" fits per reading reach the bound.
- The comprehensive-model CCK+BC tau_r is 2.3 s under the other seeds and the best of 16, against 0.415 s with seed 11.

**Questions and record**
- The onset-rule question in `questions/crcns-hc-7.yaml` now includes the verifier's new point: rule (b) cannot tell asynchronous release from summation at 160 Hz. No claim was changed.
- Round 2 is recorded under `verifications`, with all 44 results, the verifier's reasons and my responses.

**Not done**
- The verifier counted 21 assumed outcomes. The record has 16, and I noted the difference under `reviewed` without changing anything.
- Nothing was committed, as instructed.
